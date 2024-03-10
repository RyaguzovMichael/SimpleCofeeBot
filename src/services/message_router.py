from telebot import types, TeleBot

from src.handlers.greetings_handler import greetings_handler
from src.models.user_data import UserData
from src.models.user_states import UserStates


def route(bot: TeleBot, message: types.Message, user: UserData):
    match user.user_state:
        case UserStates.START:
            greetings_handler(bot, message, user)
        case _:
            pass
