import pandas as pd


def calculate_profitability(revenue: float, cost: float) -> float:
    """Возвращает рентабельность в процентах."""
    if revenue == 0:
        return 0.0
    return (revenue - cost) / revenue * 100


def calculate_average_revenue(revenues: list) -> float:
    """Возвращает среднюю выручку за период."""
    if not revenues:
        return 0.0
    return sum(revenues) / len(revenues)


def main():
    data = {
        "Месяц": ["Январь", "Февраль", "Март"],
        "Выручка": [120000, 150000, 135000],
    }
    df = pd.DataFrame(data)
    print(df)
    print("Средняя выручка:", df["Выручка"].mean())

    revenue = 150000
    cost = 100000
    print(f"Рентабельность: {calculate_profitability(revenue, cost):.2f}%")

    revenues = [120000, 150000, 135000]
    print(f"Средняя выручка (функция): {calculate_average_revenue(revenues):.2f}")


if __name__ == "__main__":
    main()