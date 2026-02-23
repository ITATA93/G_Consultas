# questionnaire.QTCENEUROQQ113

> Ingreso Neurocirugía / Neurología : Sensibilidad

**Schema:** questionnaire
**Columnas:** 10
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Ingreso Neurocirugía / Neurología : Sensibilidad

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q113Q1 | varchar |  |  | SI | Localización anatómica |
| Q113Q2 | varchar |  |  | SI | Sensibilidad táctil |
| Q113Q3 | varchar |  |  | SI | Sensibilidad térmica |
| Q113Q4 | varchar |  |  | SI | Sensibilidad nociceptiva |
| Q113Q5 | varchar |  |  | SI | Propiocepción |
| Q113Q6 | varchar |  |  | SI | Sensibilidad vibratoria |
| Q113Q7 | varchar |  |  | SI | Comentarios |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*