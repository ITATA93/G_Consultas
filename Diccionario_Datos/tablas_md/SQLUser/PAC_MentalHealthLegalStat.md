# SQLUser.PAC_MentalHealthLegalStat

**Schema:** SQLUser
**Columnas:** 23
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| MHLS_RowId | bigint | PK |  | NO | - |
| MHLS_CareType | varchar |  |  | SI | Care Type Codes |
| MHLS_Code | varchar |  |  | SI | Code |
| MHLS_CreatedDate | date |  |  | SI | Created Date |
| MHLS_CreatedTime | time |  |  | SI | Created Time |
| MHLS_CreatedUser_DR | bigint |  | FK | SI | Created User |
| MHLS_DateFrom | date |  |  | SI | Date From |
| MHLS_DateTo | date |  |  | SI | Date To |
| MHLS_Default | varchar |  |  | SI | Default |
| MHLS_Desc | varchar |  |  | SI | Description |
| MHLS_NationalCode | varchar |  |  | SI | National Code |
| MHLS_UpdatedDate | date |  |  | SI | Updated Date |
| MHLS_UpdatedTime | time |  |  | SI | Updated Time |
| MHLS_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q09Q1 | - |  |  | SI | Date |
| Q09Q2 | - |  |  | SI | Time |
| Q09Q3 | - |  |  | SI | Pressure in current cylinder >200 psi |
| Q09Q4 | - |  |  | SI | Check replacement cylinder available |
| Q09Q5 | - |  |  | SI | Empty water trap |
| Q09Q6 | - |  |  | SI | Bagging circuit intact and present |
| Q09Q7 | - |  |  | SI | Disc filter changed   (change every 12 hours) |
| Q09Q8 | - |  |  | SI | Comments / Variance notes |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*