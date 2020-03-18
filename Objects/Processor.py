import math
import time


def create_processes(pipe, manager, customer, reporter):
    if not manager.processors:
        pipe.send(_no_processors_to_use(manager, customer, reporter))
        return

    else:
        pipe.send(_process_leftovers(manager, customer, reporter))
        return


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
        manager.total_used += to_buy
        manager.processors.append(to_buy)
        manager.time_left.append(60)

    time_left = customer.sla

    for i in range(len(manager.time_left)):
        if time_left - manager.time_left[i] > 0:
            for j in range(len(manager.time_left)):
                manager.time_left[j] -= manager.time_left[i]
            time_left -= manager.time_left[i]
            current_processors = manager.processors
            manager.time_left.pop(i)
            manager.processors.pop(i)
            manager.time_left.append(60)
            manager.processors.append(current_processors)
            to_buy += current_processors
            time.sleep(manager.time_left[i])
        else:
            time_needed = math.ceil(customer.docs / manager.processors[i])
            if time_needed <= manager.time_left[i] \
                    and time_needed < customer.sla:
                for j in range(len(manager.time_left)):
                    manager.time_left[j] -= time_needed
                reporter.report_single_process(customer.docs, time_needed)
            else:
                for j in range(len(manager.time_left)):
                    manager.time_left[j] -= time_left
                    if manager.time_left[j] == 0:
                        manager.time_left.pop(j)
                        manager.processors.pop(j)
                time.sleep(time_left)
                reporter.report_single_process(customer.docs, customer.sla)
    return manager

