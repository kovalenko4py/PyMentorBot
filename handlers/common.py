from aiogram import Router, types, F
from aiogram.filters.command import Command
from keyboards.keyboards import kb1, kb2
from keyboards.inline_keyboard import inline_keyboard
from utils.random_fox import fox


router = Router()


# /start
@router.message(Command('start'))
async def command_start(message: types.Message):
    # print(message)
    await message.answer(f'Привет, {message.chat.first_name}!', reply_markup=inline_keyboard)


# /info
@router.message(Command('инфо'))
@router.message(Command('info'))
async def command_info(message: types.Message):
    await message.answer('Это бот с подключением ChatGPT!', reply_markup=kb1)


# /fox
@router.message(Command('fox'))
async def command_fox(message: types.Message):
    image_fox = fox()
    # print(image_fox)
    await message.answer_photo(image_fox)
    await message.answer(f'Понравилось фото? Да или нет?')
    # print('ОК!')

#
# if __name__ == '__main__':
#     print(fox())