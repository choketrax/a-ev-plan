from fastapi import FastAPI, Form
from twilio_sms import send_sms
from langchain_agent import get_ai_response

app = FastAPI()

@app.post("/webhook/twilio")
async def twilio_webhook(From: str = Form(...), Body: str = Form(...)):
    ai_reply = get_ai_response(Body)
    send_sms(From, ai_reply)
    return "OK"
