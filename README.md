# 🩺 Diabetes Prediction System

An AI-powered web application that predicts the likelihood of diabetes using a Machine Learning model. The application is built with **Python, Scikit-learn, and Streamlit**, allowing users to enter patient health parameters and receive real-time diabetes predictions through an interactive web interface.

---

## 🚀 Live Demo

🔗 **Streamlit App:** *(Add your Streamlit deployment link here)*

---

## 📌 Project Overview

Diabetes is one of the most common chronic diseases worldwide. Early prediction can help individuals seek timely medical advice and improve health outcomes.

This project uses a trained **Support Vector Machine (SVM)** model to predict whether a person is likely to have diabetes based on several medical parameters.

> **Note:** This application is intended for educational purposes only and should not be used as a substitute for professional medical diagnosis.

---

## ✨ Features

-  Predicts diabetes risk using a Machine Learning model
-  Interactive web interface built with Streamlit
-  User-friendly input form
-  Instant prediction results
-  Responsive layout
-  Clean and modern interface

---

## 🛠️ Technologies Used

- Python
- Streamlit
- NumPy
- Scikit-learn
- Pickle

---

## 📂 Dataset

This project is based on the **Pima Indians Diabetes Dataset**, which contains medical diagnostic measurements used to predict diabetes.

### Input Features

- Number of Pregnancies
- Glucose Level
- Blood Pressure
- Skin Thickness
- Insulin Level
- Body Mass Index (BMI)
- Diabetes Pedigree Function
- Age

---

## 🤖 Machine Learning Model

- Algorithm: Support Vector Machine (SVM)
- Language: Python
- Libraries:
  - Scikit-learn
  - NumPy
  - Pickle


## 📁 Project Structure

```
Diabetes-Prediction-System/
│
├── app.py
├── trained_model.sav
├── requirements.txt
├── README.md
├── .gitignore

```

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/your-username/Diabetes-Prediction-System.git
```

### Navigate to the project folder

```bash
cd Diabetes-Prediction-System
```

### Create a virtual environment (Optional)

```bash
python -m venv venv
```

### Activate the virtual environment

**Windows**

```bash
venv\Scripts\activate
```

**Linux/macOS**

```bash
source venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the application

```bash
streamlit run app.py
```

---

## 📈 Future Improvements

- Add prediction probability/confidence score
- Improve UI with charts and visualizations
- Store prediction history
- Add user authentication
- Deploy using Docker and cloud platforms
- Support multiple machine learning models

---

## 👨‍💻 Author

**Madhavi Sahani**

---

## ⭐ If you found this project useful

Please consider giving this repository a **⭐ Star**.
