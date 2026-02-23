# questionnaire.QTCCDPQQ40

> Cardiac Disease in Pregnancy - Labour / Birth Care Plan : Care provider(s) contributing to plan

**Schema:** questionnaire
**Columnas:** 7
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Cardiac Disease in Pregnancy - Labour / Birth Care Plan : Care provider(s) contributing to plan

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q40Q1 | date |  |  | SI | Date |
| Q40Q2 | varchar |  |  | SI | Care provider |
| Q40Q3 | varchar |  |  | SI | Care provider status |
| Q40Q4 | varchar |  |  | SI | Other status |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*