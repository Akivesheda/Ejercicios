# Calcular el tiempo total de viaje sumando horas y minutos de dos tramos.

# Tramo 1
horas_1 = 5
minutos_1 = 32

# Tramo 2
horas_2 = 7
minutos_2 = 100

# Tramo horas y minutos
horas_total = (horas_1 + horas_2)
minutos_total = (minutos_1 + minutos_2)

# Convertir minutos a horas
minutos_horas = (minutos_total // 60)

# Horas finales
horas_final = horas_total + minutos_horas

# Minutos restantes
minutos_extra = (minutos_total % 60)

# Resultado
print("Tiempo total:", horas_final,"Horas y", minutos_extra, "Minutos.")