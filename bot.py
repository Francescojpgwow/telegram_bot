import asyncio
from telegram import Update
from telegram.ext import Application, MessageHandler, filters

# Inserisci il tuo token qui
TOKEN = "8114814914:AAEfI5Ea0-MnuSQq0d9qwGQPmH7hlW0aXyU"

async def risposta_automatica(update: Update, context):
    """Risponde automaticamente a ogni messaggio privato con il nome dell'utente"""
    nome_utente = update.message.from_user.first_name  
    messaggio_risposta = f"Messaggio ricevuto ✅️ {nome_utente}, ti risponderò al più presto!"
    await update.message.reply_text(messaggio_risposta)

async def main():
    """Avvia il bot"""
    app = Application.builder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, risposta_automatica))
    
    print("Bot avviato...")
    await app.run_polling()

# Avvia il bot senza problemi di event loop
if __name__ == "__main__":
    try:
        asyncio.run(main())
    except RuntimeError:
        loop = asyncio.get_event_loop()
        loop.run_until_complete(main())
