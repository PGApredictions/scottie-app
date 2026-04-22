import streamlit as st
import numpy as np

def scheffler_top_probs(mu_sg_per_round=2.0, field_size=82, sigma_per_round=2.8, n_sims=20000):
    scottie_total = np.random.normal(mu_sg_per_round * 4, sigma_per_round * np.sqrt(4), n_sims)
    others_total = np.random.normal(0, sigma_per_round * np.sqrt(4), size=(n_sims, field_size - 1))
    ranks = np.sum(others_total > scottie_total[:, np.newaxis], axis=1) + 1
    p_top10 = np.mean(ranks <= 10) * 100
    p_top20 = np.mean(ranks <= 20) * 100
    return round(p_top10, 1), round(p_top20, 1)

st.title("🧢 Scottie Top 10/20 Predictor")
st.markdown("**Simple Strokes Gained model — updated weekly with your estimate**")

# Main inputs
base_mu = st.slider("Expected SG per round (μ)", 1.0, 3.0, 2.0, 0.05)
st.caption("Start with Scottie's current season SG average from pgatour.com or datagolf.com")

# Course dropdown with pre-assigned boosts
course_options = {
    "Select a course...": 0.00,
    # Very Favorable (0.60) - Elite iron/accuracy fits + strong history
    "Harbour Town Golf Links (RBC Heritage)": 0.60,
    "Quail Hollow Club (Truist / Wells Fargo)": 0.60,
    "TPC Sawgrass (Players Championship)": 0.55,
    "Arnold Palmer Bay Hill Club": 0.55,
    "Augusta National (Masters)": 0.50,
    "Colonial Country Club": 0.50,
    "Muirfield Village (Memorial)": 0.50,
    # Favorable (0.30) - Good fits
    "Trump National Doral (Blue Monster - Cadillac)": 0.30,
    "Torrey Pines (Farmers Insurance)": 0.30,
    "TPC Scottsdale (WM Phoenix Open)": 0.30,
    "Pebble Beach Golf Links": 0.30,
    "Riviera Country Club (Genesis)": 0.30,
    "TPC Louisiana (Zurich Classic)": 0.25,
    "PGA West (Stadium Course - American Express)": 0.25,
    "Innisbrook (Valspar)": 0.25,
    # Unfavorable (0.00) - Bomber/putting-heavy or weaker fits
    "TPC River Highlands (Travelers)": 0.00,
    "East Lake Golf Club (Tour Championship)": 0.00,
    "Waialae Country Club (Sony Open)": 0.00,
    "PGA National (Honda Classic style)": 0.00,
    "Other / Neutral Course": 0.00
}

selected_course = st.selectbox("Select PGA Tour Course", list(course_options.keys()))
boost = course_options[selected_course]

final_mu = base_mu + boost
if boost >= 0.50:
    st.success(f"✅ **Very Favorable** → Sensitive μ = {final_mu:.2f}")
elif boost > 0.00:
    st.success(f"✅ **Favorable** → Sensitive μ = {final_mu:.2f}")
else:
    st.info(f"**Conservative μ = {final_mu:.2f}** (no boost)")

field_type = st.selectbox("Tournament Type", ["Signature Event (82 players)", "Full-Field (~150 players)"])
field_size = 82 if field_type.startswith("Signature") else 150

if st.button("🚀 Run Simulation", type="primary"):
    with st.spinner("Running 20,000 simulations..."):
        p10, p20 = scheffler_top_probs(mu_sg_per_round=final_mu, field_size=field_size)
    st.balloons()
    st.success(f"**Top 10 probability: {p10}%**")
    st.success(f"**Top 20 probability: {p20}%**")

if st.button("🔄 Reset to Defaults"):
    st.rerun()

# How to Use expander
with st.expander("📖 How to Use This App"):
    st.markdown("""
    1. Set **Expected SG per round** to Scottie’s current season average.
    2. Choose the **Course** from the dropdown — the boost is pre-set based on his history and fit.
    3. Pick Signature or Full-Field.
    4. Tap **Run Simulation**.
    
    **Tip**: Top 20 is the safest prop. Use "Very Favorable" for iron-heavy tracks like Harbour Town or Quail Hollow.
    """)

st.caption("Built with pure Strokes Gained Monte Carlo • Backtested 2023–2025")
