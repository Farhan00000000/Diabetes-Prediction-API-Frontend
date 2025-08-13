## Diabetes Prediction API (Backend)
This repository contains the **Backend API** for predicting diabetes using a trained machine learning model. The API is built with FastAPI and is designed to serve predictions asynchronously. It powers the frontend Streamlit app that allows users to input patient data and receive real-time diabetes predictions.

---

## Features
- REST API built with FastAPI
- Asynchronous endpoints for faster performance
- `/health` endpoint to check service status
- `/predict` endpoint to get diabetes predictions with confidence scores
- Optional `/metrics` endpoint to view evaluation metrics of the model on the test dataset
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
## Project Structure
  ```bash
 backend/
│
├── main.py               # FastAPI application
├── diabetes_model.pkl    # Saved ML model
├── scaler.pkl            # Feature scaler
├── requirements.txt      # Python dependencies
├── Dockerfile            # Dockerfile for containerization
├── README.md             # Project documentation
└── __pycache__/          # Python cache files

  ```

---

## Dataset
- **Pima Indians Diabetes Dataset** from Kaggle
[Dataset Link](https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database)
- Features include: Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age
- Target variable: Outcome (0 = Not Diabetic, 1 = Diabetic)

---

## Model Training
- Model trained using **Logistic Regression** and **Random Forest**
- Split dataset into train/test sets
- Evaluated using: **Accuracy, Precision, Recall, F1 Score**
- Best model saved as `diabetes_model.pkl`
- Feature scaler saved as `scaler.pkl`

---

## Running Locally
1. Clone the repository:
   ```bash
   git clone https://github.com/Farhan00000000/Diabetes-Prediction-API-Frontend.git
   cd Diabetes-Prediction-API-Frontend
   ```
2. Create and activate a virtual environment:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the API server:
   ```bash
   uvicorn main:app --reload
   ```
5. Open FastAPI docs to test endpoints:
   ```bash
   http://127.0.0.1:8000/docs
   ```
- *Note: Docker must be installed and running.*
 ---

# API Endpoints
## GET /health
- Check if the service is running.
**Response:**
```json
{
  "status": "ok"
}
```
## POST /predict
- Get diabetes prediction for patient data.
**Request Example:**
```json
{
  "Pregnancies": 3,
  "Glucose": 145,
  "BloodPressure": 70,
  "SkinThickness": 20,
  "Insulin": 85,
  "BMI": 33.6,
  "DiabetesPedigreeFunction": 0.35,
  "Age": 29
}

```
**Response Example:**
```json
{
  "prediction": 0,
  "result": "Not Diabetic",
  "confidence": 0.87
}
```
## GET /metrics (Optional)
- Returns evaluation metrics of the trained model on the test dataset.

---

## Docker
1. Build Docker image:
 ```bash
docker build -t diabetes-api .
```  
2. Run Docker container:
```bash
docker run -p 8000:8000 diabetes-api
```

- **Note:** Ensure the model files `diabetes_model.pkl` and `scaler.pkl` are in the same directory as `main.py`.

---

## Deployment
- Render service (Backend API): (https://diabetes-prediction-api-frontend.onrender.com)

---

## GitHub Repository
- Backend repo: [Diabetes-Prediction-API-Frontend](https://github.com/Farhan00000000/Diabetes-Prediction-API-Frontend.git)
- Frontend repo: [diabetes-prediction-app](https://github.com/Farhan00000000/diabetes-prediction-app.git)

---

## Author
[Farhan00000000](https://github.com/Farhan00000000)

---

## License
This project is open-source and available under the MIT License.

---

## This README now includes:
- Project description
- Features and technologies
- Folder structure
- Dataset reference
- Model details and metrics
- Local setup instructions
- API endpoints with examples
- Docker instructions
- Deployment links
- GitHub repository links








