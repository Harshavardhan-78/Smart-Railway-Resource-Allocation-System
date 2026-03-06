import pandas as pd
import numpy as np
from pathlib import Path

# project root
BASE_DIR = Path(__file__).resolve().parent.parent

data_dir = BASE_DIR / "data"
data_dir.mkdir(exist_ok=True)

np.random.seed(42)

n = 500

stations = ["HYD","NDLS","MAS","SBC","VSKP","BZA"]
train_types = ["Express","Passenger","Freight"]

arrival_times = np.random.randint(0,1440,n)
departure_times = arrival_times + np.random.randint(5,30,n)

data = {
    "Train_ID": [f"T{i}" for i in range(n)],
    "Station": np.random.choice(stations,n),
    "Arrival_Time": arrival_times,
    "Departure_Time": departure_times,
    "Platform": np.random.randint(1,6,n),
    "Track": np.random.randint(1,4,n),
    "Train_Type": np.random.choice(train_types,n)
}

df = pd.DataFrame(data)

file_path = data_dir / "railway_dataset.csv"

df.to_csv(file_path,index=False)

print("Dataset Generated Successfully")
print("Saved at:",file_path)