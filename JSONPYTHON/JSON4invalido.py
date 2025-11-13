
import json

# Generar un JSON con errores en facturación (incumple NIT del emisor. Fecha de emisión. Resolución de facturación. Descripción detallada del producto o servicio.)

factura_invalida = {
    "numero_factura": "F001",  # OK
    # Falta el NIT del emisor (requisito indispensable)
    "razon_social": "Empresa XYZ",
    # Falta la fecha de emisión (requisito indispensable)
    "cliente": {
        "nombre": "Juan Pérez",
        "documento": "123456789"
    },
    "items": [
        {
            "codigo": "A001",
            # Falta la descripción detallada del producto (requisito indispensable)
            "cantidad": 2,
            "valor_unitario": 50000
        }
    ],
    "total": 100000,
    # Falta la resolución de facturación (requisito indispensable)
}

# Convertir a JSON
json_factura = json.dumps(factura_invalida, indent=4, ensure_ascii=False)
print(json_factura)
