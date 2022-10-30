from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

a3=KeyboardButton('/разное😂')
a4=KeyboardButton('/грустные😢')
a5=KeyboardButton('/не_детские🔞')
bb_client=ReplyKeyboardMarkup(resize_keyboard=True)
bb_client.row(a3,a4,a5)