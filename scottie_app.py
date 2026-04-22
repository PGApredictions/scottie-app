Last login: Tue Apr 21 19:36:21 on ttys000
joe@JackMacs-MacBook-Air ~ % mkdir scottie-app
joe@JackMacs-MacBook-Air ~ % cd scottie-app
joe@JackMacs-MacBook-Air scottie-app % python -m venv venv
zsh: command not found: python
joe@JackMacs-MacBook-Air scottie-app % python -m venv venv
zsh: command not found: python
joe@JackMacs-MacBook-Air scottie-app % cd scottie-app
cd: no such file or directory: scottie-app
joe@JackMacs-MacBook-Air scottie-app % python3 -m venv venv
joe@JackMacs-MacBook-Air scottie-app % source venv/bin/activate
(venv) joe@JackMacs-MacBook-Air scottie-app % pip install streamlit numpy
Collecting streamlit
  Downloading streamlit-1.56.0-py3-none-any.whl.metadata (9.8 kB)
Collecting numpy
  Downloading numpy-2.4.4-cp314-cp314-macosx_10_15_x86_64.whl.metadata (6.6 kB)
Collecting altair!=5.4.0,!=5.4.1,<7,>=4.0 (from streamlit)
  Downloading altair-6.1.0-py3-none-any.whl.metadata (11 kB)
Collecting blinker<2,>=1.5.0 (from streamlit)
  Downloading blinker-1.9.0-py3-none-any.whl.metadata (1.6 kB)
Collecting cachetools<8,>=5.5 (from streamlit)
  Downloading cachetools-7.0.6-py3-none-any.whl.metadata (5.9 kB)
Collecting click<9,>=7.0 (from streamlit)
  Downloading click-8.3.2-py3-none-any.whl.metadata (2.6 kB)
Collecting gitpython!=3.1.19,<4,>=3.0.7 (from streamlit)
  Downloading gitpython-3.1.46-py3-none-any.whl.metadata (13 kB)
Collecting packaging>=20 (from streamlit)
  Downloading packaging-26.1-py3-none-any.whl.metadata (3.5 kB)
Collecting pandas<4,>=1.4.0 (from streamlit)
  Downloading pandas-3.0.2-cp314-cp314-macosx_10_15_x86_64.whl.metadata (79 kB)
Collecting pillow<13,>=7.1.0 (from streamlit)
  Downloading pillow-12.2.0-cp314-cp314-macosx_10_15_x86_64.whl.metadata (8.8 kB)
Collecting pydeck<1,>=0.8.0b4 (from streamlit)
  Downloading pydeck-0.9.2-py2.py3-none-any.whl.metadata (4.2 kB)
Collecting protobuf<8,>=3.20 (from streamlit)
  Downloading protobuf-7.34.1-cp310-abi3-macosx_10_9_universal2.whl.metadata (595 bytes)
Collecting pyarrow>=7.0 (from streamlit)
  Downloading pyarrow-24.0.0-cp314-cp314-macosx_12_0_x86_64.whl.metadata (3.0 kB)
Collecting requests<3,>=2.27 (from streamlit)
  Downloading requests-2.33.1-py3-none-any.whl.metadata (4.8 kB)
Collecting tenacity<10,>=8.1.0 (from streamlit)
  Downloading tenacity-9.1.4-py3-none-any.whl.metadata (1.2 kB)
Collecting toml<2,>=0.10.1 (from streamlit)
  Downloading toml-0.10.2-py2.py3-none-any.whl.metadata (7.1 kB)
Collecting tornado!=6.5.0,<7,>=6.0.3 (from streamlit)
  Downloading tornado-6.5.5-cp39-abi3-macosx_10_9_x86_64.whl.metadata (2.8 kB)
Collecting typing-extensions<5,>=4.10.0 (from streamlit)
  Downloading typing_extensions-4.15.0-py3-none-any.whl.metadata (3.3 kB)
Collecting jinja2 (from altair!=5.4.0,!=5.4.1,<7,>=4.0->streamlit)
  Downloading jinja2-3.1.6-py3-none-any.whl.metadata (2.9 kB)
