import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

if 'expenses' not in st.session_state:
    st.session_state.expenses = pd.DataFrame(columns=['Date', 'Category', 'Amount', 'Description'])
    
st.title(" Personalised Expense Tracker")
with st.sidebar:
    st.header("Add New Expense")
    date = st.date_input("Date")
    category = st.selectbox("Category", ["Food", "Transport", "Entertainment", "Utilities", "Other"])
    amount = st.number_input("Amount", min_value=0.0, format="%.2f")
    description = st.text_input("Description")
    
    if st.button("Add Expense"):
        new_expense = pd.DataFrame({
            'Date': [date],
            'Category': [category],
            'Amount': [amount],
            'Description': [description]
        })
        st.session_state.expenses = pd.concat([st.session_state.expenses, new_expense], ignore_index=True)
        st.success("Expense added!")
    if st.button('save expenses'):
        st.session_state.expenses.to_csv('expenses.csv', index=False)
        st.success("Expenses saved to expenses.csv")
    if st.button('load expenses'):
        try:
            st.session_state.expenses = pd.read_csv('expenses.csv')
            st.success("Expenses loaded from expenses.csv")
        except FileNotFoundError:
            st.error("No saved expenses found.")
st.header("Expenses")
st.write(st.session_state.expenses)

st.header('visulization')
if st.button('visulize expenses'):
    if not st.session_state.expenses.empty:
        fig, ax = plt.subplots()
        sns.barplot(data=st.session_state.expenses, x='Category', y='Amount', ax=ax)
        ax.set_title('Expenses by Category')
        st.pyplot(fig)
    else:
        st.warning("No expenses to visualize.")
