import pandas as pd

# Load leaderboard CSV
leaderboard_file = "final_leaderboard.csv"
df = pd.read_csv(leaderboard_file)

# Sort by accuracy descending
df = df.sort_values(by="Accuracy", ascending=False).reset_index(drop=True)

# Compute ranks with ties
ranks = []
prev_score = None
prev_rank = 0
skip_count = 0

for i, score in enumerate(df["Accuracy"], start=1):
    if score == prev_score:
        rank = prev_rank
        skip_count += 1
    else:
        rank = prev_rank + 1 + skip_count
        skip_count = 0
    ranks.append(rank)
    prev_score = score
    prev_rank = rank

df["Rank"] = ranks

# Assign medal classes
def medal_class(rank):
    if rank == 1:
        return "gold"
    elif rank == 2:
        return "silver"
    elif rank == 3:
        return "bronze"
    else:
        return ""

df["Class"] = df["Rank"].apply(medal_class)

# Generate HTML
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>GNN CoRA Competition Leaderboard</title>
<style>
body {{ font-family: Arial, sans-serif; background: #f9f9f9; padding: 40px; }}
h1 {{ text-align: center; margin-bottom: 30px; }}
table {{ border-collapse: collapse; margin: auto; width: 60%; background: white; box-shadow: 0 4px 8px rgba(0,0,0,0.1); }}
th, td {{ border: 1px solid #ddd; padding: 12px; text-align: center; }}
th {{ background-color: #2c3e50; color: white; }}
tr:nth-child(even) {{ background-color: #f2f2f2; }}
.gold {{ background-color: #FFD700; color: black; font-weight: bold; }}
.silver {{ background-color: #C0C0C0; color: black; font-weight: bold; }}
.bronze {{ background-color: #CD7F32; color: black; font-weight: bold; }}
@media (max-width: 768px) {{ table {{ width: 90%; }} }}
</style>
</head>
<body>
<h1>🏆 GNN CoRA Competition Leaderboard</h1>
<table>
<thead>
<tr><th>Rank</th><th>Team</th><th>Accuracy</th></tr>
</thead>
<tbody>
"""

for _, row in df.iterrows():
    rank_display = row["Rank"]
    team = row["Team"]
    acc = f"{row['Accuracy']:.2f}%"
    class_name = row["Class"]
    html_content += f'<tr class="{class_name}"><td>{rank_display}</td><td>{team}</td><td>{acc}</td></tr>\n'

html_content += """
</tbody>
</table>
</body>
</html>
"""

# Save HTML
with open("final_leaderboard.html", "w") as f:
    f.write(html_content)

print("Leaderboard HTML updated successfully.")
