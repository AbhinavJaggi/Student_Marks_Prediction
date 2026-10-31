# 🎓 Student Marks Prediction

A Machine Learning web application that predicts student academic scores based on weekly self-study hours, attendance percentage, and class participation.

## 🚀 Live Demo

**Try the application here:**

[Student Marks Predictor – Live Website](https://studentmarksprediction-prvjvjkwrczqxbiwrbvaqr.streamlit.app/)

## 📌 Project Overview

This project uses Linear Regression, a supervised Machine Learning algorithm, to predict students' total scores based on three academic features.

The project covers the complete ML workflow, from data exploration and preprocessing to model training, evaluation, and deployment as a web application.

## ✨ Features

- Predict student scores using three input features.
- Interactive web interface built with Streamlit.
- Trained Machine Learning model loaded using Joblib.
- Real-time predictions.

## 📊 Dataset

The project uses a dataset containing student academic information.

**Features used:**
- Weekly Self Study Hours
- Attendance Percentage
- Class Participation

**Target Variable:**
- Total Score

A sample of 10,000 records was used for model development.

## 🧠 Machine Learning Model

**Algorithm:** Linear Regression

**Model Evaluation Results:**

| Metric | Result |
|---|---:|
| MAE | 7.10 |
| MSE | 81.18 |
| RMSE | 9.01 |
| R² Score | 0.674 |

The model achieved an R² score of approximately 67.39% on the test dataset.

## 🛠️ Technologies Used

- Python
- NumPy
- Pandas
- Matplotlib
- Scikit-learn
- Streamlit
- Joblib
- Google Colab
- GitHub

## 📂 Project Structure

```text
Student_Marks_Prediction/
│
├── Student_Marks_Prediction.ipynb
├── app.py
├── model.joblib
├── requirements.txt
└── README.md
```

## ⚙️ Run Locally

1. Clone the repository:

```bash
git clone https://github.com/AbhinavJaggi/Student_Marks_Prediction.git
```

2. Navigate to the project folder:

```bash
cd Student_Marks_Prediction
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the application:

```bash
streamlit run app.py
```

## 👨‍💻 Author

**Abhinav Jaggi**

[GitHub Profile](https://github.com/AbhinavJaggi)

---

⭐ If you find this project interesting, feel free to explore the repository!
