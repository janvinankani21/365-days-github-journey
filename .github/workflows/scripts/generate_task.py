from datetime import datetime
import os

today = datetime.now().strftime("%Y-%m-%d")

folder = f"tasks/{today}"
os.makedirs(folder, exist_ok=True)

with open(f"{folder}/task.txt", "w") as f:
    f.write(f"Learning log for {today}")
