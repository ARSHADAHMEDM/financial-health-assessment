def calculate_health_score(metrics: dict) -> dict:
    score = 0
    breakdown = {}

    # Profitability
    if metrics["profit_margin"] > 0.2:
        breakdown["profitability"] = {
            "score": 40,
            "reason": "Strong profit margins",
        }
        score += 40
    elif metrics["profit_margin"] > 0:
        breakdown["profitability"] = {
            "score": 20,
            "reason": "Moderate profitability",
        }
        score += 20
    else:
        breakdown["profitability"] = {
            "score": 0,
            "reason": "Unprofitable business",
        }

    # Liquidity
    if metrics["current_ratio"] >= 1.5:
        breakdown["liquidity"] = {
            "score": 30,
            "reason": "Healthy liquidity",
        }
        score += 30
    elif metrics["current_ratio"] >= 1:
        breakdown["liquidity"] = {
            "score": 15,
            "reason": "Adequate liquidity",
        }
        score += 15
    else:
        breakdown["liquidity"] = {
            "score": 0,
            "reason": "Liquidity stress detected",
        }

    # Debt
    if metrics["avg_loan_outstanding"] < metrics["total_revenue"] * 0.5:
        breakdown["debt"] = {
            "score": 30,
            "reason": "Low debt burden",
        }
        score += 30
    else:
        breakdown["debt"] = {
            "score": 10,
            "reason": "High debt exposure",
        }
        score += 10

    primary_risk = min(breakdown, key=lambda x: breakdown[x]["score"])

    return {
        "total_score": score,
        "breakdown": breakdown,
        "primary_risk": primary_risk,
    }
