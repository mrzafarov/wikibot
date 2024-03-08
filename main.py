import wikipedia
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '6764781769:AAE6g4k5TXpmrDn24P2LNsz6R7sr8zM5Zqw'

wikipedia.set_lang("uz")

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
        answer = wikipedia.summary(message.text)
        await message.answer(answer)
    except:
        await message.answer("Bu mavzuga oid maqola topilmadi!")


executor.start_polling(dp, skip_updates=True)
