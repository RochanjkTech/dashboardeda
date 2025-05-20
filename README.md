# 🎮 Steam Dataset EDA Flask App

A simple and interactive Flask web app for exploring and analyzing the **Steam 200k dataset**. It provides insights into user behavior, most played games, and overall statistics using clean and informative visualizations.

---

## 📊 Features

- Data cleaning and preprocessing of the raw `steam-200k.csv` dataset.
- Exploratory Data Analysis (EDA) with visualizations.
- Insights such as:
  - Most played games
  - Average and total playtime
  - Top active users
- Interactive charts and a user-friendly dashboard powered by Flask.

---

## 🚀 How to Run This Project

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/steam-flask-eda.git
cd steam-flask-eda
```
Set Up a Virtual Environment (Optional)
```bash

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

Install Dependencies
```bash

pip install -r requirements.txt

```

 Run the Cleaning and EDA Scripts
```bash

python clean.py
python eda.py
```
Start Flask App
```bash
python app.py
```

###Now open your browser and go to: http://127.0.0.1:5000
