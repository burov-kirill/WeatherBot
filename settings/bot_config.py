from aiogram.dispatcher.filters.state import State, StatesGroup

bot_token = '6176510825:AAGLel_QiLSlri3TMOuNoztV0ngQfdQVgpk'
tg_bot_admin = [1713163569]

class ChoiceCityWeather(StatesGroup):
    waiting_city = State()

class SetUserCity(StatesGroup):
    waiting_user_city = State()