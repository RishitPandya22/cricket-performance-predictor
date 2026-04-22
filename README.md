# 🏏 Cricket Player Performance Predictor

![Python](https://img.shields.io/badge/Python-3.13-blue?style=for-the-badge&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-Live-red?style=for-the-badge&logo=streamlit)
![scikit-learn](https://img.shields.io/badge/scikit--learn-ML-orange?style=for-the-badge&logo=scikit-learn)
![GitHub](https://img.shields.io/badge/GitHub-Public-black?style=for-the-badge&logo=github)

> A Machine Learning web app that predicts whether an IPL cricket player is **Elite**, **Good**, or **Average** based on their career statistics — built with Random Forest and deployed on Streamlit Cloud.

🚀 **Live App:** [pandya-ml-app.streamlit.app](https://pandya-ml-app.streamlit.app)

---

## 📸 Features

- 🎯 **Real-time ML Prediction** — Enter any player's stats and instantly get a performance prediction
- 📱 **FIFA-Style Player Cards** — Visual cards with overall ratings for all 15 IPL legends
- 🏆 **Interactive Leaderboard** — Rank players by runs, average, strike rate, sixes and more
- 🔍 **Head-to-Head Comparison** — Compare any 2 players with a radar chart
- 📤 **CSV Upload** — Upload your own dataset and get batch predictions
- 📊 **Analytics Dashboard** — EDA charts including scatter plots, bar charts and heatmaps

---

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| Python 3.13 | Core programming language |
| pandas & numpy | Data manipulation |
| scikit-learn | Random Forest ML model |
| Streamlit | Web app framework |
| matplotlib & seaborn | Data visualisation |
| GitHub + Streamlit Cloud | Version control & deployment |

---

## 🤖 ML Model Details

- **Algorithm:** Random Forest Classifier
- **Trees:** 100 estimators
- **Features used:** matches, innings, runs, strike rate, hundreds, fifties, highest score, fours, sixes, not outs
- **Target variable:** Performance category (Elite / Good / Average)
- **Training data:** 15 IPL legends including Virat Kohli, Rohit Sharma, MS Dhoni and more

### Performance Categories:
| Category | Batting Average |
|---|---|
| 🌟 Elite | 40+ |
| 👍 Good | 32 - 39 |
| 📈 Average | Below 32 |

---

## 📁 Project Structure
cricket-performance-predictor/
│
├── app.py                  ← Streamlit web app
├── model.py                ← ML model training script
├── data_loader.py          ← Dataset creation script
├── requirements.txt        ← Python dependencies
│
├── data/
│   ├── cricket_players.csv ← Player statistics dataset
│   ├── top_scorers.png     ← EDA chart
│   ├── strike_vs_avg.png   ← EDA chart
│   ├── correlation_heatmap.png ← EDA chart
│   └── fours_vs_sixes.png  ← EDA chart
│
└── notebooks/
└── cricket_eda.ipynb   ← Exploratory Data Analysis
---

## 🚀 Run Locally

```bash
# Clone the repo
git clone https://github.com/RishitPandya22/cricket-performance-predictor.git

# Navigate into the folder
cd cricket-performance-predictor

# Create virtual environment
python -m venv venv
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

---

## 📊 EDA Highlights

- **Shikhar Dhawan** has the most career runs in the dataset (6,617)
- **KL Rahul** has the highest batting average (47.87)
- **Andre Russell** has the highest strike rate (177.9)
- **Hundreds and fifties** are the most important features for predicting performance

---

## 👨‍💻 About Me

**Rishit Pandya**
Master of Data Science Student — University of Adelaide 🇦🇺

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?style=flat&logo=linkedin)](https://linkedin.com/in/rishitpandya)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-black?style=flat&logo=github)](https://github.com/RishitPandya22)

---

## 🗺️ Other Portfolio Projects

| Project | Tech | Link |
|---|---|---|
| 🛒 Retail Sales Analysis | pandas, matplotlib, seaborn | GitHub |
| 🏠 Adelaide Housing Map | folium, GitHub Pages | Live |
| 🏥 AI Medical Disease Predictor | LLaMA 3B, Django, React | GitHub |
| 🏏 Cricket Performance Predictor | scikit-learn, Streamlit | Live ✅ |

---

*Built with ❤️ by Rishit Pandya | Master of Data Science | University of Adelaide*
