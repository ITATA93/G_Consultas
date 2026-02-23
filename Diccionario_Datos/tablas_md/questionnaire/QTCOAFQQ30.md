# questionnaire.QTCOAFQQ30

> Osteoporosis Assessment : Bone mineral density

**Schema:** questionnaire
**Columnas:** 13
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Osteoporosis Assessment : Bone mineral density

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q30Q1 | varchar |  |  | SI | Bone mineral density |
| Q30Q10 | varchar |  |  | SI | % changes |
| Q30Q2 | date |  |  | SI | Latest result date |
| Q30Q3 | varchar |  |  | SI | Latest T score |
| Q30Q4 | varchar |  |  | SI | Latest Z score |
| Q30Q5 | varchar |  |  | SI | Latest Bone Mineral Content (BMC) |
| Q30Q6 | date |  |  | SI | Previous result date |
| Q30Q7 | varchar |  |  | SI | Previous T score |
| Q30Q8 | varchar |  |  | SI | Previous Z score |
| Q30Q9 | varchar |  |  | SI | Previous BMC |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*