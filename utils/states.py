from aiogram.fsm.state import StatesGroup, State


class IncomeStates(StatesGroup):  # add income
    income = State()


class RentState(StatesGroup):  # for rent
    rent_expense = State()


class FoodState(StatesGroup):  # for Food
    food_expense = State()


class ClothesState(StatesGroup):  # for clothes
    clothes_expense = State()


class GymState(StatesGroup):  # for gym
    gym_expense = State()


class OtherState(StatesGroup):  # for other
    other_expense = State()


class MedicineState(StatesGroup):  # for medicine
    medicine_expense = State()
