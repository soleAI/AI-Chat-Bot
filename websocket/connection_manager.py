from fastapi import WebSocket

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
