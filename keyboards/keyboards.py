from aiogram import types

button1 = types.KeyboardButton(text = '/start') #ENG
button2 = types.KeyboardButton(text = '/старт') #RUS
button3 = types.KeyboardButton(text = '/info') #ENG
button4 = types.KeyboardButton(text = '/инфо') #RUS
button5 = types.KeyboardButton(text = '/admin') #ENG
button6 = types.KeyboardButton(text = '/админ') #RUS
button7 = types.KeyboardButton(text = '/game') #ENG
button8 = types.KeyboardButton(text = '/играть') #RUS

button9 = types.KeyboardButton(text = '/stop') #ENG
button10 = types.KeyboardButton(text = '/стоп') #RUS


button11 = types.KeyboardButton(text = '/prof') #career_choice
button12 = types.KeyboardButton(text = '/hair') #my_test

button44 = types.KeyboardButton(text = 'Покажи лису')


keyboard_eng1 =[
    [button1],
]

keyboard_rus1 =[
    [button2],
]

keyboard_eng2 =[
    [button3], [button11], [button12],
    [button7], [button5],
    [button9],
]

keyboard_rus2 =[
    [button4],
    [button8],
    [button6],
    [button10],
]

kb_eng1 = types.ReplyKeyboardMarkup(keyboard=keyboard_eng1, resize_keyboard=True)
kb_rus1 = types.ReplyKeyboardMarkup(keyboard=keyboard_rus1, resize_keyboard=True)
kb_eng2 = types.ReplyKeyboardMarkup(keyboard=keyboard_eng2, resize_keyboard=True)
kb_rus2 = types.ReplyKeyboardMarkup(keyboard=keyboard_rus2, resize_keyboard=True)