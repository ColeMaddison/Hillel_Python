# Написать функцию которая будет выполнять запросы на https://httpbin.org/ с использованием 
# нескольких потоков

import requests
from threading import Thread
import time

urls = ['https://httpbin.org/'] * 10

def fetch_url(url):
    start = time.time()
    r = requests.get(url)
    print('Getting {}, time taken: {}\n'.format(url, (time.time() - start)))

threads = [Thread(target=fetch_url, args=(url, )) for url in urls]

for thread in threads:
    thread.start()
    thread.join()
