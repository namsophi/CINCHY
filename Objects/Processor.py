import math
import time


def create_processes(manager, customer, reporter):
    if manager.processors == 0:
        return _no_processors_to_use(manager, customer, reporter)

    else:
        # I can finish next customer in their sla with remaining processors
        if math.ceil(customer.docs/manager.processors) <= \
                manager.time_left:
            return _process_with_leftovers(manager, customer, reporter)

        # I have leftovers but I need more
        elif math.ceil(customer.docs/manager.processors) > \
                manager.time_left:
            _need_more_processors(manager, customer)


def _no_processors_to_use(manager, customer, reporter):
    to_buy = math.ceil(customer.docs / customer.sla)
    manager.total_used = to_buy
    manager.time_left = 60 - customer.sla
    if manager.time_left <= 0:
        manager.processors = 0
    else:
        manager.processors = to_buy
    time.sleep(customer.sla)
    reporter.report_single_process(customer.docs, customer.sla)
    return


def _process_with_leftovers(manager, customer, reporter):
    usage_time = math.ceil(customer.docs/manager.processors.value)
    manager.time_left.value -= usage_time
    if manager.time_left.value == 0:
        manager.processors.value = 0
    time.sleep(usage_time)
    reporter.report_single_process(customer.docs, usage_time)
    return


def _need_more_processors(manager, customer):


