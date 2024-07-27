from aiogram.fsm.state import StatesGroup, State
from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext


router_state = Router()

'''state for income'''


class IncomeStates(StatesGroup):  # add income
    income = State()


@router_state.message(F.text == 'Add income')
async def add_income(message: Message, state: FSMContext) -> None:
    await state.set_state(IncomeStates.income)
    await message.answer('Enter the amount of income:')


@router_state.message(IncomeStates.income)
async def general_income(message: Message, state: FSMContext) -> None:
    if message.text.isdigit():
        await state.update_data(general_income=message.text)
        data = await state.get_data()
        await message.answer(f'Your income: {data["general_income"]} $')
        await state.clear()
    else:
        await message.answer('Enter only integer or float.')
        await state.clear()

'''sequence of the states for expenses'''


class RentState(StatesGroup):  # for rent
    rent_expense = State()


@router_state.message(F.text == 'Rent')
async def add_rent_expense(message: Message, state: FSMContext) -> None:
    await state.set_state(RentState.rent_expense)
    await message.answer('Enter the amount of the expenses for RENT:')


@router_state.message(RentState.rent_expense)
async def get_rent_expense(message: Message, state: FSMContext) -> None:
    if message.text.isdigit():
        await state.update_data(rent_expense=message.text)
        data = await state.get_data()
        await message.answer(f'Your rent expense: {data["rent_expense"]} $')
        await state.clear()
    else:
        await message.answer('Enter only integer or float.')
        await state.clear()


class FoodState(StatesGroup):  # for Food
    food_expense = State()


@router_state.message(F.text == 'Food')
async def add_food_expense(message: Message, state: FSMContext) -> None:
    await state.set_state(FoodState.food_expense)
    await message.answer('Enter the amount of the expenses for FOOD:')


@router_state.message(FoodState.food_expense)
async def get_food_expense(message: Message, state: FSMContext) -> None:
    if message.text.isdigit():
        await state.update_data(food_expense=message.text)
        data = await state.get_data()
        await message.answer(f'Your food expense: {data['food_expense']}$')
        await state.clear()
    else:
        await message.answer('Enter only integer or float.')
        await state.clear()


class ClothesState(StatesGroup):  # for clothes
    clothes_expense = State()


@router_state.message(F.text == 'Clothes')
async def add_clothes_expense(message: Message, state: FSMContext) -> None:
    await state.set_state(ClothesState.clothes_expense)
    await message.answer('Enter the amount of the expenses for CLOTHES:')


@router_state.message(ClothesState.clothes_expense)
async def get_clothes_expense(message: Message, state: FSMContext) -> None:
    if message.text.isdigit():
        await state.update_data(clothes_expense=message.text)
        data = await state.get_data()
        await message.answer(f'Your clothes expense: {data["clothes_expense"]} $')
        await state.clear()
    else:
        await message.answer('Enter only integer or float.')
        await state.clear()


class GymState(StatesGroup):  # for gym
    gym_expense = State()


@router_state.message(F.text == 'Gym')
async def add_gym_expense(message: Message, state: FSMContext) -> None:
    await state.set_state(GymState.gym_expense)
    await message.answer('Enter the amount of the expenses for GYM:')


@router_state.message(GymState.gym_expense)
async def get_gym_expense(message: Message, state: FSMContext) -> None:
    if message.text.isdigit():
        await state.update_data(gym_expense=message.text)
        data = await state.get_data()
        await message.answer(f'Your gym expense: {data["gym_expense"]} $')
        await state.clear()
    else:
        await message.answer('Enter only integer or float.')
        await state.clear()


class MedicineState(StatesGroup):  # for medicine
    medicine_expense = State()


@router_state.message(F.text == 'Medicine')
async def add_medicine_expense(message: Message, state: FSMContext) -> None:
    await state.set_state(MedicineState.medicine_expense)
    await message.answer('Enter the amount of the expenses for MEDICINES:')


@router_state.message(MedicineState.medicine_expense)
async def get_medicine_state(message: Message, state: FSMContext) -> None:
    if message.text.isdigit():
        await state.update_data(medicine_expense=message.text)
        data = await state.get_data()
        await message.answer(f'Your medicine expense: {data["medicine_expense"]} $')
        await state.clear()
    else:
        await message.answer('Enter only integer or float.')
        await state.clear()


class OtherState(StatesGroup):  # for other
    other_expense = State()


@router_state.message(F.text == "Other")
async def add_other_expense(message: Message, state: FSMContext) -> None:
    await state.set_state(OtherState.other_expense)
    await message.answer('Enter the amount of expenses for OTHER:')


@router_state.message(OtherState.other_expense)
async def get_other_expense(message: Message, state: FSMContext) -> None:
    if message.text.isdigit():
        await state.update_data(other_expense=message.text)
        data = await state.get_data()
        await message.answer(f'Your other expense: {data["other_expense"]} $')
        await state.clear()
    else:
        await message.answer('Enter only integer or float.')
        await state.clear()
