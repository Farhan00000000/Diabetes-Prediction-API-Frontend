## Diabetes Prediction API (Backend)
This repository contains the **Backend API** for predicting diabetes using a trained machine learning model. The API is built with FastAPI and is designed to serve predictions asynchronously. It powers the frontend Streamlit app that allows users to input patient data and receive real-time diabetes predictions.

---

## Features
- REST API built with FastAPI
- Asynchronous endpoints for faster performance
- /health endpoint to check service status
- /predict endpoint to get diabetes predictions with confidence scores
- Optional /metrics endpoint to view evaluation metrics of the model on the test dataset
- Model trained using **Scikit-learn** with at least two classifiers (e.g., Logistic Regression, Random Forest)
- Dockerized for container deployment
- Hosted on **Render**

---

## Technologies Used
- Python 3
- FastAPI
- Scikit-learn
- Joblib (for saving/loading models)
- Docker

---

