from aiogram import types, Dispatcher
from create_bot import dp, bot
from Keyboards import kb_client, bb_client
from anek import *
import random
@dp.message_handler(commands=['start','help']) #Явно указываем в декораторе, на какую команду реагируем.
async def send_welcome(message: types.Message):
    await bot.send_message(message.from_user.id,'Привет, я анекдотный шутник, подниму настроение', reply_markup=kb_client)

@dp.message_handler(commands=['категория'])  # Явно указываем в декораторе, на какую команду реагируем.
async def send_categhory(message: types.Message):
    await bot.send_message(message.from_user.id, 'Выбери категорию',reply_markup=bb_client)

@dp.message_handler(commands=['разное'])  # Явно указываем в декораторе, на какую команду реагируем.
async def send_1(message: types.Message):
    await bot.send_message(message.from_user.id, random.choice(data["jokes"]))

@dp.message_handler(commands=['грустные'])  # Явно указываем в декораторе, на какую команду реагируем.
async def send_2(message: types.Message):
    await bot.send_message(message.from_user.id, random.choice(data["joke"]))

@dp.message_handler(commands=['не_детские'])  # Явно указываем в декораторе, на какую команду реагируем.
async def send_3(message: types.Message):
    await bot.send_message(message.from_user.id,random.choice(data["jok"]))

def regist_heand_client(dp:Dispatcher):
    dp.register_message_handler(send_welcome,commands=['start','help'])
    dp.register_message_handler(send_categhory,commands=['категория'])
    dp.register_message_handler(send_1,commands=['разное😂'])
    dp.register_message_handler(send_2,commands=['грустные😢'])
    dp.register_message_handler(send_3, commands=['не_детские🔞'])
