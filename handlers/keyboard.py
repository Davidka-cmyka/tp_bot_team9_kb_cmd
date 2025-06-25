from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

# Подстрочная клавиатура
main_keyboard_list = [
        [KeyboardButton(text="Статус"), ]
]

main_keyboard = ReplyKeyboardMarkup(keyboard=main_keyboard_list, resize_keyboard=True, one_time_keyboard=True)

start_keyboard_list = [
        [KeyboardButton(text="Преподаватель", callback_data="button_tutor"), KeyboardButton(text="Слушатель", callback_data="button_student")]
]

start_keyboard = ReplyKeyboardMarkup(keyboard=start_keyboard_list, resize_keyboard=True,one_time_keyboard=True)
