# SQLUser.PA_PersonPictures

**Schema:** SQLUser
**Columnas:** 29
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PIC_ParRef | bigint | PK |  | NO | PA_Person Parent Reference |
| PIC_ARPatBillItemObs_DR | varchar |  | FK | SI | [DEPRECATED]Deprecated in TrakCare T2019+ as of TC... |
| PIC_ARPatBillObs_DR | varchar |  | FK | SI | [DEPRECATED]Deprecated in TrakCare T2019+ as of TC... |
| PIC_AccessionNo | varchar |  |  | SI | External Document Accession NO |
| PIC_AnaestOper_DR | varchar |  | FK | SI | Des Ref OR_Anaest_Operation |
| PIC_ApprovalGroupReq_DR | bigint |  | FK | SI | Des Ref PAPayorApprovalGroupRequest |
| PIC_ApprovalReqObs_DR | varchar |  | FK | SI | [DEPRECATED]Deprecated in TrakCare T2019+ as of TC... |
| PIC_ApprovalReq_DR | bigint |  | FK | SI | Des Ref PAPayorApprovalRequest |
| PIC_Childsub | double |  |  | NO | Childsub |
| PIC_DateCreated | date |  |  | SI | Date Created |
| PIC_Desc | varchar |  |  | SI | Description |
| PIC_DocSubType_DR | bigint |  | FK | SI | Des Ref DocSubType |
| PIC_DocType_DR | bigint |  | FK | SI | des ref to PAC_DocumentType |
| PIC_EntryStatus | varchar |  |  | SI | Entry Status (Authorised, Entered, Corrected) |
| PIC_ErrorReason_DR | bigint |  | FK | SI | Des Ref Error Reason |
| PIC_ExternalID | varchar |  |  | SI | External Document ID |
| PIC_Inactive | varchar |  |  | SI | Inactive |
| PIC_IsExternal | varchar |  |  | SI | IS External Document |
| PIC_Origin | varchar |  |  | SI | External Document Origin |
| PIC_ReasonForCorrection_DR | bigint |  | FK | SI | Des Ref Reason For Correction |
| PIC_RowId | varchar |  |  | NO | - |
| PIC_TimeCreated | time |  |  | SI | Time Created |
| PIC_UpdateDate | date |  |  | SI | UpdateDate |
| PIC_UpdateHospital_DR | bigint |  | FK | SI | Des Ref UpdateHospital |
| PIC_UpdateTime | time |  |  | SI | UpdateTime |
| PIC_UpdateUser_DR | bigint |  | FK | SI | Des Ref UpdateUser |
| PIC_UserCreated | bigint |  |  | SI | User Created |
| PIC_WaitingListDR | bigint |  | FK | SI | WaitingListDR |
| PIC_websysDocument | bigint |  |  | SI | websysDocument |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*