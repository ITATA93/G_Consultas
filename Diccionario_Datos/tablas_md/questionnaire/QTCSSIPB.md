# questionnaire.QTCSSIPB

> Surgical Site Infection Prevention Bundle

**Schema:** questionnaire
**Columnas:** 85
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Surgical Site Infection Prevention Bundle

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Surgical Procedure |
| Q02 | varchar |  |  | SI | Preparation |
| Q03 | varchar |  |  | SI | Pre-Operative |
| Q04 | varchar |  |  | SI | Intra-Operative |
| Q05 | varchar |  |  | SI | Post-Operative |
| Q06 | varchar |  |  | SI | Booked procedure |
| Q07 | date |  |  | SI | Date of procedure |
| Q08 | varchar |  |  | SI | Type of operation |
| Q09 | varchar |  |  | SI | Pre-operative chlorhexidine bath supplied |
| Q10 | varchar |  |  | SI | Bath taken night prior to surgery |
| Q11 | varchar |  |  | SI | Bath taken on the day of surgery |
| Q12 | varchar |  |  | SI | Prophylactic antibiotic prescribed |
| Q13 | varchar |  |  | SI | Comments (Preparation) |
| Q14 | varchar |  |  | SI | Type of hair removal |
| Q15 | varchar |  |  | SI | Other hair removal type |
| Q16 | varchar |  |  | SI | Antibiotic prophylaxis given |
| Q17 | varchar |  |  | SI | Given in  |
| Q18 | varchar |  |  | SI | If not given 30-60 min before incision, give reaso... |
| Q19 | varchar |  |  | SI | Skin antisepsis done with |
| Q20 | varchar |  |  | SI | Other skin antiseptic |
| Q21 | varchar |  |  | SI | Type of surgery |
| Q22 | varchar |  |  | SI | Maintaining normothermia (>36 C) |
| Q23 | varchar |  |  | SI | Blood glucose level controlled |
| Q24 | varchar |  |  | SI | Pre-Operative comments |
| Q25 | varchar |  |  | SI | Intra-Operative comments |
| Q26 | varchar |  |  | SI | Post-Operative comments |
| Q27 | numeric |  |  | SI | Bundle compliance percentage |
| Q28 | varchar |  |  | SI | Target |
| Q29 | date |  |  | SI | Date audit completed |
| Q30 | varchar |  |  | SI | Infection control comments |
| Q31 | varchar |  |  | SI | Name of surgeon |
| Q32 | varchar |  |  | SI | Actual procedure |
| Q33 | varchar |  |  | SI | Theatre No: |
| Q34 | time |  |  | SI | Time of procedure: From |
| Q35 | time |  |  | SI | To |
| Q36 | bit |  |  | SI | 30 days |
| Q37 | bit |  |  | SI | 90 days |
| Q38 | varchar |  |  | SI | Evaluated by IC officer |
| Q39 | varchar |  |  | SI | Follow-up by IC officer |
| Q40 | varchar |  |  | SI | Temperature at end of procedure |
| Q40ObsDR | varchar |  | FK | SI | Temperature at end of procedure DR |
| Q41 | date |  |  | SI | Date |
| Q42 | time |  |  | SI | Time |
| Q43 | varchar |  |  | SI | Antibiotic prophylaxis given |
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