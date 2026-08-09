from aiogram.fsm.state import default_state, State, StatesGroup


available_jobs = [
    'Программист',
    'Менеджер',
    'Дизайнер',
    'Маркетолог',
]

available_grades = [
    'Junior',
    'Middle',
    'Senior',
]


class CareerChoice(StatesGroup):
    job = State()
    grade = State()
