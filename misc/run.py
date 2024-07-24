import os
import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from dotenv import load_dotenv, find_dotenv

from handlers.bot_handlers import router
from callbacks.bot_callback import router_cb


load_dotenv(find_dotenv())

logging.basicConfig(level=logging.INFO)

bot = Bot(token=os.getenv("TOKEN"), default=DefaultBotProperties(parse_mode='HTML'))

dp = Dispatcher()


async def main():
    dp.include_router(router)
    dp.include_router(router_cb)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, skip_updates=True)


if __name__ == "__main__":
    asyncio.run(main())
