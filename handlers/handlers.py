__all__ = [

    'router'
]
# TODO - Опишите вызов функций обработчиков через маршрутизацию
# Работа c Router - https://docs.aiogram.dev/en/v3.14.0/dispatcher/router.html
# Пример работы с Router через декораторы @router - https://mastergroosha.github.io/aiogram-3-guide/routers/
# Пример работы с Router через функцию сборщик https://stackoverflow.com/questions/77809738/how-to-connect-a-router-in-aiogram-3-x-x#:~:text=1-,Answer,-Sorted%20by%3A

from aiogram import types, Router, F
from aiogram.filters import Command
from .keyboard import main_keyboard   # импорт из клавиатур



router = Router()

@router.message(Command("start"))
async def process_start_command(message: types.Message):
    await message.answer(text="Привет " + f"{message.from_user.username}")

@router.message(Command("help"))
async def process_help_command(message: types.Message):
    await message.answer(text=" Помощь с вопросами по командам нашего бота ", reply_markup= main_keyboard)

@router.message(F.text == 'Статус',)
@router.message(Command("status"))
async def process_status_command(message: types.Message):
     await message.answer(f"{message.from_user.id}, {message.from_user.username}")

@router.message(Command("today"))
async def process_today_command(message: types.Message):
    await message.answer(text="Текущие курсы ключевых валют")

@router.message(Command("subscribe"))
async def process_subscribe_command(message: types.Message):
    await message.answer(text="Включение ежедневную рассылку")

@router.message(Command("unsubscribe"))
async def process_unsubscribe_command(message: types.Message):
    await message.answer(text="Выключение рассылки")











# Здесь описывается маршрутизация
def register_message_handlers():
    '''Маршрутизация обработчиков'''
    pass