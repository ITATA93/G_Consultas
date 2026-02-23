# SQLUser.PA_AdmLoc

**Schema:** SQLUser
**Columnas:** 70
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Admisión de Pacientes**. Registra episodios de atención hospitalaria.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LOC_ParRef | bigint | PK |  | NO | PA_Adm Parent Reference |
| LOC_CTLOC_DR | bigint |  | FK | SI | Des Ref CTLOC |
| LOC_Childsub | double |  |  | NO | Childsub |
| LOC_RowId | varchar |  |  | NO | - |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Tuberculosis (TB) contact |
| Q04 | - |  |  | SI | Tuberculin skin test (Mantoux test) |
| Q05 | - |  |  | SI | Nutritional status |
| Q06 | - |  |  | SI | Body weight based on present body weight |
| Q07 | - |  |  | SI | Fever of unknown origin |
| Q08 | - |  |  | SI | Lymphadenopathy (Cervical, axillary, inguinal) |
| Q09 | - |  |  | SI | Joint swelling (Hip, knee, vertebral, phalangeal) |
| Q10 | - |  |  | SI | Chest X-ray |
| Q11 | - |  |  | SI | Chest X-ray is not considered to be a main diagnos... |
| Q12 | - |  |  | SI | 1. Positive tuberculosis diagnosis if total score ... |
| Q13 | - |  |  | SI | 2. Body weight based on present body weight |
| Q14 | - |  |  | SI | 3. Fever and cough relevant if no response to stan... |
| Q15 | - |  |  | SI | 4. Chest X-ray is not considered to be a main diag... |
| Q16 | - |  |  | SI | 5. Evaluated for accelerated Bacillus Calmette-Gue... |
| Q17 | - |  |  | SI | 6. Hospital referral to be made for children < 5 y... |
| Q18 | - |  |  | SI | 7. Isoniazid (INH) prophylaxis to be prescribed fo... |
| Q19 | - |  |  | SI | Score |
| Q20 | - |  |  | SI | Classification |
| Q21 | - |  |  | SI | 0 - 5 |
| Q22 | - |  |  | SI | Not indicative of a tuberculosis diagnosis |
| Q23 | - |  |  | SI | ≥ 6 |
| Q24 | - |  |  | SI | Positive tuberculosis diagnosis |
| Q25 | - |  |  | SI | Chronic cough |
| Q26 | - |  |  | SI | A tool to aid the diagnosis of tuberculosis create... |
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