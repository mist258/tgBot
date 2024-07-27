from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_reply = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Income'),
            KeyboardButton(text='Expense')
        ]
    ],
    resize_keyboard=True,
    input_field_placeholder='Choose any action from menu',
    one_time_keyboard=True,
    selective=True
)

expense_reply = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Add expense'),
            KeyboardButton(text='Show notes'),
            KeyboardButton(text='Delete notes'),
        ],
        [
            KeyboardButton(text='Back'),
        ]
    ],
    resize_keyboard=True,
    input_field_placeholder='Choose any action from menu',
    one_time_keyboard=True,
    selective=True
)

income_reply = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Add income'),
            KeyboardButton(text='Show notes'),
            KeyboardButton(text='Delete notes'),
        ],
        [
            KeyboardButton(text='Back'),
        ]
    ],
    resize_keyboard=True,
    input_field_placeholder='Choose any action from menu',
    one_time_keyboard=True,
    selective=True
)

back_reply = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Go back'),
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
    selective=True
)
