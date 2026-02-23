# questionnaire.QCLXXDGPCMQQ21

> Registro Procedimiento Endoscópico : Administración de Medicamentos

**Schema:** questionnaire
**Columnas:** 8
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Registro Procedimiento Endoscópico : Administración de Medicamentos

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q21Q1 | time |  |  | SI | Hora |
| Q21Q2 | varchar |  |  | SI | Medicamento |
| Q21Q3 | varchar |  |  | SI | Dosis |
| Q21Q4 | varchar |  |  | SI | Vía de Administración |
| Q21Q5 | varchar |  |  | SI | Responsable |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*