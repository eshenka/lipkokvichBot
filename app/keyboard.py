from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

food_courts = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='RedRabbit🐇', callback_data='red-rabbit'),
     InlineKeyboardButton(text='Хан Буз♨️', callback_data='khan-buz')]
])


red_rabbit = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='RedRabbit🐇', url='https://redrabbit-academ.ru/')]])
khan_buz = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Хан Буз♨️', url='https://khan-buz.ru/')]])