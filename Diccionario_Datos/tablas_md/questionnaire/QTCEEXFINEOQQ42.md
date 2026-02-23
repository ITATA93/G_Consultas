# questionnaire.QTCEEXFINEOQQ42

> Ingreso Médico Neonatología : Examen Cardiaco

**Schema:** questionnaire
**Columnas:** 9
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Ingreso Médico Neonatología : Examen Cardiaco

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q42Q1 | varchar |  |  | SI | Ritmo |
| Q42Q2 | varchar |  |  | SI | Ruidos |
| Q42Q3 | varchar |  |  | SI | Soplos |
| Q42Q4 | varchar |  |  | SI | Grado (soplos) |
| Q42Q5 | varchar |  |  | SI | Ubicación |
| Q42Q6 | varchar |  |  | SI | Comentarios |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*