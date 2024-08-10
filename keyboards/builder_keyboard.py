from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import ReplyKeyboardMarkup


async def builder_main_menu() -> ReplyKeyboardMarkup:  # builder for initial menu

    categories_kb = ['Expense', 'Income', 'Statistic', 'Delete notes']
    builder_kb = ReplyKeyboardBuilder()
    [builder_kb.button(text=category) for category in categories_kb]
    return builder_kb.adjust(2).as_markup(resize_keyboard=True, one_time_keyboard=True)


async def builder_keyboard() -> ReplyKeyboardMarkup:  # builder for expenses menu

    categories_kb = ['Rent', 'Food', 'Clothes', 'Gym', 'Medicine', 'Other', 'Go back']
    builder_kb = ReplyKeyboardBuilder()
    [builder_kb.button(text=category) for category in categories_kb]
    return builder_kb.adjust(3).as_markup(resize_keyboard=True, one_time_keyboard=True)


async def builder_for_delete_notes() -> ReplyKeyboardMarkup:  # builder for deleting notes

    categories_kb = ['Delete for a day', 'Delete for a week', 'Delete for a month', 'Delete for a year', 'Back']
    builder_kb = ReplyKeyboardBuilder()
    [builder_kb.button(text=category) for category in categories_kb]
    return builder_kb.adjust(2).as_markup(resize_keyboard=True, one_time_keyboard=True)


async def builder_for_show_notes() -> ReplyKeyboardMarkup:  # builder for watching notes

    categories_kb = ['Show for a day', 'Show for a week', 'Show for a month', 'Show for a year', 'Back']
    builder_kb = ReplyKeyboardBuilder()
    [builder_kb.button(text=category) for category in categories_kb]
    return builder_kb.adjust(2).as_markup(resize_keyboard=True, one_time_keyboard=True)
