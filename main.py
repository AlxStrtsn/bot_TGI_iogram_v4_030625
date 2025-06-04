from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
import os

from pyexpat.errors import messages

#TODO ловить ошибку в блоке с чтением файла токина
#TODO пропускать только текст
#TODO файл с логами


f = open('.//gitignor//tok.txt', 'r')
BOT_TOKEN = f.read()
f.close()

# Создаём объекты бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Этот хэндлер будет срабатывать на кнопку "/start"
async def process_start_command(message: Message):
    await message.answer(f'Здравствуйте, {message.chat.first_name} ({message.chat.username})!')

# Этот хендлер будет срабатывать на команду "/help"
async def process_help_command(message: Message):
    await message.answer(
        'Напиши мне что-нибудь в ответ '
        'я пришлю тебе твоё сообщение'
    )

# Этот хендлер будет срабатывать на любые текстовые сообщения,
# кроме команд "/start" "/help"
async def send_echo(message: Message):
    await message.reply(text=message.text)

# Регистрация хендлеров
dp.message.register(process_start_command, Command(commands='start'))
dp.message.register(process_help_command, Command(commands='help'))
dp.message.register(send_echo)

if __name__ == '__main__':
    dp.run_polling(bot)