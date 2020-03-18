from Objects.Calculator import calculate


class Reporter:
    def __init__(self, file):
        self.file = file

    def report(self, manager):
        self.file.write(f'Total Number of Processors Used: {manager.total_used}'
                        f'\n')
        self.file.write(f'Total Cost: {calculate(manager)}\n')

    def report_single_process(self, docs, time):
        self.file.write(f'Processed {docs} documents in {time} minutes\n')
