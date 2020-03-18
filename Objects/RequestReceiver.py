from Objects.Customer import Customer


def request_receive():
    wait_times = []
    customers = []

    while input("Would you like to put in a new order? Answer Y/N: ") == "Y":
        docs = input("Enter the number of documents to process: ")
        sla = input("Enter the SLA in minutes: ")
        wait_times.append(
            input("Enter how many minutes to wait until next request: "))
        customers.append(Customer(sla, docs))

    return wait_times, customers
