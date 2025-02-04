from fastapi import APIRouter,WebSocket, WebSocketDisconnect
from middleware.connection import connManager
from bson.objectid import ObjectId


chat_router = APIRouter()
conn = connManager()


@chat_router.websocket('/chat/sender/{sender_id}/reciever/{reciever_id}')
async def recieve_messages(websocket:WebSocket, sender_id:str, reciever_id:str):
    await conn.connect(websocket=websocket,user_id=sender_id)
    try:
        while True:
            message = await websocket.receive_text()
            if reciever_id:
                await conn.send_message(message=message, user_id=reciever_id)
                data = {
                    'user_id': ObjectId(sender_id),
                    'reciever_id': ObjectId(reciever_id),
                    'message': message
                }
                conn.save_message(data)            
    
    except WebSocketDisconnect as e:
        print('websocket disconnected', e)
        conn.disconnect(user_id=sender_id)