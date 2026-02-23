# questionnaire.QTCENGBQQ122

**Schema:** questionnaire
**Columnas:** 8
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Cuestionario/Formulario**. Plantilla de evaluación clínica estructurada.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | varchar | PK |  | NO | - |
| Q122Q1 | date | PK |  | SI | Fecha de Vacunación a susceptibles/bloqueo |
| Q122Q2 | varchar | PK |  | SI | Población < 5 años |
| Q122Q3 | numeric | PK |  | SI | Total de < 5 años vacunados |
| Q122Q4 | numeric | PK |  | SI | N° De viviendas aproximado en a zona de vacunación |
| Q122Q5 | numeric | PK |  | SI | N° De viviendas visitadas |
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| childsub | bigint | PK |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*