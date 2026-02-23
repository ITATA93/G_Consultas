# questionnaire.QTCPARQQ40

> Perineal Assessment and Repair : Suture location and type

**Schema:** questionnaire
**Columnas:** 7
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Perineal Assessment and Repair : Suture location and type

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q40Q1 | varchar |  |  | SI | Suture location |
| Q40Q2 | varchar |  |  | SI | Suture material |
| Q40Q3 | varchar |  |  | SI | Suturing method |
| Q40Q4 | varchar |  |  | SI | Notes |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*