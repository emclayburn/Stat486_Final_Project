import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="NHL Salary Predictor", page_icon="🏒")

@st.cache_data
def load_data():
    return pd.read_csv('data/valuation_results.csv')

results = load_data()

st.sidebar.image("https://upload.wikimedia.org/wikipedia/en/3/3a/05_NHL_Shield.svg", width=100)
st.sidebar.title("Player Lookup")
player = st.sidebar.selectbox("Select a player:", results['name'].sort_values())

st.title("🏒 NHL Market Value Analyzer")
st.markdown("Predicting **2025-26 Market Value** based on 2024-25 performance stats.")

data = results[results['name'] == player].iloc[0]

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Actual AAV", f"${data['AAV']:,.0f}")

with col2:
    st.metric("Predicted Value", f"${data['Predicted_AAV']:,.0f}")

with col3:
    delta_val = data['Difference']
    st.metric("Market Gap", f"${delta_val:,.0f}", delta=f"{delta_val:,.0f}", delta_color="normal")

st.divider()

st.subheader(f"Value Verdict for {player}")

if delta_val > 1000000:
    st.success(f"🔥 **High Value:** The model suggests {player} is significantly underpaid relative to their production.")
elif delta_val < -1000000:
    st.error(f"⚠️ **Premium Price:** {player}'s contract is higher than their current statistical output justifies.")
else:
    st.info(f"✅ **Fair Market Value:** This contract aligns well with the player's performance.")

with st.expander("View Underlying Stats"):
    st.write(f"**Points (PTS):** {data['PTS']}")
    st.write(f"**Expected Goals (xG):** {data['I_F_xGoals']:.2f}")
    st.write(f"**Age:** {data['Age']}")