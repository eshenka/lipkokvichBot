import app.keyboard as keyboards

from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery, FSInputFile

router = Router()


@router.message(CommandStart())
async def command_start(message: Message):
    await message.answer(text='Где хотите покушать сегодня?', reply_markup=keyboards.food_courts)


@router.message(Command('help'))
async def command_help(message: Message):
    await message.answer('mne bi kto pomog')


@router.message(F.text == 'как дела?')
async def text_how_are_you(message: Message):
    await message.answer('im fine')


@router.callback_query(F.data.in_({'red-rabbit-menu-back', 'red-rabbit'}))
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
        await callback.message.answer(menu[callback.data])
    else:
        raise Exception("invalid callback data")


@router.callback_query(F.data == 'khan-buz')
async def khan_buz(callback: CallbackQuery):
    await callback.answer("Enjoy your meal")
    await callback.message.answer_photo(photo=FSInputFile(path='khan-buz.png'), reply_markup=keyboards.khan_buz)
