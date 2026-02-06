import pandas as pd
from backend.analysis import compute_financial_metrics
from backend.scoring import calculate_health_score


def calculate_stress_impact(base: dict, stressed: dict) -> float:
    impact = 0.0

    if base["profit_margin"] > 0:
        impact += abs(
            stressed["profit_margin"] - base["profit_margin"]
        ) / base["profit_margin"]

    if base["current_ratio"] > 0:
        impact += abs(
            stressed["current_ratio"] - base["current_ratio"]
        ) / base["current_ratio"]

    return round(impact * 100, 2)


def apply_revenue_shock(
    df: pd.DataFrame, drop_percent: float, base_metrics: dict
) -> dict:
    stressed_df = df.copy()
    stressed_df["revenue"] *= (1 - drop_percent)

    stressed_metrics = compute_financial_metrics(stressed_df)
    score = calculate_health_score(stressed_metrics)

    return {
        "scenario": f"Revenue drop of {int(drop_percent * 100)}%",
        "score": score["total_score"],
        "primary_risk": score["primary_risk"],
        "stress_impact_index": calculate_stress_impact(
            base_metrics, stressed_metrics
        ),
    }
