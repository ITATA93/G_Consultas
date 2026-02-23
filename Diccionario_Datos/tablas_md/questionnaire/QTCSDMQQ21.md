# questionnaire.QTCSDMQQ21

> Shoulder Dystocia Management : Manoeuvres / Actions performed

**Schema:** questionnaire
**Columnas:** 10
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Shoulder Dystocia Management : Manoeuvres / Actions performed

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q21Q1 | varchar |  |  | SI | Maternal position during manoeuvre / action |
| Q21Q2 | numeric |  |  | SI | Manoeuvre / action order number |
| Q21Q3 | time |  |  | SI | Time stamp |
| Q21Q4 | varchar |  |  | SI | Manoeuvre / action type |
| Q21Q5 | varchar |  |  | SI | Other, please specify |
| Q21Q6 | varchar |  |  | SI | By whom |
| Q21Q7 | varchar |  |  | SI | Comments |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*