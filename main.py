import Facades.customer_facade as CF


def main():
    # list of customers
    # TODO: customer class
    customers = [CF.make_customer("A", 1000000, 30),
                 CF.make_customer("B", 1000000, 60),
                 CF.make_customer("A1", 1000, 30),
                 CF.make_customer("C", 1, 1440)]

    cost = CF.process_documents(customers)


if __name__ == '__main__':
    main()
