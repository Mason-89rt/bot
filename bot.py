from aiogram import executor
from create_bot import dp
from Heand import client,admin,other
client.regist_heand_client(dp)
if __name__ == '__main__':
    executor.start_polling(dp,skip_updates=True)
