# SQLUser.PAC_RefDoctorServices

**Schema:** SQLUser
**Columnas:** 27
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SER_ParRef | bigint | PK |  | NO | PAC_RefDoctor Parent Reference |
| ChildQ7DR | - |  |  | SI | Child Reference: Peritoneal equilibration test (pe... |
| Q6Q1 | - |  |  | SI | Date |
| Q6Q2 | - |  |  | SI | Total Creatinine Clearance (CCL) |
| Q6Q3 | - |  |  | SI | Residual Creatinine Clearance (CCL) |
| Q6Q4 | - |  |  | SI | Dialysis Creatinine Clearance (CCL) |
| Q6Q5 | - |  |  | SI | Total KT/V |
| Q6Q6 | - |  |  | SI | Residual KT/V |
| Q6Q7 | - |  |  | SI | 24 hour urine Volume, Residual Renal Function (RRF... |
| Q6Q8 | - |  |  | SI | Comment |
| Q6Q9 | - |  |  | SI | Dialysis KT/V |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| SER_ARCIM_DR | varchar |  | FK | SI | Des Ref ARCIM |
| SER_ARCOS_DR | varchar |  | FK | SI | Des Ref ARCOS |
| SER_Childsub | double |  |  | NO | Childsub |
| SER_CreatedDate | date |  |  | SI | Created Date |
| SER_CreatedTime | time |  |  | SI | Created Time |
| SER_CreatedUser_DR | bigint |  | FK | SI | Created User |
| SER_DateFrom | date |  |  | SI | Date From |
| SER_DateTo | date |  |  | SI | Date To |
| SER_InsType_DR | bigint |  | FK | SI | Des Ref InsType |
| SER_Limit | double |  |  | SI | Limit |
| SER_Perc | double |  |  | SI | Perc |
| SER_RowId | varchar |  |  | NO | - |
| SER_UpdatedDate | date |  |  | SI | Updated Date |
| SER_UpdatedTime | time |  |  | SI | Updated Time |
| SER_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*