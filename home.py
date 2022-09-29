import requests


def weather(city, appid, wes):
      res = requests.get("http://api.openweathermap.org/data/2.5/{}".format(wes),
                         params={'q': city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
      data = res.json()
      print('Прогноз погоды на сегодня:', "\nПогодные условия:", data['weather'][0]['description'],
            '\nТемпература:', data['main']['temp'],
            '\nМинимальная температура', data['main']['temp_min'],
            '\nМаксимальная температура:', data['main']['temp_max'],
            '\nСкорость ветра:', data['wind']['speed'],
            '\nВидимость:', str(data['visibility']) + 'м')


def forecast(city, appid, wes):
      res = requests.get("http://api.openweathermap.org/data/2.5/{}".format(wes),
                         params={'q': city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
      data = res.json()
      print(data)
      for i in data['list']:
            print("Дата <", i['dt_txt'], ">\nТемпература <", '{0:+3.0f} >'.format(i['main']['temp']),
                  "\nПогодные условия <", i['weather'][0]['description'], ">",
                  '\nСкорость ветра: <', i['wind']['speed'], '>',
                  '\nВидимость: <', str(i['visibility']) + 'м', '>')
            print("------------------------------")


city = "Moscow,RU"
appid = "57aa997149b0db17f5e2a70a573bb50f"
wes = str(input('Введите "day", чтобы узнать прогноз погоды в данный момент, либо введите "week", чтобы усзнать'
                'прогноз погоды на неделю, либо "exit",чтобы выйти: '))
while wes != 'exit':
      if wes == 'day':
            weather(city, appid, 'weather')
      if wes == 'week':
            forecast(city, appid, 'forecast')
      wes = str(input('Введите "day", чтобы узнать прогноз погоды в данный момент, либо введите "week", чтобы усзнать'
                'прогноз погоды на неделю, либо "exit",чтобы выйти: '))

