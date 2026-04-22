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
st.info(f"**Latest known 2026 SG: Total ≈ +{latest_sg:.2f}** (as of April 21, 2026 — post-RBC Heritage)")

base_mu = st.slider("Expected SG per round (μ)", 1.0, 3.0, latest_sg, 0.05)

# Expanded alphabetical course list + Aronimink
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

# Live Leaderboard Integration
st.subheader("📊 Live Leaderboard Integration")
st.markdown("""
**Current Event:** Zurich Classic of New Orleans (team event — April 23-26, 2026)  
**Next Major Events:** Cadillac Championship (April 30–May 3), Truist Championship (May 7–10)

**How to use live data:**
1. Open the official PGA Tour leaderboard: [pgatour.com/leaderboard](https://www.pgatour.com/leaderboard)
2. Check Scheffler's position, strokes gained so far, and strokes relative to the field.
3. Adjust the **Expected SG (μ)** slider up/down based on his current ball-striking.
4. Update the **Tournament Stage** below.
5. Re-run the simulation for an updated betting plan.
""")

stage = st.selectbox("Current Tournament Stage", ["Pre-Tournament", "After Round 1", "After Cut (Post-R2)"])

st.subheader("Current Market Implied Probabilities (%)")
win_market = st.number_input("Win Market (%)", 0, 100, 22, step=1) / 100.0
top10_market = st.number_input("Top 10 Market (%)", 0, 100, 45, step=1) / 100.0
top20_market = st.number_input("Top 20 Market (%)", 0, 100, 65, step=1) / 100.0

field_type = st.selectbox("Tournament Type", ["Signature Event (82 players)", "Full-Field (~150 players)"])
field_size = 82 if field_type.startswith("Signature") else 150

if st.button("🚀 Run Simulation & Generate Betting Plan", type="primary"):
    p10, p20, p_win, avg_rank = scheffler_top_probs(mu_sg_per_round=final_mu, field_size=field_size)
    
    st.balloons()
    st.success(f"**Win probability: {p_win}%**")
    st.success(f"**Top 10 probability: {p10}%**")
    st.success(f"**Top 20 probability: {p20}%**")
    st.info(f"**Projected finishing position: {avg_rank}**")

    # Betting Plan using your exact rules
    st.subheader("💰 Recommended Betting Plan")
    st.caption(f"**Stage:** {stage} • **Course:** {selected_course} • **Live Edge Check**")

    # Top 10
    edge10 = p10 - (top10_market * 100)
    if stage == "Pre-Tournament":
        if edge10 >= 12 and avg_rank <= 11:
            st.success("**TOP 10: ENTER Base Size** ✅ Strong pre-tournament edge")
        else:
            st.warning("**TOP 10: No Entry**")
    elif stage == "After Round 1":
        if edge10 >= 10 and avg_rank <= 12:
            st.success("**TOP 10: ENTER Base Size** ✅ Good R1 position")
        else:
            st.warning("**TOP 10: No Entry**")
    else:  # After Cut
        if edge10 >= 10 and avg_rank <= 13:
            st.success("**TOP 10: ENTER Base Size** ✅ Made cut + solid position")
        else:
            st.warning("**TOP 10: No Entry**")

    # Top 20
    edge20 = p20 - (top20_market * 100)
    if edge20 >= 10 and avg_rank <= 23:
        st.success("**TOP 20: ENTER Base Size** ✅ High-confidence floor play")
    else:
        st.info("**TOP 20: No Action** (edge too small)")

    # Win
    edge_win = p_win - (win_market * 100)
    if stage == "Pre-Tournament":
        if edge_win >= 15 and avg_rank <= 3:
            st.success("**WIN: ENTER Base Size** 🔥 Elite outright value")
        else:
            st.warning("**WIN: No Entry**")
    elif stage == "After Round 1":
        if edge_win >= 12 and avg_rank <= 4:
            st.success("**WIN: ENTER Base Size** 🔥 In contention")
        else:
            st.warning("**WIN: No Entry**")
    else:
        if edge_win >= 12 and avg_rank <= 3:
            st.success("**WIN: ENTER Base Size** 🔥 Strong contention")
        else:
            st.warning("**WIN: No Entry**")

    st.caption("Follow your full rules for sizing, adds (Rounds 1-3 only), and max exposure. Update with live leaderboard/SG each round.")

with st.expander("📖 How to Use This App"):
    st.markdown("""
    1. Set μ (defaults to latest season value)  
    2. Pick the course (boost auto-applies)  
    3. Check live leaderboard → adjust μ/stage  
    4. Enter current market prices  
    5. Run → get simulation + rules-based betting plan
    """)

st.caption("Built with pure Strokes Gained Monte Carlo • Follows your complete rules framework")
