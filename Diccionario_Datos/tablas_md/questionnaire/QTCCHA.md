# questionnaire.QTCCHA

> Chemo Helpline Assessment

**Schema:** questionnaire
**Columnas:** 72
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Chemo Helpline Assessment

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Where has the patient had treatment? |
| Q02 | varchar |  |  | SI | Has the patient called before? |
| Q03 | date |  |  | SI | If yes, when? |
| Q04 | varchar |  |  | SI | Person calling |
| Q05 | numeric |  |  | SI | Telephone number |
| Q06 | date |  |  | SI | Date of call |
| Q07 | time |  |  | SI | Time of call |
| Q08 | numeric |  |  | SI | Duration of call |
| Q09 | varchar |  |  | SI | Presenting problem |
| Q10 | varchar |  |  | SI | Please ask the patient if they have any of the fol... |
| Q11 | varchar |  |  | SI | Diarrhoea |
| Q12 | varchar |  |  | SI | Central Venous Catheter (CVC) in situ |
| Q13 | varchar |  |  | SI | Nausea and vomiting |
| Q14 | varchar |  |  | SI | Constipation |
| Q15 | varchar |  |  | SI | Shaking and shivering |
| Q16 | varchar |  |  | SI | Raised temperature |
| Q17 | varchar |  |  | SI | Sore throat / mouth |
| Q18 | varchar |  |  | SI | Flu-like symptoms |
| Q19 | varchar |  |  | SI | Bleeding |
| Q20 | varchar |  |  | SI | If the answer to any of the above is YES, please r... |
| Q21 | varchar |  |  | SI | Temp more than 36°C |
| Q22 | varchar |  |  | SI | Persistent headache |
| Q23 | varchar |  |  | SI | Other signs of infection. e.g. cellulitis / wound |
| Q24 | varchar |  |  | SI | MRSA screen |
| Q25 | varchar |  |  | SI | Advice given |
| Q26 | varchar |  |  | SI | MRSA screen |
| Q27 | varchar |  |  | SI | Temp more than 36°C |
| Q28 | varchar |  |  | SI | Check against known UK / overseas list areas of co... |
| Q29 | varchar |  |  | SI | Multidisciplinary assessment / treatment plan |
| Q30 | date |  |  | SI | Date |
| Q31 | time |  |  | SI | Time |
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