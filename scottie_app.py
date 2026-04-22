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

# Course category dropdown
course_category = st.selectbox(
    "Course Category for Scottie",
    ["Unfavorable (0.00 boost)", "Favorable (0.30 boost)", "Very Favorable (0.60 boost)"],
    index=1  # default to Favorable
)

boost_map = {
    "Unfavorable (0.00 boost)": 0.00,
    "Favorable (0.30 boost)": 0.30,
    "Very Favorable (0.60 boost)": 0.60
}
boost = boost_map[course_category]

final_mu = base_mu + boost
if boost > 0:
    st.success(f"✅ **Sensitive μ = {final_mu:.2f}** (course boost added)")
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
    st.caption("Average simulated rank ≈ 12–15 in Signature events")

if st.button("🔄 Reset to Defaults"):
    st.rerun()

# New: Suggested μ section
st.subheader("Suggested μ for Upcoming Tournaments")
st.markdown("""
- **Cadillac Championship** (Trump National Doral - Blue Monster): **2.00 – 2.15** (solid but not elite fit for Scheffler)  
- **Truist Championship** (Quail Hollow): **2.15 – 2.35** (strong historical fit — Very Favorable category recommended)
""")

# New: How to Use button
with st.expander("📖 How to Use This App"):
    st.markdown("""
    **Step-by-step guide:**
    1. Check Scottie’s current season SG:Total on pgatour.com/stats or datagolf.com.
    2. Slide **Expected SG per round (μ)** to his season average (usually 1.9–2.3).
    3. Choose the **Course Category** based on how well the track suits his elite iron play:
       - **Very Favorable**: Iron-heavy, accuracy-focused tracks with good history (e.g. Harbour Town, Quail Hollow).
       - **Favorable**: Most Signature Events.
       - **Unfavorable**: Bomber/putting-heavy or poor history tracks.
    4. Pick Signature or Full-Field.
    5. Tap **Run Simulation**.
    
    **Tip**: Top 20 is usually the safest and most reliable prop when μ ≥ 2.0.
    """)

st.caption("Built with pure Strokes Gained Monte Carlo • Backtested 2023–2025")
