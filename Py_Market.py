


class Market:
    def __init__(self, date, value):
        self.date = date
        self.value = value

        return value


omie_price = Market("2023-05-18", 10.50)
canarias_price = Market("2023-05-18", 12.75)
baleares_price = Market("2023-05-18", 9.80)

# Acceso a los atributos de las instancias
print("Fecha de omie_price:", omie_price.date)
print("Valor de omie_price:", omie_price.value)
print("Fecha de canarias_price:", canarias_price.date)
print("Valor de canarias_price:", canarias_price.value)
print("Fecha de baleares_price:", baleares_price.date)
print("Valor de baleares_price:", baleares_price.value)

