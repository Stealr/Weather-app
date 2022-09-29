import requests


def weather(city, appid, wes):
    res = requests.get("http://api.openweathermap.org/data/2.5/{}".format(wes),
                       params={'q': city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
    data = res.json()
    print('Прогноз погоды на сегодня:', "\nПогодные условия:", data['weather'][0]['description'],
          '\nТемпература:', data['main']['temp'],
          '\nМинимальная температура:', data['main']['temp_min'],
          '\nМаксимальная температура:', data['main']['temp_max'],
          '\nСкорость ветра:', data['wind']['speed'],
          '\nВидимость:', str(data['visibility']) + 'м')


def forecast(city, appid, wes):
    res = requests.get("http://api.openweathermap.org/data/2.5/{}".format(wes),
                       params={'q': city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
    data = res.json()
    day = data['list'][0]['dt_txt'][8:10]  # Число сегоднешнего дня
    print('<', data['list'][0]['dt_txt'], '>')  # Выводит сегодняшнюю дату
    for i in data['list']:
        day2 = i['dt_txt'][8:10]  # day2 запоминает числа последующий дней
        if day != day2:  # Если наступил следующий день, то завершаем(подчёркиваем) список на день
            print('+' * 45)
            print("=" * 45)
            print("Дата <", i['dt_txt'], ">\nТемпература <", '{0:+.0f} >'.format(i['main']['temp']),
                  "\nПогодные условия <", i['weather'][0]['description'], ">",
                  '\nСкорость ветра: <', i['wind']['speed'], '>',
                  '\nВидимость: <', str(i['visibility']) + 'м', '>')
            day = day2  # Теперь day запоминает число нового дня
            print("-" * 45)
        else:  # если день всё тот же, то просто выводится время
            print("Время <", i['dt_txt'][10:19], ">\nТемпература <", '{0:+.0f} >'.format(i['main']['temp']),
                  "\nПогодные условия <", i['weather'][0]['description'], ">",
                  '\nСкорость ветра: <', i['wind']['speed'], '>',
                  '\nВидимость: <', str(i['visibility']) + 'м', '>')
            print("-" * 45)


city = "Moscow,RU"
appid = "57aa997149b0db17f5e2a70a573bb50f"
wes = str(input('Введите "day", чтобы узнать прогноз погоды в данный момент, либо введите "week", чтобы усзнать'
                'прогноз погоды на неделю, либо "exit",чтобы выйти: '))
while wes != 'exit':
    if wes == 'day':  # Прогноз погоды на данный момент
        weather(city, appid, 'weather')
    if wes == 'week':  # Прогноз погоды на неделю
        forecast(city, appid, 'forecast')
    wes = str(input('\nВведите "day", чтобы узнать прогноз погоды в данный момент, либо введите "week", чтобы усзнать'
                    'прогноз погоды на неделю, либо "exit",чтобы выйти: '))
