from aiogram import Router, types, F
from aiogram.filters.command import Command
from services.chat_gpt import ChatGptService
# from random_fox import fox


router = Router()


@router.message(F.text)
async def echo(message: types.Message, chat_gpt_service: ChatGptService):
    # print(message.text)
    # print(type(message.text))
    if message.text == '/stop':
        await message.answer('Ты точно хочешь остановиться?')
    elif 'stop' in message.text:
        await message.answer('Останавливаемя??')
    else:
        role_text = """Ты эксперт HR и помошник в телеграм боте. Отвечай на русском языке. Если вопрос по вакансиям IT, то объясняй подробно для новичков."""
        answer = await chat_gpt_service.ask(
            user_text=message.text,
            role_text=role_text,
        )
        await message.answer(f'Держи ответ {answer}')