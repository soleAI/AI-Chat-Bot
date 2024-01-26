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

class ConnectionManager:

    def __init__(self) -> None:
        self.connections : list[WebSocket] = []

    async def connect(self,websocket:WebSocket) -> None:
        await websocket.accept()
        self.connections.append(websocket)

    def disconnect(self,websocket:WebSocket) -> None:
        self.connections.remove(websocket)
    
    async def send_message(self,message:str,websocket:WebSocket) -> None:
        await websocket.send_text(message)

    


manager = ConnectionManager()


@app.websocket("/ws/{client_id}")
async def websocket_endpoint(websocket:WebSocket,client_id:str):
    await manager.connect(websocket)
    print(client_id)
    try:
        while True:
            data = await websocket.receive_text()
            response = open_ai.get_reponse(data,client_id)
            await manager.send_message(response,websocket)

    except WebSocketDisconnect:
        manager.disconnect(websocket)
        open_ai.remove(client_id)
        print(f"Socket closed for {client_id}")


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