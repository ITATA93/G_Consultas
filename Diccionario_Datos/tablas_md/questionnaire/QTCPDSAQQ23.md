# questionnaire.QTCPDSAQQ23

> Peritoneal Dialysis Suitability Assessment : Nails / Hands

**Schema:** questionnaire
**Columnas:** 10
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Peritoneal Dialysis Suitability Assessment : Nails / Hands

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q23Q1 | varchar |  |  | SI | Nails / Hands assessment for |
| Q23Q2 | varchar |  |  | SI | Clean |
| Q23Q3 | varchar |  |  | SI | Infections |
| Q23Q4 | varchar |  |  | SI | Fungal |
| Q23Q5 | varchar |  |  | SI | Trimming needed |
| Q23Q6 | varchar |  |  | SI | Current lesions, carbuncles and/or cysts |
| Q23Q7 | varchar |  |  | SI | Notes |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*