from aiogram import Router, Bot, F
from aiogram.types import Message
from aiogram.filters import CommandStart

from keyboards import reply_keyboards, builder_keyboard


router = Router()


DESCRIPTION = '''
This bot will help manage your expenses and income.
<b>What can this bot do:</b>
<i>* Adding income and expenses</i> 
<i>* Review of expenses for a certain period of time</i> 
<i>* Delete certain notes</i> 
<i>* Statistic data</i> 
'''


@router.message(CommandStart())  # cmd /start
async def cmd_start(message: Message, bot: Bot) -> None:
    await bot.send_message(message.from_user.id,
                           text=DESCRIPTION,
                           reply_markup=await builder_keyboard.builder_main_menu())


@router.message(F.text == 'Expense')
async def bot_functional(message: Message) -> None:
    await message.answer('Choose category of expense:', reply_markup=reply_keyboards.expense_reply)


@router.message(F.text == 'Income')
async def bot_functional_2(message: Message) -> None:
    await message.answer('Allowed actions for income:', reply_markup=reply_keyboards.income_reply)


@router.message(F.text == 'Back')
async def bot_functional_3(message: Message) -> None:
    await message.answer('Return to main menu:', reply_markup=await builder_keyboard.builder_main_menu())


@router.message(F.text == 'Add expense')
async def bot_functional_4(message: Message) -> None:
    await message.answer('Choose category of expense:', reply_markup=await builder_keyboard.builder_keyboard())


@router.message(F.text == 'Go back')
async def bot_functional_5(message: Message) -> None:
    await message.answer('Menu of Expenses:', reply_markup=reply_keyboards.expense_reply)


@router.message(F.text == 'Delete notes')
async def bot_functional_6(message: Message) -> None:
    await message.answer('Choose option:', reply_markup=await builder_keyboard.builder_for_delete_notes())


@router.message(F.text == 'Statistic')
async def bot_functional_7(message: Message) -> None:
    await message.answer('Choose option:', reply_markup=await builder_keyboard.builder_for_show_notes())
