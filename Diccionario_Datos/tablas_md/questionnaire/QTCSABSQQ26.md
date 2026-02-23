# questionnaire.QTCSABSQQ26

> Staphylococcus Aureus Bacteraemia Summary : Dates

**Schema:** questionnaire
**Columnas:** 6
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Staphylococcus Aureus Bacteraemia Summary : Dates

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q26Q1 | date |  |  | SI | Date of positive blood culture |
| Q26Q2 | date |  |  | SI | Date of clearance blood culture |
| Q26Q3 | varchar |  |  | SI | Surveillance blood cultures at 72-96 hours results |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*