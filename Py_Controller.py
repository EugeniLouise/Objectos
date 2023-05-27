


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

    def cups_invoices(self, Invoice):
        total_cups = []
        for Invoice in self.invoices:
            cups_fact= Invoice.cups
            total_cups.append(cups_fact)
        return total_cups

    def consumption_invoices(self, Invoice):
        total_consumption = []
        for Invoice in self.invoices:
            consumption_fact= Invoice.consumption
            total_consumption.append(consumption_fact)
        return total_consumption