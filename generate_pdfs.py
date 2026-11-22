"""
Automated PDF Generator for Milestone 2 Deliverables
Converts markdown files into professionally styled PDFs using Headless Chrome.
"""

import os
import subprocess
import markdown
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent

CSS_STYLE = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500&display=swap');

@page {
    size: A4;
    margin: 20mm 15mm 20mm 15mm;
    @bottom-right {
        content: counter(page);
    }
}

body {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
    font-size: 10.5pt;
    line-height: 1.55;
    color: #1f2937;
    background: #ffffff;
    padding: 0;
    margin: 0;
}

h1 {
    font-size: 20pt;
    font-weight: 800;
    color: #1e3a8a;
    border-bottom: 2px solid #3b82f6;
    padding-bottom: 6px;
    margin-top: 24pt;
    margin-bottom: 12pt;
    page-break-after: avoid;
}

h2 {
    font-size: 14pt;
    font-weight: 700;
    color: #1e40af;
    margin-top: 18pt;
    margin-bottom: 8pt;
    page-break-after: avoid;
}

h3 {
    font-size: 11.5pt;
    font-weight: 600;
    color: #374151;
    margin-top: 14pt;
    margin-bottom: 6pt;
    page-break-after: avoid;
}

p, li {
    font-size: 10pt;
    line-height: 1.5;
    color: #374151;
}

table {
    width: 100%;
    border-collapse: collapse;
    margin: 12pt 0;
    font-size: 9pt;
    page-break-inside: avoid;
}

th, td {
    border: 1px solid #d1d5db;
    padding: 6pt 8pt;
    text-align: left;
    vertical-align: top;
}

th {
    background-color: #f3f4f6;
    font-weight: 600;
    color: #111827;
}

tr:nth-child(even) td {
    background-color: #f9fafb;
}

pre, code {
    font-family: 'JetBrains Mono', Consolas, Monaco, monospace;
}

code {
    font-size: 8.5pt;
    background-color: #f3f4f6;
    padding: 1.5pt 3pt;
    border-radius: 3pt;
    color: #c026d3;
}

pre {
    background-color: #0f172a;
    color: #e2e8f0;
    padding: 10pt;
    border-radius: 6pt;
    overflow-x: auto;
    font-size: 8pt;
    line-height: 1.4;
    page-break-inside: avoid;
    white-space: pre-wrap;
    word-break: break-all;
}

pre code {
    background-color: transparent;
    color: inherit;
    padding: 0;
    font-size: 8pt;
}

blockquote {
    border-left: 3.5px solid #3b82f6;
    margin: 10pt 0;
    padding: 6pt 12pt;
    background-color: #eff6ff;
    color: #1e40af;
    font-size: 9.5pt;
}

.cover-page {
    text-align: center;
    padding-top: 40pt;
    page-break-after: always;
}

.cover-title {
    font-size: 26pt;
    font-weight: 800;
    color: #1e3a8a;
    margin-bottom: 8pt;
}

.cover-sub {
    font-size: 13pt;
    color: #4b5563;
    margin-bottom: 24pt;
}

hr {
    border: 0;
    height: 1px;
    background: #e5e7eb;
    margin: 16pt 0;
}
</style>
"""

def md_to_pdf(md_path: Path, output_pdf_path: Path, title: str):
    print(f"Converting {md_path.name} -> {output_pdf_path.name}...")
    text = md_path.read_text(encoding="utf-8")
    
    html_body = markdown.markdown(
        text,
        extensions=[
            "tables",
            "fenced_code",
            "codehilite",
            "attr_list",
            "def_list",
        ]
    )
    
    full_html = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>{title}</title>
    {CSS_STYLE}
</head>
<body>
{html_body}
</body>
</html>
"""
    temp_html = md_path.with_suffix(".temp.html")
    temp_html.write_text(full_html, encoding="utf-8")
    
    chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    if not os.path.exists(chrome_path):
        chrome_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
        
    cmd = [
        chrome_path,
        "--headless",
        "--disable-gpu",
        "--no-pdf-header-footer",
        f"--print-to-pdf={output_pdf_path}",
        str(temp_html)
    ]
    
    res = subprocess.run(cmd, capture_output=True, text=True)
    if temp_html.exists():
        temp_html.unlink()
        
    if output_pdf_path.exists():
        size_kb = output_pdf_path.stat().st_size / 1024
        print(f"SUCCESS: {output_pdf_path.name} generated ({size_kb:.1f} KB)")
    else:
        print(f"ERROR: Failed to generate {output_pdf_path}. Output: {res.stderr}")

if __name__ == "__main__":
    docs_dir = REPO_ROOT / "docs"
    
    # 1. Milestone 2 Report PDF
    m2_report_md = docs_dir / "milestone_2_report.md"
    m2_report_pdf = docs_dir / "M2_TeamID_VeriSightAI.pdf"
    md_to_pdf(m2_report_md, m2_report_pdf, "Milestone 2 Report - VeriSight AI")
    
    # 2. Supporting Document (Technical Report) PDF
    tech_md = docs_dir / "technical_synopsis.md"
    tech_pdf = docs_dir / "VeriSightAI_TechnicalReport.pdf"
    md_to_pdf(tech_md, tech_pdf, "VeriSight AI - Technical Report")
