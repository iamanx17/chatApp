from gateway.user import userGateway
from fastapi import Header, HTTPException, status


class userMiddleware:
    def __init__(self):
        self.user_gateway = userGateway()

    async def create_user(self, user_entity):
        try:
            response = await self.user_gateway.register_user(user_entity=user_entity)
            return response

        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=str(e)
            )

    async def login_user(self, user_entity):
        try:
            response = await self.user_gateway.login_user(user_entity=user_entity)
            return response

        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=str(e)
            )

    async def fetch_followers(self, user_id):
        try:
            response = await self.user_gateway.fetch_all_followers(user_id=user_id)

            if isinstance(response, dict) and response.get('error', None):
                return response

            if not response:
                return {
                    'message': "No followers Found",
                    'length': 0,
                    'data': []
                }
            total_followers = [str(idx.get('follower_id')) for idx in response]
            return {
                'message': f"Total followers founds are: {len(total_followers)}",
                'length': len(total_followers),
                'data': total_followers
            }

        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=str(e)
            )

    async def add_followers(self, user_id, follower_id):
        try:
            response = await self.user_gateway.add_follower(user_id=user_id, follower_id=follower_id)
            return response
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=str(e)
            )

    async def validate_api_key(self, Authorization: str = Header()):
        try:
            user_id = await userGateway().validate_api_key(api_key=Authorization)
            if not user_id:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail='Invalid API Key'
                )
            return user_id

        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=str(e)
            )
