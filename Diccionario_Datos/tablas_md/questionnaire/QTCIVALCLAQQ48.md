# questionnaire.QTCIVALCLAQQ48

> Central Line Assessment : Assessment

**Schema:** questionnaire
**Columnas:** 12
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Central Line Assessment : Assessment

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q48Q1 | varchar |  |  | SI | Line status |
| Q48Q2 | varchar |  |  | SI | Site condition |
| Q48Q3 | varchar |  |  | SI | Dressing |
| Q48Q4 | varchar |  |  | SI | Care |
| Q48Q5 | varchar |  |  | SI | Limb temperature |
| Q48Q6 | varchar |  |  | SI | Pulse distal to insertion site |
| Q48Q7 | date |  |  | SI | Assessment date and time |
| Q48Q8 | time |  |  | SI | Assessment time |
| Q48Q9 | varchar |  |  | SI | Assessing care provider |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*