import json


# Estructura básica de la factura electrónica
factura = {
    "documento": {
        "emisor": {
            "nit": "901234567",
            "razonSocial": "Empresa S.A.S.",
            "direccion": "Calle 123 #45-67",
            "municipio": "Bogotá"
        },
        "receptor": {
            "tipoIdentificacion": "31",  # 31 = NIT, 13 = CC
            "numeroIdentificacion": "123456789",
            "razonSocial": "Cliente S.A.",
            "email": "cliente@correo.com"
        },
        "tipo": "01",  # Factura de venta nacional
        "numero": "F001-000000123",
        "fecha": "2025-11-12",
        "hora": "15:44:34-05:00",
        "numeracion": {
            "prefijo": "F001",
            "desde": 1,
            "hasta": 999999,
            "claveTecnica": "ABCDEF1234567890",
            "autorizacion": "900123456789012345678901234567",
            "fechaInicio": "2025-11-01",
            "fechaFinal": "2026-10-31"
        },
        "items": [
            {
                "codigo": "001",
                "descripcion": "Producto A",
                "cantidad": 2,
                "valorUnitario": 100.0,
                "valorTotal": 200.0,
                "iva": 19.0
            }
        ],
        "totales": {
            "subtotal": 200.0,
            "impuestos": 38.0,
            "total": 238.0
        },
        "software": {
            "identificacion": "SOFTWARE-001",
            "ambiente": 2,  # 2 = Producción
            "pin": "123456"
        }
    }
}

# Convertir a JSON
factura_json = json.dumps(factura, indent=4, ensure_ascii=False)
print(factura_json)
