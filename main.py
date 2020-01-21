import requests
from bs4 import BeautifulSoup
import pandas as pd

# EUROPE
# LON weather
page_lon = requests.get('https://weather.com/en-IL/weather/today/l/7517a52d4d1815e639ae1001edb8c5fda2264ea579095b0f28f55c059599e074')
soup_lon = BeautifulSoup(page_lon.content, 'html.parser')
today_lon = soup_lon.find(class_="today_nowcard-container")
items_lon = today_lon.find_all(class_="today_nowcard-section")

city_name_lon = "LON"
description_lon = [item.find(class_='today_nowcard-phrase').get_text() for item in items_lon]


# CDG weather
page_cdg = requests.get('https://weather.com/en-GB/weather/today/l/1a8af5b9d8971c46dd5a52547f9221e22cd895d8d8639267a87df614d0912830')
soup_cdg = BeautifulSoup(page_cdg.content, 'html.parser')
today_cdg = soup_cdg.find(class_="today_nowcard-container")
items_cdg = today_cdg.find_all(class_="today_nowcard-section")

city_name_cdg = "CDG"
description_cdg = [item.find(class_='today_nowcard-phrase').get_text() for item in items_cdg]


# FRA weather
page_fra = requests.get('https://weather.com/en-GB/weather/today/l/6292322032974311cb4aa57100a300e5861c8a874ed11452686c5133294a3042')
soup_fra = BeautifulSoup(page_fra.content, 'html.parser')
today_fra = soup_fra.find(class_="today_nowcard-container")
items_fra = today_fra.find_all(class_="today_nowcard-section")

city_name_fra = "FRA"
description_fra = [item.find(class_='today_nowcard-phrase').get_text() for item in items_fra]


# FCO weather
page_fco = requests.get('https://weather.com/en-GB/weather/today/l/1d1a251383dc0d1bdbfb8efbc155374b376eff6f5232f36110b823e47362866e')
soup_fco = BeautifulSoup(page_fco.content, 'html.parser')
today_fco = soup_fco.find(class_="today_nowcard-container")
items_fco = today_fco.find_all(class_="today_nowcard-section")

city_name_fco = "FCO"
description_fco = [item.find(class_='today_nowcard-phrase').get_text() for item in items_fco]


# ZRH weather
page_zrh = requests.get('https://weather.com/en-GB/weather/today/l/151d93a8aa1a5fa8c93142a2499b472960ea57c494977eecdd6810dabed490df')
soup_zrh = BeautifulSoup(page_zrh.content, 'html.parser')
today_zrh = soup_zrh.find(class_="today_nowcard-container")
items_zrh = today_zrh.find_all(class_="today_nowcard-section")

city_name_zrh = "ZRH"
description_zrh = [item.find(class_='today_nowcard-phrase').get_text() for item in items_zrh]


# MAD weather
page_mad = requests.get('https://weather.com/en-GB/weather/today/l/66d93786ffcc98f9cd3bae34e03d05c3d4daa0178c2c4bffe4cfd354cda80400')
soup_mad = BeautifulSoup(page_mad.content, 'html.parser')
today_mad = soup_mad.find(class_="today_nowcard-container")
items_mad = today_mad.find_all(class_="today_nowcard-section")

city_name_mad = "MAD"
description_mad = [item.find(class_='today_nowcard-phrase').get_text() for item in items_mad]


# VIE weather
page_vie = requests.get('https://weather.com/en-GB/weather/today/l/b1c12cb5f559c61ffb70bb86034f904e94f0bf0817f3adc85177b27014c8fbe0')
soup_vie = BeautifulSoup(page_vie.content, 'html.parser')
today_vie = soup_vie.find(class_="today_nowcard-container")
items_vie = today_vie.find_all(class_="today_nowcard-section")

city_name_vie = "VIE"
description_vie = [item.find(class_='today_nowcard-phrase').get_text() for item in items_vie]


# AMS weather
page_ams = requests.get('https://weather.com/en-GB/weather/today/l/a0a48c0f8630d7e60cc5d03bf2dc2d039cad87e8dfdb8fc476a43473a6ff7e17')
soup_ams = BeautifulSoup(page_ams.content, 'html.parser')
today_ams = soup_ams.find(class_="today_nowcard-container")
items_ams = today_ams.find_all(class_="today_nowcard-section")

city_name_ams = "AMS"
description_ams = [item.find(class_='today_nowcard-phrase').get_text() for item in items_ams]


# IST weather
page_ist = requests.get('https://weather.com/en-GB/weather/today/l/33d1e415eb66f3e1ab35c3add45fccf4512715d329edbd91c806a6957e123b49')
soup_ist = BeautifulSoup(page_ist.content, 'html.parser')
today_ist = soup_ist.find(class_="today_nowcard-container")
items_ist = today_ist.find_all(class_="today_nowcard-section")

city_name_ist = "IST"
description_ist = [item.find(class_='today_nowcard-phrase').get_text() for item in items_ist]


# DME weather
page_dme = requests.get('https://weather.com/en-GB/weather/today/l/33d1e415eb66f3e1ab35c3add45fccf4512715d329edbd91c806a6957e123b49')
soup_dme = BeautifulSoup(page_dme.content, 'html.parser')
today_dme = soup_dme.find(class_="today_nowcard-container")
items_dme = today_dme.find_all(class_="today_nowcard-section")

city_name_dme = "DME"
description_dme = [item.find(class_='today_nowcard-phrase').get_text() for item in items_dme]


#INTs Database
city_name = city_name_lon, city_name_cdg, city_name_fra, city_name_fco, city_name_zrh, city_name_mad, city_name_vie, city_name_ams, city_name_ist, city_name_dme
description = description_lon + description_cdg + description_fra + description_fco + description_zrh + description_mad + description_vie + description_ams + description_ist + description_dme

EU_weather = pd.DataFrame(
    {'City': city_name,
    'Description': description, }
)

print("Europe")
print(EU_weather)
EU_weather.to_csv('EU_weather.csv')
