# 🚆 Smart Railway Resource Planning System

## Overview

This project demonstrates how railway planners can use data-driven methods to improve resource allocation.

The system analyzes train schedules, platform usage, and delays to provide insights for better railway management.

## Features

- Platform usage analysis
- Train delay distribution visualization
- Delay prediction using Machine Learning
- Interactive Streamlit dashboard

## Dataset

Synthetic dataset generated using Python containing:

- Train_ID
- Arrival_Time
- Departure_Time
- Platform
- Track
- Train_Type
- Delay_Minutes

## Technology Stack

Python  
Pandas  
NumPy  
Scikit-learn  
Streamlit  
Matplotlib  
Seaborn  

## Run the Project

Generate dataset

python src/generate_dataset.py

Train model

python src/train_model.py

Run dashboard

streamlit run app/app.py