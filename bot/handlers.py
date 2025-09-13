    # bot/handlers.py
from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters import Command
from .scheduler import set_user_interval, set_user_threshold, enable_alert

def register_handlers(dp):
    @dp.message(Command("start"))
    async def start_cmd(message: types.Message):
        kb = InlineKeyboardBuilder()
        kb.button(text="30 sec", callback_data="interval_30")
        kb.button(text="1 min", callback_data="interval_60")
        kb.button(text="10 min", callback_data="interval_600")
        kb.adjust(3)
        await message.answer("⏱ Choose gas check interval:", reply_markup=kb.as_markup())

    @dp.callback_query(lambda c: c.data.startswith("interval_"))
    async def interval_cb(callback: types.CallbackQuery):
        seconds = int(callback.data.split("_")[1])
        set_user_interval(callback.from_user.id, seconds)
        await callback.answer()
        await callback.message.answer(f"Interval set to {seconds} sec")

    @dp.message(Command("threshold"))
    async def threshold_cmd(message: types.Message):
        await message.answer("Send desired gas threshold in Gwei")

    @dp.message(lambda m: m.text.isdigit())
    async def set_threshold(message: types.Message):
        set_user_threshold(message.from_user.id, int(message.text))
        await message.answer(f"Threshold set to {message.text} Gwei")

    @dp.message(Command("alert"))
    async def alert_cmd(message: types.Message):
        enable_alert(message.from_user.id, True)
        await message.answer("Gas alert enabled")

    @dp.message(Command("gas"))
    async def gas_cmd(message: types.Message):
        from .utils import get_gas_price
        gwei = await get_gas_price()
        await message.answer(f"⛽ {gwei} Gwei")