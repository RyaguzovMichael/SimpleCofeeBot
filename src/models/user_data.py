from src.models.user_states import UserStates


class UserData:
    def __init__(self, user_id: id, user_name: str):
        self.user_name = user_name
        self.user_id = user_id
        self.user_state = UserStates.START
