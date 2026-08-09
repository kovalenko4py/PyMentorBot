from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# command button
inline_button_gpt = InlineKeyboardButton(text="GPT", callback_data="ask_gpt")
inline_button_deepseek = InlineKeyboardButton(text="DeepSeek", callback_data="ask_deepseek")
inline_button_info = InlineKeyboardButton(text="Info", callback_data="info")

# cansel button
inline_button_undo = InlineKeyboardButton(text="Отменить", callback_data="undo")

# famous_person button
inline_button_Freud = InlineKeyboardButton(text="Фрейд", callback_data="Freud")
inline_button_Socrates = InlineKeyboardButton(text="Сократ", callback_data="Socrates")
inline_button_Hawking = InlineKeyboardButton(text="Хокинг", callback_data="Hawking")

# quiz button
inline_button_aiogram = InlineKeyboardButton(text="Aiogram", callback_data="aiogram_Q")
inline_button_HTTP = InlineKeyboardButton(text="HTTP", callback_data="HTTP_Q")
inline_button_Python = InlineKeyboardButton(text="Python_core", callback_data="Python_core_Q")
inline_button_question = InlineKeyboardButton(text="Вопрос", callback_data="New_QuestioN")
inline_button_new_quiz = InlineKeyboardButton(text="Новая тема", callback_data="New_QuiZ")
inline_button_end_quiz = InlineKeyboardButton(text="Завершить", callback_data="undo")
inline_button_answ_1 = InlineKeyboardButton(text="1", callback_data="1")
inline_button_answ_2 = InlineKeyboardButton(text="2", callback_data="2")
inline_button_answ_3 = InlineKeyboardButton(text="3", callback_data="3")
inline_button_answ_4 = InlineKeyboardButton(text="4", callback_data="4")

# keyboard
inline_keyboard_start = InlineKeyboardMarkup(
    inline_keyboard=[[inline_button_info, inline_button_gpt, inline_button_deepseek]])
inline_keyboard_undo = InlineKeyboardMarkup(inline_keyboard=[[inline_button_undo]])
inline_keyboard_famous_person = InlineKeyboardMarkup(
    inline_keyboard=[[inline_button_Hawking, inline_button_Socrates, inline_button_Freud, inline_button_undo]])
inline_keyboard_gtp_stop = InlineKeyboardMarkup(
    inline_keyboard=[[inline_button_deepseek, inline_button_undo]])
inline_keyboard_choose_quiz = InlineKeyboardMarkup(
    inline_keyboard=[[inline_button_Python, inline_button_HTTP, inline_button_aiogram, inline_button_undo]])
inline_keyboard_play_quiz = InlineKeyboardMarkup(
    inline_keyboard=[[inline_button_question, inline_button_new_quiz, inline_button_end_quiz]])
inline_keyboard_answer_quiz = InlineKeyboardMarkup(
    inline_keyboard=[[inline_button_answ_1, inline_button_answ_2, inline_button_answ_3, inline_button_answ_4]])
