from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

a2=KeyboardButton('/категория')

kb_client=ReplyKeyboardMarkup(resize_keyboard=True)

kb_client.row(a2)
