# SQLUser.LBDR_DepartmentMedStaff

**Schema:** SQLUser
**Columnas:** 18
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio DR**. Referencias de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBDRDMS_ParRef | varchar | PK |  | NO | Parent Reference to LBDRDepartment |
| LBDRDMS_ContactNumber | varchar |  |  | SI | Care Provider Lab Contact Number |
| LBDRDMS_Name | varchar |  |  | SI | Care Provider Name |
| LBDRDMS_Role | varchar |  |  | SI | Care Provider Type |
| LBDRDMS_RowID | varchar |  |  | NO | - |
| LBDRDMS_Sequence | numeric |  |  | SI | Sequence |
| LBDRDMS_Signature | longvarbinary |  |  | SI | User Signature |
| LBDRDMS_Speciality | varchar |  |  | SI | Care Provider Speciality |
| Q01Q1 | - |  |  | SI | N° Sesión EMPC |
| Q01Q2 | - |  |  | SI | N° Sesión EC |
| Q01Q3 | - |  |  | SI | N° Sesión AEVS |
| Q01Q4 | - |  |  | SI | BORG Modificado |
| Q01Q5 | - |  |  | SI | FC en Taller |
| Q01Q6 | - |  |  | SI | Registro de la Actividad |
| Q01Q7 | - |  |  | SI | Profesional |
| Q01Q8 | - |  |  | SI | Fecha |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*