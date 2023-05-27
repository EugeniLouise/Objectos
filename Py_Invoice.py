


class Invoice:
    def __init__(self, id, cups, invoice_date, subsystem, consumption):
        self.id= id
        self.cups= cups
        self.invoice_date= invoice_date
        self.subsystem= subsystem
        self.consumption= consumption


    def calculate(self, market):
        return self.consumption * market / 1000




#Consumption en kWh, mercado en €/MWh.