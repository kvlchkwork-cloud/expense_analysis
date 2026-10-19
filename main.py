

from src.load_data import load_expenses
import pandas as pd
from src.analyze import (
    total_expenses,
    expenses_by_category,
    most_expensive_purchase,
    save_category_summary,
    save_summary_report,
    expenses_by_date,
    save_daily_summary,
    check_data_quality,
)
from src.visualize import plot_expenses_by_category


def main():
    expenses = load_expenses()

    if not check_data_quality(expenses):
        print("Анализ остановлен: проверьте данные.")
        return

    total = total_expenses(expenses)
    print(f"Общая сумма расходов: {total:.2f}")

    print("\nРасходы по категориям:")
    print(expenses_by_category(expenses))

    print("\nРасходы по дням:")
    print(expenses_by_date(expenses))

    print("\nСамая дорогая покупка:")
    print(most_expensive_purchase(expenses))

    image_path = plot_expenses_by_category(expenses)
    print(f"\nДиаграмма сохранена: {image_path}")

    save_category_summary(expenses)
    print("Сводка сохранена: outputs/category_summary.csv")

    save_summary_report(expenses)
    print("Общий отчёт сохранён: outputs/summary.csv")

    save_daily_summary(expenses)
    print("Расходы по дням сохранены: outputs/daily_summary.csv")



if __name__ == "__main__":
    main()