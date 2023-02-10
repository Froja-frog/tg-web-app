import asyncio

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.enums.parse_mode import ParseMode
from dotenv import load_dotenv, find_dotenv
from loguru import logger

from os import environ

from tg_bot.handlers import questions


async def main():
    load_dotenv(find_dotenv())
    logger.add("bot.log", format="{time} {level} {message}", level="DEBUG")
    logger.success("Bot has started")

    bot = Bot(environ["BOT_TOKEN"], parse_mode=ParseMode.MARKDOWN_V2)
    dp = Dispatcher(storage=MemoryStorage())

    dp.include_router(questions.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
