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

red_rabbit_menu_positions = {
    'Пицца': 'Мама, я рыдаю 360р. \nБарбекю пицца 390р. \nМясной босс 480р.',
    'Салаты': "Цезарь 420р. \nС ростбифом 450р.",
    'Супы': 'Сырный с фокачча 310р. \nБульон с яйцом 160р. \nТоматный 310р.',
    'Десерты': 'Морковный торт с гвоздичным кремом 260р. \nЧизкейк манговый 290p.',
}


async def inline_red_rabbit_menu():
    red_rabbit_menu_keyboard = InlineKeyboardBuilder()

    for position in red_rabbit_menu_positions.keys():
        red_rabbit_menu_keyboard.add(InlineKeyboardButton(text=position, callback_data=position))

    red_rabbit_menu_keyboard.add(InlineKeyboardButton(text='Назад🔙', callback_data='red-rabbit-menu-back'))

    return red_rabbit_menu_keyboard.adjust(2).as_markup()
