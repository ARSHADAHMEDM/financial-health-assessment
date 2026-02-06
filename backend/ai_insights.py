def generate_ai_insights(metrics: dict, score_result: dict) -> dict:
    """
    Generate explainable, human-friendly financial insights.
    This is a mock AI layer (deterministic & safe).
    """

    insights = []
    recommendations = []

    # Profitability insight
    if metrics["profit_margin"] > 0.2:
        insights.append(
            "The business demonstrates strong profitability, indicating effective cost management and pricing."
        )
    elif metrics["profit_margin"] > 0:
        insights.append(
            "The business is profitable but margins can be improved through cost optimization."
        )
    else:
        insights.append(
            "The business is currently unprofitable and requires immediate cost and revenue restructuring."
        )

    # Liquidity insight
    if metrics["current_ratio"] < 1:
        insights.append(
            "Despite being profitable, the business faces liquidity stress, meaning short-term obligations may be difficult to meet."
        )
        recommendations.extend([
            "Improve receivables collection cycles.",
            "Negotiate longer payment terms with suppliers.",
            "Maintain a minimum cash reserve buffer."
        ])
    else:
        insights.append(
            "The business maintains a healthy liquidity position to meet short-term obligations."
        )

    # Debt insight
    if score_result["breakdown"]["debt"]["score"] >= 30:
        insights.append(
            "Debt levels are manageable and do not pose a significant financial risk."
        )
    else:
        recommendations.append(
            "Consider restructuring or refinancing high-interest debt."
        )

    # Primary risk emphasis
    primary_risk = score_result["primary_risk"]
    insights.append(
        f"The primary financial risk identified is {primary_risk.lower()}, which should be addressed to improve overall financial health."
    )

    return {
        "insights": insights,
        "recommendations": recommendations
    }