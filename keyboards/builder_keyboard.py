from aiogram.utils.keyboard import ReplyKeyboardBuilder, KeyboardButton
from aiogram.types import ReplyKeyboardMarkup


async def builder_keyboard() -> ReplyKeyboardMarkup:

    categories_kb = ['Rent', 'Food', 'Clothes', 'Gym', 'Medicine', 'Other', 'Go back']
    builder_kb = ReplyKeyboardBuilder()
    for category in categories_kb:
        builder_kb.add(KeyboardButton(text=category))
    return builder_kb.adjust(3).as_markup()
