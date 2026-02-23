# questionnaire.QTCWI

> Wayne's Index

**Schema:** questionnaire
**Columnas:** 78
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Wayne's Index

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | Dyspnoea on exertion |
| Q04 | varchar |  |  | SI | Palpitation |
| Q05 | varchar |  |  | SI | Tiredness |
| Q06 | varchar |  |  | SI | Preference for heat |
| Q07 | varchar |  |  | SI | Preference for cold |
| Q08 | varchar |  |  | SI | Excessive sweating |
| Q09 | varchar |  |  | SI | Nervousness |
| Q10 | varchar |  |  | SI | Increased appetite |
| Q11 | varchar |  |  | SI | Decreased appetite |
| Q12 | varchar |  |  | SI | Increased weight |
| Q13 | varchar |  |  | SI | Decreased weight |
| Q14 | varchar |  |  | SI | Palpable thyroid |
| Q15 | varchar |  |  | SI | Bruit over thyroid |
| Q16 | varchar |  |  | SI | Exophthalmos |
| Q17 | varchar |  |  | SI | Lid retraction |
| Q18 | varchar |  |  | SI | Lid lag |
| Q19 | varchar |  |  | SI | Hyperkinesis |
| Q20 | varchar |  |  | SI | Hands: hot |
| Q21 | varchar |  |  | SI | Hands: moist |
| Q22 | varchar |  |  | SI | Casual pulse rate > 80/min |
| Q23 | varchar |  |  | SI | Casual pulse rate > 90/min |
| Q24 | varchar |  |  | SI | Atrial fibrillation |
| Q25 | varchar |  |  | SI | Score |
| Q26 | varchar |  |  | SI | Classification |
| Q27 | varchar |  |  | SI | > 19 |
| Q28 | varchar |  |  | SI | Toxic hyperthyroidism |
| Q29 | varchar |  |  | SI | 11 - 19 |
| Q30 | varchar |  |  | SI | Equivocal |
| Q31 | varchar |  |  | SI | < 11 |
| Q32 | varchar |  |  | SI | Euthyroidism |
| Q33 | varchar |  |  | SI | > 19: Toxic hyperthyroidism |
| Q34 | varchar |  |  | SI | 11 - 19: Equivocal |
| Q35 | varchar |  |  | SI | < 11: Euthyroidism |
| Q36 | varchar |  |  | SI | It is a diagnostic index that scores the presence ... |
| Q37 | varchar |  |  | SI | The Wayne’s score is a clinical score that may be ... |
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