# questionnaire.QGXXXFASTHU

> ICU FASTHUG

**Schema:** questionnaire
**Columnas:** 67
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* ICU FASTHUG

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Is your patient being fed enterally (PO/NG)? |
| Q01a | varchar |  |  | SI | Feeding |
| Q01b | varchar |  |  | SI | Early feeding significantly reduces ICU mortality |
| Q02 | varchar |  |  | SI | Have you documented the RASS and Pain Score at lea... |
| Q02a | varchar |  |  | SI | Analgesia and Sedation |
| Q02b | varchar |  |  | SI | Appropriate analgesia and sedation ensures patient... |
| Q03 | varchar |  |  | SI | Is your patient receiving pharmacologic DVT Prophy... |
| Q03a | varchar |  |  | SI | Thromboprophylaxis |
| Q03b | varchar |  |  | SI | DVT prophylaxis reduces the risk of DVTs and poten... |
| Q04 | varchar |  |  | SI | Does your patient have TEDS or PCDs on? |
| Q04a | varchar |  |  | SI | Head of Bed |
| Q04b | varchar |  |  | SI | Elevating the head of the patient's bed greater th... |
| Q05 | varchar |  |  | SI | Is the patient receiving GI Prophylaxis? |
| Q05a | varchar |  |  | SI | Ulcer Prophylaxis |
| Q05b | varchar |  |  | SI | GI ulcer prophylaxis significantly reduces GI Blee... |
| Q06 | varchar |  |  | SI | Glycaemic Control - Has your patient's blood gluco... |
| Q06a | varchar |  |  | SI | Glycaemic Control |
| Q06b | varchar |  |  | SI | Controlling a patient's blood glucose can signific... |
| Q07 | varchar |  |  | SI | Has the bed head been elevated to at least 30 degr... |
| Q07a | varchar |  |  | SI | Ulcer Prophylaxis |
| Q07b | varchar |  |  | SI | GI ulcer prophylaxis significantly reduces GI Blee... |
| Q08 | varchar |  |  | SI | Sedative interruption implemented? |
| Q08a | varchar |  |  | SI | Ventilator Component |
| Q09 | varchar |  |  | SI | Is the patient ready for extubation? |
| Q25 | varchar |  |  | SI | FAST HUG is a mnemonic used in the Intensive Care ... |
| Q26 | varchar |  |  | SI | help identify and prevent medication errors, promo... |
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