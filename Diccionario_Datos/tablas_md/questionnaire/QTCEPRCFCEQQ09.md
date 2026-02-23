# questionnaire.QTCEPRCFCEQQ09

**Schema:** questionnaire
**Columnas:** 8
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Cuestionario/Formulario**. Plantilla de evaluación clínica estructurada.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | varchar | PK |  | NO | - |
| Q09Q1 | date | PK |  | SI | Fecha |
| Q09Q2 | time | PK |  | SI | Hora |
| Q09Q3 | varchar | PK |  | SI | Acción |
| Q09Q4 | varchar | PK |  | SI | Otro |
| Q09Q5 | varchar | PK |  | SI | Ingresado por |
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| childsub | bigint | PK |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*