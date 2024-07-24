from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

main_inline = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Show notes', callback_data='showing'),
        ],
        [
            InlineKeyboardButton(text='Add expense', callback_data='adding'),
        ],
        [
            InlineKeyboardButton(text='Delete notes', callback_data='deleting')
        ],
        [
            InlineKeyboardButton(text='Back', callback_data='returning')
        ]
    ]
)
