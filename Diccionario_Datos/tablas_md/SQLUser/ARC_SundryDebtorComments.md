# SQLUser.ARC_SundryDebtorComments

**Schema:** SQLUser
**Columnas:** 81
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Arquetipo de configuración**. Definición base del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CMT_ParRef | bigint | PK |  | NO | ARC_SundryDebtor Parent Reference |
| CMT_Childsub | double |  |  | NO | Childsub |
| CMT_Comments | varchar |  |  | SI | Comments |
| CMT_CreatedDate | date |  |  | SI | Created Date |
| CMT_CreatedTime | time |  |  | SI | Created Time |
| CMT_CreatedUser_DR | bigint |  | FK | SI | Created User |
| CMT_Date | date |  |  | SI | Date |
| CMT_FutureDate | date |  |  | SI | FutureDate |
| CMT_Hospital_DR | bigint |  | FK | SI | Des Ref Hospital |
| CMT_LastUpdateDate | date |  |  | SI | LastUpateDate |
| CMT_LastUpdateHospital_DR | bigint |  | FK | SI | Des Ref LastUpdateHospital |
| CMT_LastUpdateTime | time |  |  | SI | LastUpdateTime |
| CMT_LastUpdateUser_DR | bigint |  | FK | SI | Des Ref LastUpdateUser |
| CMT_OnHold | varchar |  |  | SI | OnHold |
| CMT_RowId | varchar |  |  | NO | - |
| CMT_ShortDesc | varchar |  |  | SI | ShortDesc |
| CMT_Time | time |  |  | SI | Time |
| CMT_UpdatedDate | date |  |  | SI | Updated Date |
| CMT_UpdatedTime | time |  |  | SI | Updated Time |
| CMT_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| CMT_User_DR | bigint |  | FK | SI | Des Ref User |
| Q01 | - |  |  | SI | Condición |
| Q02 | - |  |  | SI | Criterios |
| Q03 | - |  |  | SI | Alteración del estado de conciencia agudo y/o crón... |
| Q04 | - |  |  | SI | Observación |
| Q05 | - |  |  | SI | Alteraciones neurológicas con afectación motriz y/... |
| Q06 | - |  |  | SI | Observación |
| Q07 | - |  |  | SI | Cancer terminal |
| Q08 | - |  |  | SI | Observación |
| Q09 | - |  |  | SI | Demencia en estados avanzados |
| Q10 | - |  |  | SI | Observación |
| Q11 | - |  |  | SI | Artropatías degenerativas severas |
| Q12 | - |  |  | SI | Observación |
| Q13 | - |  |  | SI | Lesiones medulares |
| Q14 | - |  |  | SI | Observación |
| Q15 | - |  |  | SI | Cualquier condición que requiera reposo absoluto |
| Q16 | - |  |  | SI | Observación |
| Q17 | - |  |  | SI | Considerar |
| Q18 | - |  |  | SI | Educar y reforzar cuidados de enfermería |
| Q19 | - |  |  | SI | Observación |
| Q20 | - |  |  | SI | Otras Observaciones |
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