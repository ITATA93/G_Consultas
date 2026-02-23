# questionnaire.QCLXXEFRNQQ52

> Examen Físico del Recién Nacido : Abdomen Alterado

**Schema:** questionnaire
**Columnas:** 8
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Examen Físico del Recién Nacido : Abdomen Alterado

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q52Q1 | varchar |  |  | SI | Palpación |
| Q52Q2 | varchar |  |  | SI | Percusión |
| Q52Q4 | varchar |  |  | SI | Auscultación |
| Q52Q5 | varchar |  |  | SI | Localización |
| Q52Q6 | varchar |  |  | SI | Lateralidad |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*