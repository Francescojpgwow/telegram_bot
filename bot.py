import asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, CallbackContext

# Messaggio di risposta automatica
RESPONSE_TEXT = "Ciao! Questo è un messaggio automatico."

async def auto_reply(update: Update, context: CallbackContext) -> None:
    """Risponde automaticamente a tutti i messaggi privati."""
    if update.message and update.message.chat.type == "private":
        await update.message.reply_text(RESPONSE_TEXT)

async def main():
    app = ApplicationBuilder().token("8114814914:AAEfI5Ea0-MnuSQq0d9qwGQPmH7hlW0aXyU").build()

    # Aggiunge un handler per tutti i messaggi privati
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, auto_reply))

    await app.run_polling()

if __name__ == "__main__":
    try:
        asyncio.run(main())  # Avvia il bot in modo sicuro
    except RuntimeError:
        loop = asyncio.get_event_loop()
        loop.create_task(main())  
        loop.run_forever()
