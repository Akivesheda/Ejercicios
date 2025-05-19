# Calcular el costo de combustible de un viaje en función de los kilómetros recorridos, consumo por kilómetro y precio del litro de nafta.

kilometros = 70
print("Kilometros:", kilometros)

nafta_kilometro = 0.3
print("Consumo de nafta por kilometro:", nafta_kilometro, "Litros")

precio_litro = 130
print("Precio del litro de nafta  $", precio_litro)

consumo_total = kilometros * nafta_kilometro
print(consumo_total, "litros en:", kilometros, "KM")

precio_kilometro = precio_litro * nafta_kilometro
print("$", precio_kilometro, "por kilometro")

precio_total = consumo_total * precio_kilometro
print("Precio total:  $", precio_total)