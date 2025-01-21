from fastapi import WebSocket
from gateway.msg import msgGateway


class connManager:
    def __init__(self):
        self.active_connection = {}
        self.msg_gateway = msgGateway()

    async def connect(self, websocket: WebSocket, user_id: str):
        await websocket.accept()
        self.active_connection[user_id] = websocket

    def disconnect(self, user_id: str):
        if user_id in self.active_connection:
            del self.active_connection[user_id]

    async def send_message(self, message: str, user_id: str):
        if user_id in self.active_connection:
            websocket = self.active_connection[user_id]
            await websocket.send_text(message)
    
    def fetch_websocket(self, user_id):
        return self.active_connection[user_id]

    
    def save_message(self, msg_entity):
        self.msg_gateway.add_messages(msg_entity=msg_entity)
