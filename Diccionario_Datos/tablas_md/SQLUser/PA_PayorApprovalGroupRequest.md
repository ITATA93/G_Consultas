# SQLUser.PA_PayorApprovalGroupRequest

**Schema:** SQLUser
**Columnas:** 18
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PAPPGRPREQ_RowId | bigint | PK |  | NO | - |
| PAPPGRPREQ_Adm_DR | bigint |  | FK | SI | Des Ref PAAdm |
| PAPPGRPREQ_ApprBatchReqStatus_DR | bigint |  | FK | SI | Des Ref BLCApprGroupRequestStatus |
| PAPPGRPREQ_ApprReqSource_DR | bigint |  | FK | SI | Des Ref BLCApprovalRequestSource |
| PAPPGRPREQ_ApprovalBatchNumber | varchar |  |  | SI | Approval Batch Number |
| PAPPGRPREQ_ApprovedAmount | double |  |  | SI | Approval Batch Approved Amount |
| PAPPGRPREQ_AssignUser_DR | bigint |  | FK | SI | Des Ref SSUser - User Assigned |
| PAPPGRPREQ_Extension | varchar |  |  | SI | Extension |
| PAPPGRPREQ_GroupRequestDesc_DR | bigint |  | FK | SI | Des Ref BLCApprGroupRequestDescription - Approval ... |
| PAPPGRPREQ_PrescNo | varchar |  |  | SI | Prescription No |
| PAPPGRPREQ_Remarks | varchar |  |  | SI | Remarks |
| PAPPGRPREQ_RequestAmount | double |  |  | SI | Approval Batch Request Amount |
| PAPPGRPREQ_RequestDate | date |  |  | NO | Request Date |
| PAPPGRPREQ_ResponseDate | date |  |  | SI | Response Date |
| PAPPGRPREQ_UpdateDate | date |  |  | SI | Update Date |
| PAPPGRPREQ_UpdateHospital_DR | bigint |  | FK | SI | Des Ref CTHospital |
| PAPPGRPREQ_UpdateTime | time |  |  | SI | Update Time |
| PAPPGRPREQ_UpdateUser_DR | bigint |  | FK | SI | Des Ref SSUser |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*