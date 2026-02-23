# questionnaire.QTCECHCFSMQQ14

> Pauta Registro Contención Física SM : Descripción de farmacos administrados durante el procedimiento

**Schema:** questionnaire
**Columnas:** 7
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Pauta Registro Contención Física SM : Descripción de farmacos administrados durante el procedimiento

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q14Q1 | varchar |  |  | SI | Fármaco |
| Q14Q2 | varchar |  |  | SI | Dosis |
| Q14Q3 | varchar |  |  | SI | Vía |
| Q14Q4 | time |  |  | SI | Hora |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*