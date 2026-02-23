# SQLUser.PA_DeviceAssociation

**Schema:** SQLUser
**Columnas:** 23
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DEVASSOC_RowId | bigint | PK |  | NO | - |
| ChildQ69DR | - |  |  | SI | Child Reference: Wound Review - Medical / Wound Sp... |
| DEVASSOC_AssociatedUser_DR | bigint |  | FK | SI | Associated By User |
| DEVASSOC_Bed_DR | varchar |  | FK | SI | Des Ref PACBed |
| DEVASSOC_Device_DR | bigint |  | FK | SI | Des Ref CTMonitoringDevice |
| DEVASSOC_Hospital_DR | bigint |  | FK | SI | Des Ref CTHospital |
| DEVASSOC_Location_DR | bigint |  | FK | SI | Des Ref CTLoc |
| DEVASSOC_MoveEndDate | date |  |  | SI | Move End Date |
| DEVASSOC_MoveEndTime | time |  |  | SI | Move End Time |
| DEVASSOC_MoveStartDate | date |  |  | SI | Move Start Date |
| DEVASSOC_MoveStartTime | time |  |  | SI | Move Start Time |
| DEVASSOC_PAADM_DR | bigint |  | FK | SI | Des Ref PAAdm |
| DEVASSOC_PAPMI_DR | bigint |  | FK | SI | Des Ref PAPatMas |
| DEVASSOC_Resource_DR | bigint |  | FK | SI | Des Ref RBResource |
| DEVASSOC_Room_DR | bigint |  | FK | SI | Des Ref PACRoom |
| DEVASSOC_Status | varchar |  |  | SI | Status |
| DEVASSOC_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q27Q1 | - |  |  | SI | Plan item |
| Q27Q2 | - |  |  | SI | Other |
| Q27Q3 | - |  |  | SI | Detail and Comment |
| Q27Q4 | - |  |  | SI | Entered by |
| Q27Q5 | - |  |  | SI | Date |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*