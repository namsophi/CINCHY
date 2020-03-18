import time
from multiprocessing import Process, Pipe
from Objects.Processor import create_processes


def request_process(wait_times, order_manager, customers, reporter):
    workers = []
    for i in range(len(customers)):
        work_pipe, parent_pipe = Pipe()
        work = Process(target=create_processes,
                       args=(work_pipe, order_manager, customers[i], reporter))
        work.start()
        workers.append(work)
        time.sleep(int(wait_times[i]))
        order_manager = parent_pipe.recv()

    [worker.join() for worker in workers]
    return order_manager
