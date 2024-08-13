from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from utils import assist_functions, states


router_filtering = Router()


@router_filtering.message(F.text == 'Show for a day')
async def show_day_filtering(message: Message, state: FSMContext, ) -> None:
    await state.set_state(states.NotesDayState.notes_day)
    await message.answer('Enter a date in the format YYYY-MM-DD:')


@router_filtering.message(states.NotesDayState.notes_day)
async def get_notes_by_day(message: Message, state: FSMContext) -> None:

    await state.update_data(note_for_day=message.text)
    read_data = assist_functions.read_data('data.json')
    for primary_key, value in read_data.items():
        for elem_data in value:
            for key, val in elem_data.items():
                if key == 'data_time':
                    continue
                else:
                    await message.answer(f' {key}: {val}')






