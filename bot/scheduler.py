import asyncio
import logging
from aiogram import Bot
from .utils import get_gas_price

logging.basicConfig(level=logging.INFO)
user_settings = {}

def set_user_interval(user_id: int, seconds: int):
    logging.info(f"Set interval for {user_id}: {seconds} sec")
    user_settings.setdefault(user_id, {})["interval"] = seconds

def set_user_threshold(user_id: int, gwei: int):
    logging.info(f"Set threshold for {user_id}: {gwei} Gwei")
    user_settings.setdefault(user_id, {})["threshold"] = gwei

def enable_alert(user_id: int, status: bool):
    logging.info(f"Alert enabled for {user_id}: {status}")
    user_settings.setdefault(user_id, {})["alert"] = status

def start_scheduler(bot: Bot):
    asyncio.create_task(scheduler_loop(bot))

async def scheduler_loop(bot: Bot):
    logging.info("Scheduler started")
    while True:
        logging.info(f"Current users: {user_settings}")
        for uid, s in user_settings.items():
            interval = s.get("interval", 60)
            last = s.get("last", 0)
            now = asyncio.get_event_loop().time()
            if now - last >= interval:
                gwei = await get_gas_price()
                logging.info(f"Sending gas price to {uid}: {gwei} Gwei")
                await bot.send_message(uid, f"⛽ {gwei} Gwei")
                s["last"] = now
                if s.get("alert") and gwei <= s.get("threshold", 20):
                    logging.info(f"Threshold alert for {uid}: {gwei} Gwei <= {s.get('threshold',20)}")
                    await bot.send_message(uid, f"⚠️ Gas below {s.get('threshold',20)} Gwei!")
        await asyncio.sleep(5)