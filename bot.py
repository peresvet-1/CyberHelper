import logging, os
from telegram.ext import Application, CommandHandler
from handlers import start, hash_command, encode_command, decode_command, whois_command, dns_command, headers_command, port_command, help_command
logging.basicConfig(
    filename='bot.log',
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

TOKEN = os.getenv('BOT_TOKEN')
if not TOKEN:
    raise RuntimeError('Переменная BOT_TOKEN не установлена')
app = Application.builder().token(TOKEN).build()

async def error_handler(update, context):
    print(f'Ошибка: {context.error}')
    logging.error(context.error)
    if update and update.message:
        await update.message.reply_text('Произошла внутренняя ошибка. Попробуй еще раз')

app.add_error_handler(error_handler)
app.add_handler(CommandHandler('start', start))
app.add_handler(CommandHandler('hash', hash_command))
app.add_handler(CommandHandler('encode', encode_command))
app.add_handler(CommandHandler('decode', decode_command))
app.add_handler(CommandHandler('whois', whois_command))
app.add_handler(CommandHandler('dns', dns_command))
app.add_handler(CommandHandler('headers', headers_command))
app.add_handler(CommandHandler('port', port_command))
app.add_handler(CommandHandler('help', help_command))

app.run_polling()
