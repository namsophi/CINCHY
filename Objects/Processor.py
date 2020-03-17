import time
from multiprocessing import Value, Lock
from Objects.Manager import Manager
from Objects.customer import Customer


def create_processes(manager, customer):
    to_buy = customer.docs // customer.sla
    if manager.total_used == 0:
        _no_processors_to_use(to_buy, manager, customer)

    elif manager.processors.value != 0:
        _left_over_processors(to_buy, manager, customer)


def _no_processors_to_use(to_buy, manager, customer):
    with manager.lock:
        manager.total_used.value = to_buy
        manager.time_left.value = 60 - customer.sla
        if manager.time_left.value <= 0:
            manager.processors.value = 0
        else:
            manager.processors.value = to_buy
    time.sleep(to_buy)

def _left_over_processors(to_buy, manager, customer):
    with manager.lock:
        manager.processors.value -= to_buy
        manager.time_left.value -= customer.sla
        if manager.processors.value < 0:

