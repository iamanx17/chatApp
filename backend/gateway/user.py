from models.user import userModel
from models.follower import followerModel
from bson.objectid import ObjectId
import uuid


class userGateway:
    async def register_user(self, user_entity):
        try:
            email = user_entity.get('email')
            user = await self.if_user_exist(unique_id=email)
            if user:
                return {'error': 'Email-id already exists!'}

            user_entity['api_key'] = str(uuid.uuid4())
            await userModel.insert_one(user_entity)
            return {'error': 'Registeration successful!!'}

        except Exception as e:
            print('error occured while registation', e)
            return {'error': str(e)}

    async def if_user_exist(self, unique_id):
        try:
            user = await userModel.find_one({'email': unique_id})
            if user:
                return user

            if not ObjectId.is_valid(unique_id):
                return {'error': f'ObjectId is not valid {unique_id}'}
            
            user = await userModel.find_one({'_id': ObjectId(unique_id)})
            if user:
                return user

        except Exception as e:
            print("error occured while checking user", e)

    async def validate_api_key(self, api_key):
        try:
            user = await userModel.find_one({'api_key': api_key})
            if not user:
                return None
            return str(user.get('_id'))

        except Exception as e:
            print('error occurred while fetching api key', e)

    async def login_user(self, user_entity):
        try:
            email = user_entity.get('email')
            password = user_entity.get('password')

            user = await self.if_user_exist(unique_id=email)
            if not user:
                return {'error': 'User does not exists!!'}

            if user.get('password') and user.get('password') != password:
                return {'error': 'Password not matched!!'}

            api_key = user.get('api_key', None)
            if not api_key:
                return {'error': 'API key not found, ask developer for further assistance'}

            return {
                'message': "Login successful",
                'api_key': api_key
            }

        except Exception as e:
            import traceback
            print(traceback.print_exc())
            print('error occurred while login', e)

    async def fetch_all_followers(self, user_id):
        try:
            user = await self.if_user_exist(user_id)
            if not user:
                return {'error': 'user does not exist'}

            follower_cursor = followerModel.find({'user_id': ObjectId(user_id)})
            followers = await follower_cursor.to_list()

            return followers

        except Exception as e:
            print('error occured while fetching followers', e)

    async def add_follower(self, user_id, follower_id):
        try:
            if not ObjectId.is_valid(user_id) or not ObjectId.is_valid(follower_id):
                return {'error': 'ObjectId is not valid'}

            existing_follower = await followerModel.find_one({
                'user_id': ObjectId(user_id),
                'follower_id': ObjectId(follower_id)
            })

            if existing_follower:
                return {'error': "User is already added as follower"}

            await followerModel.insert_one({'user_id': ObjectId(user_id), "follower_id": ObjectId(follower_id)})

            return {'message': 'Follower added successfully'}
        except Exception as e:
            print('error occurred while adding follower', e)
