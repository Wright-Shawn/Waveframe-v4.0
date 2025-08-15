import argparse, pandas as pd, datetime as dt, json, os
from pathlib import Path

TEMPLATE = """# Waveframe Report
**Generated:** {timestamp}

## Summary
This report summarizes an entropy-like curve vs redshift from the provided CSV.

- Rows: {rows}
- z-range: {zmin} → {zmax}
- S(z) range: {smin} → {smax}

## Table (first 10 rows)
{preview}

## Simple Diagnostics
- Monotonicity (z): {mono_z}
- Non-negativity (S): {nonneg_s}
"""

def analyze(df):
    mono_z = df["z"].is_monotonic_increasing
    nonneg_s = (df["S_of_z"] >= 0).all()
    return mono_z, nonneg_s

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--csv", required=True, help="Input CSV with columns z,S_of_z")
    p.add_argument("--out", default="report.md", help="Output Markdown file")
    args = p.parse_args()

    df = pd.read_csv(args.csv).sort_values("z")
    mono_z, nonneg_s = analyze(df)

    content = TEMPLATE.format(
        timestamp=dt.datetime.utcnow().isoformat() + "Z",
        rows=len(df),
        zmin=df["z"].min(),
        zmax=df["z"].max(),
        smin=df["S_of_z"].min(),
        smax=df["S_of_z"].max(),
        preview=df.head(10).to_markdown(index=False),
        mono_z=mono_z,
        nonneg_s=nonneg_s,
    )

    out_path = Path(args.out).resolve()
    out_path.write_text(content, encoding="utf-8")
    print(f"Wrote {out_path}")

if __name__ == "__main__":
    main()
