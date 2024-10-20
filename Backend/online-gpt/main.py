from fastapi import FastAPI, Query
from model import gpt_turbo_response

app = FastAPI()


@app.get("/model-response")
def get_gpt_opinion(prompt: str = Query(..., title="llm-response",
                                        description="What is gpt4-mini opinion on what you asked them")):
    model_response = gpt_turbo_response(prompt)
    api_response = [{'generated_text': model_response}]
    return api_response


@app.get("/gpt-status")
def get_gpt_status():
    return {"status": 200}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8091)
