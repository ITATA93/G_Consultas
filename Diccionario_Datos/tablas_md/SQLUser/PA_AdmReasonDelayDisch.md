# SQLUser.PA_AdmReasonDelayDisch

**Schema:** SQLUser
**Columnas:** 75
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Admisión de Pacientes**. Registra episodios de atención hospitalaria.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| READEL_ParRef | bigint | PK |  | NO | PA_Adm Parent Reference |
| Q01 | - |  |  | SI | Tone |
| Q02 | - |  |  | SI | Level of consciousness |
| Q03 | - |  |  | SI | Fits (Clinically apparent seizures) |
| Q04 | - |  |  | SI | Posture |
| Q05 | - |  |  | SI | Moro Reflex |
| Q06 | - |  |  | SI | Grasp Reflex |
| Q07 | - |  |  | SI | Suck Reflex |
| Q08 | - |  |  | SI | Respiratory Pattern |
| Q09 | - |  |  | SI | Fontanelle Tension |
| Q10 | - |  |  | SI | Score |
| Q11 | - |  |  | SI | Classification |
| Q12 | - |  |  | SI | 0 - 10 |
| Q13 | - |  |  | SI | Mild |
| Q14 | - |  |  | SI | 11 - 14 |
| Q15 | - |  |  | SI | Moderate |
| Q16 | - |  |  | SI | 15 - 22 |
| Q17 | - |  |  | SI | Severe |
| Q18 | - |  |  | SI | 0 - 10: Mild |
| Q19 | - |  |  | SI | 11 - 14: Moderate |
| Q20 | - |  |  | SI | 15 - 22: Severe |
| Q21 | - |  |  | SI | The Thompson encephalopathy score is a clinical sc... |
| Q22 | - |  |  | SI | Date |
| Q23 | - |  |  | SI | Time |
| Q24 | - |  |  | SI | Thompson C, Puterman A, Linley L, Hann F, Elst C, ... |
| Q25 | - |  |  | SI | The Thompson encephalopathy score is a clinical sc... |
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
| READEL_Childsub | double |  |  | NO | Childsub |
| READEL_Date | date |  |  | SI | Date |
| READEL_Reason_DR | bigint |  | FK | SI | Des Ref Reason |
| READEL_RowId | varchar |  |  | NO | - |
| READEL_Time | time |  |  | SI | Time |
| READEL_UpdateDate | date |  |  | SI | UpdateDate |
| READEL_UpdateTime | time |  |  | SI | UpdateTime |
| READEL_UpdateUserHospital_DR | bigint |  | FK | SI | Des Ref UpdateUserHospital |
| READEL_UpdateUser_DR | bigint |  | FK | SI | Des Ref UpdateUser |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*