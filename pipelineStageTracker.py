import streamlit as st
import pandas as pd

st.set_page_config(page_title="HR Pipeline Dashboard", layout="wide")

st.title("📊 Candidate Pipeline Dashboard")

# --- Example pipeline data ---
data = {
    "Stage": ["Applied", "Screening", "Interview", "Offer", "Hired"],
    "Count": [120, 60, 30, 10, 5]
}
df = pd.DataFrame(data)

# --- Display table ---
st.subheader("📋 Candidate Counts by Stage")
st.dataframe(df, use_container_width=True)

# --- Visualize funnel ---
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



