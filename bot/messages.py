from telegram import Message

async def send_text_message(message: Message, text: str) -> None:
    await message.reply_text(text)
