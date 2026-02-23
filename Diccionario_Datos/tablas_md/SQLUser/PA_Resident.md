# SQLUser.PA_Resident

**Schema:** SQLUser
**Columnas:** 11
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PA_RowId | bigint | PK |  | NO | - |
| PA_DateFrom | date |  |  | NO | Date From |
| PA_DateTo | date |  |  | SI | Date To |
| PA_GroupNo | double |  |  | SI | GroupNo |
| PA_MainResidence | varchar |  |  | SI | Main Residence |
| PA_PatientAlert_DR | bigint |  | FK | SI | Des Ref PACPatientAlert |
| PA_Person_DR | bigint |  | FK | SI | Des Ref PAPerson |
| PA_PrimaryResident | varchar |  |  | SI | HeadOfHousehold |
| PA_RemovalReason_DR | bigint |  | FK | SI | Des Ref Removal Reason |
| PA_Resident_DR | bigint |  | FK | SI | Des Ref Resident |
| PA_Time | time |  |  | SI | Time |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*