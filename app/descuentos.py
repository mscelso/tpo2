def calcular_descuento(precio, porcentaje_descuento):
    if precio < 0:
        raise ValueError("El precio no puede ser negativo")

    if porcentaje_descuento < 0 or porcentaje_descuento > 100:
        raise ValueError("El porcentaje de descuento debe estar entre 0 y 100")

    descuento = precio * porcentaje_descuento / 100
    precio_final = precio - descuento

    return round(precio_final, 2)