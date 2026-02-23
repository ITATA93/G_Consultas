# questionnaire.QGXXXSTOMAQQ13

**Schema:** questionnaire
**Columnas:** 9
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Cuestionario/Formulario**. Plantilla de evaluación clínica estructurada.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | varchar | PK |  | NO | - |
| Q13Q1 | date | PK |  | SI | Date |
| Q13Q2 | varchar | PK |  | SI | Skin care peristomal |
| Q13Q3 | varchar | PK |  | SI | Samples |
| Q13Q4 | varchar | PK |  | SI | Equipment |
| Q13Q5 | varchar | PK |  | SI | Note |
| Q13Q6 | time | PK |  | SI | Time |
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| childsub | bigint | PK |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*