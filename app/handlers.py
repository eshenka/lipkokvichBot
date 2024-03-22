import aiogram
import asyncio
import logging
import app.keyboard as keyboards

from aiogram import Bot, Dispatcher, F, Router
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


# @router.message(F.photo)
# async def photo_handler(message: Message):
#     await message.answer(f'ID photo: {message.photo[-1].file_id}')

@router.callback_query(F.data == 'red-rabbit')
async def red_rabbit(callback: CallbackQuery):
    await callback.answer("Not all who wander are lost")
    # await callback.message.answer(reply_markup=keyboards.red_rabbit)

    await callback.message.answer_photo(photo=FSInputFile(path='redrabbit.png'), reply_markup=keyboards.red_rabbit)


@router.callback_query(F.data == 'khan-buz')
async def red_rabbit(callback: CallbackQuery):
    await callback.answer("Enjoy your meal")
    # await callback.message.answer(reply_markup=keyboards.khan_buz)
    await callback.message.answer_photo(photo=FSInputFile(path='khan-buz.png'), reply_markup=keyboards.khan_buz)
