# questionnaire.QTCDNARQQ103

> Dietetics Nutrition Assessment Report : Nutritional Diagnosis

**Schema:** questionnaire
**Columnas:** 6
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Dietetics Nutrition Assessment Report : Nutritional Diagnosis

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q103Q1 | varchar |  |  | SI | Nutritional diagnosis |
| Q103Q2 | varchar |  |  | SI | Related to |
| Q103Q3 | varchar |  |  | SI | As evidenced by |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*