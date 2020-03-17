import math
import time


def create_processes(manager, customer):
    if manager.total_used.value == 0:
        return _no_processors_to_use(manager, customer)

    else:
        # I can finish next customer in their sla with remaining processors
        if math.ceil(customer.docs/manager.processors.value) <= \
                manager.time_left.value:
            return _process_with_leftovers(manager, customer)

        # I have leftovers but I need more
        # elif math.ceil(customer.docs/manager.processors) \
        #     > manager.time_left.value:
        # _need_more_processors(manager, customer)


def _no_processors_to_use(manager, customer):
    to_buy = math.ceil(customer.docs / customer.sla)
    with manager.lock:
        manager.total_used.value = to_buy
        manager.time_left.value = 60 - customer.sla
        if manager.time_left.value <= 0:
            manager.processors.value = 0
        else:
            manager.processors.value = to_buy
    time.sleep(customer.sla)
    print(f'Done processing {customer.docs} documents!')
    return manager


def _process_with_leftovers(manager, customer):
    with manager.lock:
        usage_time = math.ceil(customer.docs/manager.processors.value)
        manager.time_left.value -= usage_time
        if manager.time_left.value == 0:
            manager.processors.value = 0
    time.sleep(usage_time)
    print(f'Done processing {customer.docs} documents!')
    return manager


# def _need_more_processors(manager, customer):
#     with manager.lock:


