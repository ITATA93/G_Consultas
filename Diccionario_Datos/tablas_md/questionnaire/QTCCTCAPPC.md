# questionnaire.QTCCTCAPPC

> CT Coronary Angiogram Pre-Procedure Checklist

**Schema:** questionnaire
**Columnas:** 68
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* CT Coronary Angiogram Pre-Procedure Checklist

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | Relevant history |
| Q04 | varchar |  |  | SI | Patient has had a recent pulmonary function test |
| Q05 | varchar |  |  | SI | Patient a smoker or ex-smoker |
| Q06 | date |  |  | SI | Quit date if applicable |
| Q07 | varchar |  |  | SI | Patient has had a recent stress test |
| Q08 | date |  |  | SI | Date of stress test |
| Q09 | varchar |  |  | SI | Patient has had a recent  electrocardiogram (ECG) |
| Q10 | date |  |  | SI | Date of latest ECG |
| Q11 | varchar |  |  | SI | Patient has had a recent echocardiogram |
| Q12 | date |  |  | SI | Date of latest echocardiogram |
| Q13 | varchar |  |  | SI | Patient has had a recent dobutamine stress echo / ... |
| Q14 | date |  |  | SI | Date of dobutamine test |
| Q15 | varchar |  |  | SI | Recent blood results checked for estimated glomeru... |
| Q16 | varchar |  |  | SI | History and investigation notes |
| Q17 | varchar |  |  | SI | Patient female and aged between 10 and 60 years of... |
| Q18 | varchar |  |  | SI | Pregnancy test result |
| Q18ObsDR | varchar |  | FK | SI | Pregnancy test result DR |
| Q19 | varchar |  |  | SI | Patient is breastfeeding |
| Q20 | varchar |  |  | SI | Beta blocker given in the night |
| Q21 | varchar |  |  | SI | Name and dose of beta blocker |
| Q22 | varchar |  |  | SI | Beta blocker given in the morning |
| Q23 | varchar |  |  | SI | Name and dose of beta blocker |
| Q24 | varchar |  |  | SI | Other medications taken to slow heart rate |
| Q25 | varchar |  |  | SI | No caffeine or stimulants for 12 hours |
| Q26 | varchar |  |  | SI | Medication / Stimulant notes |
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