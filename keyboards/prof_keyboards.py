from aiogram import types

def make_row_keyboard(items: list[str]) -> types.ReplyKeyboardMarkup:
    row = [types.KeyboardButton(text=iten) for iten in items]
    return types.ReplyKeyboardMarkup(keyboard=[row],resize_keyboard=True)


