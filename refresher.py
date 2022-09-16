import requests
import time

while True:
    try:
        refresh_request = requests.request(url="https://www.golden-league-stream.tk/Пляжный волейбол/Матч", method="get")

    except Exception as e:
        print(e)

    time.sleep(1)
