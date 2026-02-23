# questionnaire.QTCPESAS

> Psycho-Existential Symptom Assessment Scale (PeSAS)

**Schema:** questionnaire
**Columnas:** 68
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Psycho-Existential Symptom Assessment Scale (PeSAS)

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | Please use this form to tell us about the symptoms... |
| Q04 | varchar |  |  | SI | Use the scale above to choose a number between 0 a... |
| Q05 | varchar |  |  | SI | Anxiety |
| Q06 | varchar |  |  | SI | Anxiety |
| Q07 | varchar |  |  | SI | Discouragement |
| Q08 | varchar |  |  | SI | Discouragement |
| Q09 | varchar |  |  | SI | Trapped by illness |
| Q10 | varchar |  |  | SI | Trapped by illness |
| Q11 | varchar |  |  | SI | Hopelessness |
| Q12 | varchar |  |  | SI | Hopelessness |
| Q13 | varchar |  |  | SI | Pointlessness |
| Q14 | varchar |  |  | SI | Pointlessness |
| Q15 | varchar |  |  | SI | Loss of control |
| Q16 | varchar |  |  | SI | Loss of control |
| Q17 | varchar |  |  | SI | Loss of roles |
| Q18 | varchar |  |  | SI | Loss of roles |
| Q19 | varchar |  |  | SI | Depression |
| Q20 | varchar |  |  | SI | Depression |
| Q21 | varchar |  |  | SI | Wish to die |
| Q22 | varchar |  |  | SI | Wish to die |
| Q23 | varchar |  |  | SI | Confusion |
| Q24 | varchar |  |  | SI | Confusion |
| Q25 | varchar |  |  | SI | Kissane DW, Appleton J, Lennon J,&nbsp;et al.&nbsp... |
| Q26 | varchar |  |  | SI | Simple synonyms are the use of 2-3 words you can r... |
| Q27 | varchar |  |  | SI | While there are lots of synonyms that could be use... |
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