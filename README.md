# 📊 YouTube Data Analysis and Category Prediction

## 📌 Project Overview

This project analyzes YouTube video performance using **Python, Pandas, Matplotlib, and Seaborn**, and applies **Machine Learning (Scikit-learn)** to predict video categories. It focuses on understanding engagement metrics such as views, likes, comments, and watch time.

## 📂 Dataset

A custom dataset was created with the following features:

* Video Title
* Category
* Upload Date
* Upload Day
* Views
* Likes
* Comments
* Watch Time

## 🛠️ Tools Used

* **Python**
* **Pandas**
* **Matplotlib**
* **Seaborn**
* **Scikit-learn**

## ⚙️ Workflow

### 1. Data Loading

* Created dataset using Python dictionary
* Converted into Pandas DataFrame
* Inspected using `info()` and `describe()`

### 2. Data Analysis

Performed various analyses such as:

* Sorting videos by views, comments, and watch time
* Calculating **Engagement Rate** (Likes / Views)
* Identifying top-performing videos
* Grouping data by category and upload day

### 3. Exploratory Data Analysis (EDA)

Key insights explored:

* Category-wise performance
* Engagement trends
* Upload day impact on views

### 4. Data Visualization

Visualizations created using **Matplotlib and Seaborn**:

* **Bar Chart** → Videos vs Views
* **Line Plot** → Engagement Rate vs Views
* **Scatter Plot (Seaborn)** → Likes vs Comments
* **Histogram (Seaborn)** → Distribution of Views

### 5. Machine Learning

#### 🔹 Linear Regression

* Used to predict **Views** based on **Likes**
* Model: `LinearRegression`

#### 🔹 Classification Model

* Predicted **Category** using:

  * Likes
  * Views
* Model: `LogisticRegression`
* Used `LabelEncoder` to encode categorical values

### 6. Model Evaluation

#### ✅ Confusion Matrix

* Implemented using `sklearn.metrics.confusion_matrix`
* Visualized using **Seaborn heatmap**

#### Confusion Matrix Insights:

* Shows correct and incorrect predictions
* Helps evaluate classification performance
* Easy to interpret using graphical representation

## 📊 Key Insights

* Higher likes generally lead to higher views
* Engagement rate helps identify high-performing content
* Certain categories perform better in terms of views
* Upload day influences average performance

## 📈 Project Structure

```bash
youtube-analysis/
│
├── analysis.py
└── README.md
```

## 🚀 Conclusion

This project demonstrates:

* Data analysis using Pandas
* Data visualization using Matplotlib and Seaborn
* Basic machine learning models (Regression & Classification)
* Model evaluation using confusion matrix visualization

It is a great example of combining **EDA + Visualization + Machine Learning** in a single project.

---

Feel free to extend this project by adding more data, improving models, or deploying it as a web app!
