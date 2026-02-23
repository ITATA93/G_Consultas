# questionnaire.QTCIVALCLAQQ25

> Central Line Assessment : Catheter position corrected / withdrawn

**Schema:** questionnaire
**Columnas:** 10
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Central Line Assessment : Catheter position corrected / withdrawn

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q25Q1 | numeric |  |  | SI | Central intravenous central venous pressure cathet... |
| Q25Q2 | numeric |  |  | SI | Central intravenous external catheter length |
| Q25Q3 | numeric |  |  | SI | Central internal catheter length |
| Q25Q4 | numeric |  |  | SI | Central intravenous mid arm circumference |
| Q25Q5 | date |  |  | SI | Date and time |
| Q25Q6 | time |  |  | SI | Time |
| Q25Q7 | varchar |  |  | SI | Care provider |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*