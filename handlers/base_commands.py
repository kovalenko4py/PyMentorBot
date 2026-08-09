import sys
import logging

from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state
from aiogram.filters import Command, StateFilter
from aiogram.types import FSInputFile, CallbackQuery

from keyboards.inline_keyboard import inline_keyboard_start
from keyboards.keyboards import kb_base_command
from services.image import fox, ai, duc


router = Router()


"""TODO сделать отдельную папку и сконфигурировать лог"""
logging.basicConfig(
    level=logging.DEBUG,
    format='[{asctime}] #{levelname:8} {filename}:' '{lineno} - {name} - {message}',
    style='{'
)
logger = logging.getLogger(__name__)
stdout_handler = logging.StreamHandler(sys.stdout)
logger.addHandler(stdout_handler)


logger.debug(f'Логер работает в модуле {logger.name}!')

# /start


@router.message(Command(commands=['start', 'START']))
@router.message((F.text == 'Закончить!!'))
@router.message((F.text == 'End !!'))
@router.message((F.text.lower().in_(['старт', 'начало',
                'начало работы', 'start', 'отмена', 'не хочу'])))
async def command_start(message: types.Message):
    """Метод. На вход принимает команды: start, START; слова: 'старт', 'начало', 'начало работы', 'Закончить!!','End !!' и др. Возвращает информацию о боте и его функциях, а также базовые команды в виде кнопок."""
    # отладка
    print(f'Отладка: метод command_start |')
    await message.answer(f'Привет, {message.chat.first_name}!\n Узнать обо мне подробней - info\n Или переходи к общению с ИИ', reply_markup=inline_keyboard_start)
    await message.delete()


@router.callback_query((F.data == 'undo'), ~StateFilter(default_state))
async def callback_undo_clear_state(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer(f'Привет, {callback.message.chat.first_name}!\n Узнать обо мне подробней - info\n Или переходи к общению с ИИ', reply_markup=inline_keyboard_start)
    await state.clear()


@router.callback_query((F.data == 'undo'))
async def callback_undo(callback: CallbackQuery):
    await callback.message.answer(f'Привет, {callback.message.chat.first_name}!\n Узнать обо мне подробней - info\n Или переходи к общению с ИИ', reply_markup=inline_keyboard_start)


# /ID
@router.message(Command(commands=['ID', 'id', 'user_id']))
async def command_start(message: types.Message):
    """Метод. На вход принимает команды: ID, id инфо. Возвращает ID пользователя в TG."""
    # отладка
    print(f'Отладка: метод command_ID |')
    await message.answer(f'Данные message.chat:\n {message.chat} \n Данные from_user:\n {message.from_user}')


# /info
@router.message(Command(commands=['инфо', 'info', 'help']))
@router.message((F.text.lower().in_(['info', 'информация', 'инфо',
                'расскажи о себе', 'кто ты'])), StateFilter(default_state))
async def command_info(message: types.Message):
    """Метод. На вход принимает команды info, инфо, help. Возвращает информацию о боте и его функциях, а также базовые команды в виде кнопок."""
    # отладка
    print(f'Отладка: метод command_info |')
    await message.answer('Это бот с подключением ChatGPT и DeepSeek', reply_markup=kb_base_command)


@router.callback_query(F.data == 'info')
async def callback_info(callback: CallbackQuery):
    """Метод. Вызывается по кнопке "Инфо о боте". Возвращает информацию о боте и его функциях, а также базовые команды в виде кнопок."""
    # отладка
    print(f'Отладка: метод callback_info |')
    await callback.message.answer('Это бот с подключением ChatGPT и DeepSeek', reply_markup=kb_base_command)


# /fox
@router.message(Command('fox'))
async def command_fox(message: types.Message):
    # отладка
    print(f'Отладка: метод command_fox |')
    image_fox = fox()
    await message.answer_photo(image_fox)
    await message.answer(f'Как тебе лиса?')


# /ai_image
@router.message(Command('ai_image'))
async def command_ai_image(message: types.Message):
    # отладка
    print(f'Отладка: метод command_ai_image |')
    image_ai = FSInputFile(ai())
    await message.answer_photo(image_ai)
    await message.answer(f'Понравилось фото? Да или нет?', reply_markup=kb_base_command)


# /duck
@router.message(Command('duck'))
async def command_duck(message: types.Message):
    # отладка
    print(f'Отладка: метод command_ducks |')
    duck = FSInputFile(duc())
    await message.answer_photo(duck)
    await message.answer(f'Как тебе уточка?')


# отладка
# if __name__ == '__main__':
#     print(fox())
