from aiogram import Router, F
from aiogram.types import CallbackQuery
from keyboards import reply_keyboards

router_cb = Router()


@router_cb.callback_query(F.data == 'showing')  # general cb
async def show_notes(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer('Hi')


@router_cb.callback_query(F.data == 'add_expense')
async def add_expense(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer('Hi')


@router_cb.callback_query(F.data == 'add_income')
async def add_income(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer('Hi')


@router_cb.callback_query(F.data == 'deleting')  # general cb
async def delete_notes(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer('Hi')


@router_cb.callback_query(F.data == 'returning')  # cb for expense
async def back(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer('Main categories of expenses:', reply_markup=reply_keyboards.expense_reply)


@router_cb.callback_query(F.data == 'return')  # cb for income
async def return_to_income(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer('Return to main menu:', reply_markup=reply_keyboards.main_reply)
