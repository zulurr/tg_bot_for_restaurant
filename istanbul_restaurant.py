import asyncio
from aiogram import Bot, Dispatcher
import logging
from handlers.messages import router
from key import key

API_TOKEN = key
bot = Bot(token=API_TOKEN)
dp = Dispatcher()


async def main():
    dp.include_routers(router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())