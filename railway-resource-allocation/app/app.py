import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

# Project root directory
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = BASE_DIR / "data" / "railway_dataset.csv"

st.title("🚆 Smart Railway Resource Allocation System")

st.write(
"""
This dashboard helps railway planners analyze train schedules,
platform usage, and track allocation to improve railway resource planning.
"""
)

# ----------------------------
# Load Dataset
# ----------------------------

if not DATA_PATH.exists():
    st.error("Dataset not found. Run: python src/generate_dataset.py")
    st.stop()

df = pd.read_csv(DATA_PATH)

# ----------------------------
# Key Metrics
# ----------------------------

st.subheader("System Metrics")

df["Arrival_Hour"] = df["Arrival_Time"] // 60

total_trains = len(df)
total_stations = df["Station"].nunique()
busiest_platform = df["Platform"].value_counts().idxmax()
peak_hour = df["Arrival_Hour"].value_counts().idxmax()
avg_platform_load = round(df["Platform"].value_counts().mean(),2)
busiest_station = df["Station"].value_counts().idxmax()

col1, col2, col3 = st.columns(3)

col1.metric("Total Trains", total_trains)
col2.metric("Total Stations", total_stations)
col3.metric("Busiest Platform", busiest_platform)

col4, col5, col6 = st.columns(3)

col4.metric("Peak Hour", f"{peak_hour}:00")
col5.metric("Avg Platform Load", avg_platform_load)
col6.metric("Most Active Station", busiest_station)

# ----------------------------
# Dataset Preview
# ----------------------------

st.subheader("Dataset Preview")

st.dataframe(df.head())

# ----------------------------
# Station Traffic
# ----------------------------

st.subheader("Station Traffic Analysis")

station_counts = df["Station"].value_counts()

st.bar_chart(station_counts)

# ----------------------------
# Platform Utilization
# ----------------------------

st.subheader("Platform Utilization")

fig, ax = plt.subplots()

sns.countplot(x="Platform", data=df, ax=ax)

ax.set_title("Number of Trains per Platform")

st.pyplot(fig)

# ----------------------------
# Track Usage
# ----------------------------

st.subheader("Track Utilization")

fig2, ax2 = plt.subplots()

sns.countplot(x="Track", data=df, ax=ax2)

ax2.set_title("Track Usage Distribution")

st.pyplot(fig2)

# ----------------------------
# Train Type Distribution
# ----------------------------

st.subheader("Train Type Distribution")

fig3, ax3 = plt.subplots()

sns.countplot(x="Train_Type", data=df, ax=ax3)

ax3.set_title("Distribution of Train Types")

st.pyplot(fig3)

# ----------------------------
# Peak Traffic Analysis
# ----------------------------

st.subheader("Peak Train Arrival Hours")

fig4, ax4 = plt.subplots()

sns.histplot(df["Arrival_Hour"], bins=24, ax=ax4)

ax4.set_title("Train Arrivals by Hour")

st.pyplot(fig4)

st.info(f"Peak Railway Traffic Hour: {peak_hour}:00")

# ----------------------------
# Platform Congestion
# ----------------------------

st.subheader("Platform Congestion")

platform_load = df["Platform"].value_counts()

st.bar_chart(platform_load)

# ----------------------------
# Platform Recommendation
# ----------------------------

st.subheader("Platform Recommendation")

recommended_platform = platform_load.idxmin()

st.success(f"Recommended Platform for Next Train: Platform {recommended_platform}")