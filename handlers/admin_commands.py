import sys
import logging

from aiogram import Router, types, F
from aiogram.filters.command import Command
from keyboards.inline_keyboard import inline_keyboard_start

from utils.deepseek_util import deepseek_check_balance
import utils.users


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


# TODO реализовать функцию рассылки логов
# /send_log

# TODO доработать команду set_admin. Стопер: Решить где хранить информацию об админах
# /set_admin
@router.message(Command(commands=['set_admin']))
async def command_set_admin(message: types.Message):
    """Метод. На вход принимает команду: set_admin. Добавляет."""
    # отладка
    print(f'Отладка: метод command_set_admin |')
    await message.answer(f'Привет, {message.chat.first_name}!', reply_markup=inline_keyboard_start)


# TODO сделать фильтр на проверку super_admin
# /send_balance_ds
@router.message(Command(commands=['send_balance_ds']))
async def command_send_balance_ds(message: types.Message):
    # отладка
    print(f'Отладка: метод command_send_balance_ds |')
    data = deepseek_check_balance()
    await message.answer(f'Привет, информация о балансе: \n{data}!', reply_markup=inline_keyboard_start)


# отладка
# if __name__ == '__main__':
#     print(fox())
