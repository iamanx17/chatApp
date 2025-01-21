from gateway.msg import msgGateway

class msgMiddleware:
    def __init__(self):
        self.msg_gateway = msgGateway()

    def create_mesages(self, message_entity):
        response = self.msg_gateway.add_messages(message_entity)
        return response
        

    def fetch_messages(self, user_id):
        response = self.msg_gateway.fetch_all_messages(user_id=user_id)
        return response
        
