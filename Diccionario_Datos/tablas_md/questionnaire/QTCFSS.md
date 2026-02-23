# questionnaire.QTCFSS

> Fatigue Severity Scale

**Schema:** questionnaire
**Columnas:** 69
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Fatigue Severity Scale

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | Select a number from 1 to 7, depending on how appr... |
| Q04 | varchar |  |  | SI | A low value indicates that the statement is not ve... |
| Q05 | varchar |  |  | SI | During the past week, I have found that: |
| Q06 | varchar |  |  | SI | My motivation is lower when I am fatigued. |
| Q07 | varchar |  |  | SI | Exercise brings on my fatigue. |
| Q08 | varchar |  |  | SI | I am easily fatigued. |
| Q09 | varchar |  |  | SI | Fatigue interferes with my physical functioning. |
| Q10 | varchar |  |  | SI | Fatigue causes frequent problems for me. |
| Q11 | varchar |  |  | SI | My fatigue prevents sustained physical functioning... |
| Q12 | varchar |  |  | SI | Fatigue interferes with carrying out certain dutie... |
| Q13 | varchar |  |  | SI | Fatigue is among my three most disabling symptoms. |
| Q14 | varchar |  |  | SI | Fatigue interferes with my work, family, or social... |
| Q15 | varchar |  |  | SI | The scoring is done by calculating the average res... |
| Q16 | varchar |  |  | SI | People with depression alone score about 4.5. But ... |
| Q17 | varchar |  |  | SI | The Fatigue Severity Scale (FSS) is a scored quest... |
| Q18 | varchar |  |  | SI | Please find the details of the score interpretatio... |
| Q19 | varchar |  |  | SI | Please find the details of the score interpretatio... |
| Q20 | varchar |  |  | SI | Minimum Score = 1 |
| Q21 | varchar |  |  | SI | Maximum Score = 7 |
| Q22 | varchar |  |  | SI | People with depression alone score about 4.5. |
| Q23 | varchar |  |  | SI | People with fatigue related to Multiple Sclerosis ... |
| Q24 | varchar |  |  | SI | FSS Score |
| Q25 | varchar |  |  | SI | Score |
| Q26 | varchar |  |  | SI | Classification |
| Q27 | varchar |  |  | SI | 1 - 7 |
| Q28 | varchar |  |  | SI | 1 - 7: Please find the details of the score interp... |
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