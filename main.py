import concurrent.futures
import Facades.customer_facade as CF
from Objects.Manager import Manager
from Objects.Processor import create_processes


def main():
    request_manager = Manager()
    with concurrent.futures.ProcessPoolExecutor() as executor:
        while input("Would you like to put in a new order? Answer Y or N") != "N":
            docs = input("Enter the number of documents to process: ")
            sla = input("Enter the SLA in minutes: ")
            customer = CF.make_customer(sla, docs)
            # processing each customer in parallel
            # problem: doesn't share globals
            # problem2: how to buy processors efficiently?
            results = [executor.submit(create_processes,
                                       request_manager, customer)]

        for f in concurrent.futures.as_completed(results):
            print(f.result())


if __name__ == '__main__':
    main()
