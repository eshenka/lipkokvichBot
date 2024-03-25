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


@router.callback_query(F.data == 'red-rabbit')
@router.callback_query(F.data == 'Назад🔙')
async def red_rabbit(callback: CallbackQuery):
    await callback.answer("Not all who wander are lost")
    await callback.message.answer_photo(photo=FSInputFile(path='redrabbit.png'), reply_markup=keyboards.red_rabbit)


@router.callback_query(F.data == 'red-rabbit-menu')
async def red_rabbit_menu(callback: CallbackQuery):
    await callback.message.edit_caption(text='Выберите позицию', reply_markup=await keyboards.inline_red_rabbit_menu())


@router.callback_query(F.data == 'Пицца')
@router.callback_query(F.data == 'Салаты')
@router.callback_query(F.data == 'Супы')
@router.callback_query(F.data == 'Десерты')
async def red_rabbit_positions(callback: CallbackQuery):
    match callback.data:
        case 'Пицца':
            reply_text = "Мама, я рыдаю 360р. \nБарбекю пицца 390р. \nМясной босс 480р."
        case 'Салаты':
            reply_text = 'Цезарь 420р. \nС ростбифом 450р.'
        case 'Супы':
            reply_text = 'Сырный с фокачча 310р. \nБульон с яйцом 160р. Томатный 310р.'
        case 'Десерты':
            reply_text = 'Морковный торт с гвоздичным кремом 260р. \nЧизкейк манговый 290p.'
        case _:
            reply_text = 'попробуй снова'

    await callback.message.answer(text=reply_text)


@router.callback_query(F.data == 'khan-buz')
async def khan_buz(callback: CallbackQuery):
    await callback.answer("Enjoy your meal")
    await callback.message.answer_photo(photo=FSInputFile(path='khan-buz.png'), reply_markup=keyboards.khan_buz)
