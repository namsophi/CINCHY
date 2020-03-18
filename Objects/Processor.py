import math
import time
from Objects import ProcessHelpers as pH


def create_processes(pipe, manager, customer, reporter):
    print(manager.processors)
    print(manager.time_left)
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
            pH.need_to_buy_more_processors(manager, to_buy, time_left, i)
            reporter.report_single_process(customer.docs, customer.sla)

        else:
            time_needed = math.ceil(customer.docs / manager.processors[i])
            pH.can_finish_with_leftovers(manager, time_needed)
            reporter.report_single_process(customer.docs, time_needed)
    return manager
