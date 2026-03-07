# 🚆 Smart Railway Resource Planning System

A **Machine Learning + Data Analytics** project that predicts passenger demand on railway routes and provides **resource optimization recommendations** such as coach allocation and train frequency.

This system helps railway planners **anticipate passenger load, reduce overcrowding, and optimize train resources** using data-driven insights.

---

# 📊 Features

* 📈 **Passenger Demand Prediction** using Machine Learning
* 🚉 **Route-wise demand visualization**
* 📅 **Weekend vs Weekday demand analysis**
* 🚨 **Overcrowded route detection**
* 🚆 **Coach allocation recommendation**
* ⏱ **Train frequency recommendation**
* 📊 **Interactive Streamlit dashboard**

---

# 🧠 Machine Learning Model

The system uses:

* **Random Forest Regressor**
* Features used for prediction:

  * Route_ID
  * Weekend indicator
  * Number of Coaches
  * Seat Capacity

The model predicts **Passenger_Count** for a given route configuration.

---

# 🗂 Project Structure

```
Smart-Railway-Resource-Planning/
│
├── data/
│   └── railway_data.csv           # Dataset
│
├── dashboard.py                  # Streamlit dashboard
├── prediction_model.py           # ML model training
├── recommendation_engine.py      # Resource recommendation logic
├── dataset_generator.py          # Synthetic dataset generator
│
├── requirements.txt              # Python dependencies
└── README.md                     # Project documentation
```

---

# ⚙️ Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/Harshavardhan-78/Smart-Railway-Resource-Planning.git
cd Smart-Railway-Resource-Planning
```

---

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

### 3️⃣ Run the dashboard

```bash
streamlit run dashboard.py
```

The application will start at:

```
http://localhost:8501
```

---

# 📊 Dashboard Capabilities

The Streamlit dashboard provides:

### System Overview

* Total passengers
* Average occupancy rate

### Visualizations

* Passenger demand by route
* Weekend vs weekday demand distribution

### Prediction

Users can input:

* Route
* Weekend / Weekday
* Seat Capacity
* Number of Coaches

The system predicts **expected passenger demand**.

### Recommendations

Based on predicted demand, the system suggests:

* 🚆 **Additional coaches if overcrowded**
* ⏱ **Increasing train frequency**

### Overcrowding Detection

Routes exceeding an **occupancy threshold** are automatically identified.

---

# 📦 Dataset

The dataset contains simulated railway operational data including:

| Column          | Description                |
| --------------- | -------------------------- |
| Route           | Train route                |
| Weekend         | 1 = weekend, 0 = weekday   |
| Num_Coaches     | Number of coaches in train |
| Seat_Capacity   | Total seat capacity        |
| Passenger_Count | Number of passengers       |

Synthetic data is generated using:

```
dataset_generator.py
```

---

# 🛠 Technologies Used

* **Python**
* **Pandas**
* **Scikit-learn**
* **Streamlit**
* **Plotly**

---

# 🚀 Future Improvements

Possible enhancements:

* Real-time passenger data integration
* Deep learning demand prediction
* Train timetable optimization
* Passenger flow forecasting
* Deployment on cloud platforms

---

# 👨‍💻 Author

**Harshavardhan**

GitHub:
https://github.com/Harshavardhan-78

---

# ⭐ If you like this project

Give it a **star ⭐ on GitHub** and feel free to contribute!
