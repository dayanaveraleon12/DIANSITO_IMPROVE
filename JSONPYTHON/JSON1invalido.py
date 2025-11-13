#✅ Aquí tienes el archivo JSON que NO cumple con 1 los requisitos de la DIAN (se omitió el campo obligatorio CUFE):
#El campo CUFE (Código Único de Factura Electrónica) es obligatorio según el Anexo Técnico 1.9

import json

# Generar una factura que NO cumpla con los requisitos (omitimos el campo CUFE)
factura_invalida = {
    "FacturaElectronica": {
        # "CUFE" se omite para simular incumplimiento
        "Ambiente": 2,
        "Emisor": {
            "NIT": "901234567",
            "RazonSocial": "Empresa S.A.S.",
            "Direccion": "Calle 123 #45-67",
            "Municipio": "Bogotá",
            "RegimenFiscal": "48"
        },
        "Receptor": {
            "TipoIdentificacion": "31",
            "NumeroIdentificacion": "123456789",
            "RazonSocial": "Cliente S.A.",
            "Email": "cliente@correo.com"
        },
        "Documento": {
            "Tipo": "01",
            "Numero": "F001-000000123",
            "Fecha": "2025-11-12",
            "Hora": "15:44:34-05:00",
            "Nota": "Venta de productos"
        },
        "Numeracion": {
            "Prefijo": "F001",
            "Desde": 1,
            "Hasta": 999999,
            "ClaveTecnica": "ABCDEF1234567890",
            "Autorizacion": "900123456789012345678901234567",
            "FechaInicio": "2025-11-01",
            "FechaFinal": "2026-10-31"
        },
        "Software": {
            "Identificacion": "SOFTWARE-001",
            "PIN": "123456"
        },
        "Items": [
            {
                "Codigo": "001",
                "Descripcion": "Producto A",
                "Cantidad": 2,
                "ValorUnitario": 100.0,
                "ValorTotal": 200.0,
                "Impuestos": [
                    {
                        "Tipo": "IVA",
                        "Porcentaje": 19.0,
                        "Valor": 38.0
                    }
                ]
            }
        ],
        "Totales": {
            "Subtotal": 200.0,
            "Impuestos": 38.0,
            "Total": 238.0
        }
    }
}

# Convertir a JSON y guardar en archivo
factura_invalida_json = json.dumps(factura_invalida, indent=4, ensure_ascii=False)
with open("factura_invalida.json", "w", encoding="utf-8") as f:
    f.write(factura_invalida_json)

print("Archivo JSON creado: factura_invalida.json (sin CUFE, incumple requisito DIAN).")

