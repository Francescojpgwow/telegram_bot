import asyncio
from telegram.ext import ApplicationBuilder

async def main():
    app = ApplicationBuilder().token("8114814914:AAEfI5Ea0-MnuSQq0d9qwGQPmH7hlW0aXyU").build()
    await app.run_polling()

if __name__ == "__main__":
    try:
        asyncio.run(main())  # Esegue l'event loop in modo sicuro
    except RuntimeError:
        loop = asyncio.get_event_loop()
        loop.create_task(main())  # Avvia il bot senza bloccare il loop
        loop.run_forever()  # Mantiene il bot in esecuzione
