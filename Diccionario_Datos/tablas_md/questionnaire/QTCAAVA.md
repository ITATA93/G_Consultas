# questionnaire.QTCAAVA

> Advance Audiovestibular Assessment

**Schema:** questionnaire
**Columnas:** 126
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Advance Audiovestibular Assessment

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date of examination |
| Q02 | varchar |  |  | SI | Symptoms are getting |
| Q03 | varchar |  |  | SI | Description of spells |
| Q04 | varchar |  |  | SI | If other, specify |
| Q05 | varchar |  |  | SI | Length of time spells occur |
| Q06 | varchar |  |  | SI | If other, specify |
| Q07 | varchar |  |  | SI | What increases symptoms? |
| Q08 | varchar |  |  | SI | What decreases symptoms? |
| Q09 | varchar |  |  | SI | Hearing impairments |
| Q10 | varchar |  |  | SI | If other, specify |
| Q11 | varchar |  |  | SI | Changes in hearing since onset |
| Q12 | varchar |  |  | SI | If other, specify |
| Q13 | varchar |  |  | SI | Visual changes since onset |
| Q14 | varchar |  |  | SI | If other, specify |
| Q15 | varchar |  |  | SI | Recent falls |
| Q16 | varchar |  |  | SI | If other, specify |
| Q17 | varchar |  |  | SI | History of migraines |
| Q18 | varchar |  |  | SI | If other, specify |
| Q19 | varchar |  |  | SI | Previous treatments |
| Q20 | varchar |  |  | SI | Vestibulo-Ocular Reflex (VOR) head thrust |
| Q21 | varchar |  |  | SI | Spontaneous nystagmus |
| Q22 | varchar |  |  | SI | Gaze-evoked nystagmus with fixation present |
| Q23 | varchar |  |  | SI | VOR head thrust (posterior canal function) |
| Q24 | varchar |  |  | SI | Primary |
| Q25 | varchar |  |  | SI | Right |
| Q26 | varchar |  |  | SI | Left |
| Q27 | varchar |  |  | SI | Post-horizontal head-shaking nystagmus (+/-) |
| Q28 | varchar |  |  | SI | Gaze-evoked nystagmus with fixation suppressed |
| Q29 | varchar |  |  | SI | Direction |
| Q30 | varchar |  |  | SI | Primary |
| Q31 | varchar |  |  | SI | Right |
| Q32 | varchar |  |  | SI | Left |
| Q33 | varchar |  |  | SI | Heave test (L) |
| Q34 | varchar |  |  | SI | Heave test (R) |
| Q35 | varchar |  |  | SI | Smooth pursuit |
| Q36 | varchar |  |  | SI | Saccades |
| Q37 | varchar |  |  | SI | Vestibulo-Ocular Reflex (VOR) cancellation |
| Q38 | varchar |  |  | SI | Static visual acuity using LogMAR scale |
| Q39 | varchar |  |  | SI | Dynamic visual acuity |
| Q40 | varchar |  |  | SI | Other oculomotor / vestibular test |
| Q41 | varchar |  |  | SI | Left Hallpike (+/-) |
| Q42 | varchar |  |  | SI | Right Hallpike (+/-) |
| Q43 | varchar |  |  | SI | Roll test (+/-) |
| Q44 | varchar |  |  | SI | Comments |
| Q45 | varchar |  |  | SI | Dizziness Handicap Inventory (DHI) |
| Q46 | varchar |  |  | SI | Dynamic Gait Index (DGI) |
| Q47 | varchar |  |  | SI | Berg balance score |
| Q48 | varchar |  |  | SI | Timed Up and Go (TUG) test |
| Q49 | varchar |  |  | SI | Activities-specific Balance Confidence (ABC) scale |
| Q50 | varchar |  |  | SI | Motion Sensitivity Quotient (MSQ) |
| Q51 | varchar |  |  | SI | Other |
| Q52 | varchar |  |  | SI | Cervical spine complaints |
| Q53 | varchar |  |  | SI | Cervical pain |
| Q54 | varchar |  |  | SI | Cervical spine Range of Motion (ROM) |
| Q55 | varchar |  |  | SI | If impaired, specify |
| Q56 | varchar |  |  | SI | Lower Extremities Range of Motion (ROM) |
| Q57 | varchar |  |  | SI | Hip (L) |
| Q58 | varchar |  |  | SI | Hip (R) |
| Q59 | varchar |  |  | SI | Knee (L) |
| Q60 | varchar |  |  | SI | Knee (R) |
| Q61 | varchar |  |  | SI | Ankle (L) |
| Q62 | varchar |  |  | SI | Ankle (R) |
| Q63 | varchar |  |  | SI | Lower Extremities Strength |
| Q64 | varchar |  |  | SI | Hip (L) |
| Q65 | varchar |  |  | SI | Hip (R) |
| Q66 | varchar |  |  | SI | Knee Extension (L) |
| Q67 | varchar |  |  | SI | Knee Extension (R) |
| Q68 | varchar |  |  | SI | Ankle (L) |
| Q69 | varchar |  |  | SI | Ankle (R) |
| Q70 | varchar |  |  | SI | Posture |
| Q71 | varchar |  |  | SI | Light touch |
| Q72 | varchar |  |  | SI | If impaired / absent, specify |
| Q73 | varchar |  |  | SI | Rapid alt movements |
| Q74 | varchar |  |  | SI | Heel to shin |
| Q75 | varchar |  |  | SI | Finger to nose |
| Q76 | varchar |  |  | SI | Past pointing |
| Q77 | varchar |  |  | SI | Clinical Test of Sensory Interaction for Balance (... |
| Q82 | varchar |  |  | SI | Gait |
| Q83 | varchar |  |  | SI | Problem list / functional limitations |
| Q84 | varchar |  |  | SI | If others, specify |
| Q85 | varchar |  |  | SI | Treatment plan (this is only a plan, you need to p... |
| Q86 | varchar |  |  | SI | If other plan, specify |
| Q87 | varchar |  |  | SI | Gaze-evoked nystagmus with fixation present (1st D... |
| Q88 | date |  |  | SI | Date |
| Q89 | time |  |  | SI | Time |
| QUESAnaDR | varchar |  | FK | SI | Anaesthesia |
| QUESAnaOperationDR | varchar |  | FK | SI | Operation |
| QUESConsultDR | varchar |  | FK | SI | Consult |
| QUESCopiedComments | varchar |  |  | SI | Copied Comments |
| QUESCopiedDate | date |  |  | SI | Copied Date |
| QUESCopiedEpDR | bigint |  | FK | SI | Copied Episode |
| QUESCopiedSourceDR | bigint |  | FK | SI | Copied Source DR |
| QUESCopiedTime | time |  |  | SI | Copied Time |
| QUESCopiedUserDR | bigint |  | FK | SI | Copied User |
| QUESCreateDate | date |  |  | SI | Creation Date |
| QUESCreateTime | time |  |  | SI | Creation Time |
| QUESCreateUserDR | bigint |  | FK | SI | Creation User |
| QUESDate | date |  |  | SI | Last Update Date |
| QUESErrorReasonDR | bigint |  | FK | SI | Error Reason |
| QUESFHResidentDR | bigint |  | FK | SI | Resident |
| QUESMRClinicalPathWaysDR | varchar |  | FK | SI | Clinical Pathway |
| QUESNRCarePlanIssuesDR | varchar |  | FK | SI | Nurse Care Plan Issues |
| QUESOEOrdExecDR | varchar |  | FK | SI | Order Execution |
| QUESORPreanaestheticConsultDR | bigint |  | FK | SI | Preanaesthetic Consultation |
| QUESObsEntryDR | varchar |  | FK | SI | Observation Entry |
| QUESOperRoomDR | bigint |  | FK | SI | Operating Room |
| QUESPAAdmDR | bigint |  | FK | SI | Admission |
| QUESPAAdverseEventDR | varchar |  | FK | SI | Adverse Event |
| QUESPAPatMasDR | bigint |  | FK | SI | Patient |
| QUESPAPregnancyDR | bigint |  | FK | SI | Pregnancy |
| QUESPAWaitingListDR | bigint |  | FK | SI | Waiting List |
| QUESPathwayItemDR | varchar |  | FK | SI | Pathway Item |
| QUESPrePostExamOEOrdItemDR | varchar |  | FK | SI | Pre/Post Exam OrdItem |
| QUESRBAppointmentDR | varchar |  | FK | SI | Appointments |
| QUESRBApptOutcomeDR | varchar |  | FK | SI | Appointment Outcome |
| QUESRBApptSlotDR | varchar |  | FK | SI | Appointment Slot |
| QUESReasonForCorrectionDR | bigint |  | FK | SI | Reason for Correction |
| QUESSSUserDefWindowDR | bigint |  | FK | SI | Questionnaire |
| QUESScore | varchar |  |  | SI | Score |
| QUESSecondUserDR | bigint |  | FK | SI | Second Signature |
| QUESStatusDR | bigint |  | FK | SI | Status |
| QUESTextResultDR | bigint |  | FK | SI | Text Result |
| QUESTime | time |  |  | SI | Last Update Time |
| QUESTransactionDR | varchar |  | FK | SI | Transaction |
| QUESUserDR | bigint |  | FK | SI | Last Update User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*