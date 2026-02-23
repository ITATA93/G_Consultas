# questionnaire.QTCEPLANCQQ20

> Plan Consensuado : Plan consensuado

**Schema:** questionnaire
**Columnas:** 12
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Plan Consensuado : Plan consensuado

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q20Q1 | varchar |  |  | SI | Caso índice |
| Q20Q2 | varchar |  |  | SI | Motivos |
| Q20Q3 | varchar |  |  | SI | Objetivos |
| Q20Q4 | varchar |  |  | SI | Actividades |
| Q20Q5 | varchar |  |  | SI | Tiempo de intervención |
| Q20Q6 | varchar |  |  | SI | Observaciones |
| Q20Q7 | varchar |  |  | SI | Responsables |
| Q20Q8 | varchar |  |  | SI | Profesional |
| Q20Q9 | date |  |  | SI | Fecha |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*