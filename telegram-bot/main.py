import os
import typing

import requests
import telegram
import telegram.ext


async def text_message_handler(update: telegram.Update, context: telegram.ext.ContextTypes.DEFAULT_TYPE) -> int:

    assert update.message

    response = requests.request(method="POST", url="http://ollama:11434/api/generate", json={"model": "mistral", "prompt": update.message.text, "stream": False})
    answer = response.json().get("response", "Oops: no response available!")
    await update.message.reply_text(answer)

    return telegram.ext.ConversationHandler.END


def main() -> None:

    TELEGRAM_API_TOKEN: typing.Final[str] | None = os.getenv("TELEGRAM_API_TOKEN")

    if not TELEGRAM_API_TOKEN: raise RuntimeError("Could not found environment variable for TELEGRAM_API_TOKEN")

    application = telegram.ext.Application.builder().token(TELEGRAM_API_TOKEN).concurrent_updates(True).read_timeout(30).write_timeout(30).build()
    application.add_handler(telegram.ext.MessageHandler(telegram.ext.filters.TEXT, text_message_handler))
    application.run_polling()


if __name__ == "__main__":
    main()
