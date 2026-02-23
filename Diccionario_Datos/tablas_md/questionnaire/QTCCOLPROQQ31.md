# questionnaire.QTCCOLPROQQ31

> Cervical and Vulvar Dysplasia Worksheet : Lesion details

**Schema:** questionnaire
**Columnas:** 12
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Cervical and Vulvar Dysplasia Worksheet : Lesion details

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q31Q1 | numeric |  |  | SI | Lesion number |
| Q31Q2 | numeric |  |  | SI | Clock position |
| Q31Q3 | varchar |  |  | SI | At the SCJ |
| Q31Q4 | varchar |  |  | SI | Lesion visualized |
| Q31Q5 | varchar |  |  | SI | Satellite lesion |
| Q31Q6 | numeric |  |  | SI | Lesion size (mm) |
| Q31Q7 | varchar |  |  | SI | Size of the lesion |
| Q31Q8 | numeric |  |  | SI | No. Quadrants the lesion involves |
| Q31Q9 | numeric |  |  | SI | Percentage of affected area (%) |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*