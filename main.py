import Facades.MainFacade as MF


def main():
    reporter, order_manager = MF.set_up_objects()
    wait_times, customers = MF.receive_requests()

    order_manager = \
        MF.process_requests(wait_times, order_manager, customers, reporter)

    if input("Would you like a report of today's orders? Answer Y/N: ") == "Y":
        MF.get_report(reporter, order_manager)

    return


if __name__ == '__main__':
    main()
