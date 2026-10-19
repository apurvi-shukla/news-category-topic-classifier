# 📰 News Category & Topic Classifier

## 📌 Project Overview
The News Category & Topic Classifier is a Machine Learning project that predicts the category of a news headline or article. It classifies news into four categories: World, Sports, Business, and Sci/Tech.

The project uses **TF-IDF** for text feature extraction and **Logistic Regression** for classification. A **Streamlit** web application allows users to enter news text and view the predicted category.

## 🎯 Objectives
- Classify news articles into four categories.
- Apply Natural Language Processing (NLP) techniques to text data.
- Build and evaluate a Machine Learning classification model.
- Deploy an interactive web interface using Streamlit.

## 📂 Categories
- 🌍 World
- ⚽ Sports
- 📈 Business
- 💻 Sci/Tech

## 🛠️ Tech Stack
- Python
- Pandas
- Scikit-learn
- TF-IDF Vectorization
- Logistic Regression
- Streamlit
- Joblib

## ⚙️ Project Workflow
1. Load and explore the news dataset.
2. Prepare the text data and category labels.
3. Convert text into numerical features using TF-IDF.
4. Train a Logistic Regression classification model.
5. Evaluate the model using classification metrics.
6. Save the trained model using Joblib.
7. Build an interactive Streamlit application for predictions.

## 📊 Model Performance
- **Accuracy:** 92.14%
- **Macro F1-score:** 0.9212

*These are the evaluation results obtained during model testing.*

## 🚀 Run the Project Locally

### 1. Clone the repository
```bash
git clone https://github.com/apurvi-shukla/news-category-topic-classifier.git
cd news-category-topic-classifier
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Streamlit app
```bash
streamlit run app.py
```

## 💡 How to Use
1. Open the Streamlit application.
2. Enter a news headline or article in the text box.
3. Click **Classify News**.
4. View the predicted news category.

## 🔮 Future Improvements
- Add more news categories.
- Improve text preprocessing and model evaluation.
- Deploy the application publicly.
- Add confidence scores for predictions.

  ## 🚀 Live Demo

Try the deployed News Category & Topic Classifier here:

**[Open Live App](https://news-category-topic-classifier-apurvi.streamlit.app/)**

## 👩‍💻 Author
**Apurvi Shukla**

GitHub: [apurvi-shukla](https://github.com/apurvi-shukla)
