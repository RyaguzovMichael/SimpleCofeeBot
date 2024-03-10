from telebot import TeleBot
from telebot.types import Message

from src.models.user_data import UserData
from src.services.message_router import route
from src.services.user_data_store import UserDataStore


def init_commands_handlers(bot: TeleBot, user_data_store: UserDataStore) -> None:
    def get_user(message: Message) -> UserData:
        return user_data_store.get_or_create(message.chat.id, message.from_user.first_name)

    def renew_user(message: Message) -> UserData:
        return user_data_store.renew_user(message.chat.id, message.from_user.first_name)

    @bot.message_handler(commands=['help'])
    def show_help(message: Message) -> None:
        user = get_user(message)
        response = ("Доступные команды:\n"
                    "/help - информация о всех командах\n"
                    "/start - начало взаимодействия с ботом\n"
                    "/renew - удалить все данные о себе (удалит также и заказы)")
        bot.send_message(user.user_id, response)

    @bot.message_handler(commands=['start'])
    def send_welcome(message: Message) -> None:
        user = get_user(message)
        route(bot, message, user)

    @bot.message_handler(commands=['renew'])
    def renew_user(message: Message) -> None:
        user = renew_user(message)
        response = f"{user.user_name}, вы успешно зачистили данные о себе!"
        bot.send_message(user.user_id, response)
