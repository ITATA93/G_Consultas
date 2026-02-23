# questionnaire.QCLXXTDINSUQQ22

> Taller de Insulinoterapia : TABLA REGISTRO DE AUTOMONITOREO

**Schema:** questionnaire
**Columnas:** 7
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Taller de Insulinoterapia : TABLA REGISTRO DE AUTOMONITOREO

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q22Q1 | numeric |  |  | SI | Hemoglucotest |
| Q22Q2 | varchar |  |  | SI | Comida |
| Q22Q3 | date |  |  | SI | Fecha |
| Q22Q4 | time |  |  | SI | Hora |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*