import time
from multiprocessing import Value, Lock
from Objects.Manager import Manager
from Objects.customer import Customer


def create_processes(manager, customer):
    if manager.total_used == 0:
        to_buy = customer.docs // customer.sla
        with manager.lock:
            manager.processors.value = to_buy
            manager.time_left.value = 60
            manager.total_used.value = to_buy
        time.sleep(to_buy)

    elif manager.processors.value != 0:

