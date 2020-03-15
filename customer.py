class Customer:
    def __init__(self, name, sla, docs):
        self.name = name
        self.sla = sla
        self.docs = docs

    def process_documents(self, customers):
        for