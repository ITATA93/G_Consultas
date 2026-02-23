# questionnaire.QTCEINGUPCQQ61

> INGRESO UNIDAD DE PACIENTE CRÍTICO : Cardiaco

**Schema:** questionnaire
**Columnas:** 8
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* INGRESO UNIDAD DE PACIENTE CRÍTICO : Cardiaco

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q61Q1 | varchar |  |  | SI | Ritmo |
| Q61Q2 | varchar |  |  | SI | Soplos |
| Q61Q3 | varchar |  |  | SI | Grado |
| Q61Q4 | varchar |  |  | SI | Foco |
| Q61Q5 | varchar |  |  | SI | Comentario |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*