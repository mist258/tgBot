import os
import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from dotenv import load_dotenv, find_dotenv

from handlers.bot_handlers import router
from handlers.bot_state_handlers import router_state

load_dotenv(find_dotenv())  # .env

logging.basicConfig(level=logging.INFO)  # show logs

bot = Bot(token=os.getenv("TOKEN"), default=DefaultBotProperties(parse_mode='HTML'))

dp = Dispatcher()


async def main():
    dp.include_router(router_state)  # router for bot_state_handlers.py
    dp.include_router(router)  # router for bot_handlers.py
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, skip_updates=True)


if __name__ == "__main__":
    asyncio.run(main())
