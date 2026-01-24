#TODO
# 1 - Recibe el mensaje: "100 c to f"
# 2- Llama al Parser: El parser hace el split y te devuelve: {'valor': 100, 'origen': 'c', 'destino': 'f'}.
# 3- Busca la Categoría: El bot mira en su diccionario y dice: -- Veo que 'c' es temperatura --.
# 4 - Ejecutar: Llamar función temperatura en logic.py.
# 5 -- Responde: Envía el resultado al usuario.

from src import handlers

import os
import telebot
import logging
from dotenv import load_dotenv

load_dotenv()

# Configuración básica
logging.basicConfig(
    level=logging.INFO, # Establece el nivel mínimo (DEBUG, INFO, WARNING, ERROR, CRITICAL) [2, 5]
    format='%(asctime)s - %(levelname)s - %(message)s', # Formato: Fecha - Nivel - Mensaje [6]
    datefmt='%Y-%m-%d %H:%M:%S', # Formato de fecha personalizado [6]
    filename='app.log', # Nombre del archivo para guardar los logs [2]
    filemode='a' # 'w' para sobrescribir cada vez, 'a' para añadir [3]
)

TOKEN = os.environ.get('MY_TOKEN')

def start_bot():
    return telebot.TeleBot(TOKEN)

def main():
    logging.info("El programa ha iniciado")
    # bot = start_bot()
    # handlers.register_handlers(bot)
    # bot.infinity_polling(
    #     restart_on_change=False,
    #     timeout=10,
    #     logger_level=logging.ERROR
    # )
    print(TOKEN)

if __name__ == "__main__":
    main()