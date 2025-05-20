# 🎮 Steam Dataset EDA Flask App

A simple Flask web app that cleans and analyzes the Steam 200k dataset. It generates visual insights like most played games, total/average playtime, and top users, and displays them using charts.

---

## 🚀 How to Run This Project

### 1. Clone the repository


git clone https://github.com/YOUR_USERNAME/steam-flask-eda.git
cd steam-flask-eda
2. Set up a virtual environment (optional)
bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
3. Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
4. Add dataset
Download the raw dataset (steam-200k.csv) from Kaggle and place it in the project folder.

5. Run the cleaning and EDA scripts
bash
Copy
Edit
python clean.py
python eda.py
6. Start the Flask app
bash
Copy
Edit
python app.py
Then visit: http://127.0.0.1:5000

