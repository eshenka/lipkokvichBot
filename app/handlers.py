import app.keyboard as keyboards

from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery, FSInputFile

import random

router = Router()


class Food:
    def __init__(self, name: str, price: int):
        self.name = name
        self.price = price


@router.message(CommandStart())
async def command_start(message: Message):
    await message.answer(text='Где хотите покушать сегодня?', reply_markup=keyboards.food_courts)


@router.message(Command('help'))
async def command_help(message: Message):
    await message.answer('mne bi kto pomog')


@router.message(Command('play'))
async def command_play(message: Message):
    keyboards.game_numbers[message.from_user.id] = random.randint(0, 9_999_999)

    await message.answer('Сколько раз БякБяк бякбякал, чтобы получить пятерку на экзамене?')
    await message.answer('Подсказка! От 0 до 10 000 000 раз')


@router.message(F.text.regexp(r'[0-9]'))
async def game_number(message: Message):
    user_id = message.from_user.id
    user_number = keyboards.game_numbers[user_id]
    input_number = int(message.text)

    if user_number == input_number:
        await message.answer('Ты угадал!!!')
        keyboards.game_numbers[user_id] = random.randint(0, 9_999_999)

    if input_number < user_number:
        await message.answer('Больше')

    if user_number < input_number:
        await message.answer('Меньше')


@router.message(F.content_type.in_({'sticker'}))
async def send_sticker(message: Message):
    sticker_pack = keyboards.stickers
    pack_len = len(sticker_pack)
    await message.answer_sticker(sticker=sticker_pack[random.randint(0, pack_len - 1)])


@router.message(F.text == 'как дела?')
async def text_how_are_you(message: Message):
    await message.answer('im fine')


@router.callback_query(F.data.in_({'rr-menu-back', 'red-rabbit'}))
async def red_rabbit(callback: CallbackQuery):
    await callback.answer("Not all who wander are lost")
    await callback.message.answer_photo(photo=FSInputFile(path='redrabbit.png'), reply_markup=keyboards.red_rabbit)


@router.callback_query(F.data == 'red-rabbit-menu')
async def red_rabbit_menu(callback: CallbackQuery):
    await callback.message.edit_caption(text='Выберите позицию', reply_markup=keyboards.inline_red_rabbit_menu())


@router.callback_query(F.data.in_(keyboards.red_rabbit_menu_positions.keys()))
async def red_rabbit_positions(callback: CallbackQuery):
    menu = keyboards.red_rabbit_menu_positions

    if callback.data in menu:
        await callback.message.answer(text=keyboards.process_food_data(menu[callback.data]))
    else:
        raise Exception("invalid callback data")


@router.callback_query(F.data.in_({'khan-buz', 'kh-menu-back'}))
async def khan_buz(callback: CallbackQuery):
    await callback.answer("Enjoy your meal")
    await callback.message.answer_photo(photo=FSInputFile(path='khan-buz.png'), reply_markup=keyboards.khan_buz)


@router.callback_query(F.data == 'khan-buz-menu')
async def khan_buz_menu(callback: CallbackQuery):
    await callback.message.edit_caption(text='Выберите позицию', reply_markup=keyboards.inline_khan_buz_menu())


@router.callback_query(F.data.in_(keyboards.khan_buz_menu_positions.keys()))
async def khan_buz_positions(callback: CallbackQuery):
    menu = keyboards.khan_buz_menu_positions

    if callback.data in menu:
        await callback.message.answer(text=keyboards.process_food_data(menu[callback.data]))
    else:
        raise Exception("invalid callback data")


@router.callback_query(F.data == 'rr-random')
async def red_rabbit_random(callback: CallbackQuery):
    await callback.message.answer(keyboards.process_random(keyboards.red_rabbit_menu_positions))


@router.callback_query(F.data == 'kh-random')
async def khan_buz_random(callback: CallbackQuery):
    await callback.message.answer(keyboards.process_random(keyboards.khan_buz_menu_positions))

