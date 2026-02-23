# questionnaire.QTCPROMQQ55

> Patient-reported outcome measure (UL-PROM) for Duchenne Muscular Dystrophy (DMD) : Have there been any changes in any of those activities in the last 6 months?

**Schema:** questionnaire
**Columnas:** 5
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Patient-reported outcome measure (UL-PROM) for Duchenne Muscular Dystrophy (DMD) : Have there been any changes in any of those activities in the last 6 months?

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q55Q1 | varchar |  |  | SI | Activity |
| Q55Q2 | varchar |  |  | SI | Change |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*