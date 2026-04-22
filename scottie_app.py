import streamlit as st
import numpy as np

def scheffler_top_probs(mu_sg_per_round=2.0, field_size=82, sigma_per_round=2.8, n_sims=20000):
    scottie_total = np.random.normal(mu_sg_per_round * 4, sigma_per_round * np.sqrt(4), n_sims)
    others_total = np.random.normal(0, sigma_per_round * np.sqrt(4), size=(n_sims, field_size - 1))
    ranks = np.sum(others_total > scottie_total[:, np.newaxis], axis=1) + 1
    p_top10 = np.mean(ranks <= 10) * 100
    p_top20 = np.mean(ranks <= 20) * 100
    p_win = np.mean(ranks == 1) * 100
    avg_rank = np.mean(ranks)
    return round(p_top10, 1), round(p_top20, 1), round(p_win, 1), round(avg_rank, 1)

st.title("🧢 Scottie Top 10/20 Predictor + Betting Plan")
st.markdown("**Strokes Gained model with your exact rules-based betting framework**")

# Latest SG
latest_sg = 2.05
st.info(f"**Latest known 2026 SG: Total = +{latest_sg:.2f}** (as of April 21, 2026)")

base_mu = st.slider("Expected SG per round (μ)", 1.0, 3.0, latest_sg, 0.05)

# Expanded alphabetical course list
course_options = {
    "Select a course...": 0.00,
    "Arnold Palmer Bay Hill Club": 0.55,
    "Augusta National Golf Club (Masters)": 0.50,
    "Bethpage Black": 0.25,
    "Caves Valley Golf Club": 0.20,
    "Colonial Country Club": 0.50,
    "Detroit Golf Club": 0.10,
    "East Lake Golf Club": 0.00,
    "Harbour Town Golf Links (RBC Heritage)": 0.60,
    "Innisbrook Resort (Copperhead)": 0.25,
    "Muirfield Village Golf Club (Memorial)": 0.50,
    "Oak Hill Country Club": 0.20,
    "Pebble Beach Golf Links": 0.30,
    "PGA National (Champion)": 0.10,
    "PGA West (Stadium Course)": 0.25,
    "Quail Hollow Club (Truist Championship)": 0.60,
    "Riviera Country Club (Genesis Invitational)": 0.30,
    "Sedgefield Country Club (Wyndham)": 0.10,
    "Silverado Resort (Fortinet)": 0.15,
    "The Concession Golf Club": 0.20,
    "The Country Club (Brookline)": 0.25,
    "The Greenbrier": 0.15,
    "The Players Stadium Course (TPC Sawgrass)": 0.55,
    "Torrey Pines Golf Course (South)": 0.30,
    "TPC Louisiana (Zurich Classic)": 0.25,
    "TPC River Highlands (Travelers)": 0.00,
    "TPC Scottsdale (WM Phoenix Open)": 0.30,
    "TPC Southwind (FedEx St. Jude)": 0.20,
    "Trump National Doral (Blue Monster - Cadillac Championship)": 0.30,
    "Valhalla Golf Club": 0.25,
    "Waialae Country Club (Sony Open)": 0.00,
    "Other / Neutral Course": 0.00
}

selected_course = st.selectbox("Select PGA Tour Course (boost auto-applied)", list(course_options.keys()))
boost = course_options[selected_course]

final_mu = base_mu + boost
if boost >= 0.50:
    st.success(f"✅ **Very Favorable** → Sensitive μ = {final_mu:.2f}")
elif boost > 0.00:
    st.success(f"✅ **
