![Python](https://img.shields.io/badge/Python-3.9-blue) ![TensorFlow](https://img.shields.io/badge/TensorFlow-2.12-orange) ![Flask](https://img.shields.io/badge/Flask-WebApp-black) ![License](https://img.shields.io/badge/License-MIT-green) ![Status](https://img.shields.io/badge/Project-Complete-brightgreen)
## 🌐 Web App Preview
![App Screenshot](<img width="1440" height="900" alt="Screenshot 2026-04-21 at 1 57 58 AM" src="https://github.com/user-attachments/assets/5f2a8732-3a12-41ad-82f8-cefb70c6261e" />)
# 🌸 ANN Iris Classifier

An interactive machine learning project that demonstrates how an Artificial Neural Network (ANN) can classify iris flower species based on morphological features.

---

## 📌 Project Overview

This project applies concepts of **Neural Networks and Pattern Recognition** to solve a classic classification problem using the **Iris dataset**.

It includes:

* Complete **data preprocessing pipeline**
* A **custom ANN model**
* Model evaluation (accuracy + confusion matrix)
* A **Flask-based interactive web app** for real-time predictions

---

## 🌿 About the Dataset

The Iris dataset is a well-known dataset in machine learning containing **150 samples** of iris flowers across 3 species:

* Setosa
* Versicolor
* Virginica

Each sample includes 4 features:

* Sepal Length
* Sepal Width
* Petal Length
* Petal Width

---

## ⚙️ Project Workflow

### 1. Data Preprocessing

* Feature scaling using **StandardScaler**
* Train-test split for model validation
* Clean and structured dataset preparation

### 2. ANN Model Design

* Input Layer: 4 neurons
* Hidden Layers: 1–2 Dense layers (ReLU activation)
* Output Layer: 3 neurons (Softmax)

### 3. Training

* Loss Function: Categorical Crossentropy
* Optimizer: Adam
* Model trained on preprocessed dataset

### 4. Evaluation

* Accuracy score
* Confusion matrix for performance visualization

---

## 🧠 Model Architecture

Input → Hidden Layer(s) → Output Layer

* Learns non-linear relationships between features
* Classifies input into one of 3 flower species
* Demonstrates fundamentals of deep learning

---

## 🌐 Web Application

The project includes an interactive Flask web interface where users can:

* Input flower measurements
* Get instant predictions
* Visualize ANN behavior

Run locally:

```bash
python app.py
```

Open in browser:

```
http://127.0.0.1:5000
```

---

## 📁 Project Structure

```
ANN Project/
│
├── app.py                # Flask application
├── iris_model.h5        # Trained ANN model
├── scaler.pkl           # Data scaler
├── templates/
│   └── index.html       # Frontend UI
├── .gitignore
└── README.md
```

---

## 📊 Results

* Achieved high classification accuracy on test data
* Efficient separation of classes
* Demonstrates ANN effectiveness on structured datasets

---

## 🚀 Future Improvements

* Add dynamic graphs (training loss, accuracy curves)
* Improve ANN visualization (animated network)
* Deploy as a public web app
* Extend to biomedical datasets

---

## 👩‍💻 Author

**Tanishka Bajpai**
Biomedical Engineering Student
Interested in health-tech, machine learning, and innovation

---

## 💡 Key Takeaway

This project demonstrates how even a simple ANN can effectively solve classification problems and be integrated into a real-world interactive application.

---
