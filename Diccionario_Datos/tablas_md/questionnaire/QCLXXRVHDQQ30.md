# questionnaire.QCLXXRVHDQQ30

> Registro Visita Hospitalización Domiciliaria : Antecedentes del Cuidador

**Schema:** questionnaire
**Columnas:** 8
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Registro Visita Hospitalización Domiciliaria : Antecedentes del Cuidador

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q30Q1 | varchar |  |  | SI | Nombre de Cuidador |
| Q30Q2 | varchar |  |  | SI | Parentesco del Cuidador |
| Q30Q3 | varchar |  |  | SI | Teléfono cuidador |
| Q30Q4 | numeric |  |  | SI | N° Integrante |
| Q30Q5 | varchar |  |  | SI | Detalle |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*