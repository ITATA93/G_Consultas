# questionnaire.QTCERPPQQ39

> Registro Pertenencias del Paciente : Medicamentos

**Schema:** questionnaire
**Columnas:** 6
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Registro Pertenencias del Paciente : Medicamentos

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q39Q1 | varchar |  |  | SI | Medicamento (dosis/presentación) |
| Q39Q2 | varchar |  |  | SI | Estado |
| Q39Q3 | numeric |  |  | SI | Cantidad |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*