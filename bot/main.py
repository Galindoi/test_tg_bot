from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv
import os

from .handlers import register_handlers
from .scheduler import setup_scheduler
from .database import init_db

def run_bot():
    load_dotenv()
    bot = Bot(token=os.getenv('BOT_TOKEN'))
    dp = Dispatcher(bot)
    init_db()
    register_handlers(dp, bot)
    setup_scheduler(bot)
    executor.start_polling(dp)
