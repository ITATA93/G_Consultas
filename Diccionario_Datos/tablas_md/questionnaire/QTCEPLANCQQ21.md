# questionnaire.QTCEPLANCQQ21

> Plan Consensuado : Información Social

**Schema:** questionnaire
**Columnas:** 11
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Plan Consensuado : Información Social

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q21Q1 | varchar |  |  | SI | Inclusión social |
| Q21Q2 | varchar |  |  | SI | Trabajo |
| Q21Q3 | varchar |  |  | SI | Escuela |
| Q21Q4 | varchar |  |  | SI | Grupos sociales |
| Q21Q5 | varchar |  |  | SI | Organizaciones |
| Q21Q6 | varchar |  |  | SI | Otras organzaciones |
| Q21Q7 | date |  |  | SI | Fecha |
| Q21Q8 | varchar |  |  | SI | Profesional |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*