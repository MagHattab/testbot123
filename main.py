import telebot
from pyowm import OWM
from pyowm.utils.config import get_default_config

owm = OWM('72a1f31dc5df9b64e7f6138990faaf53')
mgr = owm.weather_manager()
config_dict = get_default_config()
config_dict['language'] = 'ru'
bot = telebot.TeleBot("1432598281:AAGvRH-XwBfNgdWnUpIEHA8kslQ5dibpatA", parse_mode=None)


@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(message.chat.id, 'Укажите город, чтобы узнать погоду')

@bot.message_handler(content_types=['text'])
def weather(message):
	observation = mgr.weather_at_place(message.text)
	w = observation.weather
	temp = round(w.temperature('celsius')["temp"])

	answer = "В городе  " + message.text + " сейчас " + w.detailed_status + "\n"
	answer += "Температура сейчас в райное " + str(temp) +" градусов по цельсию " + "\n\n"

	if temp <= -30:
		answer += "На улице очень холодно, старайтесь не выходить из дома"
	elif temp <= 0:
		answer += "На улице холодно, одевайтесь теплее"
	elif temp <= 15:
		answer += "На улице прохладно, одевайтесь теплее"
	else:
		answer += "На улице тепло, одевайтесь как удобно;)"

	bot.send_message(message.chat.id, answer)

bot.polling(none_stop = True)