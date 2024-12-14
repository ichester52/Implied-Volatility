import streamlit as st
import numpy as np
import pandas as pd
import math

st.title("Implied Volatility Surface")

with st.sidebar:
    st.write("## Model Parameters"),
    st.write("Adjust the parameters for the Black Scholes model"),
    rfr = st.number_input("Risk-Free Rate (e.g., 0.015 for 1.5%)", value=0.0150),
    st.write("Divedend Yield (e.g, 0.013 for 1.3%)"),
    div_yield = st.number_input("Dividend Yield", value=0.013),
    st.write("## Visualization Parameters"),
    y_axis = option = st.selectbox("Select Y-axis:",
    ("Strike Price ($)", "Moneyness",)),
    st.write("## Ticker Symbol"),
    ticker = st.text_input("Enter Ticker Symbol", value="SPY"),
    st.write("## Strike Price Filter Parameters"),
    st.number_input(f"Minimum Strike Price (% of Spot price)", value=70.0),
    st.number_input(f"Maximum Strike Price (% of Spot price)", value=130.0)

# st.write("Mortage Repayments Calculator")

# st.write("### Input Data")
# col1, col2 = st.columns(2) # split into two different columns
# home_value = col1.number_input("Deposit", min_value=0, value=500000)
# deposit = col1.number_input('Deposit', min_value=0, value=100000)
# interest_rate = col2.number_input('Interest Rate (in %)', min_value=0.0, value=5.5)
# loan_term = col2.number_input("Loan Term (in years)", min_value=1, value=30)

# loan_amount = home_value - deposit
# monthly_interest_rate = (interest_rate / 100) / 12
# number_of_payments = loan_term * 12
# monthly_payment = (
#     loan_amount
#     * (monthly_interest_rate * (1 + monthly_interest_rate) ** number_of_payments)
#     / ((1 + monthly_interest_rate) ** number_of_payments - 1)
# )

# total_payments = monthly_payment * number_of_payments
# total_interest = total_payments - loan_amount

# st.write('### Repayments')
# col1, col2, col3 = st.columns(3)
# col1.metric("Monthly Payments", f"${monthly_payment:.2f}")
# col2.metric("Total Payments", f"${total_payments:.2f}")
# col3.metric("Total Interest", f"${total_interest:.2f}")

# schedule = []
# remaining_balance = loan_amount

# for i in range(1, number_of_payments + 1):
#     interest_payment = remaining_balance * monthly_interest_rate
#     principal_payment = monthly_payment - interest_payment
#     remaining_balance -= principal_payment
#     year = math.ceil(i / 12)  # Calculate the year into the loan
#     schedule.append(
#         [
#             i,
#             monthly_payment,
#             principal_payment,
#             interest_payment,
#             remaining_balance,
#             year,
#         ]
#     )

# df = pd.DataFrame(
#     schedule,
#     columns=["Month", "Payment", "Principal", "Interest", "Remaining Balance", "Year"],
# )

# # Display the data-frame as a chart.
# st.write("### Payment Schedule")
# payments_df = df[["Year", "Remaining Balance"]].groupby("Year").min()
# st.line_chart(payments_df)