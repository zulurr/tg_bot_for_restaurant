from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, URLInputFile
from keyboard import keyboard_start, keyboard_category
from api_restaurant import menu

START = 'Добро пожаловать, Вас приветствует бот ресторана Istanbul!'
CATEGORY = 'Выберите категорию'

router = Router()
@router.message(CommandStart())
async def start(message: Message):
    await message.answer(START, reply_markup=keyboard_start)

@router.message(F.text == ' menu')
async def menu_list(message: Message):
    for item in menu.get_data(menu.url_menu):
        image = URLInputFile(item['image'])
        await message.answer_photo(photo=image,
                                   caption= f'<b>{item['dish_name']}</b>\n\n'
                                            f'Цена блюда: <i>{item['price']}</i>\n\n'
                                            f'Описание блюда: <i>{item['dish_description']}</i>',
                                            parse_mode='HTML'
                                   )

@router.message(F.text == 'Меню')
async def category(message: Message):
    await message.answer(CATEGORY, reply_markup=keyboard_category)


@router.message(F.text == 'Завтраки')
async def breakfasts(message: Message):
    for item in menu.get_data(menu.url_breakfasts):
        image = URLInputFile(item['image'])
        await message.answer_photo(photo=image,
                                   caption= f'<b>{item['dish_name']}</b>\n\n'
                                            f'Цена блюда: <i>{item['price']}</i>\n\n'
                                            f'Описание блюда: <i>{item['dish_description']}</i>',
                                   parse_mode='HTML',
                                   reply_markup=keyboard_start
                                   )


@router.message(F.text == 'Супы')
async def soups(message: Message):
    for item in menu.get_data(menu.url_soups):
        image = URLInputFile(item['image'])
        await message.answer_photo(photo=image,
                                   caption= f'<b>{item['dish_name']}</b>\n\n'
                                            f'Цена блюда: <i>{item['price']}</i>\n\n'
                                            f'Описание блюда: <i>{item['dish_description']}</i>',
                                            parse_mode='HTML'
                                   )


@router.message(F.text == 'Напитки')
async def beverages(message: Message):
    for item in menu.get_data(menu.url_beverages):
        image = URLInputFile(item['image'])
        await message.answer_photo(photo=image,
                                   caption= f'<b>{item['dish_name']}</b>\n\n'
                                            f'Цена блюда: <i>{item['price']}</i>\n\n'
                                            f'Описание блюда: <i>{item['dish_description']}</i>',
                                            parse_mode='HTML'
                                   )




@router.message(F.text == 'Десерты')
async def desserts(message: Message):
    for item in menu.get_data(menu.url_desserts):
        image = URLInputFile(item['image'])
        await message.answer_photo(photo=image,
                                   caption= f'<b>{item['dish_name']}</b>\n\n'
                                            f'Цена блюда: <i>{item['price']}</i>\n\n'
                                            f'Описание блюда: <i>{item['dish_description']}</i>',
                                            parse_mode='HTML'
                                   )

@router.message(F.text == 'Холодные закуски')
async def starters(message: Message):
    for item in menu.get_data(menu.url_starters):
        image = URLInputFile(item['image'])
        await message.answer_photo(photo=image,
                                    caption=f'<b>{item['dish_name']}</b>\n\n'
                                               f'Цена блюда: <i>{item['price']}</i>\n\n'
                                               f'Описание блюда: <i>{item['dish_description']}</i>',
                                       parse_mode='HTML'
                                       )


@router.message(F.text == 'Горячие блюда')
async def main_courses(message: Message):
    for item in menu.get_data(menu.url_main_courses):
        image = URLInputFile(item['image'])
        await message.answer_photo(photo=image,
                                    caption=f'<b>{item['dish_name']}</b>\n\n'
                                               f'Цена блюда: <i>{item['price']}</i>\n\n'
                                               f'Описание блюда: <i>{item['dish_description']}</i>',
                                       parse_mode='HTML'
                                       )