
import json

factura_1 = {
    "numero_factura": "F2001",
    "fecha_emision": "2025-11-12",
    "hora_emision": "09:15",
    "emisor": {
        "nit": "900987654-3",
        "razon_social": "Soluciones Tecnológicas S.A.S",
        "direccion": "Av. Siempre Viva #123, Bogotá",
        "telefono": "+57 3109876543",
        "correo": "contacto@solucionestech.com",
        "resolucion_dian": {
            "numero": "18760000000002",
            "fecha": "2025-01-01",
            "vigencia": "2026-01-01",
            "rango_autorizado": "F2000-F3000"
        }
    },
    "cliente": {
        "nombre": "Carlos Gómez",
        "tipo_documento": "CC",
        "documento": "1122334455",
        "direccion": "Calle 45 #67-89, Medellín",
        "correo": "carlos.gomez@example.com"
    },
    "items": [
        {
            "codigo": "P001",
            "descripcion": "Laptop Dell Inspiron",
            "cantidad": 1,
            "valor_unitario": 2500000,
            "iva": 475000
        }
    ],
    "subtotal": 2500000,
    "iva_total": 475000,
    "total": 2975000,
    "forma_pago": "Tarjeta de crédito",
    "medio_pago": "Visa Bancolombia",
    "moneda": "COP",
    "observaciones": "Entrega en 3 días hábiles"
}

print(json.dumps(factura_1, indent=4, ensure_ascii=False))
