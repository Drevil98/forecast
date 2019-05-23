import pyowm
import telebot

Api = 'dfebe434fadd98d87243be49ce4d192a'
TOKEN = "784391239:AAGv46dDbwLRsmrTnD0lXXMWqdPS9McwVpg"

owm = pyowm.OWM('dfebe434fadd98d87243be49ce4d192a', language = "ru")
bot = telebot.TeleBot("784391239:AAGv46dDbwLRsmrTnD0lXXMWqdPS9McwVpg")

@bot.message_handler(content_types=['text'])
def send_echo(message):
    observation = owm.weather_at_place(message.text)
    w = observation.get_weather()
    temp = w.get_temperature('celsius')['temp']
    tempR = round(temp)
    windSP = w.get_wind()['speed']
    windLN = w.get_wind()['deg']
    LN = 'N'
    statusD = w.get_detailed_status()
    # Wind direction:
    if int(windLN) > 0 and int(windLN) < 90:
        LN = 'юговосточный'
    elif int(windLN) > 90 and int(windLN) < 180:
        LN = 'северозападный'
    elif int(windLN) > 180 and int(windLN) < 270:
        LN = 'северовосточный'
    elif int(windLN) > 270 and int(windLN) < 360:
        LN = 'юговосточный'
    answer = (statusD + ', Температура: ' + str(tempR) + '°C , ветер ' + LN + ', ' + str(windLN) + '° , ' + str(windSP) + ' м/сек')
    #bot.reply_to(message, answer.text)
    bot.send_message(message.chat.id, answer)
bot.polling(none_stop = True)
