# questionnaire.QTCEEXFINEOQQ18

> Ingreso Médico Neonatología : no usado

**Schema:** questionnaire
**Columnas:** 7
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Ingreso Médico Neonatología : no usado

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q18Q1 | varchar |  |  | SI | Localización |
| Q18Q2 | varchar |  |  | SI | Cuadrante |
| Q18Q3 | varchar |  |  | SI | Descripción |
| Q18Q4 | bit |  |  | SI | Hemorragia Subconjuntival |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*