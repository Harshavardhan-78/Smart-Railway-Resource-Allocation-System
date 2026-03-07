import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

def train_model():

    df = pd.read_csv("data/railway_data.csv")

    df["Route_ID"] = df["Route"].astype("category").cat.codes

    X = df[[
        "Route_ID",
        "Weekend",
        "Num_Coaches",
        "Seat_Capacity"
    ]]

    y = df["Passenger_Count"]

    X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2)

    model = RandomForestRegressor()

    model.fit(X_train,y_train)

    return model,df