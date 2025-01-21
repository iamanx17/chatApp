from models.msg import msgModel
from bson.objectid import ObjectId


class msgGateway:

    def fetch_all_messages(self, user_id):
        try:
            messages = msgModel.find({'user_id': ObjectId(user_id)})
            return messages
        except Exception as e:
            print('error occured while fetching messages', e)

    def add_messages(self, msg_entity):
        try:
            msg = msgModel.insert_one(msg_entity)
        except Exception as e:
            print('error occured while adding messages', e)
