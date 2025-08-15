import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

st.set_page_config(page_title="Waveframe v4.0 — Interactive Demo", layout="centered")

st.title("Entropy Growth vs. Redshift")
st.write("Drop in a CSV with columns `z,S_of_z` to visualize an entropy-like signal versus redshift.")

default_path = Path(__file__).parent / "data" / "sample_entropy_curve.csv"
uploaded = st.file_uploader("Upload CSV (z,S_of_z)", type=["csv"])
if uploaded is not None:
    df = pd.read_csv(uploaded)
else:
    df = pd.read_csv(default_path)
    st.caption("Using sample data bundled with the demo.")

# Basic validation
if not set(["z", "S_of_z"]).issubset(df.columns):
    st.error("CSV must contain columns: z, S_of_z")
else:
    df = df.sort_values("z")
    st.dataframe(df)

    fig, ax = plt.subplots()
    ax.plot(df["z"], df["S_of_z"], marker="o")
    ax.set_xlabel("Redshift z")
    ax.set_ylabel("Entropy-like S(z)")
    ax.set_title("S(z) vs z")
    st.pyplot(fig)

    st.write("**Notes**")
    st.markdown("- Replace sample CSV with your model output to showcase your own results.\n- This is intentionally simple: recruiters want to see applied, legible demos.")
