import logging
import wikipedia

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '5292323375:AAE_zojJFhhA7zXhMor60_elHrqhmBfk9No'
wikipedia.set_lang('uz')


logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):

    await message.reply("Assalomu alaykum Wikipedia Botga xush kelibsiz!")



@dp.message_handler()
async def senWiki(message: types.Message):
    try:
        respond = wikipedia.summary(message.text)
        await message.answer(respond)
    except:
        await message.answer('Bnday maqola yoq')



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
