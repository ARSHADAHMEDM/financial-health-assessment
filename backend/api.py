from fastapi import FastAPI, UploadFile, File, HTTPException
import pandas as pd
import io

from backend.analysis import compute_financial_metrics
from backend.scoring import calculate_health_score
from backend.ai_insights import generate_ai_insights
from backend.stress_test import apply_revenue_shock
from backend.serializers import serialize_response
from backend.llm_explainer import explain_stress_with_llm

app = FastAPI(title="Financial Health Assessment API")


@app.get("/health")
def health():
    return {"status": "ok", "message": "API is running"}


@app.post("/analyze")
def analyze(file: UploadFile = File(...)):
    try:
        df = pd.read_csv(io.BytesIO(file.file.read()))

        metrics = compute_financial_metrics(df)
        score = calculate_health_score(metrics)
        insights = generate_ai_insights(metrics, score)

        return serialize_response({
            "metrics": metrics,
            "score": score,
            "ai_insights": insights,
        })

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.post("/stress-test")
def stress_test(file: UploadFile = File(...)):
    try:
        df = pd.read_csv(io.BytesIO(file.file.read()))
        base_metrics = compute_financial_metrics(df)

        stress = apply_revenue_shock(
            df=df,
            drop_percent=0.15,
            base_metrics=base_metrics,
        )

        explanation = explain_stress_with_llm(stress)

        return serialize_response({
            "stress_result": stress,
            "explanation": explanation,
        })

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
