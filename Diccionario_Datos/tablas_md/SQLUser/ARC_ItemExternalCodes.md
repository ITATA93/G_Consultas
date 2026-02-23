# SQLUser.ARC_ItemExternalCodes

**Schema:** SQLUser
**Columnas:** 74
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Arquetipo de configuración**. Definición base del sistema. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| EXT_ParRef | varchar | PK |  | NO | ARC_ItmMast Parent Reference |
| EXT_AuxInsType_DR | bigint |  | FK | SI | Des Ref AuxInsType |
| EXT_BillSub_DR | varchar |  | FK | SI | Des Ref Bill Sub |
| EXT_CTLOC_DR | bigint |  | FK | SI | Des Ref CTLOC_DR |
| EXT_Childsub | double |  |  | NO | Childsub |
| EXT_Code | varchar |  |  | NO | Code |
| EXT_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| EXT_CreatedDate | date |  |  | SI | Created Date |
| EXT_CreatedTime | time |  |  | SI | Created Time |
| EXT_CreatedUser_DR | bigint |  | FK | SI | Created User |
| EXT_DEfaultSend | varchar |  |  | SI | Default Send |
| EXT_DateFrom | date |  |  | NO | Date From |
| EXT_DateTo | date |  |  | SI | Date To |
| EXT_DefaultReceive | varchar |  |  | SI | Default Receive |
| EXT_Desc | varchar |  |  | SI | Description |
| EXT_HL7SendingApp | varchar |  |  | SI | HL7SendingApp |
| EXT_HL7SendingFacility | varchar |  |  | SI | HL7SendingFacility |
| EXT_InsType_DR | bigint |  | FK | SI | Des Ref InsType |
| EXT_RowId | varchar |  |  | NO | - |
| EXT_TestItemSequnce | varchar |  |  | SI | Test Item Sequence |
| EXT_UpdatedDate | date |  |  | SI | Updated Date |
| EXT_UpdatedTime | time |  |  | SI | Updated Time |
| EXT_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q02 | - |  |  | SI | MES |
| Q03 | - |  |  | SI | AÑO |
| Q04 | - |  |  | SI | TOTAL DÍAS CAMAS OCUPADAS MENORES DE 15 AÑOS |
| Q05 | - |  |  | SI | TOTAL DÍAS CAMAS OCUPADAS MAYORES DE 15 AÑOS |
| Q06 | - |  |  | SI | DÍAS CAMAS OCUPADAS CON ACOMPAÑAMIENTO DIURNO MENO... |
| Q07 | - |  |  | SI | DÍAS CAMAS OCUPADAS CON ACOMPAÑAMIENTO DIURNO MAYO... |
| Q08 | - |  |  | SI | DÍAS CAMAS OCUPADAS CON ACOMPAÑAMIENTO DIURNO  MÍN... |
| Q09 | - |  |  | SI | DÍAS CAMAS OCUPADAS CON ACOMPAÑAMIENTO DIURNO MÍNI... |
| Q10 | - |  |  | SI | DÍAS CAMAS OCUPADAS CON ACAMPAÑAMIENTO NOCTURNO ME... |
| Q11 | - |  |  | SI | DÍAS CAMAS OCUPADAS CON ACAMPAÑAMIENTO NOCTURNO MA... |
| QHR | - |  |  | SI | ESTABLECIMIENTO |
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