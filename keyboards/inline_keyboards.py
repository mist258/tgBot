from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

main_inline_for_expense = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Show notes', callback_data='showing'),
        ],
        [
            InlineKeyboardButton(text='Add expense', callback_data='add_expense'),
        ],
        [
            InlineKeyboardButton(text='Delete notes', callback_data='deleting')
        ],
        [
            InlineKeyboardButton(text='Back', callback_data='returning')
        ]
    ]
)

main_inline_for_income = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Show notes', callback_data='showing'),
        ],
        [
            InlineKeyboardButton(text='Add income', callback_data='add_income'),
        ],
        [
            InlineKeyboardButton(text='Delete notes', callback_data='deleting')
        ],
        [
            InlineKeyboardButton(text='Back', callback_data='returning')
        ]
    ]
)
