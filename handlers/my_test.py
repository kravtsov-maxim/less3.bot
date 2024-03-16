from aiogram import types, F, Router
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from less3.keyboards.prof_keyboards import make_row_keyboard


router = Router()


years = ["<18", "18-25", "25-50", ">50"]
day = ["ПН", "ВТ", "СР", "ЧТ", "ПТ", "СБ", "ВС"]
hairstyle_man = ["Полубокс", "Канадка", "Кроп"]



class ChoiceHairstyle(StatesGroup):
    choice_years = State()
    choice_day = State()
    choice_hair_man = State()




#Хэндлер на команду /hair
@router.message(Command('hair'))
async def cmd_hair (message: types.Message, state: FSMContext):
    name = message.chat.full_name
    await message.answer(f'Привет, {name}! Выбери свой возраст', reply_markup=make_row_keyboard(years))
    await state.set_state(ChoiceHairstyle.choice_years)

@router.message(ChoiceHairstyle.choice_years, F.text.in_(years))
async def years_chosen (message: types.Message, state: FSMContext):
    await state.update_data(chosen_years=message.text.lower())
    await message.answer(
        f'Спасибо, теперь выбери удобный для тебя день.',
        reply_markup=make_row_keyboard(day)
    )
    await state.set_state(ChoiceHairstyle.choice_day)

@router.message(ChoiceHairstyle.choice_day, F.text.in_(day))
async def day_chosen (message: types.Message, state: FSMContext):
    await state.update_data(chosen_day=message.text.lower())
    await message.answer(
        f'Спасибо, теперь выбери стрижку.',
        reply_markup=make_row_keyboard(hairstyle_man)
    )
    await state.set_state(ChoiceHairstyle.choice_hair_man)

@router.message(ChoiceHairstyle.choice_hair_man, F.text.in_(hairstyle_man))
async def hair_man_chosen (message: types.Message, state: FSMContext):
    user_info = await state.get_data()
    await message.answer(f'Вам {user_info.get('chosen_years')}. Ваше запись состоится в {user_info.get('chosen_day')}. Вы выбрали стиль стрижки - {message.text.lower()}.', reply_markup=types.ReplyKeyboardRemove())

@router.message(ChoiceHairstyle.choice_years)
async def years_choice (message: types.Message):
    first_name = message.chat.first_name
    await message.answer(
        f'{first_name}, я не знаю такого возраста. Выберите из списка.',
        reply_markup=make_row_keyboard(years)
    )

@router.message(ChoiceHairstyle.choice_day)
async def day_choice (message: types.Message):
    first_name = message.chat.first_name
    await message.answer(
        f'{first_name}, я не знаю дня недели. Выберите из списка.',
        reply_markup=make_row_keyboard(day)
    )

@router.message(ChoiceHairstyle.choice_hair_man)
async def hair_man_choice (message: types.Message):
    first_name = message.chat.first_name
    await message.answer(
        f'{first_name}, я не знаю такой стрижки. Выберите из списка.',
        reply_markup=make_row_keyboard(hairstyle_man)
    )