# SQLUser.LBC_BloodProductGroupBloodGroupException

**Schema:** SQLUser
**Columnas:** 81
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Laboratorio**. Parámetros del módulo de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCBPGBGE_ParRef | varchar | PK |  | NO | Parent Blood Product Group |
| LBCBPGBGE_Action | varchar |  |  | SI | Action |
| LBCBPGBGE_PatientBloodGroup_DR | bigint |  | FK | NO | Patient Blood Group |
| LBCBPGBGE_RowID | varchar |  |  | NO | - |
| LBCBPGBGE_UnitBloodGroup_DR | bigint |  | FK | NO | Unit Blood Group |
| Q01 | - |  |  | SI | Reliability of client (Choose one or more) |
| Q02 | - |  |  | SI | Crisis Triage Rating Scale (CTRS)	 |
| Q03 | - |  |  | SI | Rating A: DANGEROUSNESS |
| Q04 | - |  |  | SI | Rating B: SUPPORT SYSTEM |
| Q05 | - |  |  | SI | Rating C: ABILITY TO COOPERATE |
| Q06 | - |  |  | SI | The scale evaluates the person in crisis on a scal... |
| Q07 | - |  |  | SI | 1. Dangerousness |
| Q08 | - |  |  | SI | 2. Support System |
| Q09 | - |  |  | SI | 3. Ability to Cooperate |
| Q10 | - |  |  | SI | The lowest possible score is 3 and the highest pos... |
| Q11 | - |  |  | SI | THE TOTAL CTRS SCORE CALCULATED AND PROVIDED BASED... |
| Q12 | - |  |  | SI | CTRS: Urgency of Response |
| Q13 | - |  |  | SI | 1 – 9: Extreme Urgency – immediate response requir... |
| Q14 | - |  |  | SI | 10: High Urgency – present to emergency department |
| Q15 | - |  |  | SI | 11 – 13: Medium to Low Urgency – see within 24 – 4... |
| Q16 | - |  |  | SI | 14 – 15: Non-urgent – Problem solve with individua... |
| Q17 | - |  |  | SI | CTRS Rating |
| Q18 | - |  |  | SI | Dangerousness |
| Q19 | - |  |  | SI | Support System |
| Q20 | - |  |  | SI | Ability to Cooperate	 |
| Q21 | - |  |  | SI | CTRS Total |
| Q22 | - |  |  | SI | URGENCY OF RESPONSE GUIDELINE |
| Q23 | - |  |  | SI | 3-9 |
| Q24 | - |  |  | SI | Extreme / Severe (Immediate Response Recommended) |
| Q25 | - |  |  | SI | 10 |
| Q26 | - |  |  | SI | High (See within 2 Hours) |
| Q27 | - |  |  | SI | 11 |
| Q28 | - |  |  | SI | Medium (See within 12 hours) |
| Q29 | - |  |  | SI | 12-13 |
| Q30 | - |  |  | SI | Low (See within 48 hours) |
| Q31 | - |  |  | SI | 14-15 |
| Q32 | - |  |  | SI | Non-Urgent (See within 2 weeks) |
| Q33 | - |  |  | SI | The Crisis Triage Rating Scale (CTRS) is intended ... |
| Q34 | - |  |  | SI | Score |
| Q35 | - |  |  | SI | Classification |
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
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*