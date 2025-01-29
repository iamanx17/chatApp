from fastapi import APIRouter,WebSocket, WebSocketDisconnect
from middleware.connection import connManager


chat_router = APIRouter()
conn = connManager()


@chat_router.websocket('/chat/{sender_id}')
async def recieve_messages(websocket:WebSocket, sender_id:str):
    await conn.connect(websocket=websocket,user_id=sender_id)
    try:
        while True:
            data = await websocket.receive_json()
            reciever_id = data.get('receiver_id')
            message = data.get('message')
            if reciever_id:
                await conn.send_message(message=message, user_id=reciever_id)
                data['sender_id'] = sender_id
                conn.save_message(data)            
    
    except WebSocketDisconnect:
        print('websocket disconnected')
        conn.disconnect(user_id=sender_id)