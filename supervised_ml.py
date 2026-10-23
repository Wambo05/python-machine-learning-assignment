
# To import the required libraries
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Study hours and examination scores
X = [[1], [2], [3], [4], [5],
     [6], [7], [8], [9], [10]]

y = [30, 40, 45, 55, 65, 70, 80, 85, 90, 95]

# To create and train the model
model = LinearRegression()
model.fit(X, y)

# To ask the user for study hours
hours = float(input("Enter hours studied: "))

# To predict the examination score
score = model.predict([[hours]])

# To display the prediction to two decimal places
print(f"Predicted exam score: {score[0]:.2f}")

# To draw the graph (bonus task)
plt.scatter(X, y, label="Actual scores")
plt.plot(X, model.predict(X), label="Prediction line")
plt.xlabel("Hours Studied")
plt.ylabel("Exam Score")
plt.title("Student Exam Score Prediction")
plt.legend()
plt.show()
