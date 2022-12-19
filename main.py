import logging
import wikipedia
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = 'BOTINGIZNING API TOKENI'

wikipedia.set_lang("uz")

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("WikiBot'ga xush kelibsiz!")
    

@dp.message_handler(commands=['help'])
async def send_help(message: types.Message):
    await message.reply("Dasturchi: @MrZafarov")


@dp.message_handler()
async def sendWiki(message: types.Message):
    try:
        javob = wikipedia.summary(message.text)
        await message.answer(javob)
    except:
        await message.answer('Bu mavzuga oid maqola topilmadi!')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
