# SQLUser.DT_EmployeeMeals

**Schema:** SQLUser
**Columnas:** 11
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Dieta**. Gestión de alimentación de pacientes.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| EMPM_RowId | bigint | PK |  | NO | - |
| EMPM_Date | date |  |  | SI | Date of Meal |
| EMPM_EmplJob_DR | bigint |  | FK | SI | Des Ref EmplJob |
| EMPM_MealType_DR | bigint |  | FK | SI | Des REf MealType |
| EMPM_Number | double |  |  | SI | Number of employees |
| Q120Q1 | - |  |  | SI | Time |
| Q120Q2 | - |  |  | SI | Systolic |
| Q120Q3 | - |  |  | SI | Diastolic |
| Q120Q4 | - |  |  | SI | Rating of Perceived Exertion |
| Q120Q5 | - |  |  | SI | Burdon's Modified Borg Scale |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*