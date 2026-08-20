import logging
from logging.handlers import TimedRotatingFileHandler
import asyncio
from pathlib import Path

from aiogram import Bot, Dispatcher

from configs import config
from handlers import base_commands, ai_chats, echo, http_cat, random_fact, talk, admin_commands, quiz
from services.chat_gpt import ChatGptService
from services.chat_deepseek import ChatDeepseekService
from db.memory_fms import memory_fms
from utils.redis import test_connection_redis


async def main():
    TOKEN_TG = config.token_telegram
    TOKEN_OPENAI = config.token_openai
    TOKEN_DEEPSEEK = config.token_deepseek_key

    class DebugOnlyFilter(logging.Filter):
        def filter(self, record: logging.LogRecord) -> bool:
            return record.levelno == logging.DEBUG

    form = '[%(asctime)s] #%(levelname)-8s %(filename)s:%(lineno)d - %(name)s - %(message)s'

    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    logger.handlers.clear()

    formatter = logging.Formatter(fmt=form)

    base_dir = Path(__file__).resolve().parent
    log_dir = base_dir / "logs"
    log_dir.mkdir(exist_ok=True)

    # Файл ТОЛЬКО для DEBUG
    log_debug = TimedRotatingFileHandler(
        filename=log_dir / "DebugLog.log",
        when='midnight',
        interval=1,
        backupCount=14,
        encoding='utf-8'
    )
    log_debug.setLevel(logging.DEBUG)  # принимать всё от DEBUG и выше
    log_debug.addFilter(DebugOnlyFilter())  # но записывать ТОЛЬКО DEBUG
    log_debug.setFormatter(formatter)

    # Файл для INFO и выше
    log_info = TimedRotatingFileHandler(
        filename=log_dir /"InfoLog.log",
        when='midnight',
        interval=1,
        backupCount=14,
        encoding='utf-8'
    )
    log_info.setLevel(logging.INFO)  # отсекает DEBUG, пишет INFO+
    log_info.setFormatter(formatter)

    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    console.setFormatter(formatter)

    logger.addHandler(log_debug)
    logger.addHandler(log_info)
    logger.addHandler(console)

    bot = Bot(token=TOKEN_TG)
    dp = Dispatcher(storage=memory_fms)

    await test_connection_redis()

    chat_gpt_service = ChatGptService(api_key=TOKEN_OPENAI)
    dp["chat_gpt_service"] = chat_gpt_service

    chat_deepseek_service = ChatDeepseekService(api_key=TOKEN_DEEPSEEK)
    dp["chat_deepseek_service"] = chat_deepseek_service

    dp.include_router(admin_commands.router)
    dp.include_router(base_commands.router)
    dp.include_router(talk.router)
    dp.include_router(quiz.router)
    dp.include_router(random_fact.router)
    dp.include_router(http_cat.router)
    dp.include_router(ai_chats.router)
    dp.include_router(echo.router)

    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
