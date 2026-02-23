# questionnaire.QTCIPRQQ09

> Insulin Pump Record : Insulin to carbohydrate ratio

**Schema:** questionnaire
**Columnas:** 6
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Insulin Pump Record : Insulin to carbohydrate ratio

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q09Q1 | time |  |  | SI | Time from |
| Q09Q2 | time |  |  | SI | Time to |
| Q09Q3 | varchar |  |  | SI | Insulin to carbohydrate ratio |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*