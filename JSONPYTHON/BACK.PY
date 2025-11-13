
import json
from typing import Dict, List
from transformers import pipeline

# Cargar modelo NLP para análisis semántico
nlp = pipeline("text-classification", model="distilbert-base-uncased-finetuned-sst-2-english")

# Reglas de validación
def validar_factura(factura: Dict) -> Dict:
    errores: List[str] = []

    # Validaciones básicas
    if not factura.get("numero"):
        errores.append("Falta número de factura.")
    if not factura.get("fecha"):
        errores.append("Falta fecha de expedición.")
    if not factura.get("lugar_expedicion"):
        errores.append("Falta lugar de expedición.")
    if not factura.get("vendedor") or not factura["vendedor"].get("nombre"):
        errores.append("Falta información del vendedor.")
    if not factura.get("comprador") or not factura["comprador"].get("nombre"):
        errores.append("Falta información del comprador.")
    if not factura.get("mercancia"):
        errores.append("Falta descripción de mercancía.")
    if not factura.get("moneda"):
        errores.append("Falta moneda de la transacción.")
    if not factura.get("incoterm"):
        errores.append("Falta INCOTERM.")

    # Validación semántica con IA (ejemplo: descripción coherente con INCOTERM)
    descripcion_texto = " ".join([item["descripcion"] for item in factura.get("mercancia", [])])
    incoterm_texto = factura.get("incoterm", "")
    texto_combinado = f"Descripción: {descripcion_texto}. INCOTERM: {incoterm_texto}"
    resultado_nlp = nlp(texto_combinado)[0]
    if resultado_nlp["label"] == "NEGATIVE":
        errores.append("Posible incoherencia entre descripción e INCOTERM.")

    return {
        "valida": len(errores) == 0,
        "errores": errores
    }

# Ejemplo de uso
factura_json = '''{
  "numero": "F12345",
  "fecha": "2025-11-13",
  "lugar_expedicion": "Bogotá",
  "vendedor": {"nombre": "Proveedor S.A.", "direccion": "Calle 123"},
  "comprador": {"nombre": "Importador Ltda.", "direccion": "Carrera 45"},
  "mercancia": [{"descripcion": "Computador portátil", "cantidad": 10, "precio_unitario": 500, "precio_total": 5000}],
  "moneda": "USD",
  "incoterm": "CIF",
  "descuentos": [{"concepto": "Promoción", "valor": 100}],
  "gastos_transporte": 200,
  "seguro": 50
}'''

factura = json.loads(factura_json)
resultado = validar_factura(factura)
print(json.dumps(resultado, indent=2))
