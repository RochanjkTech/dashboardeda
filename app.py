from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

# Load cleaned data
df = pd.read_csv('cleaned_steam_data.csv', header=None)
df.columns = ['user_id', 'game_name', 'behavior', 'hours']

# Pre-calculate results for display
top10_games = df[df['behavior'] == 'play']['game_name'].value_counts().head(10)
total_hours = df[df['behavior'] == 'play'].groupby('game_name')['hours'].sum().sort_values(ascending=False).head(10)
avg_hours = df[df['behavior'] == 'play'].groupby('game_name')['hours'].mean().sort_values(ascending=False).head(10)
top10_users = df[df['behavior'] == 'play'].groupby('user_id')['hours'].sum().sort_values(ascending=False).head(10)

@app.route('/')
def index():
    return render_template('index.html',
                           top10_games=top10_games,
                           total_hours=total_hours,
                           avg_hours=avg_hours,
                           top10_users=top10_users)

if __name__ == '__main__':
    app.run(debug=True)
