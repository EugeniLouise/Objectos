
from Py_Market import Market
from Py_Invoice import Invoice
from Py_Controller import Controller


omie_price = Market(date="2023-05-18", value=10.5)
canarias_price = Market(date="2023-05-18", value=12.75)
baleares_price = Market(date="2023-05-18", value=9.80)

print("Peninsula, Fecha: ", omie_price.value, ", Valor: ", omie_price.value)
print("Canarias, Fecha: ", canarias_price.date, ", Valor: ", canarias_price.value)
print("Baleares, Fecha: ", baleares_price.date, ", Valor: ", baleares_price.value)


invoice1 = Invoice(id="1", cups="ES123456789", invoice_date="2023-05'2018", subsystem="P", consumption=1000.0)
invoice2 = Invoice(id="2", cups="ES987654321", invoice_date="2023-05'2018", subsystem="P", consumption=2000.0)


precio1 = Invoice.calculate(invoice1, omie_price.value)
precio2 = Invoice.calculate(invoice2, omie_price.value)

print("Precio Omie: ", omie_price.value)
print("Consumo y precio de la factura 1: ", invoice1.consumption)
print("El precio de la factura 1 es: ", precio1)

print("Consumo de la factura 2: ", invoice2.consumption)
print("El precio de la factura 2 es: ", precio2)



controller = Controller()

controller.add_invoice(invoice1.cups)
controller.add_invoice(invoice2.cups)

total_facturas = controller.invoices
print("Cups de todas las facturas: ", total_facturas)

invoces_consumption= []
total_invoces_consumption = invoice1.consumption + invoice2.consumption
print("Consumo de las facturas: ", total_invoces_consumption)

invoces_price= []
total_invoces_price = precio1 + precio2
print("Precio de las facturas: ", total_invoces_price)





#totals = controller.calculate_invoices(omie_price.value)

# Mostramos los totales de las facturas
#for index, total in enumerate(totals):
#    print(f"Total de la factura {index + 1}: {total}")