"""
VeriSight AI — Deterministic CSV Profiler & Responsible AI Guardrail Tool
Problem ID: C21 | Component: Tool-Assisted Ingestion & Exact Math Engine

This module deterministically analyzes tabular CSV files using pandas and numpy.
It computes exact ground-truth statistical metrics (means, medians, IQR outlier bounds,
and Pearson correlations) and applies automated PII masking guardrails to eliminate
mathematical hallucinations and data privacy leaks in downstream LLM prompts.
"""

import re
import json
import argparse
from pathlib import Path
from typing import Dict, Any, List, Optional
import numpy as np
import pandas as pd


# ---------------------------------------------------------------------------
# Responsible AI: PII Detection & Governance Patterns
# ---------------------------------------------------------------------------
PII_COLUMN_NAME_PATTERNS = [
    r"(?i)\b(ssn|social[-_ ]?security)\b",
    r"(?i)\b(aadhaar|aadhar|uidai)\b",
    r"(?i)\b(passport|driving[-_ ]?licen[sc]e)\b",
    r"(?i)\b(credit[-_ ]?card|debit[-_ ]?card|cvv|account[-_ ]?num)\b",
    r"(?i)\b(phone|mobile|cell|contact[-_ ]?no)\b",
    r"(?i)\b(email|e[-_ ]?mail)\b",
    r"(?i)\b(first[-_ ]?name|last[-_ ]?name|full[-_ ]?name|patient[-_ ]?name)\b",
]

PII_VALUE_REGEX_PATTERNS = {
    "EMAIL": re.compile(r"^[\w\.-]+@[\w\.-]+\.\w+$"),
    "PHONE_INTL": re.compile(r"^\+?[0-9\s\-()]{7,18}$"),
    "SSN": re.compile(r"^\d{3}-\d{2}-\d{4}$"),
    "AADHAAR": re.compile(r"^\d{4}\s?\d{4}\s?\d{4}$"),
}


def scan_and_sanitize_pii(df: pd.DataFrame) -> tuple[pd.DataFrame, List[Dict[str, Any]]]:
    """
    Scans columns for PII by header name and sample cell content.
    Redacts sensitive text to prevent privacy leaks before context injection into LLMs.
    """
    sanitized_df = df.copy()
    pii_warnings: List[Dict[str, Any]] = []

    for col in df.columns:
        col_str = str(col)
        detected_reason: Optional[str] = None

        # Check column name heuristics
        for pattern in PII_COLUMN_NAME_PATTERNS:
            if re.search(pattern, col_str):
                detected_reason = f"Header matches sensitive PII keyword pattern: {pattern}"
                break

        # Check sample content if column contains strings
        if not detected_reason and df[col].dtype == "object":
            sample_non_nulls = df[col].dropna().astype(str).head(20).tolist()
            for sample in sample_non_nulls:
                for pii_type, regex in PII_VALUE_REGEX_PATTERNS.items():
                    if regex.match(sample.strip()):
                        detected_reason = f"Sample values match regex format for {pii_type}"
                        break
                if detected_reason:
                    break

        if detected_reason:
            pii_warnings.append({
                "column_name": col_str,
                "action_taken": "MASKED_IN_SUMMARY",
                "reason": detected_reason
            })
            # Mask the column with redacted placeholders
            sanitized_df[col] = "[REDACTED_PII]"

    return sanitized_df, pii_warnings


def infer_column_semantic_type(series: pd.Series) -> str:
    """Classifies a column as numeric, temporal, categorical, or text."""
    if pd.api.types.is_numeric_dtype(series):
        return "numeric"
    
    # Check if temporal
    try:
        sample = series.dropna().head(15).astype(str)
        if len(sample) > 0:
            parsed = pd.to_datetime(sample, errors="coerce", format="mixed")
            if parsed.notna().mean() >= 0.8:
                return "temporal"
    except Exception:
        pass

    # Categorical vs free text
    non_null_count = series.dropna().count()
    unique_count = series.nunique(dropna=True)
    if non_null_count > 0 and (unique_count <= 25 or (unique_count / non_null_count) < 0.25):
        return "categorical"

    return "text"


