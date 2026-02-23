# questionnaire.QTCINRFQQ24

> Interventional Nephrology Record - Fistula : Balloon details

**Schema:** questionnaire
**Columnas:** 7
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Interventional Nephrology Record - Fistula : Balloon details

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q24Q1 | varchar |  |  | SI | Type of balloon |
| Q24Q2 | numeric |  |  | SI | Balloon size (mm) |
| Q24Q3 | numeric |  |  | SI | Balloon length (mm) |
| Q24Q4 | varchar |  |  | SI | Balloon inflation time (min/sec) |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*