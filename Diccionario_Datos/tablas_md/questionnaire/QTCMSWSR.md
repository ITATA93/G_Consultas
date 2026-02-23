# questionnaire.QTCMSWSR

> Medical Social Worker Screening and Reassessment

**Schema:** questionnaire
**Columnas:** 82
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Medical Social Worker Screening and Reassessment

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q10 | varchar |  |  | SI | Poor appetite |
| Q11 | varchar |  |  | SI | Crying |
| Q12 | varchar |  |  | SI | Lack of sleep |
| Q13 | varchar |  |  | SI | Aggressive |
| Q14 | varchar |  |  | SI | Physical / Mental disability |
| Q15 | varchar |  |  | SI | Compliance of treatment |
| Q16 | varchar |  |  | SI | Patient and family grieving |
| Q17 | varchar |  |  | SI | Other/s (specify) |
| Q18 | varchar |  |  | SI | History of abuse / neglect |
| Q19 | varchar |  |  | SI | Patient needs spiritual / Cultural assessment |
| Q2 | varchar |  |  | SI | Legal responsibility for the patient |
| Q20 | varchar |  |  | SI | Patient needs economic assistance |
| Q21 | varchar |  |  | SI | Patient needs psychosocial assessment |
| Q22 | varchar |  |  | SI | Multidisplinary team |
| Q22A | varchar |  |  | SI | Attended Meetings |
| Q23 | date |  |  | SI | Multidisplinary team meeting date |
| Q24 | varchar |  |  | SI | Multidisplinary team meeting note |
| Q25 | varchar |  |  | SI | Patient / Family meeting |
| Q26 | date |  |  | SI | Patient / Family meeting date |
| Q27 | varchar |  |  | SI | Patient / Family meeting notes |
| Q28 | varchar |  |  | SI | Discharge Planning |
| Q29 | varchar |  |  | SI | Discharge planning |
| Q3 | varchar |  |  | SI | Specify name |
| Q30 | varchar |  |  | SI | Others (specify) |
| Q31 | varchar |  |  | SI | Recommendations |
| Q32 | varchar |  |  | SI | Medical social worker's name |
| Q33 | varchar |  |  | SI | Medical social worker's id |
| Q34 | date |  |  | SI | Date |
| Q35 | time |  |  | SI | Time |
| Q36 | longvarbinary |  |  | SI | Signature |
| Q36UDt | date |  |  | SI | Signature Last Updated Date |
| Q36UTm | time |  |  | SI | Signature Last Updated Time |
| Q39 | date |  |  | SI | Date |
| Q4 | varchar |  |  | SI | Specify relationship |
| Q40 | time |  |  | SI | Time |
| Q5 | varchar |  |  | SI | Uncooperative |
| Q5A | varchar |  |  | SI | Social Worker Screening |
| Q6 | varchar |  |  | SI | Despair |
| Q7 | varchar |  |  | SI | Depressed |
| Q8 | varchar |  |  | SI | Low morale |
| Q9 | varchar |  |  | SI | Agitated |
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