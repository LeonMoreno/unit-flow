from src import utils
from src import conversions

def enviar_saludo(mensaje, bot):
    bot.reply_to(mensaje, f"Hola! SOy miPrimer Bot tu id = {mensaje.from_user.id}")

def get_msg_and_process(menssage, bot):
    text = menssage.text
    to_convert = utils.start_parser(text)
    # data = conversions.start_conversion(to_convert)
    bot.reply_to(menssage, f"to_convert = {to_convert}")

# @bot.message_handler(commands=['start', 'ole'])
def register_handlers(bot):
    bot.register_message_handler(
        lambda m: enviar_saludo(m, bot), 
        commands=['start', 'ole']
    )
    bot.register_message_handler(
        lambda m: get_msg_and_process(m, bot),
        content_types=['text']
    )