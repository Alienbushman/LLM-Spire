from fastapi import FastAPI, Query
from LocalLLM import llm_output, gpu_available, running_on_device, gpu_details

app = FastAPI()


@app.get("/model-response")
def get_llm_response(prompt: str = Query(..., title="llm-response",
                                         description="What is gpt-2's opinion on what you asked them"),
                     model: str = Query("local-llm", title="Model", description="The model you want to use")
                     ):
    print(f"question: {prompt}")
    response = llm_output(prompt, model)
    print(f"response: {response}")
    return response


@app.get("/gpu-available")
def get_gpt_status():
    return {f"GPU available: {gpu_available()}"}


@app.get("/using-device")
def get_gpt_status():
    return {f"Running on device: {running_on_device()}"}


@app.get("/gpu-details")
def get_gpt_status():
    return gpu_details()

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8090)
