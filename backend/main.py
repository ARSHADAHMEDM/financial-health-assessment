from analysis import load_financial_data, compute_financial_metrics
from scoring import calculate_health_score
from ai_insights import generate_ai_insights
from stress_test import apply_revenue_shock
from llm_explainer import explain_stress_with_llm

def print_divider(title: str):
    print("\n" + "=" * 50)
    print(title)
    print("=" * 50)


if __name__ == "__main__":

    # 1️⃣ Load financial data
    df = load_financial_data("../sample_data/sme_financials.csv")

    # 2️⃣ Compute base financial metrics
    metrics = compute_financial_metrics(df)

    # 3️⃣ Calculate explainable health score
    score_result = calculate_health_score(metrics)

    # 4️⃣ Generate AI insights (mock, deterministic)
    ai_output = generate_ai_insights(metrics, score_result)

    # ---------------- OUTPUT SECTION ----------------

    print_divider("FINANCIAL METRICS")
    for key, value in metrics.items():
        print(f"{key}: {value}")

    print_divider("FINANCIAL HEALTH SCORE BREAKDOWN")
    for section, info in score_result["breakdown"].items():
        print(f"{section.title()}: +{info['score']} → {info['reason']}")

    print(f"\nFinal Financial Health Score: {score_result['total_score']}/100")
    print(f"Primary Risk Identified: {score_result['primary_risk'].title()}")

    print_divider("AI INSIGHTS")
    for insight in ai_output["insights"]:
        print(f"- {insight}")

    print_divider("AI RECOMMENDATIONS")
    if ai_output["recommendations"]:
        for rec in ai_output["recommendations"]:
            print(f"- {rec}")
    else:
        print("- No immediate action required")

    # ---------------- STRESS TESTING ----------------

    print_divider("STRESS TEST RESULTS (WITH IMPACT INDEX)")

    base_metrics = metrics

    stress_result = apply_revenue_shock(
        df=df,
        drop_percent=0.15,
        base_metrics=base_metrics
    )

    print(
        f"{stress_result['scenario']}:\n"
        f"Score = {stress_result['score']}\n"
        f"Stress Impact Index = {stress_result['stress_impact_index']}%\n"
        f"Primary Risk = {stress_result['primary_risk'].title()}"
    )

    print_divider("STRESS SCENARIO EXPLANATION")

    explanation = explain_stress_with_llm(stress_result)
    print(explanation)