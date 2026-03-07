# 🚆 Smart Railway Resource Planning System

A **data-driven railway planning dashboard** that analyzes historical train data to predict passenger demand and recommend optimal allocation of railway resources such as coaches, trains, and platforms.

This project was developed as a prototype to demonstrate how **data analytics and machine learning can improve railway operational efficiency** without requiring complex infrastructure simulations.

---

# 📌 Problem Statement

Railway networks often face challenges such as:

* Overcrowded trains on high-demand routes
* Underutilized coaches on low-demand routes
* Platform congestion
* Inefficient scheduling decisions

Most scheduling decisions rely on **static planning rather than dynamic data insights**.

This project proposes a **Smart Railway Resource Planning System** that uses historical operational data to predict passenger demand and provide **data-driven recommendations for resource allocation**.

---

# 🎯 Objectives

The system aims to:

* Predict passenger demand for train routes
* Identify overcrowded routes
* Recommend additional coaches or trains
* Improve platform usage
* Provide an interactive dashboard for railway planners

---

# 🧠 Solution Overview

The system processes historical railway data and generates insights using **data visualization and machine learning**.

### Workflow

Dataset → Data Processing → Demand Prediction → Resource Recommendation → Dashboard Visualization

Key components:

1. **Synthetic Dataset Generator**
2. **Demand Prediction Model**
3. **Recommendation Engine**
4. **Interactive Dashboard**

---

# 📊 Features

### 📈 Demand Analysis

Visualize passenger trends across routes and days.

### 🔮 Demand Prediction

Predict passenger demand based on route, capacity, and travel conditions.

### 🚆 Coach Allocation Recommendation

Suggest additional coaches when demand exceeds available capacity.

### 🚄 Train Frequency Suggestions

Recommend additional trains on consistently overcrowded routes.

### 🖥 Interactive Dashboard

User-friendly interface for exploring railway demand patterns.

---

# 🛠 Technology Stack

**Programming Language**

Python

**Libraries**

* Pandas
* NumPy
* Scikit-learn
* Plotly
* Streamlit

---

# 📁 Project Structure

smart-railway-planner/

│

├── data/
│   └── railway_data.csv

├── dataset_generator.py
├── prediction_model.py
├── recommendation_engine.py
├── dashboard.py

├── requirements.txt
└── README.md

---

# 📦 Installation Guide

Follow these steps to run the project locally.

---

# 1️⃣ Clone the Repository

First clone the repository using Git:

```bash
git clone https://github.com/Harshavardhan-78/Smart-Railway-Resource-Allocation-System
```


---

# 2️⃣ Install Dependencies

Install the required Python libraries:

```bash
pip install -r requirements.txt
```

---

# 3️⃣ Generate Synthetic Dataset

Since real railway data cannot be used, a synthetic dataset is generated.

Run the dataset generator:

```bash
python dataset_generator.py
```

This will create:

```
data/railway_data.csv
```

---

# 4️⃣ Run the Dashboard

Start the Streamlit application:

```bash
streamlit run dashboard.py
```

The dashboard will open automatically in your browser.

---

# 📊 Dataset Description

The project uses a **synthetic dataset** designed to simulate railway operations.

### Dataset Fields

| Column          | Description                  |
| --------------- | ---------------------------- |
| Train_ID        | Unique train identifier      |
| Route           | Source-Destination route     |
| Date            | Travel date                  |
| Passenger_Count | Number of passengers         |
| Seat_Capacity   | Total available seats        |
| Num_Coaches     | Number of train coaches      |
| Platform        | Assigned platform number     |
| Delay_Minutes   | Delay in minutes             |
| Weekend         | Indicator for weekend travel |

Passenger demand is generated using realistic assumptions such as:

* Higher demand on weekends
* Route-based demand differences
* Random variations to simulate real-world fluctuations

---

# 🔍 Example Use Case

Example scenario:

Route: **Delhi–Mumbai**

Capacity: **900 seats**

Predicted Demand: **1120 passengers**

System Recommendation:

* Add **4 additional coaches**
* Consider **special train during peak hours**

---

# 📈 Dashboard Insights

The dashboard provides:

* Passenger demand by route
* Weekend vs weekday demand patterns
* Most overcrowded routes
* Predicted passenger demand
* Resource allocation recommendations

---

# ⚠️ Assumptions

* Synthetic data simulates realistic railway demand patterns.
* Each coach is assumed to hold approximately **50 passengers**.
* Demand increases during weekends and peak travel periods.

---

# 🚀 Future Improvements

Potential enhancements include:

* Real-time railway API integration
* Geographic route visualization
* Delay prediction models
* Dynamic platform scheduling
* What-if simulation for train capacity planning

---

# 🤝 Contribution

Contributions are welcome.

To contribute:

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Submit a pull request

---

# 📜 License

This project is developed for educational and hackathon purposes.
