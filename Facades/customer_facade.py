from Objects.Customer import Customer
from Objects.Processor import create_processes
from Objects.Calculator import calculate


def make_customer(sla, docs):
    new = Customer(sla, docs)
    return new


def process(order_manager, customer):
    return create_processes(order_manager, customer)


def calculate_cost(order_manager):
    return calculate(order_manager)

