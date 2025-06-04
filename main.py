from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
import os


#TODO ловить ошибку в блоке с чтением файла токина

f = open('.//gitignor//tok.txt', 'r')
BOT_TOKEN = f.read()
f.close()

# Создаём объекты бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Этот хэндлер будет срабатывать на кнопку "/start"
@dp.message(Command(commands=["start"]))
async def process_start_command(message: Message):
    await message.answer(
        'Привет! '
        'Меня зовут Эхо-бот!'
    )

# Этот хендлер будет срабатывать на команду "/help"
@dp.message(Command(commands=['help']))
async def process_help_command(message: Message):
    await message.answer(
        'Напиши мне что-нибудь в ответ '
        'я пришлю тебе твоё сообщение'
    )

# Этот хендлер будет срабатывать на любые ваши текстовые сообщения,
# кроме команд "/start" "/help"
@dp.message()
async def send_echo(message: Message):
    await message.reply(text=message.text)

if __name__ == '__main__':
    dp.run_polling(bot)