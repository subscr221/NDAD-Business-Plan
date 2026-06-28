#!/usr/bin/env python3
"""
build_investor_plan.py — deterministic regeneration of the consolidated investor plan.

Toolchain note: the original .docx/.pdf were produced by LibreOffice-on-Linux (see
docProps in the existing .docx). That binary pipeline is NOT present on this host.
This script regenerates only the *markdown* master, which is the true source-derived
artifact: a faithful, re-runnable concatenation of the canonical section files 00-10
(each already reconciled to project-context.md decisions D-008..D-012).

Run:  python build_investor_plan.py
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "investor_plan"
OUT = SRC / "Nitrodynamics_Investor_Plan.md"

# Canonical order per project-context.md S4 Artifact Registry.
SECTIONS = [
    "00_cover_and_onepager.md",
    "01_executive_summary.md",
    "02_market_opportunity.md",
    "03_strategy_and_products.md",
    "04_financial_model.md",
    "05_funding_and_capital.md",
    "06_returns_and_sensitivity.md",
    "07_operating_model.md",
    "08_risk_register.md",
    "09_governance_compliance_ip.md",
    "10_kpis_and_appendix.md",
]

SEP = "\n\n---\n\n<!-- page-break -->\n\n"

def build():
    parts = []
    for name in SECTIONS:
        p = SRC / name
        text = p.read_text(encoding="utf-8").rstrip() + "\n"
        parts.append(text)
    consolidated = SEP.join(parts)
    OUT.write_text(consolidated, encoding="utf-8")
    return consolidated

def verify(text):
    # Guardrails against regressions to superseded facts.
    checks = {
        "no 'first platform-native' superlative (D-008)":
            "first **platform-native" not in text and "first platform-native" not in text,
        "Rs.210 Cr MoQ present (D-012)": "Rs.210" in text,
        "Rs.21 Cr/system present (D-012)": "21 Cr" in text,
        "Phase 1 framing present (D-009/D-012)": "Phase 1" in text,
        "OQ-C reconciliation note present": "OQ-C" in text,
    }
    return checks

if __name__ == "__main__":
    text = build()
    print(f"Wrote {OUT.relative_to(ROOT)}  ({len(text):,} bytes, {text.count(chr(10))+1:,} lines)")
    print(f"Sections concatenated: {len(SECTIONS)}")
    print("Verification:")
    ok = True
    for label, passed in verify(text).items():
        print(f"  [{'PASS' if passed else 'FAIL'}] {label}")
        ok = ok and passed
    print("ALL CHECKS PASS" if ok else "*** SOME CHECKS FAILED ***")
