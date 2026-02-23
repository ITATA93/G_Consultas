# SQLUser.PA_Letter

**Schema:** SQLUser
**Columnas:** 65
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LET_RowId | bigint | PK |  | NO | - |
| LET_APPT_DR | varchar |  | FK | SI | Des Ref APPT |
| LET_ApprovalReq_DR | bigint |  | FK | SI | Des Ref PAPayorApprovalRequest |
| LET_CTLetterTemplate_DR | bigint |  | FK | SI | - |
| LET_Checkbox1 | varchar |  |  | SI | General Purpose Checkbox 1 (8/10 extra checkboxes ... |
| LET_Checkbox2 | varchar |  |  | SI | General Purpose Checkbox 2 (9/10 extra checkboxes ... |
| LET_Checkbox3 | varchar |  |  | SI | General Purpose Checkbox 3 (10/10 extra checkboxes... |
| LET_CreateDate | date |  |  | SI | Create Date |
| LET_CreateTime | time |  |  | SI | Create Time |
| LET_DMPConnexionSecrete | varchar |  |  | SI | Secret connection to DMP (7/10 extra checkboxes fo... |
| LET_DMPDoNotSendToDMP | varchar |  |  | SI | Do not send the validated document to the DMP (1/1... |
| LET_DMPNoVisibilityPS | varchar |  |  | SI | Document hidden from care provider in the DMP (3/1... |
| LET_DMPNoVisibilityPatient | varchar |  |  | SI | Document not visible to patient in DMP (2/10 extra... |
| LET_DMPNoVisibilityRepresentantLegal | varchar |  |  | SI | Document not visible to the patients legal represe... |
| LET_DSSAudit_DR | bigint |  | FK | SI | Des Ref DSS Audit |
| LET_DeliverySentTo | varchar |  |  | SI | Letter Delivery Sent To |
| LET_DeliveryType | varchar |  |  | SI | Letter Delivery Type |
| LET_DistList | varchar |  |  | SI | Distribute List |
| LET_HTMLRichText | bigint |  |  | SI | - |
| LET_LastPrintDate | date |  |  | SI | LastPrint Date |
| LET_LastPrintHospital_DR | bigint |  | FK | SI | Des Ref Hospital |
| LET_LastPrintTime | time |  |  | SI | Print Time |
| LET_LastPrintUser_DR | bigint |  | FK | SI | UserPrint |
| LET_LastUpdateHospital_DR | bigint |  | FK | SI | Des Ref Hospital |
| LET_LetterType_DR | bigint |  | FK | SI | Des Ref PACLetterType |
| LET_Loc_DR | bigint |  | FK | SI | Des Ref CTLoc |
| LET_MSSSendToMSSPatient | varchar |  |  | SI | Send to patient secure health messaging system (5/... |
| LET_MSSSendToMSSPro | varchar |  |  | SI | Send to Care Provider secure health messaging syst... |
| LET_NoOfCopies | integer |  |  | SI | No Of Copies |
| LET_OtherRecipients | varchar |  |  | SI | OtherRecipients |
| LET_PAADM_DR | bigint |  | FK | SI | Des Ref PAADM |
| LET_Person_DR | bigint |  | FK | SI | Des Ref Person |
| LET_PlainRichText | bigint |  |  | SI | - |
| LET_ProvideCopyToPatient | varchar |  |  | SI | Provide a copy to patient |
| LET_RBOperatingRoom_DR | bigint |  | FK | SI | Des Ref RBOperatingRoom |
| LET_SickNotesStatus | varchar |  |  | SI | Sick Notes Status |
| LET_SickNotesStatusReason | varchar |  |  | SI | Sick Notes Status Reason for Change |
| LET_Signature1 | longvarbinary |  |  | SI | Signature 1 |
| LET_Signature2 | longvarbinary |  |  | SI | Signature 2 |
| LET_Signature3 | longvarbinary |  |  | SI | Signature 3 |
| LET_Signature4 | longvarbinary |  |  | SI | Signature 4 |
| LET_Signature5 | longvarbinary |  |  | SI | Signature 5 |
| LET_Signature6 | longvarbinary |  |  | SI | Signature 6 |
| LET_Signature7 | longvarbinary |  |  | SI | Signature 7 |
| LET_Signature8 | longvarbinary |  |  | SI | Signature 8 |
| LET_SignatureDate1 | date |  |  | SI | Signature 1 Date |
| LET_SignatureDate2 | date |  |  | SI | Signature 2 Date |
| LET_SignatureDate3 | date |  |  | SI | Signature 3 Date |
| LET_SignatureDate4 | date |  |  | SI | Signature 4 Date |
| LET_SignatureDate5 | date |  |  | SI | Signature 5 Date |
| LET_SignatureDate6 | date |  |  | SI | Signature 6 Date |
| LET_SignatureDate7 | date |  |  | SI | Signature 7 Date |
| LET_SignatureDate8 | date |  |  | SI | Signature 8 Date |
| LET_SignatureTime1 | time |  |  | SI | Signature 1 Time |
| LET_SignatureTime2 | time |  |  | SI | Signature 2 Time |
| LET_SignatureTime3 | time |  |  | SI | Signature 3 Time |
| LET_SignatureTime4 | time |  |  | SI | Signature 4 Time |
| LET_SignatureTime5 | time |  |  | SI | Signature 5 Time |
| LET_SignatureTime6 | time |  |  | SI | Signature 6 Time |
| LET_SignatureTime7 | time |  |  | SI | Signature 7 Time |
| LET_SignatureTime8 | time |  |  | SI | Signature 8 Time |
| LET_UpdateDate | date |  |  | SI | Update Date |
| LET_UpdateTime | time |  |  | SI | Update Time |
| LET_UserUpdate_DR | bigint |  | FK | SI | UserUpdate |
| LET_WaitList_DR | bigint |  | FK | SI | Des Ref WaitList |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*