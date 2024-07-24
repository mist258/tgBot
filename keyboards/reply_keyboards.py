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
            KeyboardButton(text='for Rent'),
            KeyboardButton(text='for Food'),
            KeyboardButton(text='for Clothes'),
        ],
        [
            KeyboardButton(text='for Entertainment'),
            KeyboardButton(text='for Medicine'),
            KeyboardButton(text='for Other'),
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
