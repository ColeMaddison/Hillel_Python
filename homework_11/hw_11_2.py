# Созадть очередь из задач. Создать воркеров которые будут делать выборки из очереди и  выполнять 
# эти задачи. Количество воркеров - опциональный аргумент. Количество задач - опциональный аргумент.  
# 1 воркер == 1 тред

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
