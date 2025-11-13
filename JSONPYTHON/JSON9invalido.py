
import json

# Generar un JSON que incumple TODOS los requisitos DIAN
factura_totalmente_invalida = {
    # No tiene número de factura
    # No tiene fecha de emisión
    # No tiene hora de emisión
    # No tiene datos del emisor (NIT, razón social, dirección, resolución DIAN)
    "emisor": {},
    # No tiene datos del cliente (nombre, documento, tipo documento, dirección, correo)
    "cliente": {},
    # No tiene ítems con descripción, cantidad, valor unitario ni IVA
    "items": [],
    # No tiene subtotal, IVA total ni total
    # No tiene forma de pago ni medio de pago
    # No tiene moneda
}

# Convertir a JSON
json_factura = json.dumps(factura_totalmente_invalida, indent=4, ensure_ascii=False)
print(json_factura)

'''
incumple

Sin número de factura.
Sin fecha ni hora.
Sin datos del emisor (NIT, razón social, dirección, resolución DIAN).
Sin datos del cliente.
Sin ítems válidos.
Sin valores monetarios (subtotal, IVA, total).
Sin forma de pago ni moneda.
'''