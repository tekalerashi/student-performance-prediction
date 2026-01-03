# Student Performance Prediction using Machine Learning

## Project Overview
This project predicts the **final score of a student** based on their **study hours, attendance, and previous academic performance** using Machine Learning.  
It demonstrates a **complete end-to-end ML workflow**, from data loading to model saving and GitHub version control.

---

## Problem Statement
To build a machine learning model that can predict student academic performance using historical data.

---

## Type of Machine Learning
- **Supervised Learning**
- **Regression Problem**

**Reason:**
- The dataset contains labeled output (`final_score`)
- The output is a continuous numerical value

---

## Algorithm Used
### Linear Regression

**Why Linear Regression?**
- Used for predicting continuous numerical values
- Simple and efficient
- Beginner-friendly and easy to interpret

---

## Dataset Description
The dataset is stored in CSV format and contains the following features:

| Feature Name | Description |
|-------------|------------|
| study_hours | Number of hours a student studies |
| attendance | Attendance percentage |
| previous_score | Previous exam score |
| final_score | Final exam score (Target variable) |

---

## Technologies Used
- Python  
- Pandas  
- NumPy  
- Scikit-learn  
- Joblib  
- Git & GitHub  
- VS Code  

---

## Project Workflow
1. Load dataset using Pandas  
2. Select input features and target variable  
3. Split data into training and testing sets  
4. Train Linear Regression model  
5. Predict student scores  
6. Evaluate model performance  
7. Save trained model  

---

## Model Evaluation
The model is evaluated using:
- **Mean Absolute Error (MAE)** – measures average prediction error  
- **R² Score** – measures how well the model fits the data  

---

## How to Run the Project
1. Clone the repository  
2. Create and activate a virtual environment  
3. Install required libraries  
4. Run the Python file:

```bash
python student_ml.py
