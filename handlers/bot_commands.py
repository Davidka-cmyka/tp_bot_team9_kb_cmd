from aiogram.types import BotCommand, BotCommandScopeDefault

async def set_commands(bot):
    commands = [
        BotCommand(command='start', description='Приветствие и справка '),
        BotCommand(command='status', description='Информация о пользователе'),
        BotCommand(command='help', description='Справка'),
        BotCommand(command='today', description='Текущие курсы ключевых валют'),
        BotCommand(command='subscribe', description='Включение ежедневную рассылку'),
        BotCommand(command='unsubscribe', description='Выключение рассылки'),


                ]
    await bot.set_my_commands(commands, BotCommandScopeDefault())
