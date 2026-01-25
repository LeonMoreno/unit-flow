#TODO
# 1 - Recibe el mensaje: "100 c to f"
# 2- Llama al Parser: El parser hace el split y te devuelve: {'valor': 100, 'origen': 'c', 'destino': 'f'}.
# 3- Busca la Categoría: El bot mira en su diccionario y dice: -- Veo que 'c' es temperatura --.
# 4 - Ejecutar: Llamar función temperatura en logic.py.
# 5 -- Responde: Envía el resultado al usuario.

import os
import sys
import logging
import telebot
from dotenv import load_dotenv
from src import handlers

load_dotenv()
TOKEN = os.environ.get('MY_TOKEN')

# def setup_logging():
    # TODo

def start_bot():
    if not TOKEN:
        logging.error("NOt find Token")
        exit(1)
    return telebot.TeleBot(TOKEN)

def main():
    # setup_logging()

    bot = start_bot()
    handlers.register_handlers(bot)
    bot.infinity_polling(
        restart_on_change=False,
        timeout=10,
        # logger_level=logging.ERROR
    )
    # print(__name__)

if __name__ == "__main__":
    main()