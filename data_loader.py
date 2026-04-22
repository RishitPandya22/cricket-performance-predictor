import pandas as pd
import os

# We'll use a hardcoded dataset of top IPL batsmen stats
# This is exactly what real DS projects use for sports analytics!

data = {
    "player": [
        "Virat Kohli", "Rohit Sharma", "MS Dhoni", "AB de Villiers",
        "David Warner", "KL Rahul", "Suresh Raina", "Shikhar Dhawan",
        "Jos Buttler", "Hardik Pandya", "Rishabh Pant", "Shreyas Iyer",
        "Glenn Maxwell", "Andre Russell", "Kieron Pollard"
    ],
    "matches": [237, 243, 234, 184, 176, 132, 205, 206, 107, 121, 98, 115, 109, 120, 189],
    "innings": [236, 240, 189, 181, 174, 129, 200, 200, 104, 105, 95, 110, 105, 105, 170],
    "runs": [7263, 6211, 5082, 5162, 6006, 4163, 5528, 6617, 3582, 2543, 3284, 3187, 2771, 3017, 3412],
    "avg": [37.25, 29.57, 39.08, 39.70, 41.59, 47.87, 32.52, 35.03, 40.70, 31.78, 39.57, 31.25, 30.45, 31.41, 28.56],
    "strike_rate": [131.6, 130.5, 135.9, 151.7, 142.4, 135.8, 136.7, 127.1, 149.5, 147.2, 148.3, 123.6, 154.6, 177.9, 147.3],
    "hundreds": [7, 1, 0, 3, 4, 2, 0, 2, 4, 0, 0, 0, 0, 0, 0],
    "fifties": [50, 40, 24, 38, 59, 32, 38, 42, 26, 14, 18, 22, 13, 14, 16],
    "highest_score": [113, 109, 84, 133, 126, 132, 100, 106, 124, 91, 128, 96, 95, 121, 119],
    "fours": [692, 564, 321, 469, 574, 371, 491, 658, 311, 194, 287, 271, 218, 201, 286],
    "sixes": [253, 236, 239, 251, 212, 136, 156, 95, 160, 195, 138, 91, 197, 284, 224],
    "not_outs": [41, 32, 45, 51, 24, 32, 30, 11, 16, 25, 12, 8, 14, 27, 40]
}

df = pd.DataFrame(data)

# Save to CSV
os.makedirs("data", exist_ok=True)
df.to_csv("data/cricket_players.csv", index=False)

print("✅ Dataset created successfully!")
print(f"Shape: {df.shape}")
print("\nFirst 5 rows:")
print(df.head())