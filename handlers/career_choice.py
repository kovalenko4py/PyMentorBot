from aiogram import Router, types, F
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext

from states.career_state import CareerChoice, available_grades, available_jobs
from keyboards.prof_keyboards import make_row_keyboard


# TODO доработать эту функцию
router = Router()


@router.message(Command('prof'))
async def command_prof(message: types.Message, state: FSMContext):
    # отладка
    print(f'Отладка: метод command_prof | {message.text} | {type(message.text)}')
    await message.answer('Выберите профессию', reply_markup=make_row_keyboard(available_jobs))
    await state.set_state(CareerChoice.job)


@router.message(CareerChoice.job, F.text.in_(available_jobs))
# @router.message(CareerChoice.job)
async def prof_chosen(message: types.Message, state: FSMContext):
    # отладка
    print(f'Отладка: метод prof_chosen | {message.text} | {type(message.text)}')
    await state.update_data(profession=message.text)
    await message.answer('Выберите уровень', reply_markup=make_row_keyboard(available_grades))
    await state.set_state(CareerChoice.grade)


@router.message(CareerChoice.job)
async def prof_incorrect(message: types.Message):
    # отладка
    print(f'Отладка: метод prof_incorrect | {message.text} | {type(message.text)}')
    await message.answer('Еще раз выберите профессию', reply_markup=make_row_keyboard(available_jobs))


# @router.message(CareerChoice.grade)
@router.message(CareerChoice.grade, F.text.in_(available_grades))
async def grade_chosen(message: types.Message, state: FSMContext):
    # отладка
    print(f'Отладка: метод grade_chosen | {message.text} | {type(message.text)}')
    user_data = await state.get_data()
    await message.answer(f"Профессия: {user_data.get('profession')}, уровень: {message.text}",
                         reply_markup=types.ReplyKeyboardRemove()
                         )
    await state.clear()


@router.message(CareerChoice.grade)
async def grade_incorrect(message: types.Message):
    # отладка
    print(f'Отладка: метод grade_incorrect | {message.text} | {type(message.text)}')
    await message.answer('Еще раз выберите уровень', reply_markup=make_row_keyboard(available_grades))
