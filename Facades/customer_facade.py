from Objects.Customer import Customer
from Objects.Processor import create_processes
from Objects.Reporter import Reporter


def make_customer(sla, docs):
    new = Customer(sla, docs)
    return new


def process(order_manager, customer, reporter):
    return create_processes(order_manager, customer, reporter)


def create_reporter(file):
    return Reporter(file)


def get_report(reporter, order_manager):
    return reporter.report(order_manager)

