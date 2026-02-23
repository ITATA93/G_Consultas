"""Extraer contenido del PDF de ENTREGA"""
import fitz  # PyMuPDF

doc = fitz.open("docs/ENTREGA - Hojas de cálculo de Google.pdf")
print(f"Paginas: {doc.page_count}")
for i, page in enumerate(doc):
    print(f"\n{'='*70}")
    print(f"PAGINA {i+1}")
    print('='*70)
    text = page.get_text()
    print(text[:3000] if text else "(sin texto)")
doc.close()
