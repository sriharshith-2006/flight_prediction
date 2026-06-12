# ✈️ Flight Price Prediction using Machine Learning

## 📌 Project Overview

This project aims to predict airline ticket prices based on various flight-related features such as airline, source, destination, duration, number of stops, departure time, and arrival time.

The objective is to build a regression model that can estimate flight prices accurately and help travelers make informed decisions.

---

## 📂 Dataset Features

The dataset contains the following information:

- Airline
- Source
- Destination
- Route
- Total Stops
- Date of Journey
- Departure Time
- Arrival Time
- Duration
- Price (Target Variable)

---

## 🛠️ Data Preprocessing

The following preprocessing steps were performed:

### Date Features
- Extracted:
  - Day
  - Month
  - Year

### Time Features
- Departure Hour
- Departure Minute
- Arrival Hour
- Arrival Minute

### Duration Feature
- Converted duration from format:
  - `2h 50m`
  - `1h 20m`
  
  into total minutes.

### Categorical Encoding
- Airline encoded using One-Hot Encoding
- Source and Destination encoded
- Total Stops encoded using Ordinal Encoding

### Feature Selection
- Removed redundant columns after feature extraction:
  - Route
  - Original date/time columns

---

## 🤖 Models Used

### Random Forest Regressor
Used as a baseline model for comparison.

### XGBoost Regressor
Used as the final model due to superior performance on tabular data.

---

## 📊 Model Performance

| Metric | Training | Testing |
|----------|----------|----------|
| MAE | 868.57 | 1157.97 |
| R² Score | 0.928 | 0.849 |

### Interpretation

- The model explains approximately **85% of the variance** in unseen flight prices.
- Average prediction error is approximately **₹1158** on the test set.
- The model performs well on common flight routes and price ranges.

---

## 📈 Actual vs Predicted Prices

The scatter plot below compares actual flight prices against predicted flight prices.

- Strong positive correlation between actual and predicted values.
- Most predictions closely follow the expected trend.
- Some deviation exists for high-priced flights, indicating opportunities for further improvement.

---

## 🧰 Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-Learn
- XGBoost
- Streamlit

##  Live performance

🚀 Live Demo: [Click here to view the app]

(https://flight-prediction-site.streamlit.app)


## 🚀 Future Improvements

- Hyperparameter tuning using GridSearchCV
- Cross-validation
- Feature engineering for route complexity

## 🎯 Conclusion

This project demonstrates a complete machine learning workflow including:

- Data Cleaning
- Feature Engineering
- Exploratory Data Analysis
- Model Training
- Model Evaluation
- Performance Visualization
- Model Deployment using Streamlit

The final XGBoost model achieved strong predictive performance and serves as a solid baseline for real-world flight price prediction systems.

---
