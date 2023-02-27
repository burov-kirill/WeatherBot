from aiogram import types
from aiogram.utils.callback_data import CallbackData

async def main_menu():
    cb = CallbackData('start_kb', 'action')
    markup = types.InlineKeyboardMarkup(row_width=2)
    btn1 = types.InlineKeyboardButton(text='Погода в моём городе', callback_data=cb.new('my_city'))
    btn2 = types.InlineKeyboardButton(text='Погода в другом месте', callback_data=cb.new('other_city'))
    btn3 = types.InlineKeyboardButton(text='История', callback_data=cb.new('history'))
    btn4 = types.InlineKeyboardButton(text='Установить свой город', callback_data=cb.new('set_city'))
    markup.add(btn1, btn2, btn3, btn4)
    return markup