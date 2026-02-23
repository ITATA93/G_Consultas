# SQLUser.AR_PatBillDate

**Schema:** SQLUser
**Columnas:** 31
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Cuentas por Cobrar (AR)**. Facturación y cobranza de pacientes.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DATE_ParRef | bigint | PK |  | NO | AR_PatientBill Parent Reference |
| ChildQ02DR | - |  |  | SI | Child Reference: Catéteres Venosos |
| DATE_Date | date |  |  | NO | Date |
| DATE_InsuranceUplift | double |  |  | SI | Insurance Uplift |
| DATE_PatientUplift | double |  |  | SI | Patient Uplift |
| DATE_RowId | varchar |  |  | NO | - |
| DATE_TotalAllowed | double |  |  | SI | Total Allowed |
| DATE_TotalDisallowed | double |  |  | SI | Total Disallowed |
| DATE_TotalInsCo | double |  |  | SI | Total Ins Co |
| DATE_TotalMaterialAD | double |  |  | SI | Total Material AD |
| DATE_TotalMaterialAllowed | double |  |  | SI | Total Material Allowed |
| DATE_TotalMaterialDisallow | double |  |  | SI | Total Material Disallowed |
| DATE_TotalMaterialUnauthor | double |  |  | SI | Total Material Unauthorised |
| DATE_TotalPatServiceAllowed | double |  |  | SI | Total Pat Service Allowed |
| DATE_TotalPatient | double |  |  | SI | Total Patient |
| DATE_TotalPatientOfAllowed | double |  |  | SI | Total Patient Of Allowed |
| DATE_TotalServiceAD | double |  |  | SI | Total Service AD |
| DATE_TotalServiceAllowed | double |  |  | SI | Total Service Allowed |
| DATE_TotalServiceUnauthor | double |  |  | SI | Total Service Unauthorised |
| DATE_TotalSpecialist | double |  |  | SI | Total Specialist |
| Q01Q1 | - |  |  | SI | Tipo VVP |
| Q01Q10 | - |  |  | SI | ¿Es necesario el DI?&nbsp |
| Q01Q2 | - |  |  | SI | Ubicación |
| Q01Q3 | - |  |  | SI | Actividad |
| Q01Q4 | - |  |  | SI | Tamaño Catéter |
| Q01Q5 | - |  |  | SI | N° Días VVP |
| Q01Q6 | - |  |  | SI | Permeabilidad |
| Q01Q7 | - |  |  | SI | Caracteristicas Sitio de Inserción |
| Q01Q8 | - |  |  | SI | Estado/Caracterísicas Cobertura |
| Q01Q9 | - |  |  | SI | Cuidados VVP |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*