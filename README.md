# mobile_price_classification
This project focuses on determining mobile phone prices based on their specifications. Although the dataset is somewhat dated, Streamlit makes it easy to view the values.
📱 Mobile Price Classification

A machine learning project for predicting the price range of mobile phones based on their technical specifications.

The project includes data exploration, preprocessing, model selection using GridSearchCV, and deployment of the final model as an interactive Streamlit web application.

📊 Dataset

The dataset contains 21 columns describing different mobile phone specifications.

The target variable is:

* price_range — the price category of the mobile phone

The dataset does not contain missing values, so no missing-value imputation was required.

The dataset was also examined for data quality and noise. No major noise-related issues were identified during the analysis.

🔍 Exploratory Data Analysis

The dataset was explored to understand:

* Feature distributions
* Relationships between features
* The target variable
* Data types and structure
* Potential data quality issues

Since the dataset contains no missing values, the preprocessing pipeline did not require handling null values.

🤖 Model Development

Different machine learning approaches were considered for the classification task.

To select the best-performing model and hyperparameters, GridSearchCV was used. This allowed the model configuration to be systematically evaluated instead of relying on manually selected parameters.

After comparing the results, the best configuration obtained through Grid Search was selected as the final model.

🎯 Prediction Task

The goal is to predict the price range of a mobile phone from its available technical specifications.

The problem is a multi-class classification task, where the model predicts the corresponding price category.

🌐 Streamlit Application

After selecting the final model, the trained model was integrated into a Streamlit application.

The application allows users to enter mobile phone specifications and receive a predicted price range from the trained machine learning model.

Application workflow

User Input
    ↓
Feature Processing
    ↓
Trained ML Model
    ↓
Price Range Prediction

🛠️ Technologies

* Python
* Pandas
* NumPy
* Scikit-learn
* Matplotlib
* Seaborn
* GridSearchCV
* Streamlit

📂 Project Structure

Mobile-Price-Classification/
│
├── 
│   └── train.csv
│
├── 
│   └──main.py
│
├── app.py
├── requirements.txt
└── README.md

🚀 Running the Project

Install the required dependencies:

pip install -r requirements.txt

Run the Streamlit application:

streamlit run app.py

The application will open in your browser.

💡 Project Highlights

* Dataset with 21 columns
* No missing values
* Data exploration and preprocessing
* Hyperparameter optimization using GridSearchCV
* Selection of the best-performing model
* Interactive prediction interface built with Streamlit

👩🏻‍💻 Author

Yekta

Software Engineering Student | AI & Machine Learning Enthusiast