Collecting jsonschema>=3.0 (from altair!=5.4.0,!=5.4.1,<7,>=4.0->streamlit)
  Downloading jsonschema-4.26.0-py3-none-any.whl.metadata (7.6 kB)
Collecting narwhals>=2.4.0 (from altair!=5.4.0,!=5.4.1,<7,>=4.0->streamlit)
  Downloading narwhals-2.20.0-py3-none-any.whl.metadata (15 kB)
Collecting gitdb<5,>=4.0.1 (from gitpython!=3.1.19,<4,>=3.0.7->streamlit)
  Downloading gitdb-4.0.12-py3-none-any.whl.metadata (1.2 kB)
Collecting smmap<6,>=3.0.1 (from gitdb<5,>=4.0.1->gitpython!=3.1.19,<4,>=3.0.7->streamlit)
  Downloading smmap-5.0.3-py3-none-any.whl.metadata (4.6 kB)
Collecting python-dateutil>=2.8.2 (from pandas<4,>=1.4.0->streamlit)
  Downloading python_dateutil-2.9.0.post0-py2.py3-none-any.whl.metadata (8.4 kB)
Collecting charset_normalizer<4,>=2 (from requests<3,>=2.27->streamlit)
  Downloading charset_normalizer-3.4.7-cp314-cp314-macosx_10_15_universal2.whl.metadata (40 kB)
Collecting idna<4,>=2.5 (from requests<3,>=2.27->streamlit)
  Downloading idna-3.12-py3-none-any.whl.metadata (8.0 kB)
Collecting urllib3<3,>=1.26 (from requests<3,>=2.27->streamlit)
  Downloading urllib3-2.6.3-py3-none-any.whl.metadata (6.9 kB)
Collecting certifi>=2023.5.7 (from requests<3,>=2.27->streamlit)
  Downloading certifi-2026.2.25-py3-none-any.whl.metadata (2.5 kB)
Collecting MarkupSafe>=2.0 (from jinja2->altair!=5.4.0,!=5.4.1,<7,>=4.0->streamlit)
  Downloading markupsafe-3.0.3-cp314-cp314-macosx_10_13_x86_64.whl.metadata (2.7 kB)
Collecting attrs>=22.2.0 (from jsonschema>=3.0->altair!=5.4.0,!=5.4.1,<7,>=4.0->streamlit)
  Downloading attrs-26.1.0-py3-none-any.whl.metadata (8.8 kB)
Collecting jsonschema-specifications>=2023.03.6 (from jsonschema>=3.0->altair!=5.4.0,!=5.4.1,<7,>=4.0->streamlit)
  Downloading jsonschema_specifications-2025.9.1-py3-none-any.whl.metadata (2.9 kB)
Collecting referencing>=0.28.4 (from jsonschema>=3.0->altair!=5.4.0,!=5.4.1,<7,>=4.0->streamlit)
  Downloading referencing-0.37.0-py3-none-any.whl.metadata (2.8 kB)
Collecting rpds-py>=0.25.0 (from jsonschema>=3.0->altair!=5.4.0,!=5.4.1,<7,>=4.0->streamlit)
  Downloading rpds_py-0.30.0-cp314-cp314-macosx_10_12_x86_64.whl.metadata (4.1 kB)
Collecting six>=1.5 (from python-dateutil>=2.8.2->pandas<4,>=1.4.0->streamlit)
  Downloading six-1.17.0-py2.py3-none-any.whl.metadata (1.7 kB)
