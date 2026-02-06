def calculate_health_score(metrics: dict) -> dict:
    """
    Calculate explainable Financial Health Score (0–100).
    """

    breakdown = {
        "profitability": {
            "score": 0,
            "reason": ""
        },
        "liquidity": {
            "score": 0,
            "reason": ""
        },
        "debt": {
            "score": 0,
            "reason": ""
        }
    }

    total_score = 0

    # 1️⃣ Profitability (40 points)
    pm = metrics["profit_margin"]
    if pm > 0.20:
        breakdown["profitability"]["score"] = 40
        breakdown["profitability"]["reason"] = "Strong profit margins"
    elif pm > 0.10:
        breakdown["profitability"]["score"] = 30
        breakdown["profitability"]["reason"] = "Moderate profit margins"
    elif pm > 0:
        breakdown["profitability"]["score"] = 20
        breakdown["profitability"]["reason"] = "Low but positive profitability"
    else:
        breakdown["profitability"]["reason"] = "Business is not profitable"

    total_score += breakdown["profitability"]["score"]

    # 2️⃣ Liquidity (30 points)
    cr = metrics["current_ratio"]
    if cr > 1.5:
        breakdown["liquidity"]["score"] = 30
        breakdown["liquidity"]["reason"] = "Healthy liquidity position"
    elif cr > 1.0:
        breakdown["liquidity"]["score"] = 20
        breakdown["liquidity"]["reason"] = "Adequate liquidity"
    elif cr > 0.75:
        breakdown["liquidity"]["score"] = 10
        breakdown["liquidity"]["reason"] = "Tight liquidity"
    else:
        breakdown["liquidity"]["reason"] = "Liquidity stress detected"

    total_score += breakdown["liquidity"]["score"]

    # 3️⃣ Debt (30 points)
    avg_loan = metrics["avg_loan_outstanding"]
    total_revenue = metrics["total_revenue"]

    if avg_loan < total_revenue * 0.5:
        breakdown["debt"]["score"] = 30
        breakdown["debt"]["reason"] = "Low debt burden"
    elif avg_loan < total_revenue:
        breakdown["debt"]["score"] = 20
        breakdown["debt"]["reason"] = "Moderate debt exposure"
    else:
        breakdown["debt"]["score"] = 10
        breakdown["debt"]["reason"] = "High debt burden"

    total_score += breakdown["debt"]["score"]

    # Primary risk identification
    primary_risk = min(
        breakdown,
        key=lambda k: breakdown[k]["score"]
    )

    return {
        "total_score": min(total_score, 100),
        "breakdown": breakdown,
        "primary_risk": primary_risk
    }