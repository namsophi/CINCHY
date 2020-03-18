from multiprocessing import Process
import Facades.customer_facade as CF


def main():
    f = open("report.txt", "a")
    reporter = CF.create_reporter(f)
    order_manager = CF.create_manager()
    workers = []

    while input("Would you like to put in a new order? Answer Y/N: ") == "Y":
        docs = input("Enter the number of documents to process: ")
        sla = input("Enter the SLA in minutes: ")
        customer = CF.make_customer(sla, docs)

        worker = Process(target=CF.process,
                         args=(order_manager, customer, reporter))
        worker.start()
        workers.append(worker)

    [worker.join() for worker in workers]

    if input("Would you like a report of today's orders? Answer Y/N: ") == "Y":
        CF.get_report(reporter, order_manager)

    f.close()
    return


if __name__ == '__main__':
    main()
