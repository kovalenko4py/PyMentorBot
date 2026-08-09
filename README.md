
<div align="center">
<img src="images/ai/AI_image_0.png" width="30%" style="position: relative; top: 10px; right: 0" alt="Project Logo"/>
</div>

# PyMentor Bot 

Форк [лекции Project_tg_4](https://github.com/Stanislavzzz/JR_PyVenom/tree/main/m1/lesson.32_Project_tg_4) от [Stanislavzzz](https://github.com/Stanislavzzz)
<div align="center">
<img src="https://img.shields.io/badge/.ENV-ECD53F.svg?style=default&logo=dotenv&logoColor=black" alt=".ENV">
<img src="https://img.shields.io/badge/Python-3776AB.svg?style=default&logo=Python&logoColor=white" alt="Python">
<img src="https://img.shields.io/badge/OpenAI-412991.svg?style=default&logo=OpenAI&logoColor=white" alt="OpenAI">
<img src="https://img.shields.io/badge/redis-FF0000.svg?style=default&logo=redis&logoColor=white" alt="redis">
</div>

Создан для проверки знаний и навыков Python core автора проекта в рамках обучения на курсе Python JavaRush, поэтому написан без использования ИИ.    
Но может быть полезен для проверки и закрепления знаний по основам python для начинающих изучать программирование.   
Бот использует GPT и DeepSeek для ответов на вопросы.   
Бот использует сайт [HTTP Cat](https://http.cat/) для демонстрации картинок котов с кодами HTTP и информацией об HTTP кодах.  


### Возможности
#### Для пользователей с правами админ и выше:
| Функция                                                   |     Команды     | 
|:----------------------------------------------------------|:---------------:|
| Отправляет файлы с логами                                 |      текст      | 
| Показывает баланс и информацию по использованию DeepSeek  | send_balance_ds |


#### Для пользователей без спец прав:
| Функция                                                                                                                                       |                                        Команды и текст                                         | 
|:----------------------------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------:|
| Возврат на начало работы бота                                                                                                                 | /start, /START <br> или текст:'старт', 'начало', 'начало работы', 'start', 'отмена', 'не хочу' | 
| Дает информацию о себе                                                                                                                        |                /инфо, /info, /help <br> или текст: 'info', 'информация', 'инфо'                | 
| Рассказывает факты о Python                                                                                                                   |                     /random, /Random, /RANDOM <br> или текст: 'Еще факт!'                      |
| Дает ответы на вопросы, используя информацию от GPT и DeepSeek (по выбору пользователя)                                                       |                                    /ask_deepseek, /ask_gpt                                     |
| Дает возможность пообщаться с Сократом, Стивеном Хокингом, Зигмундом Фрейдом (по выбору пользователя), используя информацию от GPT и DeepSeek |                                      /talk, /Talk, /TALK                                       |
| Дает возможность пройти квиз по темам: "Python Core", "HTTP", "Aiogram" (по выбору пользователя)                                              |                                      /quiz, /Quiz, /QUIZ                                       |
| Отправляет фотографии уточек, AI и лис (по выбору пользователя)                                                                               |                                     /duck, /ai_image, /fox                                     |
| Дает информацию и картинки котов по HTTP кодам                                                                                                |                                           /http_cat                                            |
| Передает информацию о ID пользователя в TG                                                                                                    |                                      /ID, /id, /user_id                                        | 


### Стек

- Python 3.13+
- requests
- beautifulsoup4
- python-telegram-bot
- Redis 

Подробно можно посмотреть тут [requirements.txt](requirements.txt)


### Установка

```bash
git clone https://github.com/username/project-name.git
cd project-name
pip install -r requirements.txt
```


### Настройка
Создайте файл `.env` и укажите:

```env
BOT_TOKEN=your_telegram_bot_token
TARGET_URL=https://example.com
```


### Запуск
```pwsh

py .\main.py
```

### Структура проекта
```sh
└── /
    ├── README.md
    ├── configs
    │   ├── __init__.py
    │   ├── __pycache__
    │   └── config.py
    ├── db
    │   ├── __init__.py
    │   ├── __pycache__
    │   └── memory_fms.py
    ├── env.example
    ├── handlers
    │   ├── __init__.py
    │   ├── __pycache__
    │   ├── admin_commands.py
    │   ├── ai_chats.py
    │   ├── base_commands.py
    │   ├── career_choice.py
    │   ├── echo.py
    │   ├── http_cat.py
    │   ├── quiz.py
    │   ├── random_fact.py
    │   └── talk.py
    ├── images
    │   ├── ai
    │   ├── ducks
    │   ├── person
    │   └── quiz
    ├── keyboards
    │   ├── __init__.py
    │   ├── __pycache__
    │   ├── inline_keyboard.py
    │   ├── keyboards.py
    │   └── prof_keyboards.py
    ├── logs
    │   ├── DebugLog.log
    │   ├── DebugLog.log.2026-06-18
    │   ├── InfoLog.log
    │   ├── InfoLog.log.2026-06-20
    │   ├── InfoLog.log.2026-..-..
    ├── main.py
    ├── my_bad_code_style
    ├── requirements.txt
    ├── services
    │   ├── __init__.py
    │   ├── __pycache__
    │   ├── chat_deepseek.py
    │   ├── chat_gpt.py
    │   ├── http_cat.py
    │   └── image.py
    ├── setup.cfg
    ├── states
    │   ├── __init__.py
    │   ├── __pycache__
    │   ├── base_state.py
    │   └── career_state.py
    └── utils
        ├── __init__.py
        ├── __pycache__
        ├── deepseek_util.py
        ├── filters.py
        ├── redis.py
        └── users.py
```


### TODO
- Добавить логирование
- Добавить обработку ошибок сети
- Добавить кэширование
- Перевести настройки в `.env`
