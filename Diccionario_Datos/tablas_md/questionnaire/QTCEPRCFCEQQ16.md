# questionnaire.QTCEPRCFCEQQ16

**Schema:** questionnaire
**Columnas:** 7
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Cuestionario/Formulario**. Plantilla de evaluación clínica estructurada.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | varchar | PK |  | NO | - |
| Q16Q1 | date | PK |  | SI | Fecha |
| Q16Q2 | time | PK |  | SI | Hora |
| Q16Q3 | varchar | PK |  | SI | Revisión |
| Q16Q4 | varchar | PK |  | SI | Responsable |
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| childsub | bigint | PK |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*