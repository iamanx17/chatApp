from fastapi import APIRouter, Depends
from models import UserLoginEntity, UserRegisterEntity
from middleware.user import userMiddleware
import constants

user_router = APIRouter()
user_middleware = userMiddleware()


@user_router.post('/register')
async def user_register(user: UserRegisterEntity):
    try:
        user_dict = user.model_dump()
        response = await user_middleware.create_user(user_entity=user_dict)
        return response
    except Exception as e:
        print('Error occured while creating the user', e)
        return constants.ERROR_RESPONSE['error'].format(str(e))


@user_router.post('/login')
async def user_login(user: UserLoginEntity):
    try:
        user_json = user.model_dump()
        response = await user_middleware.login_user(user_entity=user_json)
        return response

    except Exception as e:
        print('Error occured while login', e)
        return constants.ERROR_RESPONSE['error'].format(str(e))

@user_router.get('/getuser/{user_id}')
async def fetch_user(user_id:str):
    try:
        response = await user_middleware.fetch_user(user_id=user_id)
        return response
    except Exception as e:
        return constants.ERROR_RESPONSE['error'].format(str(e))


@user_router.get('/getfollowers')
async def fetch_followers(user_id: str = Depends(user_middleware.validate_api_key)):
    try:
        response = await user_middleware.fetch_followers(user_id=user_id)
        return response

    except Exception as e:
        print('Error occured while fetching followers', e)
        return constants.ERROR_RESPONSE['error'].format(str(e))

@user_router.post('/addfollowers')
async def add_followers(follower_id:str, user_id: str = Depends(user_middleware.validate_api_key)):
    try:
        response = await user_middleware.add_followers(user_id=user_id, follower_id=follower_id)
        return response

    except Exception as e:
        print('error occured while adding followers', e)
        return constants.ERROR_RESPONSE['error'].format(str(e))