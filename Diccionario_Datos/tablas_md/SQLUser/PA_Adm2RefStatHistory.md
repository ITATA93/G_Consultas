# SQLUser.PA_Adm2RefStatHistory

**Schema:** SQLUser
**Columnas:** 77
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Admisión de Pacientes**. Registra episodios de atención hospitalaria. Histórico de cambios.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| REFHIS_ParRef | bigint | PK |  | NO | PA_Adm2 Parent Reference |
| Q01 | - |  |  | SI | Phototherapy Start Date |
| Q02 | - |  |  | SI | Phototherapy Start Time |
| Q03 | - |  |  | SI | Phototherapy Stop Date |
| Q04 | - |  |  | SI | Phototherapy Stop Time |
| Q05 | - |  |  | SI | Oxygen Therapy Start Date |
| Q06 | - |  |  | SI | Oxygen Therapy Start Time |
| Q07 | - |  |  | SI | Oxygen Therapy Stop Date |
| Q08 | - |  |  | SI | Oxygen Therapy Stop Time |
| Q09 | - |  |  | SI | CPAP Ventilation Start Date |
| Q10 | - |  |  | SI | CPAP Ventilation Start Time |
| Q11 | - |  |  | SI | CPAP Ventilation Stop Date |
| Q12 | - |  |  | SI | CPAP Ventilation Stop Time |
| Q13 | - |  |  | SI | aEEG Start Date |
| Q14 | - |  |  | SI | aEEG Start Time |
| Q15 | - |  |  | SI | aEEG Stop Date |
| Q16 | - |  |  | SI | aEEG Stop Time |
| Q17 | - |  |  | SI | Date |
| Q18 | - |  |  | SI | Time |
| Q19 | - |  |  | SI | Date |
| Q20 | - |  |  | SI | Time |
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
| REFHIS_Childsub | double |  |  | NO | Childsub |
| REFHIS_Date | date |  |  | SI | Date |
| REFHIS_DateUpdated | date |  |  | SI | DateUpdated |
| REFHIS_HospitalUpdated_DR | bigint |  | FK | SI | Des Ref CTHospital |
| REFHIS_RefStatusReason_DR | bigint |  | FK | SI | Des Ref RefStatusReason |
| REFHIS_ReferralPriority_DR | bigint |  | FK | SI | Des Ref ReferralPriority |
| REFHIS_ReferralStatus_DR | bigint |  | FK | SI | Des Ref ReferralStatus |
| REFHIS_RowId | varchar |  |  | NO | - |
| REFHIS_Time | time |  |  | SI | Time |
| REFHIS_TimeUpdated | time |  |  | SI | Time Updated |
| REFHIS_TransCareProv_DR | varchar |  | FK | SI | Des Ref TransCareProv |
| REFHIS_TransHospital_DR | bigint |  | FK | SI | Des Ref TransHospital |
| REFHIS_TransLocation_DR | bigint |  | FK | SI | Des Ref TransLocation |
| REFHIS_TransNotes | varchar |  |  | SI | TransNotes |
| REFHIS_TransReason_DR | bigint |  | FK | SI | Des Ref TransReason |
| REFHIS_UserUpdated_DR | bigint |  | FK | SI | Des Ref UserUpdated |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*