# У вас есть пулл адрессов (можно использовать https://httpbin.org/ ).  Создать 2-3 функции которые 
# будут делать реквесты к этому адресу. Ваши реквесты должны быть асинхронны с использованием asyncio 

# solution 1 - 0.75 sec
import grequests
from time import time

urls = ['https://httpbin.org/'] * 10

def on_response(res):
    print(res.status_code)

async_list = []

for url in urls:
    async_list.append(grequests.get(url, hooks={'response': on_response}))

start = time()
grequests.map(async_list)
print(time() - start)


# solution 2 - 5.78 sec
# import asyncio
# import requests
# from time import time

# urls = ['https://httpbin.org/'] * 10

# async def req(url):
#     requests.get(url)
    
#     print("Request to {} Done.".format(url))

# try:
#     loop = asyncio.get_event_loop()
#     start = time()
#     loop.run_until_complete(asyncio.gather(*[req(url) for url in urls]))
#     print("Tasks finished in {} seconds".format(time() - start))

# finally:
#     loop.close()

# solution 3 - 6.02 sec
# import asyncio
# import requests
# from time import time

# async def req(url):
#     requests.get(url)
    
#     print("Request to {} Done.".format(url))

# async def req_generator():
#     for url in urls:
#         asyncio.ensure_future(req(url))

# loop = asyncio.get_event_loop()
# start = time()
# loop.run_until_complete(req_generator())
# print("Tasks finished in {} seconds".format(time() - start))
# loop.close()


