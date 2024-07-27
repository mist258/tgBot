from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import ReplyKeyboardMarkup


async def builder_keyboard() -> ReplyKeyboardMarkup:

    categories_kb = ['Rent', 'Food', 'Clothes', 'Gym', 'Medicine', 'Other', 'Go back']
    builder_kb = ReplyKeyboardBuilder()
    [builder_kb.button(text=category) for category in categories_kb]
    return builder_kb.adjust(3).as_markup(resize_keyboard=True, one_time_keyboard=True)
