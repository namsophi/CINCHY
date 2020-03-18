from multiprocessing import Manager


class ProcessManager:
    def __init__(self):
        self.processors = []
        self.time_left = []
        self.total_used = 0

# def create_manager():
#     manager = Manager()
#     order_manager = manager.Namespace()
#     order_manager.processors = []
#     order_manager.time_left = []
#     order_manager.total_used = 0
#     return order_manager




