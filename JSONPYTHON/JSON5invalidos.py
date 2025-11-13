
import json

# Generar un JSON con errores en facturación (incumple 5 requisitos DIAN)
factura_invalida = {
    "numero_factura": "F003",  # OK
    # Falta la fecha de emisión (requisito indispensable)
    "emisor": {
        "nit": "900123456-7",
        "razon_social": "Comercial XYZ S.A.S",
        "direccion": "Calle 45 #67-89, Bogotá",
        "telefono": "+57 3109876543",
        "correo": "facturacion@comercialxyz.com"
        # Falta la resolución DIAN (requisito indispensable)
    },
    "cliente": {
        "nombre": "Carlos Gómez",
        "documento": "1122334455",
        "tipo_documento": "CC"
        # Falta la dirección del cliente (requisito indispensable)
    },
    "items": [
        {
            "codigo": "C001",
            "descripcion": "Consultoría en sistemas",
            "cantidad": 1,
            "valor_unitario": 300000
            # Falta el IVA discriminado (requisito indispensable)
        }
    ],
    "subtotal": 300000,
    "iva_total": 0,  # Incorrecto, debería calcularse y discriminarse
    "total": 300000,
    # Falta la forma de pago (requisito indispensable)
    "moneda": "COP"
}

# Convertir a JSON
json_factura = json.dumps(factura_invalida, indent=4, ensure_ascii=False)
print(json_factura)


'''
✅ Este JSON incumple los siguientes requisitos DIAN:

Fecha de emisión.
Resolución DIAN.
IVA discriminado por ítem.
Dirección del cliente.
Forma de pago.
'''