from Objects.customer import Customer
from Objects.Processor import create_processes


def make_customer(sla, docs):
    new = Customer(sla, docs)
    return new


def process(order_manager, customer):
    create_processes(order_manager, customer)

