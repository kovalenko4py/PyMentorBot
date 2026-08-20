import logging
import sys

from aiogram import Router, types, F
from aiogram.filters import StateFilter, Command
from aiogram.fsm.context import FSMContext
from states.base_state import FMSUser
from aiogram.types import FSInputFile, Message

from keyboards.inline_keyboard import inline_keyboard_undo, inline_keyboard_gtp_stop
from services.image import ai
from services.chat_gpt import ChatGptService
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

@router.message(Command('ask_gpt'))
@router.callback_query(F.data == 'ask_gpt')
async def callback_ask_gpt(callback: types.CallbackQuery, state: FSMContext):
    """Метод. На вход принимает текст 'ask_gpt'. Возвращает фото и ответ для старта общения с GPT."""
    # отладка
    print(f'Отладка: метод callback_ask_gpt ')

    image_ai = FSInputFile(ai())
    if isinstance(callback, types.CallbackQuery):
        message = callback.message
    else:
        message = callback

    await message.answer_photo(image_ai)
    # answer = "GPT устал, пообщайся с DeepSeek, он еще бодрый." # если есть ключ GPT раскоментарить
    answer = "Чтобы задать вопрос GPT, напиши его в чате и отправь."  # если есть ключ GPT закоментарить
    await message.answer(f'{answer} ', reply_markup=inline_keyboard_gtp_stop)
    await state.set_state(FMSUser.ask_gpt)

# TODO сделать условие: что-то с ключом - стандарт ответ,иначе - запрос к GPT


@router.message(StateFilter(FMSUser.ask_gpt))
async def answer_gpt(message: types.Message, state: FSMContext, chat_gpt_service: ChatGptService):
    # отладка
    print(f'Отладка: метод answer_gpt | {message.text} | {type(message.text)}')
    if message.text == '/stop':
        await message.answer('Ты точно хочешь остановиться?')
    elif 'stop' in message.text:
        await message.answer('Останавливаемcя?')
    else:
        # role_text = """Ты опытный специалист. Можешь найти ответ на любой вопрос"""
        # answer = await chat_gpt_service.ask(
        #     user_text=message.text,
        #     role_text=role_text,
        # )
        answer = "GPT устал, пообщайся с DeepSeek, он еще бодрый."
        await message.answer(f'Держи ответ:\n{answer}', reply_markup=inline_keyboard_gtp_stop)
        await state.clear()  # если есть ключ GPT закоментарить и убрать 'state: FSMContext' во входящих параметрах

@router.message(Command('ask_deepseek'))
@router.callback_query(F.data == 'ask_deepseek')
async def callback_ask_deepseek(callback: types.CallbackQuery, state: FSMContext):
    """Метод. На вход принимает текст 'ask_gpt'. Возвращает фото и ответ для старта общения с DeepSeek."""
    # отладка
    print(f'Отладка: метод callback_ask_deepseek ')
    image_ai = FSInputFile(ai())
    if isinstance(callback, types.CallbackQuery):
        message = callback.message
    else:
        message = callback
    await message.answer_photo(image_ai)
    await message.answer('Чтобы задать вопрос DeepSeek, напиши его в чате и отправь.', reply_markup=inline_keyboard_undo)
    await state.set_state(FMSUser.ask_deepseek)


@router.message(StateFilter(FMSUser.ask_deepseek))
async def answer_deepseek(message: types.Message, chat_deepseek_service: ChatDeepseekService):
    # отладка
    print(f'Отладка: метод answer_deepseek | {message.text} | {type(message.text)}')

    role_text = """Отвечай кратко. Без вступлений и вежливости. Формат: факты → список → вывод (1 строка). """
    answer = await chat_deepseek_service.ask_deepseek(
        role_text_deepseek=role_text,
        user_text_deepseek=message.text,
    )
    await message.answer(f'Держи ответ:\n{answer}', reply_markup=inline_keyboard_undo)
