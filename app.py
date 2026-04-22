import streamlit as st
import pandas as pd
import numpy as np
import pickle
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import seaborn as sns
import io

# ================================
# PAGE CONFIG
# ================================
st.set_page_config(
    page_title="🏏 Cricket Performance Predictor",
    page_icon="🏏",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ================================
# CUSTOM CSS
# ================================
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;900&display=swap');

    html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
    .stApp { background: #0a0e1a; }

    .hero-card {
        background: linear-gradient(135deg, #0d1b2a 0%, #1b2838 50%, #0d2137 100%);
        padding: 2.5rem 2rem;
        border-radius: 20px;
        text-align: center;
        margin-bottom: 2rem;
        border: 1px solid #00d4aa33;
        box-shadow: 0 0 60px rgba(0,212,170,0.1), 0 8px 32px rgba(0,0,0,0.4);
        position: relative;
        overflow: hidden;
    }
    .hero-card::before {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: radial-gradient(circle, rgba(0,212,170,0.05) 0%, transparent 60%);
        pointer-events: none;
    }
    .hero-title {
        font-size: 2.8rem;
        font-weight: 900;
        color: #00d4aa;
        margin: 0;
        letter-spacing: -1px;
        text-shadow: 0 0 40px rgba(0,212,170,0.4);
    }
    .hero-subtitle {
        font-size: 1.1rem;
        color: #718096;
        margin-top: 0.5rem;
        letter-spacing: 2px;
        text-transform: uppercase;
    }
    .hero-badges {
        margin-top: 1rem;
        display: flex;
        justify-content: center;
        gap: 0.5rem;
        flex-wrap: wrap;
    }
    .badge {
        background: rgba(0,212,170,0.1);
        border: 1px solid rgba(0,212,170,0.3);
        color: #00d4aa;
        padding: 0.3rem 0.8rem;
        border-radius: 20px;
        font-size: 0.75rem;
        font-weight: 600;
        letter-spacing: 1px;
    }

    .fifa-card {
        background: linear-gradient(145deg, #1a2744 0%, #0f1929 100%);
        border: 2px solid #00d4aa44;
        border-radius: 16px;
        padding: 1.2rem;
        text-align: center;
        transition: all 0.3s ease;
        box-shadow: 0 4px 20px rgba(0,0,0,0.3);
        height: 100%;
    }
    .fifa-card:hover {
        border-color: #00d4aa;
        box-shadow: 0 8px 30px rgba(0,212,170,0.2);
        transform: translateY(-2px);
    }
    .fifa-card-name {
        font-size: 1rem;
        font-weight: 700;
        color: white;
        margin-bottom: 0.5rem;
    }
    .fifa-card-rating {
        font-size: 2.5rem;
        font-weight: 900;
        margin: 0.3rem 0;
    }
    .fifa-card-stats {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 0.3rem;
        margin-top: 0.8rem;
        font-size: 0.75rem;
    }
    .fifa-stat {
        color: #a0aec0;
        text-align: left;
        padding: 0.2rem 0;
    }
    .fifa-stat span {
        color: #00d4aa;
        font-weight: 700;
    }
    .elite-card { border-color: #f6d36588 !important; }
    .elite-rating { color: #f6d365; }
    .good-card { border-color: #43e97b88 !important; }
    .good-rating { color: #43e97b; }
    .average-card { border-color: #4facfe88 !important; }
    .average-rating { color: #4facfe; }

    .leaderboard-row {
        display: flex;
        align-items: center;
        background: #1a1f2e;
        border: 1px solid #2d3748;
        border-radius: 12px;
        padding: 0.8rem 1.2rem;
        margin: 0.4rem 0;
        transition: all 0.2s;
    }
    .leaderboard-row:hover {
        border-color: #00d4aa44;
        background: #1e2433;
    }
    .rank-badge {
        width: 36px;
        height: 36px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: 900;
        font-size: 0.9rem;
        margin-right: 1rem;
        flex-shrink: 0;
    }
    .rank-1 { background: linear-gradient(135deg, #f6d365, #fda085); color: #1a1a1a; }
    .rank-2 { background: linear-gradient(135deg, #c0c0c0, #a8a8a8); color: #1a1a1a; }
    .rank-3 { background: linear-gradient(135deg, #cd7f32, #a0522d); color: white; }
    .rank-other { background: #2d3748; color: #a0aec0; }

    .prediction-elite {
        background: linear-gradient(135deg, #f6d365 0%, #fda085 100%);
        padding: 2rem;
        border-radius: 20px;
        text-align: center;
        color: #1a1a1a;
        font-size: 2rem;
        font-weight: 900;
        box-shadow: 0 8px 40px rgba(246,211,101,0.4);
        letter-spacing: -0.5px;
    }
    .prediction-good {
        background: linear-gradient(135deg, #43e97b 0%, #38f9d7 100%);
        padding: 2rem;
        border-radius: 20px;
        text-align: center;
        color: #1a1a1a;
        font-size: 2rem;
        font-weight: 900;
        box-shadow: 0 8px 40px rgba(67,233,123,0.4);
    }
    .prediction-average {
        background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
        padding: 2rem;
        border-radius: 20px;
        text-align: center;
        color: #1a1a1a;
        font-size: 2rem;
        font-weight: 900;
        box-shadow: 0 8px 40px rgba(79,172,254,0.4);
    }

    .stat-card {
        background: linear-gradient(145deg, #1a1f2e, #151a27);
        border: 1px solid #2d3748;
        border-radius: 14px;
        padding: 1.2rem;
        text-align: center;
        transition: all 0.2s;
    }
    .stat-card:hover { border-color: #00d4aa44; }
    .stat-number { font-size: 2rem; font-weight: 900; color: #00d4aa; }
    .stat-label { font-size: 0.75rem; color: #718096; text-transform: uppercase; letter-spacing: 1.5px; margin-top: 0.2rem; }

    .section-header {
        font-size: 1.3rem;
        font-weight: 700;
        color: #00d4aa;
        border-left: 3px solid #00d4aa;
        padding-left: 0.8rem;
        margin: 1.5rem 0 1rem 0;
    }
    .compare-vs {
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 2rem;
        font-weight: 900;
        color: #f6d365;
        padding: 1rem;
        text-shadow: 0 0 20px rgba(246,211,101,0.5);
    }
    .footer {
        text-align: center;
        padding: 2.5rem;
        color: #4a5568;
        border-top: 1px solid #1a1f2e;
        margin-top: 3rem;
        font-size: 0.9rem;
    }
    div[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0d1117 0%, #0a0e1a 100%);
        border-right: 1px solid #1a1f2e;
    }
    .stTabs [data-baseweb="tab-list"] {
        background: #0d1117;
        border-radius: 12px;
        padding: 4px;
        gap: 4px;
    }
    .stTabs [data-baseweb="tab"] {
        border-radius: 8px;
        color: #718096;
        font-weight: 600;
    }
    .stTabs [aria-selected="true"] {
        background: #1a1f2e !important;
        color: #00d4aa !important;
    }
</style>
""", unsafe_allow_html=True)

# ================================
# LOAD MODEL & DATA
# ================================
@st.cache_resource
def load_model():
    with open('data/cricket_model.pkl', 'rb') as f:
        model = pickle.load(f)
    with open('data/label_encoder.pkl', 'rb') as f:
        le = pickle.load(f)
    return model, le

@st.cache_data
def load_data():
   return pd.read_csv('data/cricket_players.csv')

model, le = load_model()
df = load_data()

def categorize_performance(avg):
    if avg >= 40: return 'Elite'
    elif avg >= 32: return 'Good'
    else: return 'Average'

def get_rating(row):
    score = (
        (row['avg'] / 50) * 30 +
        (row['strike_rate'] / 200) * 20 +
        (row['runs'] / 8000) * 20 +
        (row['hundreds'] / 10) * 15 +
        (row['fifties'] / 60) * 10 +
        (row['sixes'] / 300) * 5
    )
    return min(99, max(50, int(score * 100)))

df['performance'] = df['avg'].apply(categorize_performance)
df['rating'] = df.apply(get_rating, axis=1)

def predict_performance(data_array):
    pred_encoded = model.predict(data_array)[0]
    pred = le.inverse_transform([pred_encoded])[0]
    probs = model.predict_proba(data_array)[0]
    return pred, probs

# ================================
# HERO
# ================================
st.markdown("""
<div class="hero-card">
    <div class="hero-title">🏏 Cricket Performance Predictor</div>
    <div class="hero-subtitle">Machine Learning · Player Analytics · IPL Stats</div>
    <div class="hero-badges">
        <span class="badge">🌲 Random Forest</span>
        <span class="badge">⚡ Real-time Prediction</span>
        <span class="badge">📊 15 IPL Legends</span>
        <span class="badge">🎯 ML Powered</span>
    </div>
</div>
""", unsafe_allow_html=True)

# ================================
# SIDEBAR
# ================================
st.sidebar.markdown("## 🎯 Predict a Player")
st.sidebar.markdown("---")
player_name = st.sidebar.text_input("Player Name (optional)", placeholder="e.g. Virat Kohli")
st.sidebar.markdown("**Career Statistics:**")
matches = st.sidebar.slider("🏟️ Matches", 50, 300, 150)
innings = st.sidebar.slider("🏏 Innings", 50, 280, 140)
runs = st.sidebar.slider("🏆 Runs", 500, 8000, 3000)
strike_rate = st.sidebar.slider("⚡ Strike Rate", 100.0, 200.0, 135.0)
hundreds = st.sidebar.slider("💯 Hundreds", 0, 10, 1)
fifties = st.sidebar.slider("5️⃣0️⃣ Fifties", 0, 60, 20)
highest_score = st.sidebar.slider("📈 Highest Score", 50, 200, 90)
fours = st.sidebar.slider("4️⃣ Fours", 50, 800, 300)
sixes = st.sidebar.slider("6️⃣ Sixes", 20, 300, 100)
not_outs = st.sidebar.slider("🛡️ Not Outs", 0, 60, 15)
st.sidebar.markdown("---")
predict_btn = st.sidebar.button("🚀 Predict!", use_container_width=True)

input_data = np.array([[matches, innings, runs, strike_rate,
                         hundreds, fifties, highest_score,
                         fours, sixes, not_outs]])
prediction, probabilities = predict_performance(input_data)

# ================================
# TABS
# ================================
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "🎯 Predict",
    "📱 Player Cards",
    "🏆 Leaderboard",
    "🔍 Compare",
    "📤 Upload CSV"
])

# ================================
# TAB 1 — PREDICT
# ================================
with tab1:
    name_str = f"**{player_name}**" if player_name else "This player"
    st.markdown(f'<p class="section-header">🎯 {name_str} — Prediction Result</p>', unsafe_allow_html=True)

    pred_col, info_col = st.columns([1, 1])

    with pred_col:
        if prediction == "Elite":
            st.markdown('<div class="prediction-elite">🌟 ELITE PLAYER 🌟<br><span style="font-size:1rem;opacity:0.8">Top tier performer</span></div>', unsafe_allow_html=True)
            if predict_btn: st.balloons()
        elif prediction == "Good":
            st.markdown('<div class="prediction-good">👍 GOOD PLAYER 👍<br><span style="font-size:1rem;opacity:0.8">Consistent performer</span></div>', unsafe_allow_html=True)
        else:
            st.markdown('<div class="prediction-average">📈 AVERAGE PLAYER 📈<br><span style="font-size:1rem;opacity:0.8">Developing performer</span></div>', unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)
        c1, c2, c3 = st.columns(3)
        c1.markdown(f'<div class="stat-card"><div class="stat-number">{probabilities[0]*100:.0f}%</div><div class="stat-label">Average</div></div>', unsafe_allow_html=True)
        c2.markdown(f'<div class="stat-card"><div class="stat-number">{probabilities[1]*100:.0f}%</div><div class="stat-label">Elite</div></div>', unsafe_allow_html=True)
        c3.markdown(f'<div class="stat-card"><div class="stat-number">{probabilities[2]*100:.0f}%</div><div class="stat-label">Good</div></div>', unsafe_allow_html=True)

    with info_col:
        fig, ax = plt.subplots(figsize=(5, 4))
        fig.patch.set_facecolor('#0d1117')
        ax.set_facecolor('#0d1117')
        colors = ['#4facfe', '#f6d365', '#43e97b']
        bars = ax.bar(le.classes_, probabilities * 100, color=colors,
                      edgecolor='#1a1f2e', linewidth=1.5, width=0.5)
        ax.set_ylim(0, 110)
        ax.set_ylabel('Probability (%)', color='#718096', fontsize=10)
        ax.set_title('Confidence Score', color='#00d4aa', fontweight='bold', fontsize=12)
        ax.tick_params(colors='white', labelsize=10)
        for spine in ax.spines.values():
            spine.set_color('#1a1f2e')
        for bar, prob in zip(bars, probabilities):
            ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 2,
                    f'{prob*100:.1f}%', ha='center', color='white',
                    fontweight='bold', fontsize=11)
        plt.tight_layout()
        st.pyplot(fig)

    st.markdown('<p class="section-header">📝 Input Summary</p>', unsafe_allow_html=True)
    s1,s2,s3,s4,s5 = st.columns(5)
    s1.metric("Matches", matches)
    s2.metric("Runs", f"{runs:,}")
    s3.metric("Avg SR", f"{strike_rate:.1f}")
    s4.metric("100s/50s", f"{hundreds}/{fifties}")
    s5.metric("Not Outs", not_outs)

# ================================
# TAB 2 — PLAYER CARDS
# ================================
with tab2:
    st.markdown('<p class="section-header">📱 FIFA-Style Player Cards</p>', unsafe_allow_html=True)
    st.markdown("Each card shows a player's **overall rating** calculated from all their stats!")

    sort_by = st.selectbox("Sort by:", ["Rating (High to Low)", "Runs (High to Low)", "Strike Rate (High to Low)", "Average (High to Low)"])
    sort_map = {
        "Rating (High to Low)": ("rating", False),
        "Runs (High to Low)": ("runs", False),
        "Strike Rate (High to Low)": ("strike_rate", False),
        "Average (High to Low)": ("avg", False)
    }
    sort_col, sort_asc = sort_map[sort_by]
    df_sorted = df.sort_values(sort_col, ascending=sort_asc).reset_index(drop=True)

    cols = st.columns(3)
    for i, (_, row) in enumerate(df_sorted.iterrows()):
        perf = row['performance']
        card_class = f"{perf.lower()}-card"
        rating_class = f"{perf.lower()}-rating"
        perf_emoji = "🌟" if perf == "Elite" else "👍" if perf == "Good" else "📈"

        with cols[i % 3]:
            st.markdown(f"""
            <div class="fifa-card {card_class}">
                <div class="fifa-card-name">{perf_emoji} {row['player']}</div>
                <div class="fifa-card-rating {rating_class}">{row['rating']}</div>
                <div style="color:#718096;font-size:0.7rem;text-transform:uppercase;letter-spacing:1px">{perf} · OVR</div>
                <div class="fifa-card-stats">
                    <div class="fifa-stat">RNS <span>{row['runs']:,}</span></div>
                    <div class="fifa-stat">AVG <span>{row['avg']}</span></div>
                    <div class="fifa-stat">SR <span>{row['strike_rate']}</span></div>
                    <div class="fifa-stat">100s <span>{row['hundreds']}</span></div>
                    <div class="fifa-stat">50s <span>{row['fifties']}</span></div>
                    <div class="fifa-stat">6s <span>{row['sixes']}</span></div>
                </div>
            </div>
            <br>
            """, unsafe_allow_html=True)

# ================================
# TAB 3 — LEADERBOARD
# ================================
with tab3:
    st.markdown('<p class="section-header">🏆 Player Leaderboard</p>', unsafe_allow_html=True)

    metric = st.selectbox("Rank by:", ["Overall Rating", "Total Runs", "Batting Average", "Strike Rate", "Sixes", "Hundreds"])
    metric_map = {
        "Overall Rating": "rating",
        "Total Runs": "runs",
        "Batting Average": "avg",
        "Strike Rate": "strike_rate",
        "Sixes": "sixes",
        "Hundreds": "hundreds"
    }
    rank_col = metric_map[metric]
    df_ranked = df.sort_values(rank_col, ascending=False).reset_index(drop=True)

    for i, (_, row) in enumerate(df_ranked.iterrows()):
        rank = i + 1
        rank_class = f"rank-{rank}" if rank <= 3 else "rank-other"
        rank_display = ["🥇", "🥈", "🥉"][i] if i < 3 else str(rank)
        perf = row['performance']
        perf_color = "#f6d365" if perf == "Elite" else "#43e97b" if perf == "Good" else "#4facfe"

        st.markdown(f"""
        <div class="leaderboard-row">
            <div class="rank-badge {rank_class}">{rank_display}</div>
            <div style="flex:1">
                <div style="color:white;font-weight:700;font-size:1rem">{row['player']}</div>
                <div style="color:#718096;font-size:0.8rem">
                    {row['runs']:,} runs · {row['avg']} avg · {row['strike_rate']} SR · {row['hundreds']} 100s
                </div>
            </div>
            <div style="text-align:right">
                <div style="color:{perf_color};font-weight:900;font-size:1.3rem">{row[rank_col]}</div>
                <div style="color:#718096;font-size:0.75rem">{metric}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

# ================================
# TAB 4 — COMPARE
# ================================
with tab4:
    st.markdown('<p class="section-header">🔍 Head-to-Head Player Comparison</p>', unsafe_allow_html=True)

    player_list = df['player'].tolist()
    comp_col1, vs_col, comp_col2 = st.columns([2, 0.5, 2])

    with comp_col1:
        p1 = st.selectbox("Player 1", player_list, index=0)
    with vs_col:
        st.markdown('<div class="compare-vs">VS</div>', unsafe_allow_html=True)
    with comp_col2:
        p2 = st.selectbox("Player 2", player_list, index=1)

    r1 = df[df['player'] == p1].iloc[0]
    r2 = df[df['player'] == p2].iloc[0]

    st.markdown("<br>", unsafe_allow_html=True)

    compare_stats = [
        ("🏆 Total Runs", "runs", False),
        ("📊 Batting Average", "avg", False),
        ("⚡ Strike Rate", "strike_rate", False),
        ("💯 Hundreds", "hundreds", False),
        ("5️⃣0️⃣ Fifties", "fifties", False),
        ("6️⃣ Sixes", "sixes", False),
        ("4️⃣ Fours", "fours", False),
        ("📈 Highest Score", "highest_score", False),
        ("🌟 Overall Rating", "rating", False),
    ]

    for stat_name, stat_col, _ in compare_stats:
        v1 = r1[stat_col]
        v2 = r2[stat_col]
        winner_color_1 = "#00d4aa" if v1 >= v2 else "#718096"
        winner_color_2 = "#00d4aa" if v2 >= v1 else "#718096"

        col_a, col_mid, col_b = st.columns([2, 2, 2])
        with col_a:
            st.markdown(f'<div style="text-align:right;color:{winner_color_1};font-weight:700;font-size:1.1rem;padding:0.3rem 0">{v1:,}</div>', unsafe_allow_html=True)
        with col_mid:
            st.markdown(f'<div style="text-align:center;color:#4a5568;font-size:0.8rem;padding:0.4rem 0">{stat_name}</div>', unsafe_allow_html=True)
        with col_b:
            st.markdown(f'<div style="text-align:left;color:{winner_color_2};font-weight:700;font-size:1.1rem;padding:0.3rem 0">{v2:,}</div>', unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Radar chart
    st.markdown('<p class="section-header">🕸️ Radar Chart Comparison</p>', unsafe_allow_html=True)
    radar_stats = ['runs', 'avg', 'strike_rate', 'hundreds', 'fifties', 'sixes']
    radar_labels = ['Runs', 'Average', 'Strike Rate', '100s', '50s', 'Sixes']
    maxvals = [8000, 50, 200, 10, 60, 300]

    v1_norm = [r1[s]/m for s, m in zip(radar_stats, maxvals)]
    v2_norm = [r2[s]/m for s, m in zip(radar_stats, maxvals)]

    angles = np.linspace(0, 2*np.pi, len(radar_labels), endpoint=False).tolist()
    v1_norm += v1_norm[:1]
    v2_norm += v2_norm[:1]
    angles += angles[:1]

    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
    fig.patch.set_facecolor('#0d1117')
    ax.set_facecolor('#0d1117')
    ax.plot(angles, v1_norm, 'o-', linewidth=2, color='#00d4aa', label=p1)
    ax.fill(angles, v1_norm, alpha=0.2, color='#00d4aa')
    ax.plot(angles, v2_norm, 'o-', linewidth=2, color='#f6d365', label=p2)
    ax.fill(angles, v2_norm, alpha=0.2, color='#f6d365')
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(radar_labels, color='white', fontsize=10)
    ax.set_yticklabels([])
    ax.grid(color='#2d3748', linewidth=0.5)
    ax.spines['polar'].set_color('#2d3748')
    ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1),
              facecolor='#1a1f2e', labelcolor='white', fontsize=10)
    plt.tight_layout()
    st.pyplot(fig)

# ================================
# TAB 5 — UPLOAD CSV
# ================================
with tab5:
    st.markdown('<p class="section-header">📤 Upload Your Own Player CSV</p>', unsafe_allow_html=True)
    st.markdown("Upload a CSV with player stats and the ML model will predict performance for **all players at once!**")

    st.markdown("**Your CSV must have these columns:**")
    sample_cols = ['player', 'matches', 'innings', 'runs', 'avg', 'strike_rate',
                   'hundreds', 'fifties', 'highest_score', 'fours', 'sixes', 'not_outs']
    st.code(", ".join(sample_cols))

    # Download sample CSV
    sample_df = df[sample_cols].head(3)
    csv_buffer = io.StringIO()
    sample_df.to_csv(csv_buffer, index=False)
    st.download_button(
        "⬇️ Download Sample CSV Template",
        data=csv_buffer.getvalue(),
        file_name="sample_cricket_template.csv",
        mime="text/csv"
    )

    st.markdown("---")
    uploaded_file = st.file_uploader("Upload your CSV file", type=['csv'])

    if uploaded_file:
        try:
            uploaded_df = pd.read_csv(uploaded_file)
            st.success(f"✅ Loaded {len(uploaded_df)} players!")
            st.dataframe(uploaded_df, use_container_width=True)

            features = ['matches', 'innings', 'runs', 'strike_rate',
                        'hundreds', 'fifties', 'highest_score', 'fours',
                        'sixes', 'not_outs']

            missing = [f for f in features if f not in uploaded_df.columns]
            if missing:
                st.error(f"❌ Missing columns: {', '.join(missing)}")
            else:
                X_upload = uploaded_df[features].values
                preds_encoded = model.predict(X_upload)
                preds = le.inverse_transform(preds_encoded)
                probs = model.predict_proba(X_upload)
                uploaded_df['prediction'] = preds
                uploaded_df['confidence'] = [f"{max(p)*100:.1f}%" for p in probs]
                uploaded_df['rating'] = uploaded_df.apply(get_rating, axis=1)

                st.markdown('<p class="section-header">🎯 Predictions for Your Players</p>', unsafe_allow_html=True)

                for _, row in uploaded_df.iterrows():
                    perf = row['prediction']
                    emoji = "🌟" if perf == "Elite" else "👍" if perf == "Good" else "📈"
                    color = "#f6d365" if perf == "Elite" else "#43e97b" if perf == "Good" else "#4facfe"
                    st.markdown(f"""
                    <div class="leaderboard-row">
                        <div style="flex:1">
                            <div style="color:white;font-weight:700">{emoji} {row.get('player', 'Unknown')}</div>
                            <div style="color:#718096;font-size:0.8rem">{row['runs']:,} runs · {row['avg']} avg · {row['strike_rate']} SR</div>
                        </div>
                        <div style="text-align:right">
                            <div style="color:{color};font-weight:900;font-size:1.2rem">{perf}</div>
                            <div style="color:#718096;font-size:0.75rem">Confidence: {row['confidence']}</div>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)

                result_csv = io.StringIO()
                uploaded_df.to_csv(result_csv, index=False)
                st.download_button(
                    "⬇️ Download Results CSV",
                    data=result_csv.getvalue(),
                    file_name="cricket_predictions.csv",
                    mime="text/csv"
                )
        except Exception as e:
            st.error(f"❌ Error reading file: {e}")
    else:
        st.info("👆 Upload a CSV file above to get started!")

# ================================
# FOOTER
# ================================
st.markdown("""
<div class="footer">
    <p>🏏 Cricket Performance Predictor · Random Forest ML · scikit-learn · Streamlit</p>
    <p>Built with ❤️ by <strong>Rishit Pandya</strong> · Master of Data Science · University of Adelaide</p>
</div>
""", unsafe_allow_html=True)