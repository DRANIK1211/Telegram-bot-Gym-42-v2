# Состояния для разных последовательных действий

from aiogram.fsm.state import StatesGroup, State


class Registration(StatesGroup):
    name = State()
    role = State()
