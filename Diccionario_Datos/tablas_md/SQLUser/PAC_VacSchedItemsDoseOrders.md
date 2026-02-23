# SQLUser.PAC_VacSchedItemsDoseOrders

**Schema:** SQLUser
**Columnas:** 70
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ORD_ParRef | varchar | PK |  | NO | PAC_VaccinationDesease Parent Reference |
| ORD_ARCIM_DR | varchar |  | FK | SI | Des Ref ARCItmMast |
| ORD_Childsub | double |  |  | NO | Childsub |
| ORD_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| ORD_CreatedDate | date |  |  | SI | Created Date |
| ORD_CreatedTime | time |  |  | SI | Created Time |
| ORD_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ORD_DateFrom | date |  |  | SI | Date From |
| ORD_DateTo | date |  |  | SI | Date To |
| ORD_RowId | varchar |  |  | NO | - |
| ORD_UpdatedDate | date |  |  | SI | Updated Date |
| ORD_UpdatedTime | time |  |  | SI | Updated Time |
| ORD_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Device applied date |
| Q02 | - |  |  | SI | Device applied time |
| Q03 | - |  |  | SI | New order required date |
| Q04 | - |  |  | SI | New order required time |
| Q05 | - |  |  | SI | Patient informed regarding reason and alternatives... |
| Q06 | - |  |  | SI | The patient received periodic explanations regardi... |
| Q07 | - |  |  | SI | Restraint education provided to |
| Q08 | - |  |  | SI | Others (please specify) |
| Q09 | - |  |  | SI | Type of restraint |
| Q10 | - |  |  | SI | Others (please specify) |
| Q11 | - |  |  | SI | Patient exhibits behaviour that is harmful to self... |
| Q12 | - |  |  | SI | Others (please specify) |
| Q13 | - |  |  | SI | Alternative interventions attempted before placing... |
| Q14 | - |  |  | SI | Others (please specify) |
| Q15 | - |  |  | SI | Patient response to interventions attempted |
| Q16 | - |  |  | SI | Date |
| Q17 | - |  |  | SI | Time |
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