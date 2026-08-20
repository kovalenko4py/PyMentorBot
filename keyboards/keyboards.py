from aiogram import types


button_start = types.KeyboardButton(text='/start')
button_info = types.KeyboardButton(text='/info')
button_fox = types.KeyboardButton(text='/fox')
button_duck = types.KeyboardButton(text='/duck')
button_ai = types.KeyboardButton(text='/ai_image')
button_prof = types.KeyboardButton(text='/prof')
button_id = types.KeyboardButton(text='/user_id')
button_random = types.KeyboardButton(text='/random')
button_new_fact = types.KeyboardButton(text='Еще факт!')
button_end = types.KeyboardButton(text='Закончить!!')
button_quiz = types.KeyboardButton(text='/quiz')
button_talk = types.KeyboardButton(text='/talk')
button_http = types.KeyboardButton(text='/http_cat')
button_end_http = types.KeyboardButton(text='End !!')
button_new_http = types.KeyboardButton(text='New code!')
button_gpt = types.KeyboardButton(text='/ask_gpt')
button_deepseek = types.KeyboardButton(text='/ask_deepseek')

keyboard_base_l = [button_info, button_gpt, button_deepseek, button_random, button_quiz, button_talk, button_http, button_id, button_fox, button_duck, button_ai]
keyboard_base: list[keyboard_base_l] = [
    keyboard_base_l[0:3],
    keyboard_base_l[3:8],
    keyboard_base_l[8:11]]

keyboard_random = [[button_new_fact, button_end],]
keyboard_http = [[button_end_http, button_new_http],]

kb_base_command = types.ReplyKeyboardMarkup(keyboard=keyboard_base, resize_keyboard=True)
kb_random_command = types.ReplyKeyboardMarkup(keyboard=keyboard_random, resize_keyboard=True)
kb_http_command = types.ReplyKeyboardMarkup(keyboard=keyboard_http, resize_keyboard=True)