import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

routes = [
    ("Delhi","Mumbai"),
    ("Delhi","Kolkata"),
    ("Hyderabad","Chennai"),
    ("Bangalore","Mumbai"),
    ("Chennai","Kolkata"),
    ("Delhi","Hyderabad")
]

train_ids = [12001,12002,12003,12004,12005,12006]

start_date = datetime(2025,1,1)

data = []

for i in range(365):

    date = start_date + timedelta(days=i)
    weekend = 1 if date.weekday() >=5 else 0

    for train,route in zip(train_ids,routes):

        source,destination = route
        
        base_demand = random.randint(400,800)

        passenger_count = base_demand + weekend*200 + random.randint(-50,150)

        capacity = random.choice([900,1000,1100])

        coaches = capacity//50

        platform = random.randint(1,8)

        delay = max(0,int(np.random.normal(10,5)))

        data.append([
            train,
            source+"-"+destination,
            date,
            passenger_count,
            capacity,
            coaches,
            platform,
            delay,
            weekend
        ])

df = pd.DataFrame(data,columns=[
    "Train_ID",
    "Route",
    "Date",
    "Passenger_Count",
    "Seat_Capacity",
    "Num_Coaches",
    "Platform",
    "Delay_Minutes",
    "Weekend"
])

df.to_csv("data/railway_data.csv",index=False)

print("Dataset generated successfully")