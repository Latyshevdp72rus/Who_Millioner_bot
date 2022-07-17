import asyncio
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram import Bot, Dispatcher, executor
from config import BOT_TOKEN, admin_id
import json


loop = asyncio.get_event_loop()
bot = Bot(BOT_TOKEN, parse_mode="HTML")
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage, loop=loop)

# Загрузка ответов
with open('assets/quest.json', 'r', encoding="UTF-8") as jsLoader:
    question = json.load(jsLoader)

# Защита анти-флуд
async def anti_flood(*args, **kwargs):
    m = args[0]
    await m.answer("Не флудите!")

# Функция уведомления запуска что бот включен
async def send_to_enter(dp):
    await bot.send_message(chat_id=admin_id, text=f"Бот Включен!")

# Функция уведомления запуска что бот отключен
async def send_to_exit(dp):
    await bot.send_message(chat_id=admin_id, text=f"Бот Выключен!")


if __name__ == "__main__":
    from handlers.commands import dp
    executor.start_polling(dp, on_startup= send_to_enter,on_shutdown=send_to_exit, skip_updates=True)
    import handlers