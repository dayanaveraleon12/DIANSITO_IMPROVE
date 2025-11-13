
import json

# Generar un JSON que incumple TODOS los requisitos DIAN (orden diferente)
factura_totalmente_invalida = {
    "items": [],  # No hay productos ni servicios
    "cliente": {},  # Sin datos del cliente
    "emisor": {},  # Sin datos del emisor
    # No hay número de factura
    # No hay fecha ni hora de emisión
    # No hay resolución DIAN
    # No hay NIT ni razón social
    # No hay dirección ni correo
    # No hay subtotal, IVA ni total
    # No hay forma de pago ni moneda
}

# Convertir a JSON
json_factura = json.dumps(factura_totalmente_invalida, indent=4, ensure_ascii=False)
print(json_factura)

'''
Este JSON está completamente inválido porque:

No tiene número de factura, fecha ni hora.
No tiene datos del emisor (NIT, razón social, dirección, resolución DIAN).
No tiene datos del cliente (nombre, documento, tipo documento).
No tiene ítems válidos (sin descripción, cantidad, valor unitario, IVA).
No tiene valores monetarios (subtotal, IVA, total).
No tiene forma de pago ni moneda.
'''