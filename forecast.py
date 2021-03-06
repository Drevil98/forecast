import pyowm
import telebot

Api = 'dfebe434fadd98d87243be49ce4d192a'
TOKEN = "784391239:AAGv46dDbwLRsmrTnD0lXXMWqdPS9McwVpg"

owm = pyowm.OWM('dfebe434fadd98d87243be49ce4d192a', language = "ru")
bot = telebot.TeleBot("784391239:AAGv46dDbwLRsmrTnD0lXXMWqdPS9McwVpg")

@bot.message_handler(content_types=['text'])
def send_echo(message):
    try:
        observation = owm.weather_at_place(message.text)
    except:
        observation = owm.weather_at_place('Moscow')
    w = observation.get_weather()
    temp = w.get_temperature('celsius')['temp']
    tempR = round(temp)
    windSP = w.get_wind()['speed']
    windLN = w.get_wind()['deg']
    windLNR = round(int(windLN))
    windSPR = round(int(windSP))
    LN = 'N'
    a = 'a'
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
    elif int(windLN) == 180:
        LN = 'северный'
    elif int(windLN) == 270:
        LN = 'восточный'
    elif int(windLN) == 0 or int(windLN) == 360:
        LN = 'южный'
    elif int(windLN) == 90:
        LN = 'западный'
    # Text forecast:    
    if tempR < 10:
        a = 'На улице очень холодно, надевай всё что есть! =0'
    elif tempR < 20:
        a = 'На улице прохладно, одевайся теплее. ;)'
    else:
        a = 'Снаружи тепло, надевай что хочешь. =)'
    answer = ('На улице ' + statusD + ', Температура: ' + str(tempR) + '°C , ветер ' + LN + ', ' + str(windLNR) + '° , ' + str(windSPR) + ' м/сек' '\n' + a)
    bot.send_message(message.chat.id, answer)
bot.polling(none_stop = True)
