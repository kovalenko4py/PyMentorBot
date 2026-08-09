import sys
import logging

from aiogram import Router, types, F, fsm
from aiogram.filters.command import Command

from keyboards.inline_keyboard import inline_keyboard_undo
from services.http_cat import http_cat


router = Router()
# router = Router(memory_fms)


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


# /http_cat
@router.message(Command('http_cat'))
async def command_http_cat_1(message: types.Message, state):
    # отладка
    print(f'Отладка: метод command_http_cat_1 |')
    await message.answer(f'Напиши HTTP код, который ты хотел бы изучить или слово "отмена"', reply_markup=inline_keyboard_undo)


# CODE
@router.message(F.data == 'New code!')  # TODO не работает
# @router.message(StateFilter(FMSHttpCat.edu_http),lambda x: x.text.isdigit() and 100 <= int(x.text) <= 599)
@router.message(lambda x: x.text.isdigit() and 100 <= int(x.text) <= 599)
async def command_http_cat_2(message: types.Message):
    code_info = http_cat(message.text)

    # отладка
    print(f'Отладка: метод command_http_cat_2 |')
    # print(f'Параметр : {message.text}')
    # print(f"IMAGE: {code_info["image"]}")
    # print(f"CONTENT: {code_info["content"]}")

    await message.answer(code_info["image"])
    await message.answer(code_info["content"])
    await message.answer(f'Как тебе котик?', reply_markup=inline_keyboard_undo)


# отладка
# if __name__ == '__main__':
#     print(command_http_cat_2())
