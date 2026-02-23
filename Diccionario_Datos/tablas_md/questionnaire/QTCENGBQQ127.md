# questionnaire.QTCENGBQQ127

**Schema:** questionnaire
**Columnas:** 7
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Cuestionario/Formulario**. Plantilla de evaluación clínica estructurada.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | varchar | PK |  | NO | - |
| Q127Q1 | varchar | PK |  | SI | Nombre del Investigador |
| Q127Q2 | varchar | PK |  | SI | Cargo |
| Q127Q3 | date | PK |  | SI | Fecha |
| Q127Q4 | varchar | PK |  | SI | Comentarios |
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| childsub | bigint | PK |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*