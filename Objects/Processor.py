import math
import time


def create_processes(manager, customer, reporter):
    if not manager.processors:
        return _no_processors_to_use(manager, customer, reporter)

    else:
        return _process_leftovers(manager, customer, reporter)


def _no_processors_to_use(manager, customer, reporter):
    to_buy = math.ceil(customer.docs / customer.sla)
    manager.total_used += to_buy
    if 60 - customer.sla != 0:
        manager.processors.append(to_buy)
        manager.time_left.append(60 - customer.sla)
    time.sleep(customer.sla)
    reporter.report_single_process(customer.docs, customer.sla)
    return manager


def _process_leftovers(manager, customer, reporter):
    to_buy = math.ceil(customer.docs / customer.sla) - sum(manager.processors)
    if to_buy > 0:
        manager.processors.append(to_buy)
        manager.time_left.append(60)

    time_left = customer.sla

    for i in range(len(manager.time_left)):
        if time_left - manager.time_left[i] > 0:
            for j in range(len(manager.time_left)):
                manager.time_left[j] -= manager.time_left[i]
            time_left -= manager.time_left[i]
            time.sleep(manager.time_left[i])
            current_processors = manager.processors
            manager.time_left.pop(i)
            manager.processors.pop(i)
            manager.time_left.append(60)
            manager.processors.append(current_processors)
            to_buy += current_processors
        else:
            for j in range(len(manager.time_left)):
                manager.time_left[j] -= time_left
                if manager.time_left[j] == 0:
                    manager.time_left.pop(j)
                    manager.processors.pop(j)
            time.sleep(time_left)
    manager.total_used += to_buy
    reporter.report_single_process(customer.docs, customer.sla)
    return manager

