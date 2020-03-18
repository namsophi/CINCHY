from Objects.Customer import Customer
from Objects.Processor import create_processes
from Objects.Reporter import Reporter
from Objects.ProcessManager import ProcessManager


def make_customer(sla, docs):
    new = Customer(sla, docs)
    return new


def set_up_manager():
    return ProcessManager()


def process(pipe, order_manager, customer, reporter):
    return create_processes(pipe, order_manager, customer, reporter)


def create_reporter(file):
    return Reporter(file)


def get_report(reporter, order_manager):
    return reporter.report(order_manager)

