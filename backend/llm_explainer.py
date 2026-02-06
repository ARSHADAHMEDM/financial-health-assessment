import os


def explain_stress_with_llm(scenario: dict) -> str:
    """
    Uses Grok LLM (if available) to explain stress test results.
    Falls back to rule-based explanation if API fails.
    """

    try:
        # 1️⃣ Read API key safely
        api_key = os.getenv("GROK_API_KEY")
        if not api_key:
            raise RuntimeError("Grok API key not found")

        # 2️⃣ Lazy import (important)
        from groq import Groq

        client = Groq(api_key=api_key)

        prompt = f"""
        A small business has undergone a financial stress test.

        Scenario: {scenario['scenario']}
        Financial Health Score: {scenario['score']}
        Stress Impact Index: {scenario['stress_impact_index']}%
        Primary Risk: {scenario['primary_risk']}

        Explain the business impact in simple language
        and give 2 practical recommendations.
        """

        response = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3,
        )

        return response.choices[0].message.content.strip()

    except Exception as e:
        # 3️⃣ Fallback (VERY IMPORTANT)
        return fallback_stress_explanation(scenario)


def fallback_stress_explanation(scenario: dict) -> str:
    """
    Deterministic fallback explanation if LLM fails.
    """

    return (
        f"Under the scenario '{scenario['scenario']}', the financial health score "
        f"remained at {scenario['score']}, but the Stress Impact Index of "
        f"{scenario['stress_impact_index']}% indicates reduced financial resilience. "
        f"The primary concern is {scenario['primary_risk'].lower()}, suggesting the "
        f"business should focus on improving cash flow stability and short-term planning."
    )