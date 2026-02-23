# SQLUser.AR_RemittanceAdvice

**Schema:** SQLUser
**Columnas:** 39
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Cuentas por Cobrar (AR)**. Facturación y cobranza de pacientes.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| REMADV_RowId | bigint | PK |  | NO | - |
| ChildQ04DR | - |  |  | SI | Child Reference: Diagnósticos complementarios, Con... |
| Q03Q1 | - |  |  | SI | Procedimiento |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| REMADV_BillDesc_DR | bigint |  | FK | SI | Des Ref ARCBillDescription |
| REMADV_Date1 | date |  |  | SI | Date1 |
| REMADV_Date2 | date |  |  | SI | Date2 |
| REMADV_Date3 | date |  |  | SI | Date3 |
| REMADV_Date4 | date |  |  | SI | Date4 |
| REMADV_Date5 | date |  |  | SI | Date5 |
| REMADV_FacilityID | varchar |  |  | SI | Facility ID |
| REMADV_Hospital_DR | bigint |  | FK | SI | Des Ref CTHospital |
| REMADV_InsType_DR | bigint |  | FK | SI | Des Ref InsType |
| REMADV_ManualUpload | varchar |  |  | SI | Manual Upload |
| REMADV_Number1 | double |  |  | SI | Number1 |
| REMADV_Number2 | double |  |  | SI | Number2 |
| REMADV_Number3 | double |  |  | SI | Number3 |
| REMADV_Number4 | double |  |  | SI | Number4 |
| REMADV_Number5 | double |  |  | SI | Number5 |
| REMADV_RAComment | varchar |  |  | SI | RA Comment |
| REMADV_RAFileName | varchar |  |  | SI | RA File Name |
| REMADV_RANetAmount | double |  |  | SI | RA Net Amount |
| REMADV_RAPaymentAmount | double |  |  | SI | RA Payment Amount |
| REMADV_RAProcessed | varchar |  |  | SI | RA Processed |
| REMADV_RAProcessedDate | date |  |  | SI | RA Processed Date |
| REMADV_RAProcessedUser_DR | bigint |  | FK | SI | RA Processed User |
| REMADV_RATransactionDate | date |  |  | SI | RA Transaction Date |
| REMADV_RATransactionNumber | varchar |  |  | SI | RA Transaction Number |
| REMADV_RAVATAmount | double |  |  | SI | RA VAT Amount |
| REMADV_ReceiverID | varchar |  |  | SI | Receiver ID |
| REMADV_RecordCount | double |  |  | SI | Record Count |
| REMADV_RemitAdviceStatus_DR | bigint |  | FK | SI | Des Ref ARCRemittanceAdviceStatus |
| REMADV_SenderID | varchar |  |  | SI | Sender ID |
| REMADV_Text1 | varchar |  |  | SI | Text1 |
| REMADV_Text2 | varchar |  |  | SI | Text2 |
| REMADV_Text3 | varchar |  |  | SI | Text3 |
| REMADV_Text4 | varchar |  |  | SI | Text4 |
| REMADV_Text5 | varchar |  |  | SI | Text5 |
| REMADV_UserAssign_DR | bigint |  | FK | SI | Des Ref User Assign |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*