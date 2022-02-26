import random
import time
from multiprocessing import Queue, Pool


def worker_func(counter_queue, time_queue):
    while True:
        t = random.uniform(0, 4)
        time.sleep(t)
        counter_queue.put(1)
        time_queue.put(t)


def run():
    counter = 0
    counter_queue = Queue()
    work_time = 0.0
    time_queue = Queue()

    worker_pool = Pool(8, worker_func, (counter_queue, time_queue))

    while True:
        # get() on a queue is by default blocking
        counter += counter_queue.get()
        work_time += time_queue.get()

        if counter % 10 == 0:
            print(
                f"Counter is at {counter} and time consumed by pool is {work_time:.4f}")


if __name__ == "__main__":
    run()
