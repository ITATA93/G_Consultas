# questionnaire.QTCEICRIQQ01

> Instrumento de Clasificación del Riesgo Familiar V2 : INSTRUMENTO DE CLASIFICACION DEL RIESGO

**Schema:** questionnaire
**Columnas:** 12
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Instrumento de Clasificación del Riesgo Familiar V2 : INSTRUMENTO DE CLASIFICACION DEL RIESGO

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q01Q1 | varchar |  |  | SI | Factores de Riesgo Alto de Daño Familiar y/o Indiv... |
| Q01Q2 | varchar |  |  | SI | Factores de Riesgo Intermedio de Daño Familiar y/o... |
| Q01Q3 | varchar |  |  | SI | Factores de Riesgo Bajo de Daño Familiar y/o Indiv... |
| Q01Q4 | varchar |  |  | SI | Comentarios |
| Q01Q5 | date |  |  | SI | Fecha |
| Q01Q6 | time |  |  | SI | Hora |
| Q01Q7 | varchar |  |  | SI | Profesional |
| Q01Q8 | varchar |  |  | SI | CESFAM |
| Q01Q9 | varchar |  |  | SI | Riego Familiar Evaluado |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*