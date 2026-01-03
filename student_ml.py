import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error,r2_score
import joblib
data = pd.read_csv("student_data.csv")
print("Dataset: ")
print(data)
x= data[["study_hours","attendance","previous_score"]]
y= data['final_score']
x_train, x_test, y_train, y_test = train_test_split(x, y,test_size=0.2,random_state=42)
model = LinearRegression()
model.fit(x_train,y_train)
y_pred = model.predict(x_test)
mae = mean_absolute_error(y_test,y_pred)
r2=r2_score(y_test,y_pred)
print("\nModel Evaluation: ")
print("Mean Absolute Error: ",mae)
print("r2 Score: ",r2)
joblib.dump(model,"model.pkl")
print("\nmodel saved as model.pkl")

new_student = np.array([[7,85,75]])
predicted_score =model.predict(new_student)
print("\npredicted final score:",predicted_score[0])
