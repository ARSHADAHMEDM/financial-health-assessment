import copy
import pandas as pd

from analysis import compute_financial_metrics
from scoring import calculate_health_score


def apply_revenue_shock(df: pd.DataFrame, drop_percent: float, base_metrics: dict) -> dict:
    stressed_df = df.copy()
    stressed_df["revenue"] = stressed_df["revenue"] * (1 - drop_percent)

    stressed_metrics = compute_financial_metrics(stressed_df)
    score_result = calculate_health_score(stressed_metrics)

    impact = calculate_stress_impact(base_metrics, stressed_metrics)

    return {
        "scenario": f"Revenue drop of {int(drop_percent * 100)}%",
        "score": score_result["total_score"],
        "primary_risk": score_result["primary_risk"],
        "stress_impact_index": impact
    }


def apply_expense_increase(df: pd.DataFrame, increase_percent: float) -> dict:
    """
    Simulate an expense increase scenario.
    """
    stressed_df = df.copy()
    stressed_df["expense"] = stressed_df["expense"] * (1 + increase_percent)

    metrics = compute_financial_metrics(stressed_df)
    score_result = calculate_health_score(metrics)

    return {
        "scenario": f"Expense increase of {int(increase_percent * 100)}%",
        "score": score_result["total_score"],
        "primary_risk": score_result["primary_risk"]
    }


def apply_receivables_delay(df: pd.DataFrame, increase_percent: float) -> dict:
    """
    Simulate receivables collection delay.
    """
    stressed_df = df.copy()
    stressed_df["receivables"] = stressed_df["receivables"] * (1 + increase_percent)

    metrics = compute_financial_metrics(stressed_df)
    score_result = calculate_health_score(metrics)

    return {
        "scenario": f"Receivables increase of {int(increase_percent * 100)}%",
        "score": score_result["total_score"],
        "primary_risk": score_result["primary_risk"]
    }

def calculate_stress_impact(base_metrics: dict, stressed_metrics: dict) -> float:
    """
    Measure percentage deterioration in key financial indicators.
    """

    impact = 0.0

    # Profit margin impact
    if base_metrics["profit_margin"] > 0:
        impact += abs(
            stressed_metrics["profit_margin"] - base_metrics["profit_margin"]
        ) / base_metrics["profit_margin"]

    # Liquidity impact
    if base_metrics["current_ratio"] > 0:
        impact += abs(
            stressed_metrics["current_ratio"] - base_metrics["current_ratio"]
        ) / base_metrics["current_ratio"]

    return round(impact * 100, 2)