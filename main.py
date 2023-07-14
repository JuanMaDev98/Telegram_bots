import telebot
from token_api import token

chat_id = 1166287745
bot = telebot.TeleBot(token)  # Crea un nuevo bot usando el API_KEY que nos dio @bot_father


@bot.message_handler(commands=["start"])  # el decorador message.handler escucha al comando dado como parametro y reacciona ejecutando la funcion de debajo
def start(message):
    # reply_to es simplemente el comando para responder a cierta acción
    # en este caso responde a message que es el parámetro pasado por el decorador
    bot.reply_to(message, "Buenas, soy un bot encargado de reenviar tus escritos creativos al admin del grupo sin revelar tu identidad, simplemente envíalo en un documento (en cualquier formato) y yo me encargo del resto")


@bot.message_handler(content_types=["document"])  # Ahora uso el message_handler para verificar si el usuario manda un documento
def forward_doc(message):
    file_info = bot.get_file(message.document.file_id)  # Obtiene información básica sobre el archivo y lo prepara para descarga
    downloaded_file = bot.download_file(file_info.file_path)  # Obtengo el path del documento en los servidores de Telegram
    file_name = message.document.file_name  # Obtengo el nombre original del documento
    try:
        bot.send_document(chat_id, downloaded_file, visible_file_name=file_name)  # Envio el documento al chat predefinido con su nombre original
        bot.reply_to(message, f"Tu escrito <{file_name}> ha sido enviado con éxito al admin del grupo")
    except:  # Except solo porque YOLO, no hagan esto en casa chicos
        bot.reply_to(message, f"Tu escrito <{file_name}> ha fallado en su envío, por favor trata de nuevo mas tarde")


if __name__ == "__main__":
    bot.polling()
