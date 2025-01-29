from fastapi import APIRouter, Depends
from models.user import userRegisterEntity, userLoginEntity
from models.follower import followerEntity
from middleware.user import userMiddleware
import constants

user_router = APIRouter()
user_middleware = userMiddleware()


@user_router.post('/register')
async def user_register(user: userRegisterEntity):
    try:
        user_dict = user.model_dump()
        response = await user_middleware.create_user(user_entity=user_dict)
        return response
    except Exception as e:
        print('Error occured while creating the user', e)
        return constants.ERROR_RESPONSE['error'].format(str(e))


@user_router.post('/login')
async def user_login(user: userLoginEntity):
    try:
        user_json = user.model_dump()
        response = await user_middleware.login_user(user_entity=user_json)
        return response

    except Exception as e:
        print('Error occured while login', e)
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
async def add_followers(follower_entity:followerEntity, user_id: str = Depends(user_middleware.validate_api_key)):
    try:
        data = follower_entity.model_dump()
        follower_id = data.get('follower_id')
        response = await user_middleware.add_followers(user_id=user_id, follower_id=follower_id)
        return response

    except Exception as e:
        print('error occured while adding followers', e)
        return constants.ERROR_RESPONSE['error'].format(str(e))