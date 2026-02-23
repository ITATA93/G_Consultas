# questionnaire.QTCEIDCTQQ21

> Informe de Derivación Centros de Tratamiento : Causas Pendientes

**Schema:** questionnaire
**Columnas:** 12
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Informe de Derivación Centros de Tratamiento : Causas Pendientes

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q21Q1 | varchar |  |  | SI | RIT / RUC / ROL |
| Q21Q2 | varchar |  |  | SI | Delito Tipo |
| Q21Q3 | varchar |  |  | SI | Delito Causa |
| Q21Q4 | varchar |  |  | SI | Tribunal |
| Q21Q5 | varchar |  |  | SI | Sanción accesoria |
| Q21Q6 | varchar |  |  | SI | Sanción Ley 20.084 |
| Q21Q7 | varchar |  |  | SI | Duración de la sanción |
| Q21Q8 | varchar |  |  | SI | Delegado Responsable y Fono |
| Q21Q9 | varchar |  |  | SI | Programa Sename |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*