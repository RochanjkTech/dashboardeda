import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv('cleaned_steam_data.csv', header=None)


df.columns = ['user_id', 'game_name', 'behavior', 'hours']


print("Basic Info:")
print(df.info())
print("\nMissing Values:\n", df.isnull().sum())
print("\nBehavior Distribution:\n", df['behavior'].value_counts())


print("\nNumber of Unique Users:", df['user_id'].nunique())


print("\nTop 10 Most Played Games:")
print(df[df['behavior'] == 'play']['game_name'].value_counts().head(10))


total_hours = df[df['behavior'] == 'play'].groupby('game_name')['hours'].sum().sort_values(ascending=False)
print("\nTop 10 Games by Total Hours Played:\n", total_hours.head(10))

avg_hours = df[df['behavior'] == 'play'].groupby('game_name')['hours'].mean().sort_values(ascending=False)
print("\nTop 10 Games by Average Play Time:\n", avg_hours.head(10))


user_hours = df[df['behavior'] == 'play'].groupby('user_id')['hours'].sum().sort_values(ascending=False)
print("\nTop 10 Users by Total Hours Played:\n", user_hours.head(10))


plt.figure(figsize=(6, 4))
sns.countplot(x='behavior', data=df)
plt.title("Distribution of Behaviors")
plt.xlabel("Behavior Type")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("behavior_distribution.png")
plt.close()

plt.figure(figsize=(10, 6))
top10_games = total_hours.head(10)
sns.barplot(x=top10_games.values, y=top10_games.index, palette='viridis')
plt.title("Top 10 Games by Total Play Hours")
plt.xlabel("Total Hours Played")
plt.ylabel("Game Name")
plt.tight_layout()
plt.savefig("top10_played_games.png")
plt.close()


plt.figure(figsize=(10, 6))
top10_users = user_hours.head(10)
sns.barplot(x=top10_users.values, y=top10_users.index, palette='magma')
plt.title("Top 10 Users by Total Play Hours")
plt.xlabel("Total Hours Played")
plt.ylabel("User ID")
plt.tight_layout()
plt.savefig("top10_users_play.png")
plt.close()
