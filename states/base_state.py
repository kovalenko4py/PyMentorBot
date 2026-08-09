from aiogram.fsm.state import default_state, State, StatesGroup


user_dict: dict[int, dict[str, str | int | bool]] = {}


class FMSUser(StatesGroup):
    edu_http = State()
    ask_gpt = State()
    ask_deepseek = State()
    ask_famous_person = State()


class FMSQuiz(StatesGroup):
    play = State()
    answ = State()
