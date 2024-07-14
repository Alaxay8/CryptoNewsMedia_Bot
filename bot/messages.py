from telegram import Bot

async def send_text_message(bot: Bot, chat_id: str, text: str) -> None:
    await bot.send_message(chat_id=chat_id, text=text)

# файл: bot/translator.py
from translate import Translator

translator = Translator(to_lang="ru")

def translate_to_russian(text):
    translation = translator.translate(text)
    return translation
