# questionnaire.QGXXXWOUNDMQQ06

**Schema:** questionnaire
**Columnas:** 9
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Cuestionario/Formulario**. Plantilla de evaluación clínica estructurada.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | varchar | PK |  | NO | - |
| Q06Q1 | date | PK |  | SI | Date |
| Q06Q2 | time | PK |  | SI | Time |
| Q06Q3 | varchar | PK |  | SI | Pain prevention |
| Q06Q4 | varchar | PK |  | SI | Care |
| Q06Q5 | varchar | PK |  | SI | Type of Dressing |
| Q06Q6 | varchar | PK |  | SI | Note |
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| childsub | bigint | PK |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*