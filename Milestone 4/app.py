import streamlit as st
import pandas as pd
import plotly.express as px
from prophet import Prophet

st.set_page_config(page_title="FitPulse Dashboard", layout="wide")
st.title("🏃 FitPulse Health Anomaly Dashboard")

uploaded_file = st.file_uploader("Upload Fitness Dataset (CSV)", type=["csv"])

@st.cache_data
def load_data(file):
    df = pd.read_csv(file)
    df["date"] = pd.to_datetime(df["date"], dayfirst=True, errors="coerce")
    df = df.dropna(subset=["date"])
    return df

def prophet_residuals(df, metric):
    p_df = df[["date", metric]].dropna().rename(
        columns={"date": "ds", metric: "y"}
    )

    model = Prophet()
    model.fit(p_df)
    forecast = model.predict(p_df)

    df[f"{metric}_predicted"] = None
    df[f"{metric}_residual"] = None

    df.loc[p_df.index, f"{metric}_predicted"] = forecast["yhat"].values
    df.loc[p_df.index, f"{metric}_residual"] = (
        df.loc[p_df.index, metric] - forecast["yhat"].values
    )
    return df

def threshold_anomaly(series, k=3):
    valid = series.dropna()
    mean = valid.mean()
    std = valid.std()

    anomaly = abs(series - mean) > k * std
    anomaly = anomaly.fillna(False)

    return anomaly

if uploaded_file:
    df = load_data(uploaded_file)

    metric = st.selectbox(
        "Select Metric",
        ["avg_heart_rate", "hours_sleep", "daily_steps"]
    )

    k = st.slider("Anomaly Sensitivity (k)", 1.5, 4.0, 3.0, 0.1)

    df = prophet_residuals(df, metric)

    df[f"{metric}_anomaly"] = False
    df[f"{metric}_anomaly"] = threshold_anomaly(df[f"{metric}_residual"], k)

    st.subheader(f"{metric.replace('_',' ').title()} Trend & Anomalies")

    fig = px.line(df, x="date", y=metric)

    anomalies = df[df[f"{metric}_anomaly"]]

    fig.add_scatter(
        x=anomalies["date"],
        y=anomalies[metric],
        mode="markers",
        name="Anomaly",
        marker=dict(color="red", size=8)
    )

    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Download Anomaly Report")

    st.download_button(
        "Download CSV",
        anomalies.to_csv(index=False),
        file_name="anomaly_report.csv",
        mime="text/csv"
    )
