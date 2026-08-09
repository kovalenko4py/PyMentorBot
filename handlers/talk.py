import sys
import logging

from aiogram import Router, types, F
from aiogram.types import FSInputFile, CallbackQuery
from aiogram.filters import StateFilter
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext
from states.base_state import FMSUser

from keyboards.keyboards import kb_random_command
from keyboards.inline_keyboard import inline_keyboard_famous_person, inline_keyboard_undo
from services.image import person_image
# from services.chat_gpt import ChatGptService
from services.chat_deepseek import ChatDeepseekService


router = Router()

# TODO сделать отдельную папку и сконфигурировать лог
logging.basicConfig(
    level=logging.DEBUG,
    format='[{asctime}] #{levelname:8} {filename}:' '{lineno} - {name} - {message}',
    style='{'
)
logger = logging.getLogger(__name__)
stdout_handler = logging.StreamHandler(sys.stdout)
logger.addHandler(stdout_handler)

logger.debug(f'Логер работает в модуле {logger.name}!')


# /talk
@router.message(Command(commands=['talk', 'Talk', 'TALK']))
async def command_choose_famous_person(message: types.Message, state: FSMContext):
    """Метод. На вход принимает команду 'talk'. Возвращает ответ и вариант для общения с известной персоной с GPT."""
    # отладка
    logging.info(f'Отладка: метод command_choose_famous_person |')
    await message.answer('Выбери кому хочешь задать вопрос.', reply_markup=inline_keyboard_famous_person)
    await state.set_state(FMSUser.ask_famous_person)


@router.callback_query(StateFilter(FMSUser.ask_famous_person),
                       F.data.in_(['Hawking', 'Freud', 'Socrates']))
async def callback_choosing_famous_person(callback: CallbackQuery, state: FSMContext):
    # отладка
    logging.info(f'Отладка: метод callback_choosing_famous_person | {callback.data}')
    famous_person = callback.data
    image_famous_person = FSInputFile(person_image(famous_person))
    await callback.message.delete()
    await callback.message.answer_photo(image_famous_person)
    await callback.message.answer(f'Привет {callback.message.chat.first_name}, о чем ты хочешь поговорить?', reply_markup=inline_keyboard_undo)
    await state.update_data(famous_person=famous_person)


@router.message(StateFilter(FMSUser.ask_famous_person))
async def answer_famous_person(
        message: types.Message, chat_deepseek_service: ChatDeepseekService, state: FSMContext):
    """Метод. На вход принимает команду talk. Реализует возможность общения с чатом GPT в роли известной личности из списка: Сократ, Хокинг, Фрейд."""
    person = await state.get_data()
    # отладка
    print(f'Отладка: метод answer_famous_person | {person}')
    role_text = f"""Ты отвечаешь в образе личности: {person["famous_person"]}.
    Правила:
    1. Сохраняй узнаваемую манеру речи, стиль мышления и подачу этой личности, но не уходи в карикатуру.
    2. Не придумывай биографические факты, которых не знаешь. Если факт неочевиден, говори нейтрально и без вымысла.
    3. Отвечай сразу по сути, без вступлений, без фраз вроде "конечно", "интересный вопрос", "давай разберём".
    4. В конце добавляй отдельный блок: "Чем это полезно начинающему программисту:" и 2–4 коротких практических вывода."""
    user_text = message.text
    answer = await chat_deepseek_service.ask_deepseek(
        role_text_deepseek=role_text,
        user_text_deepseek=user_text,
    )
    await message.answer(f'Держи ответ:\n{answer}', reply_markup=inline_keyboard_undo)


# отладка
# if __name__ == '__main__':
#     print(fox())
