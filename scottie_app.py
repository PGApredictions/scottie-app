import streamlit as st
import numpy as np

def scheffler_top_probs(mu_sg_per_round=2.0, field_size=82, sigma_per_round=2.8, n_sims=20000):
    scottie_total = np.random.normal(mu_sg_per_round * 4, sigma_per_round * np.sqrt(4), n_sims)
    others_total = np.random.normal(0, sigma_per_round * np.sqrt(4), size=(n_sims, field_size - 1))
    ranks = np.sum(others_total > scottie_total[:, np.newaxis], axis=1) + 1
    p_top5 = np.mean(ranks <= 5) * 100
    p_top10 = np.mean(ranks <= 10) * 100
    p_top20 = np.mean(ranks <= 20) * 100
    p_win = np.mean(ranks == 1) * 100
    avg_rank = np.mean(ranks)
    return round(p_top5, 1), round(p_top10, 1), round(p_top20, 1), round(p_win, 1), round(avg_rank, 1)

# Custom CSS - Timeless masculine style with requested color changes
st.markdown("""
<style>
    .stApp {
        background-color: #0f172a;
        color: #e2e8f0;
    }
    h1 {
        color: #f8fafc;
        font-family: 'Georgia', serif;
        font-weight: 700;
        letter-spacing: 1px;
    }
    .stButton>button {
        background-color: #b91c1c;
        color: white;
        font-weight: bold;
        border: none;
        border-radius: 8px;
        padding: 12px 24px;
    }
    /* Red for No Entry */
    .stWarning {
        background-color: #7f1d1d !important;
        border-left: 5px solid #ef4444;
        color: #fee2e2;
    }
    /* Yellow for No Action */
    .element-container div[data-testid="stAlert"] {
        background-color: #78350f !important;
        border-left: 5px solid #fbbf24;
        color: #fef3c7;
    }
</style>
""", unsafe_allow_html=True)

st.title("⛳ Scheffler Sharps ⛳")
st.markdown("**Insights on Scottie Scheffler**")

latest_sg = 2.05
st.info(f"**Latest known 2026 SG: Total ≈ +{latest_sg:.2f}** (as of April 21, 2026 — post-RBC Heritage)")

base_mu = st.slider("Expected SG per round (μ)", 1.0, 3.0, latest_sg, 0.05)

course_options = {
    "Select a course...": 0.00,
    "Arnold Palmer Bay Hill Club": 0.55,
    "Aronimink Golf Club (Donald Ross)": 0.40,
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
    st.success(f"✅ **Favorable** → Sensitive μ = {final_mu:.2f}")
else:
    st.info(f"**Conservative μ = {final_mu:.2f}** (no boost)")

stage = st.selectbox("Current Tournament Stage", ["Pre-Tournament", "After Round 1", "After Cut (Post-R2)"])

st.subheader("Current Market Implied Probabilities (%)")
win_market = st.number_input("Win Market (%)", 0, 100, 22, step=1) / 100.0
top5_market = st.number_input("Top 5 Market (%)", 0, 100, 28, step=1) / 100.0
top10_market = st.number_input("Top 10 Market (%)", 0, 100, 45, step=1) / 100.0
top20_market = st.number_input("Top 20 Market (%)", 0, 100, 65, step=1) / 100.0

field_type = st.selectbox("Tournament Type", ["Signature Event (82 players)", "Full-Field (~150 players)"])
field_size = 82 if field_type.startswith("Signature") else 150

if st.button("🚀 Run Simulation & Generate Betting Plan", type="primary"):
    p_top5, p10, p20, p_win, avg_rank = scheffler_top_probs(mu_sg_per_round=final_mu, field_size=field_size)
    
    st.balloons()
    st.success(f"**Win probability: {p_win}%**")
    st.success(f"**Top 5 probability: {p_top5}%**")
    st.success(f"**Top 10 probability: {p10}%**")
    st.success(f"**Top 20 probability: {p20}%**")
    st.info(f"**Projected finishing position: {avg_rank}**")

    st.subheader("💰 Recommended Betting Plan")
    st.caption(f"**Stage:** {stage} • **Course:** {selected_course}")

    # Win
    edge_win = p_win - (win_market * 100)
    if (stage == "Pre-Tournament" and edge_win >= 15 and avg_rank <= 3) or \
       (stage == "After Round 1" and edge_win >= 12 and avg_rank <= 4) or \
       (stage == "After Cut (Post-R2)" and edge_win >= 12 and avg_rank <= 3):
        st.success("**WIN: ENTER Base Size** 🔥 Elite outright value")
    else:
        st.error("**WIN: No Entry**")   # Red background

    # Top 5
    edge5 = p_top5 - (top5_market * 100)
    if edge5 >= 14 and avg_rank <= 8:
        st.success("**TOP 5: ENTER Base Size** ✅ Strong contention play")
    else:
        st.warning("**TOP 5: No Action**")   # Yellow background

    # Top 10
    edge10 = p10 - (top10_market * 100)
    if (stage == "Pre-Tournament" and edge10 >= 12 and avg_rank <= 11) or \
       (stage == "After Round 1" and edge10 >= 10 and avg_rank <= 12) or \
       (stage == "After Cut (Post-R2)" and edge10 >= 10 and avg_rank <= 13):
        st.success("**TOP 10: ENTER Base Size** ✅ Strong edge")
    else:
        st.error("**TOP 10: No Entry**")

    # Top 20
    edge20 = p20 - (top20_market * 100)
    if edge20 >= 10 and avg_rank <= 23:
        st.success("**TOP 20: ENTER Base Size** ✅ High-confidence floor")
    else:
        st.warning("**TOP 20: No Action**")

    st.caption("Follow your full rules for sizing, adds (Rounds 1-3 only), and max exposure.")

with st.expander("📖 How to Use This App"):
    st.markdown("""
    1. Set **Expected SG per round (μ)**  
    2. Choose the **Course** — boost applies automatically  
    3. Select **Stage** and enter current **Market Prices**  
    4. Tap **Run Simulation & Generate Betting Plan**
    """)

st.caption("Built with pure Strokes Gained Monte Carlo • Follows your complete rules framework")
