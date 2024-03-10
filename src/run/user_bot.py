import sys

import telebot
from telebot.types import Message

from src.handlers.commands_handlers import init_commands_handlers
from src.services.message_router import route
from src.services.user_data_store import UserDataStore


def start(token: str) -> None:
    user_data_store = UserDataStore()
    bot = telebot.TeleBot(token)

    init_commands_handlers(bot, user_data_store)

    @bot.message_handler(content_types=['text'])
    def message_handler(message: Message) -> None:
        user = user_data_store.get_or_create(message.chat.id, message.from_user.first_name)
        route(bot, message, user)

    print("Bot is enabled")
    bot.polling()
    print("Bot was stopped")


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python user_bot.py <token>")
        sys.exit(1)
    start(sys.argv[1])
