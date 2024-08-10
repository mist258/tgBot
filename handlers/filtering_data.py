from aiogram import Router, F
from aiogram.types import Message

from utils import assist_functions

router_filtering = Router()


@router_filtering.message(F.text == 'Show for a day')
async def show_day_filtering(message: Message):

    read_data = assist_functions.read_data('data.json')
    for k, v in read_data.items():
        for index, elem_data in enumerate(v):
            for key, val in elem_data.items():
                await message.answer(f' Number: {index}\nCategories: {key},\ndata: {val}')
