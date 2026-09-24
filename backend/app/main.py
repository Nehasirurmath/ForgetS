from fastapi import FastAPI

app=FastAPI(title="ForgetS",description="AI-Powered personal reminder assistant",version="1.0.0")


@app.get("/")
def root():
    return {"app":"ForgetS","message":"Never Forgets little things","status":"running"}

@app.get("/health")
def health():
    return {"status": "healthy"}