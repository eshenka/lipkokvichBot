from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

food_courts = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='RedRabbit🐇', callback_data='red-rabbit'),
     InlineKeyboardButton(text='Хан Буз♨️', callback_data='khan-buz')]
])


red_rabbit = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='RedRabbit🐇', url='https://redrabbit-academ.ru/')], [InlineKeyboardButton(text='Меню', callback_data='red-rabbit-menu')]])
khan_buz = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Хан Буз♨️', url='https://khan-buz.ru/')]])

red_rabbit_menu_positions = ['Пицца', 'Салаты', 'Супы', 'Десерты', 'Назад🔙']


async def inline_red_rabbit_menu():
    red_rabbit_menu_keyboard = InlineKeyboardBuilder()

    for position in red_rabbit_menu_positions:
        red_rabbit_menu_keyboard.add(InlineKeyboardButton(text=position, callback_data=position))

    return red_rabbit_menu_keyboard.adjust(2).as_markup()
