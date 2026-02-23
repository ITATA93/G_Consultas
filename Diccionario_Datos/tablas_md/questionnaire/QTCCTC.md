# questionnaire.QTCCTC

> Chemotherapy Treatment Checklist

**Schema:** questionnaire
**Columnas:** 74
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Chemotherapy Treatment Checklist

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Height |
| Q01ObsDR | varchar |  | FK | SI | Height DR |
| Q02 | varchar |  |  | SI | Weight |
| Q02ObsDR | varchar |  | FK | SI | Weight DR |
| Q03 | varchar |  |  | SI | Patient's protocol	 |
| Q04 | numeric |  |  | SI | Cycle number	 |
| Q05 | date |  |  | SI | Date of assessment	 |
| Q06 | numeric |  |  | SI | Dose reduction %	 |
| Q07 | varchar |  |  | SI | Is dose reduction permanent? 	 |
| Q08 | varchar |  |  | SI | Biochemistry / Tumour Markers	 |
| Q09 | varchar |  |  | SI | Bloods checked	 |
| Q10 | date |  |  | SI | Date bloods taken	 |
| Q11 | date |  |  | SI | Date of chemotherapy	 |
| Q12 | varchar |  |  | SI | Other test results	 |
| Q13 | varchar |  |  | SI | Grade - Please select the appropriate item in each... |
| Q14 | varchar |  |  | SI | Performance status	 |
| Q15 | varchar |  |  | SI | Nausea	 |
| Q16 | varchar |  |  | SI | Vomiting	 |
| Q17 | varchar |  |  | SI | Diarrhoea	 |
| Q18 | varchar |  |  | SI | Skin rash	 |
| Q19 | varchar |  |  | SI | Neurosensory	 |
| Q20 | varchar |  |  | SI | Assessment findings: 	 |
| Q21 | varchar |  |  | SI | Bloods reviewed and chemotherapy to proceed? 	 |
| Q22 | varchar |  |  | SI | Take home medications ordered |
| Q23 | varchar |  |  | SI | Method of next appointment	 |
| Q24 | varchar |  |  | SI | Is end of treatment letter needed? If last cycle	 |
| Q25 | varchar |  |  | SI | Toxicity assessment completed?	 |
| Q27 | varchar |  |  | SI | Confirmed patient received the pre medication if a... |
| Q28 | varchar |  |  | SI | Secured patient and family education |
| Q29 | varchar |  |  | SI | Secured informed consent for every new protocol |
| Q30 | varchar |  |  | SI | Double checking of dose calculation and orders ind... |
| Q31 | date |  |  | SI | Date |
| Q32 | time |  |  | SI | Time |
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