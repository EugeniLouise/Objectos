
import pandas as pd

class Market:
    def __init__(self, date, value):
        self.date = date
        self.value = value

#Abre excel
df = pd.read_excel("C:/Users/Eugenia Subirons/Downloads/Pych/Precios_21.xlsx")

#Adjudicar cada columna del excel a una variables
Fecha = df['Fecha']
Omie_Precio = df['Precio Omie']
Canarias_Precio = df['Precio Canarias']
Baleares_Precio = df['Precio Baleares']

#Definir instancias con las variables creadas
omie_price = Market(date=Fecha, value=Omie_Precio)
canarias_price = Market(date=Fecha, value=Canarias_Precio)
baleares_price = Market(date=Fecha, value=Baleares_Precio)


#Printear las instancias
print(f"Fecha: {omie_price.date}, Valor: {omie_price.value}")
print(f"Fecha: {canarias_price.date}, Valor: {canarias_price.value}")
print(f"Fecha: {baleares_price.date}, Valor: {baleares_price.value}")





#omie_price = Market("2023-05-18", 10.50)
#canarias_price = Market("2023-05-18", 12.75)
#baleares_price = Market("2023-05-18", 9.80)


# Acceso a los atributos de las instancias
#print("Peninsula, Fecha: ", omie_price.date, ", Valor: ", omie_price.value)
#print("Canarias, Fecha: ", canarias_price.date, ", Valor: ", canarias_price.value)
#print("Baleares, Fecha: ", baleares_price.date, ", Valor: ", baleares_price.value)
