from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

reklama_qabul=InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton("Xa",callback_data="yes"),
            InlineKeyboardButton(text="Bekor qilish", callback_data="no")
        ]
    ]
)