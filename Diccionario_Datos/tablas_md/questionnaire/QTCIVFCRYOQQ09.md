# questionnaire.QTCIVFCRYOQQ09

> Cryopreservation : Vital Embryo Numbers

**Schema:** questionnaire
**Columnas:** 6
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Cryopreservation : Vital Embryo Numbers

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q09Q1 | numeric |  |  | SI | <50% surviving |
| Q09Q2 | numeric |  |  | SI | 51-99% surviving |
| Q09Q3 | numeric |  |  | SI | 100% surviving |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*