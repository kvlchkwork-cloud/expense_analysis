import pandas as pd

def total_expenses(expenses):
    return expenses["amount"].sum()

def expenses_by_category(expenses):
    return expenses.groupby("category")["amount"].sum().sort_values(ascending=False)

def most_expensive_purchase(expenses):
    return expenses.loc[expenses["amount"].idxmax()]


def save_category_summary(expenses):
    summary = expenses_by_category(expenses)

    summary.to_csv(
        "outputs/category_summary.csv",
        header=["amount"],
        index_label="category",
    )

def save_summary_report(expenses):
    report = pd.DataFrame({
        "metric": [
            "total_expenses",
            "average_expense",
            "max_expense",
            "number_of_expenses",
        ],
        "value": [
            round(total_expenses(expenses), 2),
            round(expenses["amount"].mean(), 2),
            round(expenses["amount"].max(), 2),
            len(expenses),
        ],
    })

    report.to_csv("outputs/summary.csv", index=False)


def expenses_by_date(expenses):
    daily_totals = (
        expenses.groupby("date")["amount"]
        .sum()
        .sort_values(ascending=False)
    )

    return daily_totals


def save_daily_summary(expenses):
    daily_totals = expenses_by_date(expenses)
    daily_totals.to_csv(
        "outputs/daily_summary.csv",
        header=["amount"],
        index_label="date",
    )


def check_missing_values(expenses):
    missing_values = expenses.isnull().sum()

    print("\nПропущенные значения:")
    print(missing_values)

    return missing_values


def check_duplicates(expenses):
    duplicates = expenses.duplicated().sum()

    print("\nКоличество дубликатов:")
    print(duplicates)

    return duplicates


def check_invalid_values(expenses):
    # Ищем суммы меньше нуля
    negative_amounts = expenses[expenses["amount"] < 0]

    # Ищем даты, которые не удалось распознать
    invalid_dates = expenses[expenses["date"].isna()]

    print("\nНекорректные данные:")

    print("Отрицательные суммы:", len(negative_amounts))
    print("Некорректные даты:", len(invalid_dates))

    return negative_amounts, invalid_dates


def check_data_quality(expenses):
    print("\n===== ОТЧЁТ О КАЧЕСТВЕ ДАННЫХ =====")

    missing_values = check_missing_values(expenses)
    duplicates = check_duplicates(expenses)
    negative_amounts, invalid_dates = check_invalid_values(expenses)

    has_problems = (
        missing_values.sum() > 0
        or duplicates > 0
        or len(negative_amounts) > 0
        or len(invalid_dates) > 0
    )

    if has_problems:
        print("\nОбнаружены проблемы. Нужно проверить данные.")
    else:
        print("\nПроблем не обнаружено!")

    print("===== КОНЕЦ ОТЧЁТА =====")









