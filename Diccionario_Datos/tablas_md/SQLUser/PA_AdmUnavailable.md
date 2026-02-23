# SQLUser.PA_AdmUnavailable

**Schema:** SQLUser
**Columnas:** 73
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Admisión de Pacientes**. Registra episodios de atención hospitalaria.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| UNAV_ParRef | bigint | PK |  | NO | PA_Adm Parent Reference |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Number of exchanges required |
| Q04 | - |  |  | SI | Frequency of exchange |
| Q05 | - |  |  | SI | Dummy1 |
| Q06 | - |  |  | SI | Patient access |
| Q07 | - |  |  | SI | Pre-haematocrit (%) |
| Q08 | - |  |  | SI | Replacement fluid volume (mls) |
| Q09 | - |  |  | SI | Fresh frozen plasma (mls) |
| Q10 | - |  |  | SI | Albumin 4% (mls) |
| Q11 | - |  |  | SI | Other fluid |
| Q12 | - |  |  | SI | Other fluid volume (mls) |
| Q13 | - |  |  | SI | Pre-blood pump rate (mls/hr) |
| Q14 | - |  |  | SI | Heparin |
| Q15 | - |  |  | SI | Prescription notes |
| Q16 | - |  |  | SI | Target blood flow rate: 200mls/min |
| Q17 | - |  |  | SI | Target filtration fraction: 25% |
| Q18 | - |  |  | SI | Prescribing medical officer |
| Q19 | - |  |  | SI | Other (please specify) |
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
| UNAV_Childsub | double |  |  | NO | Childsub |
| UNAV_DateFrom | date |  |  | SI | Date From |
| UNAV_DateTo | date |  |  | SI | DateTo |
| UNAV_DaysOfTheWeek | varchar |  |  | SI | DaysOfTheWeek |
| UNAV_ReasonText | varchar |  |  | SI | ReasonText |
| UNAV_Reason_DR | bigint |  | FK | SI | Des Ref Reason |
| UNAV_RowId | varchar |  |  | NO | - |
| UNAV_TimeFrom | time |  |  | SI | TimeFrom |
| UNAV_TimeTo | time |  |  | SI | TimeTo |
| UNAV_UpdateDate | date |  |  | SI | UpdateDate |
| UNAV_UpdateTime | time |  |  | SI | UpdateTime |
| UNAV_UpdateUserHospital_DR | bigint |  | FK | SI | Des Ref UpdateUserHospital |
| UNAV_UpdateUser_DR | bigint |  | FK | SI | Des Ref UpdateUser |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*