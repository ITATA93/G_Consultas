# SQLUser.OE_ReviewItems

**Schema:** SQLUser
**Columnas:** 63
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ITM_ParRef | bigint | PK |  | NO | OE_Review Parent Reference |
| ITM_Adm_DR | bigint |  | FK | SI | Des Ref PAAdm |
| ITM_Childsub | double |  |  | NO | Childsub |
| ITM_OrdItem_DR | varchar |  | FK | SI | Des Ref OEOrdItem |
| ITM_OrdPhRevwStat_DR | bigint |  | FK | SI | Des Ref OECPharmacyReviewStatus |
| ITM_RowId | varchar |  |  | NO | - |
| Q01 | - |  |  | SI | 1. What is your age group? |
| Q02 | - |  |  | SI | 2. Gender? |
| Q03 | - |  |  | SI | 3. How far on average can you walk? (a block is 20... |
| Q04 | - |  |  | SI | 4. Which gait aid do you use? (more often than not... |
| Q05 | - |  |  | SI | 5. Do you use community supports? (home help, meal... |
| Q06 | - |  |  | SI | (home help, meals on wheels, district nursing) |
| Q07 | - |  |  | SI | 6. Will you live with someone who can care for you... |
| Q08 | - |  |  | SI | Score < 6 = extended inpatient rehabilitation (com... |
| Q09 | - |  |  | SI | Score 6 – 9 = Directly home after additional acute... |
| Q10 | - |  |  | SI | Score > 9 = Directly home |
| Q12 | - |  |  | SI | Patients expectation of discharge is also a determ... |
| Q13 | - |  |  | SI | Patient’s preference |
| Q14 | - |  |  | SI | Agreed discharge destination |
| Q15 | - |  |  | SI | Patient Signature |
| Q15UDt | - |  |  | SI | Patient Signature Last Updated Date |
| Q15UTm | - |  |  | SI | Patient Signature Last Updated Time |
| Q16 | - |  |  | SI | Date |
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