def generate_ai_insights(metrics: dict, score_result: dict) -> dict:
    insights = []
    recommendations = []

    if metrics["profit_margin"] > 0.2:
        insights.append(
            "The business demonstrates strong profitability, indicating effective cost management."
        )
    else:
        recommendations.append(
            "Improve pricing strategy or reduce operating expenses."
        )

    if metrics["current_ratio"] < 1:
        insights.append(
            "The business faces liquidity stress and may struggle with short-term obligations."
        )
        recommendations.extend([
            "Improve receivables collection.",
            "Maintain higher cash reserves.",
        ])

    if score_result["primary_risk"] == "liquidity":
        insights.append(
            "Liquidity is the primary financial risk that needs immediate attention."
        )

    return {
        "insights": insights,
        "recommendations": recommendations,
    }
