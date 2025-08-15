# Demos

This folder proves the skills are **transferable** beyond cosmology.

- `streamlit_app.py` — interactive S(z) vs z viewer. Drop in your own CSV.  
- `report_generator.py` — CLI tool that turns a CSV into a short Markdown report.  
- `pipelines/langflow_waveframe_template.json` — starter graph for a no‑code pipeline.

## Quickstart

```bash
pip install -r demos/requirements.txt
# Streamlit app
streamlit run demos/streamlit_app.py
# Report generator
python demos/report_generator.py --csv demos/data/sample_entropy_curve.csv --out demos/reports/demo_report.md
```
