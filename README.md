
# Python Machine Learning Assignment

**Student Name:** Lucy Wambui_1528

## Project Description

This project demonstrates supervised and unsupervised
machine learning using Python.

### Part A: Student Exam Score Prediction

Linear Regression is used to predict examination scores
based on the number of hours a student studies.

The model learns from the supplied study hours and scores,
then predicts a score for new study-hour input.

### Part B: Customer Segmentation

K-Means Clustering is used to group ten supermarket customers
based on monthly spending and monthly shopping visits.

StandardScaler is used to scale the data before clustering.
The program displays cluster assignments, cluster counts
and a scatter plot.

## Installation Instructions

1. Install Python.
2. Open the project folder in VS Code.
3. Create a virtual environment:

   python -m venv .venv

4. Activate it in Windows PowerShell:

   .\.venv\Scripts\Activate.ps1

5. Install the required libraries:

   python -m pip install -r requirements.txt

## How to Run the Programs

Run the supervised learning program:

    python supervised_ml.py

Run the unsupervised learning program:

    python unsupervised_ml.py

## Theory Questions

### 1. What is supervised machine learning?

Supervised machine learning trains a model using labelled
data that contains inputs and known answers. The model
learns from the examples to predict outputs for new data.

### 2. What is unsupervised machine learning?

Unsupervised machine learning identifies patterns or groups
in data without predefined target labels.

### 3. What is the difference between supervised and
unsupervised learning?

Supervised learning uses known target values to train a model.
Unsupervised learning discovers patterns or groups without
known target values.

### 4. Why is Linear Regression supervised learning?

Linear Regression learns from study hours and their known
examination scores to predict scores for new inputs.

### 5. Why is K-Means unsupervised learning?

K-Means groups customers based on similarities in their
spending and shopping visits without predefined group labels.

### 6. What is the difference between fit() and predict()?

fit() trains a model using data. predict() uses a trained
model to estimate an output for new input data.
K-Means can also use fit_predict() to train the model and
return cluster assignments for the supplied data.

### 7. Give two real-world applications of supervised
learning and two of unsupervised learning.

Supervised learning:
1. Predicting house prices.
2. Detecting fraudulent financial transactions.

Unsupervised learning:
1. Grouping supermarket customers by shopping behaviour.
2. Grouping news articles by similar content.

## Conclusion

This assignment demonstrates how Linear Regression can
predict numerical values and how K-Means can group similar
data points.
