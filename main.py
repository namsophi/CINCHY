import concurrent.futures
import Facades.customer_facade as CF
from Objects.Manager import Manager


def main():
    order_manager = Manager()
    with concurrent.futures.ProcessPoolExecutor() as executor:
        while input("Would you like to put in a new order? Answer Y/N") == "Y":
            docs = input("Enter the number of documents to process: ")
            sla = input("Enter the SLA in minutes: ")
            customer = CF.make_customer(sla, docs)
            results = [executor.submit(CF.process, order_manager, customer)]

        for _ in concurrent.futures.as_completed(results):
            print(f'This order cost: ${order_manager.total_used * 5}')


if __name__ == '__main__':
    main()
