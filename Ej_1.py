# Calcular el precio total de una compra incluyendo el 21% de IVA.

# Precio inicial
print("ingresar precio:")
precio = float(input())

# Impuesto
IVA = precio * 0.21
print("IVA:" , IVA)

# Precio total
precio_total = precio + IVA
print("Precio total:" , precio_total)