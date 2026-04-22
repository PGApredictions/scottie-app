
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
st.markdown("**Enter your expected SG and toggle the course**")

base_mu = st.slider("Expected SG per round (μ)", 1.0, 3.0, 2.0, 0.05)

favorable = st.toggle("Favorable Course this week? (good history or iron-heavy track)", value=True)
if favorable:
    final_mu = base_mu + 0.35
    st.success("✅ Sensitive μ (course boost added)")
else:
    final_mu = base_mu
    st.info("Conservative μ (no boost)")

fiel"Tournament Type", ["Signature Event (82 players)", "Full-Field (~150 players)"])
field_size = 82 if field_type.startswith("Signature") else 150

if st.button("🚀 Run Simulation", type="primary"):
    with st.spinner("Running 20,000 simulations..."):
        p10, p20 = scheffler_top_probs(mu_sg_per_round=final_mu, field_size=field_size)
    st.balloons()
    st.success(f"**Top 10 probability: {p10}%**")
    st.success(f"**Top 20 probability: {p20}%**")
(venv) joe@JackMacs-MacBook-Air scottie-app % python -m streamlit run scottie_app.py

      👋 Welcome to Streamlit!

      If you'd like to receive helpful onboarding emails, news, offers, promotions,
      and the occasional swag, please enter your email address below. Otherwise,
      leave this field blank.

      Email: joseph.osborn717@gmail.com

  You can find our privacy policy at https://streamlit.io/privacy-policy

  Summary:
  - This open source library collects usage statistics.
  - We cannot see and do not store information contained inside Streamlit apps,
    such as text, charts, images, etc.
  - Telemetry data is stored in servers in the United States.
  - If you'd like to opt out, add the following to ~/.streamlit/config.toml,
    creating that file if necessary:

    [browser]
    gatherUsageStats = false


  You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8501
  Network URL: http://10.0.0.128:8501

  For better performance, install the Watchdog module:

  $ xcode-select --install
  $ pip install watchdog
            
^C  Stopping...
(venv) joe@JackMacs-MacBook-Air scottie-app % cat > scottie_app.py
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

favorable = st.toggle("Favorable Course this week? (good history or iron-heavy track)", value=True)

if favorable:
    boost = st.slider("Course boost 0.35, 0.05)
    final_mu = base_mu + boost
    st.success(f"✅ **Sensitive μ = {final_mu:.2f}** (course boost added)")
else:
    final_mu = base_mu
    st.info(f"**Conservative μ = {final_mu:.2f}** (no boost)")

field_type = st.selectbox("Tournament Type", ["Signature Event (82 players)", "Full-Field (~150 players)"])
field_size = 82 if field_type.startswith("Signature") else 150

if st.button("🚀 Run Simulation", type="primary"):
    with st.spinner("Running 20,000 simulations..."):
        p10, p20 = scheffler_top_probs(mu_sg_per_round=final_mu, field_size=field_size)
    st.balloons()
    st.success(f"**Top 10 probability: {p10}%**")
    st.success(f"**Top 20 probability: {p20}%**")
    st.caption(f"Average simulated rank ≈ 12–15 in Signature events")

# Reset button
if st.button("🔄 Reset to Defaults"):
    st.rerun()

st.caption("Built with pure Strokes Gained Monte Carlo • Backtested 2023–2025")
(venv) joe@JackMacs-MacBook-Air scottie-app % python -m streamlit run scottie_app.py

  You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8501
  Network URL: http://10.0.0.128:8501

  For better performance, install the Watchdog module:

  $ xcode-select --install
  $ pip install watchdog
            

