class Reporter:
    def __init__(self):
        self.file = "report.txt"
        f = open(self.file, "r+")
        f.truncate()
        f.close()

    def report(self, manager):
        f = open(self.file, "a")
        f.write(f'Total Number of Processors Used: {manager.total_used} \n')
        f.write(f'Total Cost: {manager.total_used * 5} \n')
        f.close()

    def report_single_process(self, docs, time):
        f = open(self.file, "a")
        f.write(f'Processed {docs} documents in {time} minutes\n')
        f.close()
