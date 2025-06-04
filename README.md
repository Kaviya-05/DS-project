# 🎯 Career Prediction Model

This project predicts suitable job roles based on a user's **technical skills** and **personality traits** using a machine learning model built with `RandomForestClassifier`. The project is deployed as a **Flask web app on Hugging Face Spaces**, providing an interactive interface for users to explore potential career paths.

👉 **Try the live app here:** [Career Predictor on Hugging Face Spaces](https://huggingface.co/spaces/Ansilin/Career_Path_Predictor)  
*(Replace the above link with your actual Hugging Face URL)*

---

## 📌 Table of Contents
- [Introduction](#introduction)
- [Dataset Description](#dataset-description)
- [Model Training Process](#model-training-process)
- [How It Works](#how-it-works)
- [Deployment Details](#deployment-details)
- [Getting Started Locally](#getting-started-locally)
- [License](#license)

---

## 🧠 Introduction

The **Career Prediction Model** suggests job roles such as _Software Developer_ or _Database Administrator_ based on input values representing an individual's technical and personality attributes.

Key features:
- Trained using `RandomForestClassifier`
- Uses 14 input features (skills and traits)
- Deployed using Flask
- Accessible via a user-friendly interface on Hugging Face Spaces

---

## 📊 Dataset Description

- Source: [Kaggle Dataset ID 7573843](https://www.kaggle.com/datasets)  
- Format: `Prediction_datasetcsv.csv`

**Input Features**:
- **Technical Skills** (rated 0–5):  
  - Computer Architecture  
  - Programming Skills  
  - Project Management  
  - Communication Skills

- **Personality Traits** (normalized 0–1):  
  - Openness  
  - Conscientiousness  
  - Extraversion  
  - Agreeableness  
  - Emotional Range  
  - Conversation  
  - Openness to Change  
  - Hedonism  
  - Self-enhancement  
  - Self-transcendence

**Target Variable**: `Role` (e.g., _Software Developer_, _Database Administrator_)

---

## 🛠️ Model Training Process

The training is performed in `prediction_training.ipynb` and includes:

1. **Data Loading** using `pandas`
2. **EDA** via `ydata-profiling` to understand distributions and missing values
3. **Outlier Handling** with `feature_engine`'s `Winsorizer`
4. **Train-Test Split** with stratification (`80/20`)
5. **Model Training** using `RandomForestClassifier`
6. **Evaluation** with `accuracy_score` and `classification_report`
7. **Saving Artifacts**:  
   - `career_predictor_model1.pkl`  
   - `feature_columns1.pkl`

---

## ⚙️ How It Works

The app accepts user input via sliders (for both skills and traits). The values are passed to a trained `RandomForestClassifier` model which:
- Loads the saved model and feature columns
- Processes the input features
- Predicts a role based on majority voting from decision trees
- Displays the result in a styled modal dialog box

---

## 🚀 Deployment Details

- **Backend**: Flask + Gunicorn (Port 7860)
- **Frontend**: `predict.html` with a clean UI
- **Static Assets**: Served from `/static` (e.g., `background.jpg`)
- **Model Files**:  
  - `career_predictor_model1.pkl`  
  - `feature_columns1.pkl`

### Hosted on Hugging Face Spaces:
👉 [Try It Live](https://huggingface.co/spaces/your-username/your-app-name)

---

## 🧰 Getting Started Locally

### Clone the repo:
```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
