# questionnaire.QTCAHPRHLSAQQ17

> Lumbar Spine Assessment : Constant Symptom

**Schema:** questionnaire
**Columnas:** 7
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Lumbar Spine Assessment : Constant Symptom

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q17Q1 | varchar |  |  | SI | Body Part |
| Q17Q2 | varchar |  |  | SI | Symptoms |
| Q17Q3 | varchar |  |  | SI | Location  |
| Q17Q4 | varchar |  |  | SI | Nature |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*