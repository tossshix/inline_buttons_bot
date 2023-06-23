from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from config import load_config, Config
from aiogram.utils.keyboard import InlineKeyboardBuilder

config: Config = load_config('.env')
API_TOKEN: str = config.tg_bot.token

bot: Bot = Bot(API_TOKEN)
dp: Dispatcher = Dispatcher()

LEXICON: dict[str, str] = {
    'but_1': 'Кнопка 1',
    'but_2': 'Кнопка 2',
    'but_3': 'Кнопка 3',
    'but_4': 'Кнопка 4',
    'but_5': 'Кнопка 5',
    'but_6': 'Кнопка 6',
    'but_7': 'Кнопка 7',}

BUTTONS: dict[str, str] = {
    'btn_1': '1',
    'btn_2': '2',
    'btn_3': '3',
    'btn_4': '4',
    'btn_5': '5',
    'btn_6': '6',
    'btn_7': '7',
    'btn_8': '8',
    'btn_9': '9',
    'btn_10': '10',
    'btn_11': '11'}


def create_inline_kb(width: int,
                     *args: str,
                     **kwargs: str) -> InlineKeyboardMarkup:
    kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
    buttons: list[InlineKeyboardButton] = []

    if args:
        for button in args:
            buttons.append(InlineKeyboardButton(text=LEXICON[button] if button in LEXICON else button,
                                                callback_data=button))
    if kwargs:
        for button, text in kwargs.items():
            buttons.append(InlineKeyboardButton(text=text,
                                                callback_data=button))
    kb_builder.row(*buttons, width=width)
    return kb_builder.as_markup()


@dp.message(CommandStart())
async def process_start_command(message: Message):
    keyboard = create_inline_kb(2,
                                btn_tel='Телефон',
                                btn_email='email',
                                btn_website='Web-сайт',
                                btn_vk='VK',
                                btn_tgbot='Наш телеграм-бот')
    await message.answer(text='Вот клава кока)', reply_markup=keyboard)


if __name__ == '__main__':
    dp.run_polling(bot)

