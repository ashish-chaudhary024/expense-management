import streamlit as st
import pandas as pd

# text elements
st.header('Streamlit Core Features')
st.subheader("Text Elements")
st.text("This is a simple text element.")

# Data Display
st.subheader("Data Display")
st.write("Here is a simple table:")

df = pd.DataFrame({
    "Date": ["2024-08-01", "2024-08-02", "2024-08-03"],
    "Amount": [250, 134, 340]
})
st.table(df)

# Charts
st.subheader("Charts")
st.line_chart([1, 2, 3, 4])

# User Input
st.subheader("User Input")
value = st.slider("Select a value", 0, 100)
st.write(f"Selected value: {value}")

st.title("Interactive Widgets Example")

# Checkbox
if st.checkbox ("Show/Hide"):
    st.write("Checkbox is checked!")

# Selectbox
options = st.selectbox("Select a number", [1, 2, 3, 4])
st.write(f"You selected: {options}")

# Multiselect
multi_options = st.multiselect("Select multiple numbers", [1, 2, 3, 4, 5])
st.write(f"You selected: {multi_options}")


expense_dt = st.date_input("Expense Date: ")
if expense_dt:
    st.write(f"Fetching expenses for {expense_dt}")
name = st.number_input("Enter your name")