import pandas as pd


def load_financial_data(path: str) -> pd.DataFrame:
    return pd.read_csv(path)


def compute_financial_metrics(df: pd.DataFrame) -> dict:
    total_revenue = df["revenue"].sum()
    total_expense = df["expense"].sum()
    net_profit = total_revenue - total_expense

    current_assets = df["cash"].mean() + df["receivables"].mean()
    current_liabilities = df["payables"].mean() + df["short_term_loans"].mean()

    current_ratio = (
        current_assets / current_liabilities
        if current_liabilities > 0
        else 0
    )

    profit_margin = (
        net_profit / total_revenue
        if total_revenue > 0
        else 0
    )

    return {
        "total_revenue": total_revenue,
        "total_expense": total_expense,
        "net_profit": net_profit,
        "current_ratio": round(current_ratio, 2),
        "profit_margin": round(profit_margin, 2),
        "avg_cash_balance": df["cash"].mean(),
        "avg_loan_outstanding": df["loan_balance"].mean(),
    }
