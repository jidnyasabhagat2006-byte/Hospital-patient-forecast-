# hospital_forecast_app.py

import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

# ---------------------------------
# PAGE TITLE
# ---------------------------------
st.title("🏥 Hospital Patient Forecast Modelling")

# ---------------------------------
# USER INPUTS (SIDEBAR)
# ---------------------------------
st.sidebar.header("Adjust Parameters")

P0 = st.sidebar.number_input("Initial Patients (P0)", value=50)
r = st.sidebar.slider("Growth Rate (r)", 0.01, 1.0, 0.25)
K = st.sidebar.number_input("Hospital Capacity (K)", value=300)
months = st.sidebar.slider("Months to Predict", 1, 24, 12)

# ---------------------------------
# TIME ARRAY
# ---------------------------------
t = np.arange(0, months + 1)

# ---------------------------------
# EXPONENTIAL GROWTH
# ---------------------------------
exp_growth = P0 * np.exp(r * t)

# ---------------------------------
# LOGISTIC GROWTH
# ---------------------------------
log_growth = K / (1 + ((K - P0)/P0) * np.exp(-r * t))

# ---------------------------------
# PLOT GRAPH
# ---------------------------------
fig, ax = plt.subplots()

ax.plot(t, exp_growth, label="Exponential Growth")
ax.plot(t, log_growth, label="Logistic Growth")
ax.axhline(y=K, linestyle="--", label="Hospital Capacity (K)")

ax.set_xlabel("Months")
ax.set_ylabel("Number of Patients")
ax.set_title("Hospital Patient Forecast Model")
ax.legend()

# Show in Streamlit
st.pyplot(fig)

# ---------------------------------
# EXTRA INFO
# ---------------------------------
st.subheader("📊 Insights")
st.write("""
- Exponential growth increases rapidly without limits.
- Logistic growth slows as it nears hospital capacity.
- Dashed line shows maximum capacity.
""")
