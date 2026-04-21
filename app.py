from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Command(BaseModel):
    text: str


@app.get("/")
def home():
    return {"message": "FRIDAY backend running"}


@app.post("/process")
def process_command(command: Command):
    user_input = command.text.lower()

    if "hello" in user_input:
        return {"response": "Hello! How can I assist you?"}
    elif "time" in user_input:
        from datetime import datetime

        return {"response": str(datetime.now())}
    else:
        return {"response": "I didn't understand that."}
