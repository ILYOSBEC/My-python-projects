
import telebot
from eng_uz_words import translate_word

TOKEN = "7980821300:AAHnxrPWKk02Y66CbArnBNHHbcEfYUE-mHk"
bot = telebot.TeleBot(TOKEN, parse_mode=None)


@bot.message_handler(commands=["start"])
def start(message):
    text = (
        "👋 Assalomu alaykum!\n"
        "🇬🇧 Inglizcha yoki 🇺🇿 o‘zbekcha so‘z yozing — men tarjima qilib beraman!\n"
    )
    bot.send_message(message.chat.id, text)


@bot.message_handler(func=lambda message: True)
def echo(message):
    msg = message.text.lower()
    sozlar = msg.split()  
    
    tarjima = [translate_word(soz) for soz in sozlar]

    javob = " ".join(tarjima)
    bot.reply_to(message, javob)


bot.polling()
