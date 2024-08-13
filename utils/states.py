from aiogram.fsm.state import StatesGroup, State


class IncomeStates(StatesGroup):  # add income
    income = State()


class RentState(StatesGroup):  # expenses for rent
    rent_expense = State()


class FoodState(StatesGroup):  # expenses for Food
    food_expense = State()


class ClothesState(StatesGroup):  # expenses for clothes
    clothes_expense = State()


class GymState(StatesGroup):  # expenses for gym
    gym_expense = State()


class OtherState(StatesGroup):  # expenses for other
    other_expense = State()


class MedicineState(StatesGroup):  # expenses for medicine
    medicine_expense = State()


class NotesDayState(StatesGroup):  # state for filtering notes by day
    notes_day = State()
