from aiogram import Router, F
from aiogram.types import CallbackQuery

router_cb = Router()


@router_cb.callback_query(F.data == 'showing')
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


@router_cb.callback_query(F.data == 'deleting')
async def delete_notes(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer('Hi')


@router_cb.callback_query(F.data == 'returning')
async def back(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer('Hi')

