# My_FastAPI/src/main.py
from fastapi import FastAPI, Depends
from web import creature, explorer
from fastapi.security import HTTPBasic, HTTPBasicCredentials

app = FastAPI()

basic = HTTPBasic()

@app.get("/who")
def get_user(creds: HTTPBasicCredentials = Depends(basic)):
    return {"username": creds.username, "password": creds.password}


app.include_router(explorer.router)
app.include_router(creature.router)

@app.get("/")
def top() -> str:
    return "top here"


@app.get("/echo/{thing}")
def echo(thing) -> str:
    return f"echoing {thing}"


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", reload=True, port=9000)
