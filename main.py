import asyncio
from aiogram import Bot, Dispatcher
from config.settings import BOT_TOKEN
from bot import setup_bot

async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()
    setup_bot(dp, bot)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())