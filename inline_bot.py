from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from config import load_config, Config

config: Config = load_config('.env')
API_TOKEN: str = config.tg_bot.token

bot: Bot = Bot(API_TOKEN)
dp: Dispatcher = Dispatcher()

url_button_1: InlineKeyboardButton = InlineKeyboardButton(text='Курс телеграмм боты на Python и AIOgram',
                                                          url='https://stepik.org/120924')
url_button_2: InlineKeyboardButton = InlineKeyboardButton(text='Документация Telegram Bot API',
                                                          url='https://core.telegram.org/bots/api')

keyboard: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[[url_button_1],
                     [url_button_2]])


@dp.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text='Это инлайн-кнопки с параметром url', reply_markup=keyboard)

if __name__ == '__main__':
    dp.run_polling(bot)