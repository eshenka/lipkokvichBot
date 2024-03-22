from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

# main = ReplyKeyboardMarkup(keyboard=[
#     [KeyboardButton(text='btn1')],
#     [KeyboardButton(text='btn2'), KeyboardButton(text='btn3')]
# ],
#     resize_keyboard=True,
#     input_field_placeholder='choose')
#
# settings = InlineKeyboardMarkup(inline_keyboard=[
#     [InlineKeyboardButton(text='pinterest', url='https://pin.it/78jOQY9AX')]
# ])
#
# cars = ['car1', 'car2', 'car3', 'car4']
#
#
# async def inline_cars():
#     keyboard = InlineKeyboardBuilder()
#     for car in cars:
#         keyboard.add(InlineKeyboardButton(text=car, url='https://youtube.com/'))
#     return keyboard.adjust(2).as_markup()


food_courts = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='RedRabbit🐇', callback_data='red-rabbit'),
     InlineKeyboardButton(text='Хан Буз♨️', callback_data='khan-buz')]
])


red_rabbit = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='RedRabbit🐇', url='https://redrabbit-academ.ru/')]])
khan_buz = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Хан Буз♨️', url='https://khan-buz.ru/')]])