# import time
# from threading import Thread
# from multiprocessing import Process

# def count(n):
#     for i in range(n):
#         print(n - i - 1, 'left')
#         time.sleep(1)

# t = Process(target=count, args=(3,))
# t.start()
# t = Thread(target=count, args=(3,))
# t.start()


# class Count(Thread):
#     def __init__(self, n):
#         super().__init__()
#         self.n = n

#     def run(self):
#         for i in range(self.n):
#             print(self.n - i - 1, 'left')
#             print(Thread().name)
#             time.sleep(1)

# t = Count(3)
# t.start()
# print(t.ident)

# потоки демоны daemon=True - автоматич уничтож при выходе из интерпр
# не использовать для задач с использоваем ресурсов
# процесс не завершится пока все потоки не завершатся
# демон - самоуничтожился после выполнения

# нет встроенного завершения потока
# так как поток может работать с файлок который надо закрыть
# захватить мьютекс

# примитивы синхронизации:
# lock - обычный локер - не позволит работать потоку с данными - никогда
# rlock - рекурсивный мьютекс - разрешающий потоку владеющему мьтексом захватить мьютекс более 1 раза - круто
# semaphore - разреш себя захват не более фиксир числа
# boudedsemaphore - следит чтобы его захватили и отпустили одинак количество раз
# метод acquire - захват притива синхр
# метод release - отпускает

# from threading import Lock

# class Shared:
#     def __init__(self, value):
#         self._value = value
#         self._lock = Lock()

#     def incr(self, delta=1):
#         self._lock.acquire()
#         self._value += delta
#         self._lock.release()

# queue - модуль потокобезопасных очередей - делает захват мьютекса, чтото делает, отпускает
# fifo, lifo, priority
# этот модуль только для многопоточности

# def worker(q):
#     while True:
#         item = q.get()
#         dos(item)
#         q.task_done()

# def master(q):
#     for item in source():
#         q.put(item)
#     q.join()

# параллельность и конкурентность
# парал - 2 ресурса - 2 очереди
# конк - 1 ресурс - 2 очереди

# callback, зеленые потоки