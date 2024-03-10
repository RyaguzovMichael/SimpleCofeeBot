from src.models.user_data import UserData


class UserDataStore:

    def __init__(self):
        self.store = {}

    def get_or_create(self, user_id: int, user_name: str) -> UserData:
        user_data = self.store.get(user_id)
        if user_data is None:
            user_data = UserData(user_id, user_name)
            self.store[user_id] = user_data
        return user_data

    def renew_user(self, user_id: int, user_name: str) -> UserData:
        user_data = UserData(user_id, user_name)
        self.store[user_id] = user_data
        return user_data
