from multiprocessing import Process, Pipe
import time
import Facades.customer_facade as CF


def main():
    f = open("report.txt", "a")
    reporter = CF.create_reporter(f)
    order_manager = CF.set_up_manager()
    workers = []
    wait_times = []
    customers = []

    while input("Would you like to put in a new order? Answer Y/N: ") == "Y":
        docs = input("Enter the number of documents to process: ")
        sla = input("Enter the SLA in minutes: ")
        wait_times.append(
            input("Enter how many minutes to wait until next request: "))
        customers.append(CF.make_customer(sla, docs))
    wait_times.append(0)

    for i in range(len(customers)):
        work_pipe, parent_pipe = Pipe()
        worker = Process(target=CF.process,
                         args=(work_pipe, order_manager, customers[i], reporter))
        worker.start()
        workers.append(worker)
        time.sleep(int(wait_times[i]))
        order_manager = parent_pipe.recv()

    [worker.join() for worker in workers]

    if input("Would you like a report of today's orders? Answer Y/N: ") == "Y":
        CF.get_report(reporter, order_manager)

    f.close()
    return


if __name__ == '__main__':
    main()
