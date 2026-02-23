# SQLUser.AR_Batch

**Schema:** SQLUser
**Columnas:** 93
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Cuentas por Cobrar (AR)**. Facturación y cobranza de pacientes.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| BAT_RowId | bigint | PK |  | NO | - |
| BAT_AuxInsType_DR | bigint |  | FK | SI | Des Ref AuxInsType |
| BAT_BatchRunNumber | varchar |  |  | SI | Batch Run Number |
| BAT_BatchStatus | varchar |  |  | SI | BatchStatus |
| BAT_BillDateFrom | date |  |  | SI | Bill Date From |
| BAT_BillDateTo | date |  |  | SI | Bill Date To |
| BAT_BillDesc_DR | bigint |  | FK | SI | Des Ref ARCBillDescription |
| BAT_CareProv_DR | varchar |  | FK | SI | Des Ref CareProv |
| BAT_DateCreated | date |  |  | SI | Date Created |
| BAT_DatePrinted | date |  |  | SI | Date Printed |
| BAT_EpisSubType_DR | bigint |  | FK | SI | Des Ref EpisSubType |
| BAT_EpisodeType | varchar |  |  | SI | Episode Type |
| BAT_Hospital_DR | bigint |  | FK | SI | Des Ref CTHospital |
| BAT_InsType_DR | bigint |  | FK | SI | Des Ref InsType |
| BAT_InterfaceRefFileName | varchar |  |  | SI | Interface Reference File Name |
| BAT_InterfaceRefFileNumber | varchar |  |  | SI | Interface Reference File Number |
| BAT_InterfaceRefNumber | varchar |  |  | SI | Interface Reference Number |
| BAT_InvoiceNumber | varchar |  |  | SI | Invoice Number |
| BAT_LaboratoryBatch | varchar |  |  | SI | Laboratory Batch |
| BAT_Number | varchar |  |  | SI | Batch Number |
| BAT_OriginalNumber | varchar |  |  | SI | Original Batch Number |
| BAT_PrevBatchStatus | varchar |  |  | SI | PrevBatchStatus |
| BAT_PrincipalCPNumber | varchar |  |  | SI | Principal Care Provider Number |
| BAT_ServicingProviderNum | varchar |  |  | SI | ServicingProviderNum |
| BAT_TimeCreated | time |  |  | SI | Time Created |
| BAT_TimePrinted | time |  |  | SI | Time Printed |
| BAT_UserCreated_DR | bigint |  | FK | SI | Des Ref User |
| BAT_UserPrinted_DR | bigint |  | FK | SI | Des Ref UserPrinted |
| Q107 | - |  |  | SI | Nombre Madre |
| Q108 | - |  |  | SI | Nombre Padre |
| Q109 | - |  |  | SI | Uso de  Tuto |
| Q110 | - |  |  | SI | Comentario uso de Tuto |
| Q111 | - |  |  | SI | Uso de Chupete |
| Q112 | - |  |  | SI | Comentario uso de Chupete |
| Q113 | - |  |  | SI | Uso de Mamaderas |
| Q114 | - |  |  | SI | Comentario uso de Mamaderas |
| Q115 | - |  |  | SI | Uso de Pañal |
| Q116 | - |  |  | SI | Comentario uso de Pañal |
| Q117 | - |  |  | SI | Alimentación |
| Q118 | - |  |  | SI | Higiene |
| Q119 | - |  |  | SI | Vestuario |
| Q120 | - |  |  | SI | Deambulación |
| Q121 | - |  |  | SI | Movilización |
| Q122 | - |  |  | SI | Comunicación |
| Q1221 | - |  |  | SI | Eliminación |
| Q123 | - |  |  | SI | Comentario Alimentación |
| Q124 | - |  |  | SI | Comentario Higiene |
| Q125 | - |  |  | SI | Comentario Vestuario |
| Q126 | - |  |  | SI | Comentario Deambulación |
| Q127 | - |  |  | SI | Comentario Movilización |
| Q128 | - |  |  | SI | Comentario Comunicación |
| Q1281 | - |  |  | SI | Comentario Eliminación |
| Q170 | - |  |  | SI | Profesional de Salud |
| QUESAnaDR | - |  |  | SI | Anaesthesia |
| QUESAnaOperationDR | - |  |  | SI | Operation |
| QUESConsultDR | - |  |  | SI | Consult |
| QUESCopiedComments | - |  |  | SI | Copied Comments |
| QUESCopiedDate | - |  |  | SI | Copied Date |
| QUESCopiedEpDR | - |  |  | SI | Copied Episode |
| QUESCopiedSourceDR | - |  |  | SI | Copied Source DR |
| QUESCopiedTime | - |  |  | SI | Copied Time |
| QUESCopiedUserDR | - |  |  | SI | Copied User |
| QUESCreateDate | - |  |  | SI | Creation Date |
| QUESCreateTime | - |  |  | SI | Creation Time |
| QUESCreateUserDR | - |  |  | SI | Creation User |
| QUESDate | - |  |  | SI | Last Update Date |
| QUESErrorReasonDR | - |  |  | SI | Error Reason |
| QUESFHResidentDR | - |  |  | SI | Resident |
| QUESMRClinicalPathWaysDR | - |  |  | SI | Clinical Pathway |
| QUESNRCarePlanIssuesDR | - |  |  | SI | Nurse Care Plan Issues |
| QUESOEOrdExecDR | - |  |  | SI | Order Execution |
| QUESORPreanaestheticConsultDR | - |  |  | SI | Preanaesthetic Consultation |
| QUESObsEntryDR | - |  |  | SI | Observation Entry |
| QUESOperRoomDR | - |  |  | SI | Operating Room |
| QUESPAAdmDR | - |  |  | SI | Admission |
| QUESPAAdverseEventDR | - |  |  | SI | Adverse Event |
| QUESPAPatMasDR | - |  |  | SI | Patient |
| QUESPAPregnancyDR | - |  |  | SI | Pregnancy |
| QUESPAWaitingListDR | - |  |  | SI | Waiting List |
| QUESPathwayItemDR | - |  |  | SI | Pathway Item |
| QUESPrePostExamOEOrdItemDR | - |  |  | SI | Pre/Post Exam OrdItem |
| QUESRBAppointmentDR | - |  |  | SI | Appointments |
| QUESRBApptOutcomeDR | - |  |  | SI | Appointment Outcome |
| QUESRBApptSlotDR | - |  |  | SI | Appointment Slot |
| QUESReasonForCorrectionDR | - |  |  | SI | Reason for Correction |
| QUESSSUserDefWindowDR | - |  |  | SI | Questionnaire |
| QUESScore | - |  |  | SI | Score |
| QUESSecondUserDR | - |  |  | SI | Second Signature |
| QUESStatusDR | - |  |  | SI | Status |
| QUESTextResultDR | - |  |  | SI | Text Result |
| QUESTime | - |  |  | SI | Last Update Time |
| QUESTransactionDR | - |  |  | SI | Transaction |
| QUESUserDR | - |  |  | SI | Last Update User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*