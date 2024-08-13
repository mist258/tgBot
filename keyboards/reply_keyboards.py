from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


expense_reply = ReplyKeyboardMarkup(  # kb for expenses
    keyboard=[
        [
            KeyboardButton(text='Add expense'),
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

income_reply = ReplyKeyboardMarkup(  # kb for incomes
    keyboard=[
        [
            KeyboardButton(text='Add income'),
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

back_reply = ReplyKeyboardMarkup(  # kb for return
    keyboard=[
        [
            KeyboardButton(text='Go back'),
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
    selective=True
)
