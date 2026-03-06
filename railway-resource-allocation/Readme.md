# 🚆 Smart Railway Resource Allocation System

## 📌 Overview

The **Smart Railway Resource Allocation System** is a data-driven application designed to assist railway planners in analyzing train schedules, platform utilization, and track allocation.

The system provides insights into railway operations and helps planners make better decisions to improve **resource allocation efficiency**, reduce congestion, and identify peak traffic patterns.

The dashboard visualizes railway operational data and provides recommendations for better platform management.

---

# 🎯 Project Objectives

The goal of this project is to:

* Analyze railway operational data
* Identify platform and track usage patterns
* Detect peak traffic hours
* Identify platform congestion
* Recommend optimal platform allocation
* Provide railway planning insights through a visual dashboard

---

# ✨ Key Features

## 1️⃣ System Metrics Dashboard

Displays key railway operational metrics such as:

* Total number of trains
* Total stations in the dataset
* Most active station
* Busiest platform
* Peak traffic hour
* Average platform load

These metrics help railway planners quickly understand the system status.

---

## 2️⃣ Station Traffic Analysis

Visualizes train traffic across different stations to identify:

* High-traffic stations
* Station congestion patterns

---

## 3️⃣ Platform Utilization Analysis

Shows how frequently each platform is used.

This helps planners detect:

* Overloaded platforms
* Underutilized platforms

---

## 4️⃣ Track Usage Analysis

Analyzes how railway tracks are utilized.

Helps planners determine:

* Track congestion
* Track distribution efficiency

---

## 5️⃣ Train Type Distribution

Shows the distribution of different train types:

* Express
* Passenger
* Freight

This helps understand how different train types impact resource allocation.

---

## 6️⃣ Peak Traffic Detection

Identifies the busiest hours when trains arrive.

This helps planners:

* Allocate additional staff
* Manage peak-hour congestion
* Optimize train scheduling

---

## 7️⃣ Platform Congestion Analysis

Displays how many trains are assigned to each platform.

This allows planners to detect congestion and rebalance platform assignments.

---

## 8️⃣ Platform Recommendation System

The system recommends the **least busy platform** for the next incoming train.

This simple decision-support feature helps planners allocate resources more efficiently.

---

# 📊 Dataset

A **synthetic railway dataset** was generated using Python to simulate realistic railway operations.

The dataset includes the following features:

| Column         | Description                                 |
| -------------- | ------------------------------------------- |
| Train_ID       | Unique train identifier                     |
| Station        | Station code                                |
| Arrival_Time   | Train arrival time (minutes of day)         |
| Departure_Time | Train departure time                        |
| Platform       | Platform number assigned                    |
| Track          | Track number used                           |
| Train_Type     | Type of train (Express, Passenger, Freight) |

The dataset is automatically generated using the script:

```
src/generate_dataset.py
```

---

# 🛠 Technology Stack

| Component            | Technology          |
| -------------------- | ------------------- |
| Programming Language | Python              |
| Data Analysis        | Pandas, NumPy       |
| Visualization        | Matplotlib, Seaborn |
| Dashboard            | Streamlit           |
| Version Control      | Git & GitHub        |

---

# 📂 Project Structure

```
railway-resource-allocation
│
├── app
│   └── app.py
│
├── data
│   └── railway_dataset.csv
│
├── src
│   └── generate_dataset.py
│
├── requirements.txt
└── README.md
```

---

# ⚙️ Installation

Clone the repository

```
git clone https://github.com/Harshavardhan-78/Smart-Railway-Resource-Allocation-System
```

Navigate to the project directory

```
cd railway-resource-allocation
```

Install dependencies

```
pip install -r requirements.txt
```

---

# ▶️ Running the Project

## 1️⃣ Generate Dataset

```
python src/generate_dataset.py
```

## 2️⃣ Start the Dashboard

```
streamlit run app/app.py
```

---

# 📈 Expected Outcomes

This system helps railway planners:

* Understand railway traffic patterns
* Detect congestion in platforms and stations
* Identify peak traffic hours
* Improve platform allocation
* Support better railway planning decisions

---

# 🔮 Future Improvements

Possible improvements include:

* Real railway dataset integration
* Advanced scheduling optimization
* Time-series traffic forecasting
* Passenger demand prediction
* AI-based platform allocation

---

# 👨‍💻 Author

Smart Railway Resource Allocation System
Data-Driven Railway Planning Project

