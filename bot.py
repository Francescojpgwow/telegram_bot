import asyncio
import os
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, CallbackContext

async def auto_reply(update: Update, context: CallbackContext) -> None:
    """Risponde automaticamente a tutti i messaggi privati."""
    if update.message and update.message.chat.type == "private":
        username = update.message.from_user.first_name  # Ottiene il nome dell'utente
        response_text = f"Messaggio ricevuto ✅️ {username}, ti risponderò al più presto!"
        await update.message.reply_text(response_text)

async def main():
    """Crea l'istanza dell'applicazione Telegram e avvia il bot."""
    TOKEN = os.getenv("8114814914:AAEfI5Ea0-MnuSQq0d9qwGQPmH7hlW0aXyU")  # Recupera il token dalla variabile d'ambiente su Railway
    app = ApplicationBuilder().token(TOKEN).build()

    # Aggiunge un handler per tutti i messaggi privati
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, auto_reply))

    print("Bot avviato e in ascolto...")
    await app.run_polling()

if __name__ == "__main__":
    loop = asyncio.new_event_loop()  # Crea un nuovo event loop (evita il conflitto)
    asyncio.set_event_loop(loop)
    loop.run_until_complete(main())  # Avvia il bot
