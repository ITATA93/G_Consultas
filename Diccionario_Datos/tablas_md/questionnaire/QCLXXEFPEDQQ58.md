# questionnaire.QCLXXEFPEDQQ58

> Examen Físico Pediátrico : Abdomen y dorso

**Schema:** questionnaire
**Columnas:** 8
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Examen Físico Pediátrico : Abdomen y dorso

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q58Q1 | varchar |  |  | SI | Palpación |
| Q58Q2 | varchar |  |  | SI | Percusión |
| Q58Q3 | varchar |  |  | SI | Auscultación |
| Q58Q4 | varchar |  |  | SI | Localización |
| Q58Q5 | varchar |  |  | SI | Comentarios |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*