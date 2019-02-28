# Написать функцию которая будет выполнять запросы на https://httpbin.org/ с 
# использованием нескольких потоков

# from multiprocessing.pool import Pool
# from threading import Thread
# import requests
# import time


# urls = ['https://httpbin.org/'] * 10

# def fetch_url(url):
#     start = time.time()
#     r = requests.get(url)
#     print('Getting {}, time taken: {}\n'.format(url, (time.time() - start)))

# threads = [Thread(target=fetch_url, args=(url, )) for url in range(2)]

# thread1 = Thread(target=fetch_url)

# for thread in threads:
#     thread.start()
#     thread.join()

# def main():
#     p = Pool(processes=3)
#     p.daemon = True
#     result = p.map(fetch_url, urls)
#     p.join()

# main()


from threading import Thread
from queue import Queue
import requests
from time import time

class Requester(Thread):
    def __init__(self, q):
        super().__init__()
        self.q = q

    def run(self):
        while True:
            link = self.q.get()
            try:
                r = requests.get(link)
            finally:
                print('Got request to {}, with status {}'.format(link, r.status_code))
                self.q.task_done()

def main():
    start = time()
    queue = Queue()
    links = ['https://httpbin.org/'] * 10

    for x in range(3):
        worker = Requester(queue)
        worker.daemon = True
        worker.start()

    for link in links:
        queue.put(link)
    
    queue.join()
    print('Work finished in {}'.format(time() - start))

main()