def explain_stress_with_llm(stress_result: dict) -> str:
    return (
        f"Under the scenario '{stress_result['scenario']}', the financial "
        f"health score remained at {stress_result['score']}. "
        f"However, the Stress Impact Index of "
        f"{stress_result['stress_impact_index']}% indicates reduced "
        f"financial resilience. The primary concern is "
        f"{stress_result['primary_risk']}."
    )
