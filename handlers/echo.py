import logging
import sys

from aiogram import Router, types, F
from keyboards.inline_keyboard import inline_keyboard_undo

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


@router.message(F.text)
async def echo(message: types.Message, chat_deepseek_service: ChatDeepseekService):
    # отладка
    print(f'Отладка: метод echo | {message.text} | {type(message.text)}')

    if message.text == '/stop':
        await message.answer('Ты точно хочешь остановиться?')
    elif 'stop' in message.text:
        await message.answer('Останавливаемcя?')
    else:
        role_text = """Ты опытный специалист. Можешь найти ответ на любой вопрос. Но отвечаешь очень кратко.
                    Предлагаешь познакомиться с ботом с помощью команды /info и воспользоваться профильными функциями бота.
                    Заканчивай сообщение предложением: Познакомьтесь с ботом с помощью команды /info и воспользуйтесь профильными функциями."""
        answer = await chat_deepseek_service.ask_deepseek(
            user_text_deepseek=message.text,
            role_text_deepseek=role_text,
        )
        await message.answer(f'Держи ответ:\n{answer}', reply_markup=inline_keyboard_undo)
