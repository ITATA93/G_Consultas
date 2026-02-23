# questionnaire.QCLXXPCIQQ03

> Plan de Cuidado Integral  : Antecedentes de su Red

**Schema:** questionnaire
**Columnas:** 12
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Plan de Cuidado Integral  : Antecedentes de su Red

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q03Q1 | varchar |  |  | SI | Cuenta con Familiar o Red de Apoyo |
| Q03Q2 | varchar |  |  | SI | ¿Quién? Nombre Completo |
| Q03Q3 | varchar |  |  | SI | Rut |
| Q03Q4 | date |  |  | SI | Fecha de Nacimiento  |
| Q03Q5 | varchar |  |  | SI | Estado Civil |
| Q03Q6 | varchar |  |  | SI | Escolaridad |
| Q03Q7 | varchar |  |  | SI | Domicilio |
| Q03Q8 | varchar |  |  | SI | Teléfono |
| Q03Q9 | varchar |  |  | SI | Tipo de relación o parentesco  |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*