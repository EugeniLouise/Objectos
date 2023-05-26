


class Controller:
    def __init__(self):
        self.invoices = []

    def add_invoice(self, invoice):
        self.invoices.append(invoice)

    def calculate_invoices(self, market):
        total_invoices = []
        for invoice in self.invoices:
            total = invoice.calculate(market)
            total_invoices.append(total)
        return total_invoices

