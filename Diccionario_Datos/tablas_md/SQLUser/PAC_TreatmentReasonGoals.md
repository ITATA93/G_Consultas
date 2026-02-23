# SQLUser.PAC_TreatmentReasonGoals

**Schema:** SQLUser
**Columnas:** 84
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PACTG_ParRef | bigint | PK |  | NO | PACTreatmentReason Parent Reference |
| PACTG_Childsub | double |  |  | NO | Childsub |
| PACTG_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| PACTG_CreatedDate | date |  |  | SI | Created Date |
| PACTG_CreatedTime | time |  |  | SI | Created Time |
| PACTG_CreatedUser_DR | bigint |  | FK | SI | Created User |
| PACTG_Goal_DR | bigint |  | FK | SI | Des Ref NRCCarePlanGoal |
| PACTG_RowId | varchar |  |  | NO | - |
| PACTG_UpdatedDate | date |  |  | SI | Updated Date |
| PACTG_UpdatedTime | time |  |  | SI | Updated Time |
| PACTG_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q04 | - |  |  | SI | Altered mental status: GCS ≤ 15 |
| Q05 | - |  |  | SI | Respiratory rate ≥ 22 bpm |
| Q06 | - |  |  | SI | Systolic BP ≤ 100 mmHg |
| Q07 | - |  |  | SI | Score |
| Q08 | - |  |  | SI | Classification |
| Q09 | - |  |  | SI | 0 |
| Q10 | - |  |  | SI | Patient with suspected infection not in the intens... |
| Q11 | - |  |  | SI | 1 |
| Q12 | - |  |  | SI | Patient with suspected infection not in the intens... |
| Q13 | - |  |  | SI | 2 |
| Q14 | - |  |  | SI | Patient with suspected infection not in the intens... |
| Q15 | - |  |  | SI | 3 |
| Q16 | - |  |  | SI | Patient with suspected infection not in the intens... |
| Q17 | - |  |  | SI | 0: Patient with suspected infection not in the int... |
| Q18 | - |  |  | SI | 1: Patient with suspected infection not in the int... |
| Q19 | - |  |  | SI | 2: Patient with suspected infection not in the int... |
| Q20 | - |  |  | SI | 3: Patient with suspected infection not in the int... |
| Q21 | - |  |  | SI | The qSOFA score (also known as quickSOFA) is a bed... |
| Q22 | - |  |  | SI | 1% risk |
| Q23 | - |  |  | SI | of a bad outcome. |
| Q24 | - |  |  | SI | Sepsis considered |
| Q25 | - |  |  | SI | unlikely |
| Q26 | - |  |  | SI | 3% risk |
| Q27 | - |  |  | SI | of a bad outcome. Sepsis considered |
| Q28 | - |  |  | SI | possible. |
| Q29 | - |  |  | SI | 6% risk |
| Q30 | - |  |  | SI | of a bad outcome. Sepsis considered |
| Q31 | - |  |  | SI | likely. |
| Q32 | - |  |  | SI | 23% risk |
| Q33 | - |  |  | SI | of a bad outcome. Sepsis considered |
| Q34 | - |  |  | SI | very likely. |
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