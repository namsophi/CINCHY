from Objects.Customer import Customer
from Objects.Processor import create_processes
from Objects.Reporter import Reporter
from Objects.ProcessManager import create_manager


def make_customer(sla, docs):
    new = Customer(sla, docs)
    return new


def set_up_manager():
    return create_manager()


def process(order_manager, customer, reporter):
    return create_processes(order_manager, customer, reporter)


def create_reporter(file):
    return Reporter(file)


def get_report(reporter, order_manager):
    return reporter.report(order_manager)

