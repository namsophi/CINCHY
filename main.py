import os
import Facades.customer_facade as CF
from Objects.Manager import Manager


def main():
    order_manager = Manager()
    while input("Would you like to put in a new order? Answer Y/N: ") == "Y":
        docs = input("Enter the number of documents to process: ")
        sla = input("Enter the SLA in minutes: ")
        customer = CF.make_customer(sla, docs)
        worker = os.fork()
        if worker == 0:
           CF.process(order_manager, customer)
    if input("Would you like the total cost? Answer Y/N: ") == "Y":
        CF.calculate_cost(order_manager)
    return


if __name__ == '__main__':
    main()