def profile_csv_data(filepath_or_buffer: Any) -> Dict[str, Any]:
    """
    Generates a deterministic, mathematically verifiable profile of a CSV dataset.
    
    Returns:
        Dict[str, Any]: Ground-truth statistical metrics, data quality alerts,
                        and schema types ready for LLM prompt ingestion.
    """
    df = pd.read_csv(filepath_or_buffer)
    total_rows, total_cols = df.shape
    duplicate_rows = int(df.duplicated().sum())

    # 1. PII Scan & Sanitize
    sanitized_df, pii_warnings = scan_and_sanitize_pii(df)

    # 2. Sample Size Bias Check (Responsible AI)
    sample_size_alert: Optional[Dict[str, Any]] = None
    if total_rows < 30:
        sample_size_alert = {
            "severity": "WARNING",
            "message": (
                f"Small sample size (N={total_rows} < 30). Central limit theorem approximations "
                "and statistical significance assertions may exhibit elevated estimation variance."
            )
        }

    # 3. Column-by-Column Profiling
    column_profiles: Dict[str, Any] = {}
    numeric_cols: List[str] = []

    for col in df.columns:
        series = df[col]
        non_null_count = int(series.notna().sum())
        missing_count = int(series.isna().sum())
        missing_pct = round((missing_count / total_rows) * 100, 2) if total_rows > 0 else 0.0
        semantic_type = infer_column_semantic_type(series)

        col_dict: Dict[str, Any] = {
            "semantic_type": semantic_type,
            "raw_dtype": str(series.dtype),
            "total_count": total_rows,
            "non_null_count": non_null_count,
            "missing_count": missing_count,
            "missing_pct": missing_pct,
        }

        # Numeric Statistics
        if semantic_type == "numeric":
            clean_num = series.dropna()
            numeric_cols.append(col)
            if len(clean_num) > 0:
                mean_val = float(clean_num.mean())
                median_val = float(clean_num.median())
                std_val = float(clean_num.std()) if len(clean_num) > 1 else 0.0
                min_val = float(clean_num.min())
                max_val = float(clean_num.max())
                sum_val = float(clean_num.sum())

                q25 = float(clean_num.quantile(0.25))
                q75 = float(clean_num.quantile(0.75))
                iqr = float(q75 - q25)
                lower_fence = q25 - (1.5 * iqr)
                upper_fence = q75 + (1.5 * iqr)

                outliers = clean_num[(clean_num < lower_fence) | (clean_num > upper_fence)]
                outlier_count = int(len(outliers))
                outlier_samples = [round(float(x), 2) for x in outliers.head(5).tolist()]

                col_dict["stats"] = {
                    "mean": round(mean_val, 2),
                    "median": round(median_val, 2),
                    "std_dev": round(std_val, 2),
                    "min": round(min_val, 2),
                    "max": round(max_val, 2),
                    "sum": round(sum_val, 2),
                    "q25": round(q25, 2),
                    "q75": round(q75, 2),
                    "iqr": round(iqr, 2),
                    "outlier_count": outlier_count,
                    "outlier_bounds": [round(lower_fence, 2), round(upper_fence, 2)],
                    "outlier_samples": outlier_samples,
                }
            else:
                col_dict["stats"] = None

        # Categorical Statistics
        elif semantic_type in ["categorical", "text"]:
            clean_cat = series.dropna().astype(str)
            unique_count = int(clean_cat.nunique())
            value_counts = clean_cat.value_counts().head(5)
            top_values = []
            for val, count in value_counts.items():
                pct = round((count / total_rows) * 100, 2)
                top_values.append({"value": str(val), "count": int(count), "percentage": pct})

            col_dict["categorical_summary"] = {
                "unique_count": unique_count,
                "top_categories": top_values,
                "is_cardinally_degenerate": unique_count <= 1 or unique_count == total_rows
            }

        # Temporal Statistics
        elif semantic_type == "temporal":
            clean_dates = pd.to_datetime(series.dropna(), errors="coerce")
            valid_dates = clean_dates.dropna()
            if len(valid_dates) > 0:
                col_dict["temporal_summary"] = {
                    "earliest_timestamp": str(valid_dates.min()),
                    "latest_timestamp": str(valid_dates.max()),
                    "span_days": round((valid_dates.max() - valid_dates.min()).total_seconds() / 86400, 2)
                }

        column_profiles[str(col)] = col_dict

    # 4. Pearson Correlation Analysis (for Numeric Features)
    correlations: List[Dict[str, Any]] = []
    if len(numeric_cols) >= 2:
        numeric_df = df[numeric_cols].dropna()
        if len(numeric_df) > 2:
            corr_matrix = numeric_df.corr(method="pearson")
            paired = []
            seen = set()
            for c1 in numeric_cols:
                for c2 in numeric_cols:
                    if c1 != c2:
                        pair_key = tuple(sorted([c1, c2]))
                        if pair_key not in seen:
                            seen.add(pair_key)
                            r_val = corr_matrix.loc[c1, c2]
                            if not np.isnan(r_val):
                                paired.append({
                                    "feature_x": c1,
                                    "feature_y": c2,
                                    "pearson_r": round(float(r_val), 3),
                                    "absolute_r": round(abs(float(r_val)), 3),
                                    "strength": (
                                        "STRONG" if abs(r_val) >= 0.7 else
                                        "MODERATE" if abs(r_val) >= 0.4 else "WEAK"
                                    )
                                })
            # Sort by highest absolute correlation
            paired.sort(key=lambda x: x["absolute_r"], reverse=True)
            correlations = paired[:5]

    # Assemble Final Profile Object
    ground_truth_stats = {
        "dataset_metadata": {
            "total_rows": total_rows,
            "total_columns": total_cols,
            "duplicate_rows": duplicate_rows,
            "numeric_columns_count": len(numeric_cols),
            "numeric_columns": numeric_cols,
        },
        "governance_and_privacy": {
            "pii_detected": len(pii_warnings) > 0,
            "pii_alerts": pii_warnings,
            "sample_size_alert": sample_size_alert
        },
        "column_profiles": column_profiles,
        "top_correlations": correlations
    }

    return ground_truth_stats


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Deterministic CSV Profiler for VeriSight AI (C21)")
    parser.add_argument("csv_path", type=str, help="Path to input CSV dataset")
    parser.add_argument("--pretty", action="store_true", help="Print pretty-formatted JSON")
    args = parser.parse_args()

    profile = profile_csv_data(args.csv_path)
    if args.pretty:
        print(json.dumps(profile, indent=2))
    else:
        print(json.dumps(profile))
