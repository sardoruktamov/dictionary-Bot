import logging
from aiogram import Bot, Dispatcher, executor, types

from oxfordlookup import getDefinitions
from googletrans import Translator
translator = Translator()

API_TOKEN = '2128796946:AAEzQfTV4Y05Lyif-dh8dAbulygtIHOwagc'


logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Uzbek-English tarjimon botiga hush kelibsiz")

@dp.message_handler(commands=['help'])
async def help_welcome(message: types.Message):
    await message.reply("Uzbek-English tarjimon boti orqali hohlagan so`zingizni tarjima qilib izhlarini ham topib beradi")

@dp.message_handler()
async def tarjimon(message: types.Message):
    lang = translator.detect(message.text).lang
    if len(message.text.split()) > 2:
        dest = 'uz' if lang == 'en' else 'en'
        await message.reply(translator.translate(message.text, dest).text)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)