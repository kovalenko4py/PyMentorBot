import sys
import logging
from random import randint

from aiogram import Router, types, F
from aiogram.types import FSInputFile, CallbackQuery
from aiogram.filters import StateFilter
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.redis import RedisStorage
from redis.asyncio import Redis

from states.base_state import FMSQuiz
from keyboards.inline_keyboard import inline_keyboard_choose_quiz, inline_keyboard_undo, inline_keyboard_play_quiz, inline_keyboard_answer_quiz
from services.image import quiz_image
# from services.chat_gpt import ChatGptService - если колюч активный у GPT
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


# /quiz
@router.message(Command(commands=['quiz', 'Quiz', 'QUIZ']))
async def command_choose_quiz(message: types.Message, state: FSMContext):
    """Метод. На вход принимает команду 'quiz'. Возвращает ответ и варианты выбора для quiz."""
    # отладка
    logging.info(f'Отладка: метод command_choose_quiz |')
    image_quiz = FSInputFile(quiz_image())
    await message.answer_photo(image_quiz)
    await message.answer('Выбери тему для quiz.', reply_markup=inline_keyboard_choose_quiz)
    await state.set_state(FMSQuiz.play)


@router.callback_query(StateFilter(FMSQuiz.play), F.data.in_(['New_QuiZ']))
async def callback_choose_new_quiz(callback: CallbackQuery):
    # отладка
    logging.info(f'Отладка: метод callback_choosing_quiz | {callback.data}')

    image_quiz = FSInputFile(quiz_image())
    await callback.message.answer_photo(image_quiz)
    await callback.message.answer('Выбери тему для quiz.', reply_markup=inline_keyboard_choose_quiz)


@router.callback_query(StateFilter(FMSQuiz.play),
                       F.data.in_(['Python_core_Q', 'HTTP_Q', 'aiogram_Q']))
async def callback_choosing_quiz(callback: CallbackQuery, state: FSMContext):
    # отладка
    logging.info(f'Отладка: метод callback_choosing_quiz | {callback.data}')
    quiz_name = callback.data
    await callback.message.answer(f'Привет {callback.message.chat.first_name}, \nмы начинаем quiz по теме - {quiz_name}. \nОтвечая выбирай цифру от 1 до 4.', reply_markup=inline_keyboard_play_quiz)
    await state.update_data(quiz_name=quiz_name, win=0, lose=0)


@router.callback_query(StateFilter(FMSQuiz.play), F.data.in_(['New_QuestioN']))
async def quiz(callback: CallbackQuery,
               chat_deepseek_service: ChatDeepseekService, state: FSMContext):
    """Метод. На вход принимает команду talk. Реализует возможность общения с чатом GPT в роли известной личности из списка: Сократ, Хокинг, Фрейд."""
    quiz = await state.get_data()
    num = randint(1, 4)
    # отладка
    print(f'Отладка: метод answer_famous_quiz |quiz -  {quiz}, num - {num}')
    role_text = f"""Ты задаешь вопросы по теме: {quiz["quiz_name"]}.
    Правила:
    1. Выбирай интересные вопросы.
    2. Начинай вопрос со слова "ВОПРОС:" после текста вопроса делай два пропуска строки пиши слово "ВАРИАНТЫ ОТВЕТОВ" и потом давай ответы.
    3. Предлагай 4 ответа на вопрос:
    3.1 нумеруй вопросы от 1 до 4
    3.2 только один из них должен быть правильный
    3.3 ВАЖНО - правильный ответ должен быть под номером - {num}
    4. В конце добавляй отдельный блок: "Чем это полезно начинающему программисту:" и 2 коротких практических вывода."""
    user_text = 'Задай вопрос'
    answer = await chat_deepseek_service.ask_deepseek(
        role_text_deepseek=role_text,
        user_text_deepseek=user_text,
    )
    await callback.message.answer(f'{answer}', reply_markup=inline_keyboard_answer_quiz)
    await state.update_data(correct_answer=num)
    await state.set_state(FMSQuiz.answ)


@router.callback_query(StateFilter(FMSQuiz.answ), F.data.in_(['1', '2', '3', '4']))
async def callback_answer_quiz(callback: CallbackQuery, state: FSMContext):
    quiz_score = await state.get_data()
    # отладка
    print(f'Отладка: метод callback_answer_quiz | {quiz_score} -- {callback.data}')
    data = await state.get_data()
    win = data.get("win", 0)
    lose = data.get("lose", 0)
    if int(data["correct_answer"]) == int(callback.data):
        await state.update_data(win=win + 1)
    else:
        await state.update_data(lose=lose + 1)
    data = await state.get_data()
    await state.set_state(FMSQuiz.play)
    await callback.message.answer(f'Так держать, {callback.message.chat.first_name},\nСЧЕТ: \nправильные ответы - {data["win"]}, ошибки - {data["lose"]}\n\nВыбери следующий шаг.', reply_markup=inline_keyboard_play_quiz)


@router.message(StateFilter(FMSQuiz.answ))
async def wrong_answer_quiz(message: types.Message,
                            chat_deepseek_service: ChatDeepseekService, state: FSMContext):
    """Метод. На вход принимает команду talk. Реализует возможность общения с чатом GPT в роли известной личности из списка: Сократ, Хокинг, Фрейд."""
    await message.answer(f'Выбери цифру от 1 до 4', reply_markup=inline_keyboard_answer_quiz)


# отладка
# if __name__ == '__main__':
#     print(fox())
