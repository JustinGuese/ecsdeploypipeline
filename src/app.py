from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.post("/")
async def root(text: str):
    new = ""
    for i in range(len(text)):
        if i % 2 == 0:
            new += text[i].upper()
        else:
            new += text[i].lower()
    return new

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)