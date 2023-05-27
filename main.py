
from Py_Market import Market
from Py_Invoice import Invoice
from Py_Controller import Controller


omie_price = Market(date="2023-05-18", value=10.5)
canarias_price = Market(date="2023-05-18", value=12.75)
baleares_price = Market(date="2023-05-18", value=9.80)

#print("Peninsula, Fecha: ", omie_price.value, ", Valor: ", omie_price.value)
#print("Canarias, Fecha: ", canarias_price.date, ", Valor: ", canarias_price.value)
#print("Baleares, Fecha: ", baleares_price.date, ", Valor: ", baleares_price.value)


invoice1 = Invoice(id="1", cups="ES123456789", invoice_date="2023-05'2018", subsystem="P", consumption=1000.0)
invoice2 = Invoice(id="2", cups="ES987654321", invoice_date="2023-05'2018", subsystem="P", consumption=2000.0)


precio1 = Invoice.calculate(invoice1, omie_price.value)
precio2 = Invoice.calculate(invoice2, omie_price.value)

#print("Consumo de la factura 1: ", invoice1.consumption)
#print("El precio de la factura 1 es: ", precio1)

#print("Consumo de la factura 2: ", invoice2.consumption)
#print("El precio de la factura 2 es: ", precio2)



controller = Controller()

controller.add_invoice(invoice1)
controller.add_invoice(invoice2)

totals = controller.calculate_invoices(omie_price.value)
cups_factura = controller.cups_invoices(Invoice)
consumo = controller.consumption_invoices(Invoice)

resumen = []
for cups, total, consum in zip(cups_factura, totals, consumo):
    resumen.append((cups, total, consum))
    print(f"El total de la factura con CUPS: {cups} es de: {total} €, con un cosumo de {consum} Kwh.")

suma = sum(totals)
print("La suma total de todas las facturas emitidas es: ", suma, " €.")

