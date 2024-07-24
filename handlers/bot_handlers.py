from aiogram import Router, F, Bot
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart
from keyboards import reply_keyboards, inline_keyboards


router = Router()

DESCRIPTION = '''
This bot will help manage your expenses and income.
<b>What can this bot do:</b>
<i>* Adding income and expenses</i> 
<i>* Review of expenses for a certain period of time</i> 
<i>* Delete certain notes</i> 
<i>* Statistic data</i> 
'''


@router.message(CommandStart())
async def cmd_start(message: Message, bot: Bot) -> None:

    await bot.send_message(message.from_user.id,
                           text=DESCRIPTION,
                           reply_markup=reply_keyboards.main_reply)


@router.message(F.text.lower() == '/python')
async def get_id(message: Message) -> None:
    await message.reply(f'ID: {message.from_user.id}\nName {message.from_user.last_name}\n First name{message.from_user.first_name}')


@router.message()
async def bot_functional(message: Message) -> None:
    msg = message.text.lower()

    if msg == 'expense':
        await message.answer('Main categories of expenses:', reply_markup=reply_keyboards.expense_reply)
    if (
            msg == 'for food'
            or msg == 'for medicine'
            or msg == 'for other'
            or msg == 'for clothes'
            or msg == 'for entertainment'
            or msg == 'for rent'
    ):
        await message.answer('Allowed actions for category:', reply_markup=inline_keyboards.main_inline)

    if msg == 'income':
        await message.answer('Allowed actions for income:', reply_markup=inline_keyboards.main_inline)




