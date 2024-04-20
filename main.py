from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def top() -> str:
    return "top here"

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", reload=True, port=9000)

