from fastapi import FastAPI, UploadFile, File, HTTPException
import pandas as pd
import io
from backend.serializers import serialize_response
from backend.analysis import compute_financial_metrics
from backend.scoring import calculate_health_score
from backend.ai_insights import generate_ai_insights
from backend.stress_test import apply_revenue_shock
from backend.llm_explainer import explain_stress_with_llm

app = FastAPI(
    title="Financial Health Assessment API",
    description="Explainable financial health and stress testing for SMEs",
    version="1.0.0"
)


# ---------------- BASIC HEALTH CHECK ----------------

@app.get("/health")
def health_check():
    return {"status": "ok", "message": "API is running"}


# ---------------- ANALYSIS ENDPOINT ----------------

@app.post("/analyze")
def analyze_financials(file: UploadFile = File(...)):
    try:
        contents = file.file.read()
        df = pd.read_csv(io.BytesIO(contents))

        metrics = compute_financial_metrics(df)
        score_result = calculate_health_score(metrics)
        ai_output = generate_ai_insights(metrics, score_result)

        response = {
            "metrics": metrics,
            "score": score_result,
            "ai_insights": ai_output
        }

        return serialize_response(response)

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


# ---------------- STRESS TEST ENDPOINT ----------------

@app.post("/stress-test")
def stress_test_financials(file: UploadFile = File(...)):
    try:
        contents = file.file.read()
        df = pd.read_csv(io.BytesIO(contents))

        base_metrics = compute_financial_metrics(df)

        stress_result = apply_revenue_shock(
            df=df,
            drop_percent=0.15,
            base_metrics=base_metrics
        )

        explanation = explain_stress_with_llm(stress_result)

        response = {
            "stress_result": stress_result,
            "llm_explanation": explanation
        }

        return serialize_response(response)

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
