
import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
import joblib


dataset = pd.read_csv("train.csv")

x = dataset.drop("price_range", axis=1)
y = dataset["price_range"]

x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=42
)

scaler = StandardScaler()

x_train_scaled = scaler.fit_transform(x_train)
x_test_scaler = scaler.transform(x_test)


models = {
    "Logistic Regression": LogisticRegression(max_iter=3000),
    "KNN": KNeighborsClassifier(),
    "Gaussian Naive Bayes": GaussianNB(),
    "Decision Tree": DecisionTreeClassifier(random_state=42),
    "SVM": SVC(),
    "Random Forest": RandomForestClassifier(random_state=42),
    "Adaboost": AdaBoostClassifier(random_state=42)
}


param_grids = {

    "Logistic Regression": {
        "C": [0.01, 0.1, 1, 10, 100]
    },

    "KNN": {
        "n_neighbors": [3, 5, 7, 9, 11, 15],
        "weights": ["uniform", "distance"],
        "metric": ["euclidean", "manhattan", "minkowski"]
    },

    "Gaussian Naive Bayes": {
        "var_smoothing": [1e-11, 1e-10, 1e-9, 1e-8, 1e-7, 1e-6]
    },

    "Decision Tree": {
        "criterion": ["gini", "entropy", "log_loss"],
        "max_depth": [None, 5, 10, 15, 20],
        "min_samples_split": [2, 5, 10],
        "min_samples_leaf": [1, 2, 4]
    },

    "SVM": [
        {
        "C": [0.01,1, 10, 100],
        "kernel": ["linear"]
        },
        {
        "C": [0.01,1, 10, 100],
        "kernel": ["rbf"]
        },
        {
        "C": [0.01,1, 10, 100],
        "kernel": ["poly"],
        "gamma": ["scale", "auto"],
        "degree": [2, 3]
        }
    ],

    "Random Forest": {
        "n_estimators": [100, 200, 300],
        "criterion": ["gini", "entropy", "log_loss"],
        "max_depth": [None, 5, 10, 15, 20],
        "min_samples_split": [2, 5, 10],
        "min_samples_leaf": [1, 2, 4],
        "max_features": ["sqrt", "log2", None]
    },

    "Adaboost": {
        "n_estimators": [50, 100, 200, 300],
        "learning_rate": [0.01, 0.05, 0.1, 0.5, 1]
    }
}


best_models = {}

for name, model in models.items():

    grid = GridSearchCV(
        model,
        param_grids[name],
        cv=5,
        scoring="accuracy",
        n_jobs=-1,
        error_score="raise"
    )

    if name in ["Logistic Regression", "KNN", "SVM"]:
        grid.fit(x_train_scaled, y_train)
    else:
        grid.fit(x_train, y_train)

    best_models[name] = grid.best_estimator_

best_model = best_models["Logistic Regression"]

best_model.fit(x_train_scaled, y_train)

joblib.dump(best_model, "mobile_price_model.pkl")
joblib.dump(scaler, "scaler.pkl")

result = []

for name, model in best_models.items():

    if name in ["Logistic Regression", "KNN", "SVM"]:
        model.fit(x_train_scaled, y_train)
        yhat = model.predict(x_test_scaler)
    else:
        model.fit(x_train, y_train)
        yhat = model.predict(x_test)

    accuracy = accuracy_score(y_test, yhat)

    result.append({
        "Model": name,
        "Accuracy": accuracy
    })


result_dataset = pd.DataFrame(result)
result_dataset = result_dataset.sort_values(
    by="Accuracy",
    ascending=False
)


#print("Best Model:", result_dataset.iloc[0]["Model"])
#print("Best Accuracy:", result_dataset.iloc[0]["Accuracy"])