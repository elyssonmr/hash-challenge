class UserDB:
    def __init__(self, db_client):
        self.users_collection = db_client['users']

    def get_user_data(self, user_id):
        return self.users_collection.find_one({'id': user_id})
