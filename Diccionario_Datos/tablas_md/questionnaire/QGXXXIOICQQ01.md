# questionnaire.QGXXXIOICQQ01

> Intra-Operative Items Count : Items Count

**Schema:** questionnaire
**Columnas:** 13
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Intra-Operative Items Count : Items Count

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q0100 | varchar |  |  | SI | Item |
| Q0101 | numeric |  |  | SI | Start |
| Q0102 | numeric |  |  | SI | 1st Count |
| Q0103 | numeric |  |  | SI | 2nd Count |
| Q0104 | numeric |  |  | SI | 3rd Count |
| Q0105 | bit |  |  | SI | Complete |
| Q0106 | bit |  |  | SI | Incomplete |
| Q01Q10 | bit |  |  | SI | Additions |
| Q01Q8 | varchar |  |  | SI | Accountable items |
| Q01Q9 | varchar |  |  | SI | Count all |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*