
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="ROI Estimator", page_icon="💹")

st.title("💼 ROI Estimator Tool")
st.write("Estimate your project's Return on Investment (ROI) easily.")

st.header("Enter your project details:")
investment = st.number_input("Total Investment (₹)", min_value=0.0, step=1000.0)
annual_savings = st.number_input("Estimated Annual Savings (₹)", min_value=0.0, step=1000.0)
duration = st.number_input("Benefit Duration (in years)", min_value=1, step=1)

if investment > 0:
    total_benefit = annual_savings * duration
    net_benefit = total_benefit - investment
    roi_percentage = (net_benefit / investment) * 100
else:
    roi_percentage = 0

if st.button("Calculate ROI"):
    st.subheader("📊 ROI Results:")
    st.write(f"**Total Benefit:** ₹{total_benefit:,.2f}")
    st.write(f"**Net Benefit:** ₹{net_benefit:,.2f}")
    st.write(f"**ROI:** {roi_percentage:.2f}%")

    labels = ['Investment', 'Total Benefit']
    values = [investment, total_benefit]
    fig, ax = plt.subplots()
    ax.bar(labels, values, color=['red', 'green'])
    ax.set_title("Investment vs Benefit")
    st.pyplot(fig)
