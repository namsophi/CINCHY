from Objects import Reporter, ProcessManager, RequestReceiver, RequestProcessor


def set_up_objects():
    reporter = Reporter.Reporter()
    order_manager = ProcessManager.ProcessManager()
    return reporter, order_manager


def receive_requests():
    return RequestReceiver.request_receive()


def process_requests(wait_times, order_manager, customers, reporter):
    return RequestProcessor.request_process(
        wait_times, order_manager, customers, reporter)


def get_report(reporter, order_manager):
    return reporter.report(order_manager)

