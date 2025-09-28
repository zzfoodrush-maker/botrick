import telebot

BOT_TOKEN = "8400858750:AAHpl1agw_n6abJAl77R9MUh9nuCDOH9K3M"
bot = telebot.TeleBot(BOT_TOKEN)

DEMO_URL = "https://www.google.com"  # Remplace par le lien que tu veux envoyer

welcome_text = (
    "Salut ! Ceci est une démo.\n\n"
    "Cliquez sur le bouton ci-dessous pour ouvrir le lien :"
)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton("Ouvrir le lien", url=DEMO_URL))
    bot.send_message(message.chat.id, welcome_text, reply_markup=markup)

if __name__ == "__main__":
    print("Bot en mode polling")
    bot.infinity_polling()
