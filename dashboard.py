import streamlit as st
import pandas as pd
import plotly.express as px

from prediction_model import train_model
from recommendation_engine import coach_recommendation,train_frequency_recommendation

st.title("🚆 Smart Railway Resource Planning System")

model,df = train_model()

# Sidebar
st.sidebar.header("Filters")

route = st.sidebar.selectbox(
    "Select Route",
    ["All"] + list(df["Route"].unique())
)

if route == "All":
    filtered_df = df
else:
    filtered_df = df[df["Route"] == route]

# Overview metrics
st.subheader("System Overview")

total_passengers =filtered_df["Passenger_Count"].sum()
avg_occupancy = (filtered_df["Passenger_Count"]/filtered_df["Seat_Capacity"]).mean()

col1,col2 = st.columns(2)

col1.metric("Total Passengers",int(total_passengers))
col2.metric("Average Occupancy",round(avg_occupancy,2))


# Demand visualization
st.subheader("Passenger Demand by Route")

route_demand = filtered_df.groupby("Route")["Passenger_Count"].mean().reset_index()

fig = px.bar(
    route_demand,
    x="Route",
    y="Passenger_Count",
    color="Route"
)

st.plotly_chart(fig)


# Peak travel days
st.subheader("Weekend vs Weekday Demand")

fig2 = px.box(
    filtered_df,
    x="Weekend",
    y="Passenger_Count"
)

st.plotly_chart(fig2)


# Prediction section
st.subheader("Predict Passenger Demand")

weekend = st.selectbox("Weekend?",["No","Yes"])
weekend = 1 if weekend == "Yes" else 0
capacity = st.number_input("Seat Capacity",800,1200,1000)
coaches = st.number_input("Number of Coaches",16,24,20)

if route == "All":
    route_id = df["Route_ID"].iloc[0]
else:
    route_row = df[df["Route"] == route]
    route_id = route_row["Route_ID"].iloc[0]

input_data = pd.DataFrame({
    "Route_ID":[route_id],
    "Weekend":[weekend],
    "Num_Coaches":[coaches],
    "Seat_Capacity":[capacity]
})

prediction = model.predict(input_data)[0]

st.success(f"Predicted Passenger Demand: {int(prediction)}")

# Recommendations

st.subheader("Resource Recommendation")

coach_advice = coach_recommendation(prediction,capacity)

train_advice = train_frequency_recommendation(prediction,capacity)

st.write("Coach Recommendation:",coach_advice)

st.write("Train Recommendation:",train_advice)


# Crowded routes
st.subheader("Most Crowded Routes")

filtered_df = filtered_df.copy()

filtered_df["Occupancy"] = (
    filtered_df["Passenger_Count"] / filtered_df["Seat_Capacity"]
) * 100
crowded = (
    filtered_df.groupby("Route")["Occupancy"]
    .mean()
    .sort_values(ascending=False)
    .round(2)
)

st.dataframe(
    crowded.head(5).rename("Occupancy (%)")
)
threshold = st.slider("Overcrowding Threshold (%)",70,120,90)

overcrowded = crowded[crowded > threshold]

st.write("Routes exceeding threshold:")
st.dataframe(overcrowded)