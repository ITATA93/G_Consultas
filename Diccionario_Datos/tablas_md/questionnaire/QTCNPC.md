# questionnaire.QTCNPC

> Neurosurgical Post-Operative Checklist

**Schema:** questionnaire
**Columnas:** 74
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Neurosurgical Post-Operative Checklist

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | Variance |
| Q04 | varchar |  |  | SI | Alert and&nbsp;orientated&nbsp;- Glasgow coma&nbsp... |
| Q05 | varchar |  |  | SI | Variance |
| Q06 | varchar |  |  | SI | Patient received prescribed analgesia and reports ... |
| Q07 | varchar |  |  | SI | Patient provided education on using Patient&nbsp;C... |
| Q08 | varchar |  |  | SI | Variance |
| Q09 | varchar |  |  | SI | Variance |
| Q10 | varchar |  |  | SI | Observations are within acceptable limits and stab... |
| Q11 | varchar |  |  | SI | Variance |
| Q12 | varchar |  |  | SI | Administer oxygen via nasal prongs at 2L/min until... |
| Q13 | varchar |  |  | SI | Variance |
| Q14 | varchar |  |  | SI | Patients fluid intake and output recorded on the f... |
| Q15 | varchar |  |  | SI | Variance |
| Q16 | varchar |  |  | SI | Drain remained patent and all drainage documented ... |
| Q17 | varchar |  |  | SI | Variance |
| Q18 | varchar |  |  | SI | Patient has voided post operatively (can stand wit... |
| Q19 | varchar |  |  | SI | Variance |
| Q20 | varchar |  |  | SI | All medication and intravenous (IV) fluid administ... |
| Q21 | varchar |  |  | SI | Variance |
| Q22 | varchar |  |  | SI | Post-operative wash attended |
| Q23 | varchar |  |  | SI | Variance |
| Q24 | varchar |  |  | SI | Wound site remained free from haematoma |
| Q25 | varchar |  |  | SI | Variance |
| Q26 | varchar |  |  | SI | Patient preformed deep breathing and coughing exer... |
| Q27 | varchar |  |  | SI | Variance |
| Q28 | varchar |  |  | SI | Patient position and movement as per post operativ... |
| Q29 | varchar |  |  | SI | Variance |
| Q30 | varchar |  |  | SI | Patient mobilised in/out of bed while maintaining ... |
| Q31 | varchar |  |  | SI | Variance |
| Q32 | varchar |  |  | SI | Referrals&nbsp;arranged as necessary |
| Q33 | varchar |  |  | SI | Variance |
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