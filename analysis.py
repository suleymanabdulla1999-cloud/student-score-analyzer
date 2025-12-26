import pandas as pd

data = pd.read_csv("scores.csv")

average = data["score"].mean()
highest = data["score"].max()
lowest = data["score"].min()
pass_rate = (data["score"] >= 50).mean() * 100

print("Average score:", average)
print("Highest score:", highest)
print("Lowest score:", lowest)
print("Pass rate:", pass_rate, "%")
