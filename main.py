import requests

city = "Moscow,RU"
appid = "57aa997149b0db17f5e2a70a573bb50f"
res = requests.get("http://api.openweathermap.org/data/2.5/forecast",
                   params={'q': city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
data = res.json()

print(data)

print('Прогноз погоды на неделю:')
for i in data['list']:
    print("Дата<", i['dt_txt'], ">\r\nТемпература<", '{0:+3.0f}'.format(i['main']['temp']), "\r\nПогодные условия<",
          i['weather'][0]['description'], ">")
    print("------------------------------")
# print("Город", city)
# print("Погодные условия:", data['weather'][0]['description'])
# print("Температура:", data['main']['temp'])
# print("Минимальная температура:", data['main']['temp_min'])
# print("Максимальная температура:", data['main']['temp_max'])
