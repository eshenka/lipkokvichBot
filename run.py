import aiogram
import asyncio
import logging

from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from config import TOKEN
from app.handlers import router

bot = Bot(TOKEN)
dispatcher = Dispatcher()


async def main():
    dispatcher.include_router(router)

    await dispatcher.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)

    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('cancelled')
