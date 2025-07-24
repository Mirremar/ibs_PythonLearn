import threading
import time

def countdown(thread_name):
    print(f"Thread '{thread_name}' started")

    for i in range(10, 0, -1): #Вывод обратного отсчёта с интервалом 1 сек
        print(f"Thread '{thread_name}': {i}")
        time.sleep(1)

    print(f"Thread '{thread_name}' finished")
#Создали потоки
thread1 = threading.Thread(target=countdown, args=("Thread-1",))
thread2 = threading.Thread(target=countdown, args=("Thread-2",))
#Стартовали потоки
thread1.start()
thread2.start()
#Подождали завершения потоков
thread1.join()
thread2.join()