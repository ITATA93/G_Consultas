# questionnaire.QTCENGBQQML117

**Schema:** questionnaire
**Columnas:** 11
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Cuestionario/Formulario**. Plantilla de evaluación clínica estructurada.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | varchar | PK |  | NO | - |
| QML117Q1 | varchar | PK |  | SI | Muestra |
| QML117Q2 | varchar | PK |  | SI | Nombre |
| QML117Q3 | varchar | PK |  | SI | Apellidos |
| QML117Q4 | numeric | PK |  | SI | Edad |
| QML117Q5 | varchar | PK |  | SI | N° Dosis VPO |
| QML117Q6 | date | PK |  | SI | Fecha última Dosis |
| QML117Q7 | date | PK |  | SI | Fecha toma de Muestra |
| QML117Q8 | date | PK |  | SI | Fecha de Recepción |
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| childsub | bigint | PK |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*