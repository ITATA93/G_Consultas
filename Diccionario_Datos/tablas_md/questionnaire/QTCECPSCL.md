# questionnaire.QTCECPSCL

> ECP Session Checklist

**Schema:** questionnaire
**Columnas:** 85
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* ECP Session Checklist

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q1 | date |  |  | SI | Date |
| Q10 | varchar |  |  | SI | Pertinent health issues / concerns have been discu... |
| Q11 | varchar |  |  | SI | Inclusion and Exclusion Criteria |
| Q12 | varchar |  |  | SI | Inclusion criteria |
| Q13 | varchar |  |  | SI | Exclusion criteria |
| Q14 | varchar |  |  | SI | Signatures |
| Q15 | varchar |  |  | SI | Nurse |
| Q16 | varchar |  |  | SI | If any of the exclusion criteria have been selecte... |
| Q17 | varchar |  |  | SI | Name |
| Q18 | longvarbinary |  |  | SI | Signature |
| Q18UDt | date |  |  | SI | Signature Last Updated Date |
| Q18UTm | time |  |  | SI | Signature Last Updated Time |
| Q19 | date |  |  | SI | Date |
| Q2 | time |  |  | SI | Time |
| Q20 | varchar |  |  | SI | Doctor |
| Q21 | varchar |  |  | SI | Notes |
| Q22 | varchar |  |  | SI | Name |
| Q23 | longvarbinary |  |  | SI | Signature |
| Q23UDt | date |  |  | SI | Signature Last Updated Date |
| Q23UTm | time |  |  | SI | Signature Last Updated Time |
| Q24 | date |  |  | SI | Date |
| Q25 | varchar |  |  | SI | Blood and Bag Samples (As per Doctor's Orders) |
| Q26 | varchar |  |  | SI | Pre-procedure |
| Q27 | varchar |  |  | SI | During procedure |
| Q28 | varchar |  |  | SI | Post procedure |
| Q29 | varchar |  |  | SI | Bag: Pre-photoactivation |
| Q3 | numeric |  |  | SI | ECP session number |
| Q30 | varchar |  |  | SI | Bag: Post photoactivation |
| Q31 | varchar |  |  | SI | Notes |
| Q32 | varchar |  |  | SI | Nurse |
| Q33 | longvarbinary |  |  | SI | Signature |
| Q33UDt | date |  |  | SI | Signature Last Updated Date |
| Q33UTm | time |  |  | SI | Signature Last Updated Time |
| Q34 | date |  |  | SI | Date |
| Q35 | varchar |  |  | SI | Doctor |
| Q36 | longvarbinary |  |  | SI | Signature |
| Q36UDt | date |  |  | SI | Signature Last Updated Date |
| Q36UTm | time |  |  | SI | Signature Last Updated Time |
| Q37 | date |  |  | SI | Date |
| Q5 | varchar |  |  | SI | Documentation Checklist |
| Q6 | varchar |  |  | SI | Dermatology clearance |
| Q7 | varchar |  |  | SI | Hematology clearance |
| Q8 | varchar |  |  | SI | Other relevant clearance(s) given |
| Q9 | varchar |  |  | SI | Evaluation |
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