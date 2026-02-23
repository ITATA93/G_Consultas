# questionnaire.QTCENDONPRQQ10

**Schema:** questionnaire
**Columnas:** 7
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Cuestionario/Formulario**. Plantilla de evaluación clínica estructurada.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | varchar | PK |  | NO | - |
| Q10Q1 | varchar | PK |  | SI | Scope type |
| Q10Q2 | varchar | PK |  | SI | Scope number |
| Q10Q3 | time | PK |  | SI | Insertion time |
| Q10Q4 | time | PK |  | SI | Removal time |
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| childsub | bigint | PK |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*