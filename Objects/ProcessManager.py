from multiprocessing import Manager


def create_manager():
    manager = Manager()
    order_manager = manager.Namespace()
    order_manager.processors = []
    order_manager.time_left = []
    order_manager.total_used = 0
    return order_manager




