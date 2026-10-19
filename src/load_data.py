import pandas as pd


def load_expenses():
    expenses = pd.read_csv("data/expenses.csv")

    expenses["date"] = pd.to_datetime(expenses["date"])

    return expenses
