# Smartphone Price Prediction

This project is an end-to-end machine learning system that predicts smartphone prices based on their specifications.
Instead of using a ready-made dataset, the entire pipeline was built from scratch — starting from web scraping to deployment.

---

## Project Overview

The goal of this project is to simulate a real-world data science workflow:

- Collect raw data from the web  
- Clean and preprocess messy data  
- Perform feature engineering  
- Build and optimize machine learning models  
- Deploy the model as an interactive web app  

---

## Data Collection

- Data scraped from Smartprix using Selenium  
- Handled dynamic content loading  
- Extracted raw and unstructured data  

---

## Data Cleaning & Preprocessing

- Extracted meaningful features like:
  - RAM, Storage, Processor Speed (GHz), Battery, etc.  
- Handled missing values using:
  - Simple Imputer  
  - KNN Imputer  
  - Iterative Imputer  
- Standardized inconsistent formats  

---

## Feature Engineering

- Performance Score = RAM × Processor Speed  
- Camera Score = Front Camera + Rear Camera  
- Processor Tier classification (Low / Mid / High)  

---

## Exploratory Data Analysis

- Univariate, Bivariate, and Multivariate analysis  
- Identified key factors affecting price:
  - Processor performance  
  - RAM and storage  
  - Battery capacity  

---

## Machine Learning

- Built pipeline using ColumnTransformer
- Applied:
  - OneHot Encoding  
  - Ordinal Encoding  
  - Robust Scaling  

### Models Used:

- Linear Regression  
- Decision Tree  
- Random Forest  
- XGBoost  

---

## Hyperparameter Tuning

- Used:
  - GridSearchCV  
  - Optuna  

- Achieved:
  - **R² Score ≈ 0.93**  
  - Minimal overfitting (train/test scores close)

---

## Feature Importance

Key features influencing price:
- Processor speed  
- Performance score  
- Storage (ROM)  
- RAM  

---

## Deployment

- Built using **Streamlit**  
- User can input smartphone specifications  
- Model predicts price instantly  

---

## Tech Stack

- Python  
- Pandas, NumPy  
- Scikit-learn  
- XGBoost  
- Optuna  
- Selenium  
- Streamlit  

---

## Key Learning

Real-world data science is not just about building models —  
it’s about handling messy data, creating meaningful features, and building complete systems.

---

## 🔗 Demo

Run locally using:
streamlit run app.py

---

