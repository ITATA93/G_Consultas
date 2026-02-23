# questionnaire.QCLXXENFGERQQ174

**Schema:** questionnaire
**Columnas:** 7
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Cuestionario Regional Chile**. Formulario de evaluación clínica adaptado para Chile.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | varchar | PK |  | NO | - |
| Q174Q1 | varchar | PK |  | SI | Tipo de Tratamiento |
| Q174Q2 | date | PK |  | SI | Fecha de Inicio  |
| Q174Q3 | date | PK |  | SI | Fecha de Término  |
| Q174Q4 | varchar | PK |  | SI | Esquema / Tipo / Comentarios |
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| childsub | bigint | PK |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*