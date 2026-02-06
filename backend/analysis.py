import pandas as pd

def load_financial_data(csv_path: str) -> pd.DataFrame:
    """
    Load and validate SME financial data from CSV.
    """

    df = pd.read_csv(csv_path)

    required_columns = [
        "date",
        "revenue",
        "expense",
        "receivables",
        "payables",
        "cash_balance",
        "loan_outstanding",
        "inventory_value"
    ]

    missing = set(required_columns) - set(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {missing}")

    df["date"] = pd.to_datetime(df["date"])
    df = df.sort_values("date")

    return df



def compute_financial_metrics(df: pd.DataFrame) -> dict:
    """
    Compute core financial metrics for SME health assessment.
    """

    total_revenue = df["revenue"].sum()
    total_expense = df["expense"].sum()
    net_profit = total_revenue - total_expense

    avg_cash = df["cash_balance"].mean()
    avg_receivables = df["receivables"].mean()
    avg_payables = df["payables"].mean()
    avg_inventory = df["inventory_value"].mean()
    avg_loan = df["loan_outstanding"].mean()

    current_assets = avg_cash + avg_receivables + avg_inventory
    current_liabilities = avg_payables + avg_loan

    current_ratio = (
        current_assets / current_liabilities
        if current_liabilities > 0 else 0
    )

    profit_margin = (
        net_profit / total_revenue
        if total_revenue > 0 else 0
    )

    return {
        "total_revenue": total_revenue,
        "total_expense": total_expense,
        "net_profit": net_profit,
        "current_ratio": round(current_ratio, 2),
        "profit_margin": round(profit_margin, 2),
        "avg_cash_balance": round(avg_cash, 2),
        "avg_loan_outstanding": round(avg_loan, 2)
    }