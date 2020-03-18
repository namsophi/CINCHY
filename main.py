import Facades.MainFacade as MF


def main():
    f = open("report.txt", "a")
    reporter, order_manager = MF.set_up_objects(f)
    wait_times, customers = MF.receive_requests()

    order_manager = \
        MF.process_requests(wait_times, order_manager, customers, reporter)

    if input("Would you like a report of today's orders? Answer Y/N: ") == "Y":
        MF.get_report(reporter, order_manager)

    f.close()
    return


if __name__ == '__main__':
    main()
