import hashlib, whois, base64
from tools import get_dns, get_headers, check_port

async def start(update, context):
    await update.message.reply_text('Привет! Я CyberHelper — учебный бот для работы с инструментами кибербезопасности.')

async def hash_command(update, context):
    if not context.args:
        await update.message.reply_text('Напиши текст после /hash')
        return
    text = ' '.join(context.args)
    data = text.encode('utf-8')
    result = hashlib.sha256(data).hexdigest()
    await update.message.reply_text(result)

async def encode_command(update, context):
    if not context.args:
        await update.message.reply_text('Напиши текст после /encode')
        return
    text = ' '.join(context.args)
    result = base64.b64encode(text.encode('utf-8')).decode('utf-8')
    await update.message.reply_text(result)

async def decode_command(update, context):
    if not context.args:
        await update.message.reply_text('Напиши текст после /decode')
        return
    text = ' '.join(context.args)
    try:
        result = base64.b64decode(text).decode('utf-8')
        await update.message.reply_text(result)
    except Exception:
        await update.message.reply_text('Неверная строка base-64!')

async def whois_command(update, context):
    if not context.args:
        await update.message.reply_text('Напиши текст после /whois')
        return
    domain = ' '.join(context.args)
    try:
        result = whois.whois(domain)
        message =f'''
Домен: {result.domain_name}
Регистратор: {result.registrar}
Дата регистрации: {result.creation_date}
Дата окончания: {result.expiration_date}'''
        await update.message.reply_text(message)
    except Exception:
        await update.message.reply_text('Ошибка при получении WHOIS!')

async def dns_command(update, context):
    if not context.args:
        await update.message.reply_text('Напиши домен после /dns')
        return
    domain = ' '.join(context.args)
    ips = get_dns(domain)
    if not ips:
        await update.message.reply_text('Не удалось получить A-запись для этого домена.')
        return
    message = '\n'.join(ips)
    await update.message.reply_text(f'DNS-записи для {domain}:\n{message}')

async def headers_command(update, context):
    if not context.args:
        await update.message.reply_text('Напиши URL после /headers.')
        return
    url = context.args[0]
    headers = get_headers(url)
    if not headers:
        await update.message.reply_text('Не удалось получить Headers.')
        return
    message = ''
    for key, value in headers.items():
        message += f'{key}: {value}\n'
    await update.message.reply_text(message)

async def port_command(update, context):
    if len(context.args) < 2:
        await update.message.reply_text('Использование /port: <host> <port>')
        return
    host = context.args[0]
    try:
        port = int(context.args[1])
    except ValueError:
        await update.message.reply_text('Порт должен быть числом')
        return

    result = check_port(host, port)
    if result == 0:
        await update.message.reply_text(f'Порт {port} на {host} открыт')
    else:
        await update.message.reply_text(f'Порт {port} на {host} закрыт или недоступен')

async def help_command(update, context):
    message = '''CyberHelper
/start — запуск
/hash <text> — SHA-256
/encode <text> — Base64
/decode <base64> — декодирование Base64
/whois <domain> — WHOIS
/dns <domain> — A-запись DNS
/headers <url> — HTTP-заголовки
/port <host> <port> — проверка TCP-порта'''
    await update.message.reply_text(message)
