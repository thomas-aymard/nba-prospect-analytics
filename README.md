# 🏀 NBA Rookie Performance & All-Star Predictor

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Machine_Learning-orange.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-Interactive_App-red.svg)

## 📌 Overview
This project is an End-to-End Machine Learning pipeline designed to predict whether an NBA rookie has the statistical profile to become a future All-Star. It bridges the gap between sports analytics and predictive modeling, allowing users to input rookie season metrics and receive a real-time probability score.

🌐 **[Try the Live Web App Here]** *(Link to your Streamlit Community Cloud URL once deployed)*

## 🎯 Objectives
- **Data Engineering:** Extract, clean, and preprocess historical NBA player statistics from 1980 to present.
- **Machine Learning:** Train and optimize classification models (Random Forest, XGBoost) to identify complex non-linear patterns in player development.
- **Deployment:** Build an interactive web application using Streamlit to make the ML model accessible to non-technical users (scouts, fans, analysts).

## 🛠️ Tech Stack
- **Data Manipulation:** `Pandas`, `NumPy`
- **Machine Learning:** `Scikit-Learn` (Random Forest Classifier, Hyperparameter tuning)
- **Visualization:** `Matplotlib`, `Seaborn`
- **Deployment:** `Streamlit`, `Joblib`

## 📊 Features & App Usage
1. **Interactive Sliders:** Adjust key rookie metrics such as Points Per Game (PTS), Minutes (MIN), Rebounds (REB), and Field Goal Percentage (FG%).
2. **Real-time Inference:** The model instantly calculates the probability of the player reaching All-Star status.
3. **Feature Importance Visualization:** Understand the "Why" behind the model's decision with a breakdown of which statistical categories influenced the prediction the most.

*Example:* Testing the model with the rookie stats of players like Victor Wembanyama yields a high probability, accurately reflecting the model's capability to identify generational talent early on.

## 🚀 How to Run Locally

1. Clone the repository:
   ```bash
   git clone [https://github.com/thomas-aymard/nba-rookie-predictor.git](https://github.com/thomas-aymard/nba-rookie-predictor.git)
   cd nba-rookie-predictor