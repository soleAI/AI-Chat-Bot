from fastapi import WebSocket,WebSocketDisconnect
from websocket import manager
from app import app

from services.openai import OpenAIService
open_ai = OpenAIService(temp=0.6)

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