from fastapi import FastAPI

from web import explorer

app = FastAPI()
app.include_router(explorer.router)

@app.get("/")
def top() -> str:
    return "top here"


@app.get("/echo/{thing}")
def echo(thing) -> str:
    return f"echoing {thing}"


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main_ex:app", reload=True, port=9000)
