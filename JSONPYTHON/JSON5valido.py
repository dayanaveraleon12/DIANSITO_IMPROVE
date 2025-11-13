
import json

factura_3 = {
    "items": [
        {
            "codigo": "R001",
            "descripcion": "Repuesto de impresora HP",
            "cantidad": 3,
            "valor_unitario": 80000,
            "iva": 45600
        },
        {
            "codigo": "R002",
            "descripcion": "Cartucho de tinta",
            "cantidad": 2,
            "valor_unitario": 60000,
            "iva": 22800
        }
    ],
    "subtotal": 360000,
    "iva_total": 68400,
    "total": 428400,
    "numero_factura": "F4008",
    "fecha_emision": "2025-11-12",
    "hora_emision": "18:30",
    "emisor": {
        "nit": "902345678-9",
        "razon_social": "Impresiones y Más S.A.",
        "direccion": "Calle 50 #30-20, Barranquilla",
        "telefono": "+57 3123456789",
        "correo": "ventas@impresionesymas.com",
        "resolucion_dian": {
            "numero": "18760000000004",
            "fecha": "2025-03-01",
            "vigencia": "2026-03-01",
            "rango_autorizado": "F4000-F5000"
        }
    },
    "cliente": {
        "nombre": "Empresa XYZ",
        "tipo_documento": "NIT",
        "documento": "800123456",
        "direccion": "Av. Las Palmas #45-67, Bucaramanga",
        "correo": "compras@empresa.xyz"
    },
    "forma_pago": "Efectivo",
    "medio_pago": "Caja",
    "moneda": "COP",
    "observaciones": "Garantía de 6 meses"
}

print(json.dumps(factura_3, indent=4, ensure_ascii=False))


'''
Cumplen todos los requisitos DIAN: número, fecha, hora, emisor completo (NIT, razón social, dirección, resolución DIAN), cliente completo, ítems con IVA discriminado, subtotal, IVA total, total, forma y medio de pago, moneda.
Incluyen datos adicionales como teléfono, correo, observaciones.
Cada una tiene orden diferente en la estructura.
'''