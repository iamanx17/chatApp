from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers.user import user_router
from routers.chat import chat_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=['*'],
    allow_methods=['*'],
    allow_headers=['*']
)


app.include_router(user_router, prefix='/user', tags=['User'])
app.include_router(chat_router, prefix='/ws', tags=['Chat'])


@app.get('/')
def welcome_chat_app():
    return {'message': "Welcome to the chatApp"}
