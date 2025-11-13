import json

factura_2 = {
    "cliente": {
        "nombre": "Ana Torres",
        "tipo_documento": "NIT",
        "documento": "900123456",
        "direccion": "Carrera 10 #20-30, Cali",
        "correo": "ana.torres@empresa.com"
    },
    "numero_factura": "F3005",
    "fecha_emision": "2025-11-12",
    "hora_emision": "14:45",
    "items": [
        {
            "codigo": "S001",
            "descripcion": "Servicio de consultoría TI",
            "cantidad": 10,
            "valor_unitario": 150000,
            "iva": 285000
        }
    ],
    "subtotal": 1500000,
    "iva_total": 285000,
    "total": 1785000,
    "emisor": {
        "nit": "901234567-8",
        "razon_social": "Consultores Globales Ltda",
        "direccion": "Calle 80 #15-30, Bogotá",
        "telefono": "+57 3112345678",
        "correo": "facturacion@consultoresglobales.com",
        "resolucion_dian": {
            "numero": "18760000000003",
            "fecha": "2025-02-01",
            "vigencia": "2026-02-01",
            "rango_autorizado": "F3000-F4000"
        }
    },
    "forma_pago": "Transferencia bancaria",
    "medio_pago": "Cuenta Bancaria Davivienda",
    "moneda": "COP",
    "observaciones": "Incluye soporte remoto"
}

print(json.dumps(factura_2, indent=4, ensure_ascii=False))
