import streamlit as st
import pandas as pd

st.set_page_config(page_title="HR Pipeline Dashboard", layout="wide")
st.title("📊 Candidate Pipeline Dashboard")

# --- File Upload ---
uploaded_file = st.file_uploader("📂 Upload a CSV file with pipeline data", type=["csv"])

if uploaded_file is not None:
    # Read the CSV
    df = pd.read_csv(uploaded_file)

    # Ensure it has Stage & Count columns
    if "Stage" in df.columns and "Count" in df.columns:
        st.subheader("📋 Candidate Counts by Stage")
        st.dataframe(df, use_container_width=True)

        # --- Visualizations ---
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("📊 Bar Chart")
            st.bar_chart(df.set_index("Stage"))

        with col2:
            st.subheader("📈 Line Chart")
            st.line_chart(df.set_index("Stage"))

        # --- Conversion Rates ---
        st.subheader("📉 Conversion Rates")
        df["Conversion %"] = (df["Count"] / df["Count"].iloc[0] * 100).round(2)
        st.dataframe(df[["Stage", "Conversion %"]], use_container_width=True)

    else:
        st.error("CSV must contain 'Stage' and 'Count' columns.")
else:
    st.info("👆 Upload a CSV file to visualize your pipeline.")
