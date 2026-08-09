import sys
import logging

from aiogram import Router, types, F
from aiogram.filters.command import Command
from aiogram.types import FSInputFile

from keyboards.keyboards import kb_random_command
from services.image import ai
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


# /random
@router.message(Command(commands=['random', 'Random', 'RANDOM']))
@router.message((F.text == 'Еще факт!'))
async def command_random(message: types.Message, chat_deepseek_service: ChatDeepseekService):
    """Метод. На вход принимает команду random. Возвращает рандомный факт и фото."""
    # отладка
    logger.info(f'Отладка: метод command_random |')
    image_ai = FSInputFile(ai())
    await message.answer_photo(image_ai)
    role_text = """Ты эксперт Python разработчик и помощник в телеграм боте. Отвечай на русском языке. Рассказывай интересные факты о Python для начинающих разработчиков."""
    user_text = """Расскажи интересный и полезный факт о программировании на Python. Говори сразу факт без вступительных слов и тд. В конце резюмируй, чем факт может быть полезен для начинающего программиста. Отдавай ответ формате MarkdownV2, который будет парситься aiogram"""
    answer = await chat_deepseek_service.ask_deepseek(
        role_text_deepseek=user_text,
        user_text_deepseek=role_text,
    )
    await message.answer(f'Интересный факт о Python:\n{answer}', parse_mode="MarkdownV2", reply_markup=kb_random_command)


# отладка
# if __name__ == '__main__':
#     print(fox())
