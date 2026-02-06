import pandas as pd


def load_financial_data(path: str) -> pd.DataFrame:
    return pd.read_csv(path)


def compute_financial_metrics(df: pd.DataFrame) -> dict:
    """
    Computes core financial metrics from SME financial data.
    Handles real-world datasets gracefully.
    """

    # Required columns for YOUR dataset
    REQUIRED_COLUMNS = {
        "revenue",
        "expense",
        "receivables",
        "payables",
        "cash",
        "loan_outstanding",
    }

    missing = REQUIRED_COLUMNS - set(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {', '.join(missing)}")

    # Core calculations
    total_revenue = df["revenue"].sum()
    total_expense = df["expense"].sum()
    net_profit = total_revenue - total_expense

    # Liquidity
    current_assets = df["cash"].mean() + df["receivables"].mean()
    current_liabilities = df["payables"].mean() + df["loan_outstanding"].mean()

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
        "total_revenue": round(total_revenue, 2),
        "total_expense": round(total_expense, 2),
        "net_profit": round(net_profit, 2),
        "current_ratio": round(current_ratio, 2),
        "profit_margin": round(profit_margin, 2),
        "avg_cash_balance": round(df["cash"].mean(), 2),
        "avg_loan_outstanding": round(df["loan_outstanding"].mean(), 2),
    }
