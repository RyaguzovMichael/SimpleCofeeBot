from telebot import TeleBot
from telebot.types import Message, ReplyKeyboardMarkup
from src.models.user_data import UserData


def greetings_handler(bot: TeleBot, message: Message, user: UserData):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add('Напитки', 'Еда')
    bot.send_message(user.user_id, "Добро пожаловать в мой бот! Что вы хотите заказать,", reply_markup=keyboard)
