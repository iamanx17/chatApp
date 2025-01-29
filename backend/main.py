from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers.user import user_router
from routers.chat import chat_router
import constants

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=constants.ALLOWED_HOSTS,
    allow_credentials=['*'],
    allow_methods=['*'],
    allow_headers=['*']
)


app.include_router(user_router, prefix='/user', tags=['Users API'])
app.include_router(chat_router, prefix='/ws', tags=['chat webscoket'])