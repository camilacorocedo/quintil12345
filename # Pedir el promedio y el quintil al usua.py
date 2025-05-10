# Pedir el promedio y el quintil al usuario
promedio = float(input("Ingrese su promedio: "))
quintil = int(input("Ingrese el quintil (1, 2, 3, 4 o 5): "))

# Valores base
arancel = 1800000
matricula = 90000

# Calcular el descuento en el arancel según el promedio y quintil
if promedio > 6.0:
    if quintil == 1 or quintil == 2:
        descuento_arancel = 0.20
    elif quintil == 3 or quintil == 4:
        descuento_arancel = 0.15
else:
    if 5.0 < promedio <= 6.0:
        if quintil == 1 or quintil == 2:
            descuento_arancel = 0.13
        elif quintil == 3 or quintil == 4:
            descuento_arancel = 0.10
    else:
        descuento_arancel = 0

# Calcular el descuento en matrícula según el quintil y el promedio
descuento_matricula = 0
if quintil == 1 or quintil == 2 or quintil == 3:
    descuento_matricula = 0.10
    if promedio >= 5.5:
        descuento_matricula += 0.056
    

# Calcular los valores finales con descuento
arancel_final = arancel * (1 - descuento_arancel)
matricula_final = matricula * (1 - descuento_matricula)

# Mostrar los resultados
print(f"\nEl valor del arancel es: {int(arancel_final)}")
print(f"El valor de la matrícula es: {int(matricula_final)}")
