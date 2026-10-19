
import matplotlib.pyplot as plt

def plot_expenses_by_category(expenses):
 
 category_totals = (
     expenses.groupby("category")["amount"]
     .sum()
    .sort_values(ascending=False)
 )

 category_totals.plot(kind="bar")

 plt.title("Expenses by Category")
 plt.xlabel("Category")
 plt.ylabel("Amount")
 plt.tight_layout()

 output_path = "outputs/expenses_by_category.png"
 plt.savefig(output_path)
 plt.show()

 return output_path