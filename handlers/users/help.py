from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("Buyruqlar:\n ",
            "/start - Botni ishga tushirish\n",
            "/help - Yordam\n"
            "/qrneed boshlash\n")
    
    await message.answer("\n".join(text))