from fastapi import FastAPI,WebSocket,WebSocketDisconnect
import os
from keys.key import open_ai_key
import warnings
from pydantic import BaseModel
from services.openai import OpenAIService


class BotMessage(BaseModel):
    message : str 
    id : int | None = None


warnings.filterwarnings('ignore')

os.environ['OPENAI_API_KEY'] = open_ai_key
app = FastAPI()

open_ai = OpenAIService(temp=0.6)


@app.websocket("/ws")
async def websocket_endpoint(websocket:WebSocket):
    await websocket.accept()

    try:
        while True:
            data = await websocket.receive_text()
            response = open_ai.get_reponse(data)
            await websocket.send_text(f"AI : {response}")
    except WebSocketDisconnect:
        print("Socket closed")


@app.post("/bot")
async def root(bot_message : BotMessage):

    response = open_ai.get_reponse(bot_message.message)
    ctx = {
        'human':bot_message.message,
        'ai':response
    }
    return ctx

if __name__=='__main__':
    app.run()