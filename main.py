
from Py_Market import Market
from Py_Invoice import Invoice
from Py_Controller import Controller


omie_price = Market("omie_price", "2023-05-18", 2.5)
canarias_price = Market("canarias_price", "2023-05-18", 3)
baleares_price = Market("baleares_price", "2023-05-18", 4)

controller = Controller()


invoice1 = Invoice(1, "123456789", "2023-05-01", "Subsistema A", 100)
invoice2 = Invoice(2, "987654321", "2023-05-02", "Subsistema B", 150)
controller.add_invoice(invoice1)
controller.add_invoice(invoice2)

print(omie_price.value)


totals = controller.calculate_invoices(omie_price.value)

# Mostramos los totales de las facturas
for index, total in enumerate(totals):
    print(f"Total de la factura {index + 1}: {total}")