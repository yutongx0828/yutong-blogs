from fastapi import FastAPI


app = FastAPI()

@app.get("/")
async def root():
    return "<html><body><h1>Hello, World!</h1></body></html>"