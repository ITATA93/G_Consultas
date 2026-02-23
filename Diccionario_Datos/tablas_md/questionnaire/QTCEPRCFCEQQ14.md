# questionnaire.QTCEPRCFCEQQ14

**Schema:** questionnaire
**Columnas:** 10
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Cuestionario/Formulario**. Plantilla de evaluación clínica estructurada.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | varchar | PK |  | NO | - |
| Q14Q1 | varchar | PK |  | SI | Farmaco |
| Q14Q2 | varchar | PK |  | SI | Dosis |
| Q14Q3 | varchar | PK |  | SI | Vía |
| Q14Q4 | varchar | PK |  | SI | Indicado por |
| Q14Q5 | varchar | PK |  | SI | Administrado por |
| Q14Q6 | time | PK |  | SI | Hora |
| Q14Q7 | date | PK |  | SI | Fecha |
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| childsub | bigint | PK |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*