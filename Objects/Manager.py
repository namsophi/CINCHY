from multiprocessing import Value, Lock


class Manager:
    def __init__(self):
        self.processors = Value('i', 0)
        self.time_left = Value('i', 0)
        self.total_used = Value('i', 0)
        self.lock = Lock()