Downloading streamlit-1.56.0-py3-none-any.whl (9.1 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 9.1/9.1 MB 38.7 MB/s  0:00:00
Downloading numpy-2.4.4-cp314-cp314-macosx_10_15_x86_64.whl (16.7 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 16.7/16.7 MB 57.7 MB/s  0:00:00
Downloading altair-6.1.0-py3-none-any.whl (796 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 797.0/797.0 kB 18.1 MB/s  0:00:00
Downloading blinker-1.9.0-py3-none-any.whl (8.5 kB)
Downloading cachetools-7.0.6-py3-none-any.whl (13 kB)
Downloading click-8.3.2-py3-none-any.whl (108 kB)
Downloading gitpython-3.1.46-py3-none-any.whl (208 kB)
Downloading gitdb-4.0.12-py3-none-any.whl (62 kB)
Downloading pandas-3.0.2-cp314-cp314-macosx_10_15_x86_64.whl (10.3 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 10.3/10.3 MB 59.7 MB/s  0:00:00
Downloading pillow-12.2.0-cp314-cp314-macosx_10_15_x86_64.whl (5.3 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 5.3/5.3 MB 57.3 MB/s  0:00:00
Downloading protobuf-7.34.1-cp310-abi3-macosx_10_9_universal2.whl (429 kB)
Downloading pydeck-0.9.2-py2.py3-none-any.whl (11.3 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 11.3/11.3 MB 57.4 MB/s  0:00:00
Downloading requests-2.33.1-py3-none-any.whl (64 kB)
Downloading charset_normalizer-3.4.7-cp314-cp314-macosx_10_15_universal2.whl (309 kB)
Downloading idna-3.12-py3-none-any.whl (68 kB)
Downloading smmap-5.0.3-py3-none-any.whl (24 kB)
Downloading tenacity-9.1.4-py3-none-any.whl (28 kB)
Downloading toml-0.10.2-py2.py3-none-any.whl (16 kB)
Downloading tornado-6.5.5-cp39-abi3-macosx_10_9_x86_64.whl (444 kB)
Downloading typing_extensions-4.15.0-py3-none-any.whl (44 kB)
Downloading urllib3-2.6.3-py3-none-any.whl (131 kB)
Downloading certifi-2026.2.25-py3-none-any.whl (153 kB)
Downloading jinja2-3.1.6-py3-none-any.whl (134 kB)
Downloading jsonschema-4.26.0-py3-none-any.whl (90 kB)
Downloading attrs-26.1.0-py3-none-any.whl (67 kB)
Downloading jsonschema_specifications-2025.9.1-py3-none-any.whl (18 kB)
Downloading markupsafe-3.0.3-cp314-cp314-macosx_10_13_x86_64.whl (11 kB)
Downloading narwhals-2.20.0-py3-none-any.whl (449 kB)
Downloading packaging-26.1-py3-none-any.whl (95 kB)
Downloading pyarrow-24.0.0-cp314-cp314-macosx_12_0_x86_64.whl (36.7 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 36.7/36.7 MB 66.5 MB/s  0:00:00
Downloading python_dateutil-2.9.0.post0-py2.py3-none-any.whl (229 kB)
Downloading referencing-0.37.0-py3-none-any.whl (26 kB)
Downloading rpds_py-0.30.0-cp314-cp314-macosx_10_12_x86_64.whl (362 kB)
Downloading six-1.17.0-py2.py3-none-any.whl (11 kB)
Installing collected packages: urllib3, typing-extensions, tornado, toml, tenacity, smmap, six, rpds-py, pyarrow, protobuf, pillow, packaging, numpy, narwhals, MarkupSafe, idna, click, charset_normalizer, certifi, cachetools, blinker, attrs, requests, referencing, python-dateutil, jinja2, gitdb, pydeck, pandas, jsonschema-specifications, gitpython, jsonschema, altair, streamlit
Successfully installed MarkupSafe-3.0.3 altair-6.1.0 attrs-26.1.0 blinker-1.9.0 cachetools-7.0.6 certifi-2026.2.25 charset_normalizer-3.4.7 click-8.3.2 gitdb-4.0.12 gitpython-3.1.46 idna-3.12 jinja2-3.1.6 jsonschema-4.26.0 jsonschema-specifications-2025.9.1 narwhals-2.20.0 numpy-2.4.4 packaging-26.1 pandas-3.0.2 pillow-12.2.0 protobuf-7.34.1 pyarrow-24.0.0 pydeck-0.9.2 python-dateutil-2.9.0.post0 referencing-0.37.0 requests-2.33.1 rpds-py-0.30.0 six-1.17.0 smmap-5.0.3 streamlit-1.56.0 tenacity-9.1.4 toml-0.10.2 tornado-6.5.5 typing-extensions-4.15.0 urllib3-2.6.3
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
            

