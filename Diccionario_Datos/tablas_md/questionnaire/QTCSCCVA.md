# questionnaire.QTCSCCVA

> Screening Checklist for Contraindications to Vaccines for Adults

**Schema:** questionnaire
**Columnas:** 63
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Screening Checklist for Contraindications to Vaccines for Adults

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Are you sick today |
| Q02 | varchar |  |  | SI | Do you have allergies to medications, food, a vacc... |
| Q03 | varchar |  |  | SI | Have you ever had a serious reaction after receivi... |
| Q04 | varchar |  |  | SI | Do you have a long-term health problem with heart ... |
| Q05 | varchar |  |  | SI | Do you have cancer, leukemia, HIV/AIDS, or any oth... |
| Q06 | varchar |  |  | SI | In the past 3 months, have you taken medication th... |
| Q07 | varchar |  |  | SI | drugs for the treatment of rheumatoid arthritis, C... |
| Q08 | varchar |  |  | SI |  Have you had a seizure or a brain or other nervou... |
| Q09 | varchar |  |  | SI |  During the past year, have you received a transfu... |
| Q10 | varchar |  |  | SI | Are you pregnant or is there a chance you could be... |
| Q11 | varchar |  |  | SI | Have you received any vaccinations in the past 4 w... |
| Q12 | varchar |  |  | SI | Did you bring your Immunization Record Card with y... |
| Q13 | longvarbinary |  |  | SI | Patient's signature |
| Q13UDt | date |  |  | SI | Patient's signature Last Updated Date |
| Q13UTm | time |  |  | SI | Patient's signature Last Updated Time |
| Q14 | varchar |  |  | SI | For patients: The above questions will help us det... |
| Q15 | varchar |  |  | SI | answer “yes” to any question, it does not necessar... |
| Q16 | varchar |  |  | SI | additional questions must be asked. If a question ... |
| Q17P1 | varchar |  |  | SI | drugs for the treatment of rheumatoid arthritis, C... |
| Q17P2 | varchar |  |  | SI | or psoriasis; or psoriasis; or have you had radiat... |
| Q19 | date |  |  | SI | Date |
| Q20 | time |  |  | SI | Time |
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