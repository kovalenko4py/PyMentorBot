import sys
import logging

from aiogram import Router, types, F, fsm
from aiogram.filters.command import Command
from aiogram.filters import StateFilter

from keyboards.inline_keyboard import inline_keyboard_undo
from services.http_cat_info import http_cat
from states.base_state import FMSUser

router = Router()
# router = Router(memory_fms)


# TODO сделать отдельную папку и сконфигурировать логирование
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
async def command_http_cat(message: types.Message, state):
    # отладка
    print(f'Отладка: метод command_http_cat |')
    await message.answer(f'Напиши HTTP код, который ты хотел бы изучить или слово "отмена"', reply_markup=inline_keyboard_undo)
    await state.set_state(FMSUser.edu_http)


# CODE
@router.message(StateFilter(FMSUser.edu_http))
async def answer_http_cat(message: types.Message):
    # отладка
    print(f'Отладка: метод answer_http_cat |')
    m = message.text
    if m.isdigit() and 100 <= int(m) <= 599:
        code_info = http_cat(message.text)

        # отладка
        print(f'Отладка: подходит под код HTTP |')
        # print(f'Параметр : {message.text}')
        # print(f"IMAGE: {code_info["image"]}")
        # print(f"CONTENT: {code_info["content"]}")

        await message.answer(code_info["image"])
        await message.answer(code_info["content"])
        await message.answer(f'Как тебе котик?', reply_markup=inline_keyboard_undo)

    else:
        # отладка
        print(f'Отладка: не похож на код HTTP |')
        await message.answer('HTTP код представляет 3-х значное число от 100 до 599. Введи новый HTTP код или нажми\напиши "Отмена"', reply_markup=inline_keyboard_undo)

#отладка
# if __name__ == '__main__':
#     print(answer_http_cat(333))
