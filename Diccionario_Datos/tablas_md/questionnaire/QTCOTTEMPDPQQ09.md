# questionnaire.QTCOTTEMPDPQQ09

> "Perioperative - Temperature Maintenance and Diathermy Plate : Diathermy Plate	"

**Schema:** questionnaire
**Columnas:** 9
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* "Perioperative - Temperature Maintenance and Diathermy Plate : Diathermy Plate	"

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q09Q1 | varchar |  |  | SI | Specify site	 |
| Q09Q2 | varchar |  |  | SI | Lot number	 |
| Q09Q3 | date |  |  | SI | Expiry date	 |
| Q09Q4 | varchar |  |  | SI | Monopolar |
| Q09Q5 | varchar |  |  | SI | Bipolar |
| Q09Q6 | varchar |  |  | SI | Has the diathermy site been shaved? |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*