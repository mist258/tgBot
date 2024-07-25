from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext


class FoodExpenseStates(StatesGroup):  # add food expense
    food_expense = State()


class ClothesExpenseStates(StatesGroup):  # add clothes expense
    clothes_expense = State()


class MedicineExpenseStates(StatesGroup):  # add medicine expense
    medicine_expense = State()


class RentExpenseStates(StatesGroup):  # add rent expense
    rent_expense = State()


class EntertainmentExpenseStates(StatesGroup):  # add entertainment expense
    entertainment_expense = State()


class OtherExpenseStates(StatesGroup):  # add other expense
    other_expense = State()


class IncomeStates(StatesGroup):  # add income
    income = State()

