
import json

# Generar un JSON con todos los requisitos DIAN cumplidos
factura_valida = {
    "numero_factura": "F1001",
    "fecha_emision": "2025-11-12",
    "hora_emision": "14:30",
    "emisor": {
        "nit": "900123456-7",
        "razon_social": "Comercial ABC S.A.S",
        "direccion": "Calle 123 #45-67, Bogotá",
        "telefono": "+57 3101234567",
        "correo": "facturacion@comercialabc.com",
        "resolucion_dian": {
            "numero": "18760000000001",
            "fecha": "2025-01-01",
            "vigencia": "2026-01-01",
            "rango_autorizado": "F1000-F2000"
        }
    },
    "cliente": {
        "nombre": "Juan Pérez",
        "documento": "987654321",
        "tipo_documento": "CC",
        "direccion": "Carrera 10 #20-30, Medellín",
        "correo": "juan.perez@example.com"
    },
    "items": [
        {
            "codigo": "B001",
            "descripcion": "Servicio de mantenimiento preventivo",
            "cantidad": 1,
            "valor_unitario": 200000,
            "iva": 38000  # IVA discriminado
        },
        {
            "codigo": "B002",
            "descripcion": "Repuesto de motor",
            "cantidad": 2,
            "valor_unitario": 150000,
            "iva": 57000
        }
    ],
    "subtotal": 500000,
    "iva_total": 95000,
    "total": 595000,
    "forma_pago": "Transferencia bancaria",
    "medio_pago": "Cuenta Bancaria Bancolombia",
    "moneda": "COP"
}

# Convertir a JSON
json_factura = json.dumps(factura_valida, indent=4, ensure_ascii=False)
print(json_factura)
