# questionnaire.QGXXXLACHISQQ04

> Laceration History : Laceration length

**Schema:** questionnaire
**Columnas:** 11
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Laceration History : Laceration length

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q04Q1 | varchar |  |  | SI | Length (cm) |
| Q04Q2 | varchar |  |  | SI | Note |
| Q04Q3 | varchar |  |  | SI | Wound Location |
| Q04Q4 | date |  |  | SI | Date |
| Q04Q5 | varchar |  |  | SI | Actively bleeding |
| Q04Q6 | varchar |  |  | SI | Numbness or paresthesias distal to wound |
| Q04Q7 | varchar |  |  | SI | Loss of movement or strength distal to wound |
| Q04Q8 | varchar |  |  | SI | Foreign body possible |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*