import requests


def weather(city, appid):
      res = requests.get("http://api.openweathermap.org/data/2.5/weather",  # forecast если нужен прогноз погоды на неделю. Попробовать добавить format
                         params={'q': city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})  # weather на день           Выбор между на неделю и на день
      data = res.json()
      print('Прогноз погоды на сегодня:', "\nПогодные условия:", data['weather'][0]['description'],
            '\nТемпература:', data['main']['temp'],
            '\nМинимальная температура', data['main']['temp_min'],
            '\nМаксимальная температура:', data['main']['temp_max'],
            '\nСкорость ветра:', data['wind']['speed'],
            '\nВидимость:', str(data['visibility']) + 'м')


def forecast(city, appid):
      res = requests.get("http://api.openweathermap.org/data/2.5/forecast",
                         params={'q': city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
      data = res.json()
      for i in data['list']:
            print("Дата<", i['dt_txt'], ">\r\nТемпература<", '{0:+3.0f}'.format(i['main']['temp']),
                  "\r\nПогодные условия<", i['weather'][0]['description'], ">",
                  '\nСкорость ветра: <', i['wind']['speed'], '>',
                  '\nВидимость: <', str(i['visibility']) + 'м', '>')
            print("------------------------------")


city = "Moscow,RU"
appid = "57aa997149b0db17f5e2a70a573bb50f"
forecast(city, appid)



