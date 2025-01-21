from fastapi import FastAPI
from routers.user import user_router
from routers.chat import chat_router

app = FastAPI()


app.include_router(user_router, prefix='/user', tags=['User'])
app.include_router(chat_router, prefix='/ws', tags=['Chat'])

@app.get('/')
def welcome_chat_app():
    return {'message': "Welcome to the chatApp"}