from aiogram import types, F, Router
from aiogram.filters.command import Command
import logging
import random
from less3.keyboards.keyboards import kb_eng1, kb_eng2
from less3.utils.random_fox import fox


router = Router()


#Хэндлер на команду /start
@router.message(Command('start')) #ENG
@router.message(Command('cтарт')) #RUS
async def cmd_start (message: types.Message):
    name = message.chat.first_name
    await message.answer(f'Привет, {name}', reply_markup=kb_eng1)
    await message.answer(f'{name}, для продолжения работы воспользуйся клавиатурой', reply_markup=kb_eng2)

#Хэндлер на команду /info
@router.message(Command('info')) #ENG
@router.message(Command('инфо')) #RUS
async def cmd_info (message: types.Message):
    name = message.chat.first_name
    await message.answer(f'Я начинающий бот, не судите меня строго :), {name}', reply_markup=kb_eng2)
    await message.answer(f'Я умею кидать кости и показывать картинки. Остальному мы обучаемся и пробуем новое)')

#Хэндлер на команду /admin
@router.message(Command('admin')) #ENG
@router.message(Command('админ')) #RUS
async def cmd_admin (message: types.Message):
    name = message.chat.first_name
    await message.answer(f'Мой разработчик только начинает разбираться, как я работаю. Если я сломаюсь o_0, напишите об это ему в личные сообщения, {name}', reply_markup=kb_eng2)

#Хэндлер на команду /game_cube
@router.message(Command('game')) #ENG
@router.message(Command('игра')) #RUS
@router.message(Command('играть'))
async def cmd_game (message: types.Message):
    await message.answer_dice(emoji="🎲", reply_markup=kb_eng2)

#Хэндлер на команду /fox
@router.message(Command('fox'))
@router.message(Command('лиса'))
@router.message(F.text.lower() == 'покажи лису')
async def cmd_fox (message: types.Message):
    name = message.chat.first_name
    img_fox = fox()
 #   await message.answer(f'Держи лису, {name}', reply_markup=kb1)
   # await message.answer_photo(photo = img_fox)
  #  await bot.send_photo(message.from_user.id, photo = img_fox)

#Хэндлер на команду /stop
@router.message(Command('stop'))
@router.message(Command('стоп'))
async def cmd_stop (message: types.Message):
    name = message.chat.first_name
    await message.answer(f'До новых встреч!')
    await message.answer(f'{name}, для продолжения работы нажми /start', reply_markup=kb_eng1)


#Хендлер на сообщения

#@dp.message(F.text)
#async def msg_echo(message: types.Message):
#    msg_user = message.text
#    await message.answer(f'Ты написал - {msg_user}')

@router.message(F.text)
async def msg_echo(message: types.Message):
    msg_user = message.text.lower()
    name = message.chat.first_name
    if 'привет' in msg_user:
        await message.answer(f'Приветствую Вас, {name}!', reply_markup=kb_eng2)
    elif 'здорово' in msg_user:
        await message.answer(f'Приветствую Вас, {name}!', reply_markup=kb_eng2)
    elif 'пока' == msg_user:
        await message.answer(f'Пока-пока, {name}', reply_markup=kb_eng2)
    elif 'до свидания' == msg_user:
        await message.answer(f'Хорошего Вам отдыха!, {name}', reply_markup=kb_eng2)
    elif 'лиса' in msg_user:
        await message.answer(f'Смотри что у меня есть  - {name}', reply_markup=kb2)
    else:
        await message.answer(f'Я не знаю такого слова')
