# questionnaire.QTCNSOTAF

> Occupational Therapy Assessment Form

**Schema:** questionnaire
**Columnas:** 118
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Occupational Therapy Assessment Form

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Prior level of function |
| Q02 | varchar |  |  | SI | Occupation (hobbies, routine, work, etc...) |
| Q03 | varchar |  |  | SI | Environmental situation (house level, stairs, acce... |
| Q04 | varchar |  |  | SI | On observation |
| Q05 | varchar |  |  | SI | Level of consciousness |
| Q05ObsDR | varchar |  | FK | SI | Level of consciousness DR |
| Q06 | varchar |  |  | SI | Orientation |
| Q06ObsDR | varchar |  | FK | SI | Orientation DR |
| Q07 | varchar |  |  | SI | Language |
| Q08 | varchar |  |  | SI | Other spoken language |
| Q09 | varchar |  |  | SI | Communication |
| Q10 | varchar |  |  | SI | Communication comments |
| Q11 | varchar |  |  | SI | Hearing |
| Q12 | varchar |  |  | SI | Vision |
| Q13 | varchar |  |  | SI | Cognitive status (able to follow commands, multist... |
| Q14 | varchar |  |  | SI | Memory (short term, long term) |
| Q15 | varchar |  |  | SI | Comprehension |
| Q16 | varchar |  |  | SI | Emotional status |
| Q17 | varchar |  |  | SI | Sensation and perception status |
| Q18 | varchar |  |  | SI | Body awareness |
| Q19 | varchar |  |  | SI | Right |
| Q20 | varchar |  |  | SI | Left |
| Q21 | varchar |  |  | SI | Body awareness right |
| Q22 | varchar |  |  | SI | Body awareness left |
| Q23 | varchar |  |  | SI | Neglect |
| Q24 | varchar |  |  | SI | Neglect right |
| Q25 | varchar |  |  | SI | Neglect left |
| Q26 | varchar |  |  | SI | Body Image |
| Q27 | varchar |  |  | SI | Body image right |
| Q28 | varchar |  |  | SI | Body image left |
| Q29 | varchar |  |  | SI | Body image comment |
| Q30 | varchar |  |  | SI | Homonymous Hemianopsia Right |
| Q31 | varchar |  |  | SI | Functional status |
| Q32 | varchar |  |  | SI | Bed mobility - rolling to left |
| Q32ObsDR | varchar |  | FK | SI | Bed mobility - rolling to left DR |
| Q33 | varchar |  |  | SI | Bed mobility - rolling to right |
| Q33ObsDR | varchar |  | FK | SI | Bed mobility - rolling to right DR |
| Q34 | varchar |  |  | SI | Supine to sit |
| Q34ObsDR | varchar |  | FK | SI | Supine to sit DR |
| Q35 | varchar |  |  | SI | Sitting balance - static |
| Q35ObsDR | varchar |  | FK | SI | Sitting balance - static DR |
| Q36 | varchar |  |  | SI | Sitting balance - dynamic |
| Q36ObsDR | varchar |  | FK | SI | Sitting balance - dynamic DR |
| Q37 | varchar |  |  | SI | Sit to stand |
| Q37ObsDR | varchar |  | FK | SI | Sit to stand DR |
| Q38 | varchar |  |  | SI | Functional transfer - bed to wheelchair |
| Q38ObsDR | varchar |  | FK | SI | Functional transfer - bed to wheelchair DR |
| Q39 | varchar |  |  | SI | Functional transfer - wheelchair to toilet |
| Q39ObsDR | varchar |  | FK | SI | Functional transfer - wheelchair to toilet DR |
| Q40 | varchar |  |  | SI | Ambulation |
| Q40ObsDR | varchar |  | FK | SI | Ambulation DR |
| Q41 | varchar |  |  | SI | Wheelchair mobility |
| Q41ObsDR | varchar |  | FK | SI | Wheelchair mobility DR |
| Q42 | varchar |  |  | SI | ADL status |
| Q43 | varchar |  |  | SI | Feeding |
| Q43ObsDR | varchar |  | FK | SI | Feeding DR |
| Q44 | varchar |  |  | SI | Washing |
| Q44ObsDR | varchar |  | FK | SI | Washing DR |
| Q45 | varchar |  |  | SI | Grooming |
| Q45ObsDR | varchar |  | FK | SI | Grooming DR |
| Q46 | varchar |  |  | SI | Dressing |
| Q46ObsDR | varchar |  | FK | SI | Dressing DR |
| Q47 | varchar |  |  | SI | Toileting |
| Q47ObsDR | varchar |  | FK | SI | Toileting DR |
| Q48 | varchar |  |  | SI | Transfers |
| Q48ObsDR | varchar |  | FK | SI | Transfers DR |
| Q49 | varchar |  |  | SI | Mobilizing |
| Q49ObsDR | varchar |  | FK | SI | Mobilizing DR |
| Q50 | varchar |  |  | SI | Fine hand function (buttons, laces, zips, writing,... |
| Q51 | varchar |  |  | SI | Goals |
| Q52 | varchar |  |  | SI | Short term goals |
| Q53 | varchar |  |  | SI | Long term goals |
| Q54 | varchar |  |  | SI | Treatement plan |
| Q55 | varchar |  |  | SI | Treatement frequency and duration |
| Q56 | varchar |  |  | SI | Patient education |
| Q57 | varchar |  |  | SI | Homonymous Hemianopsia Left |
| Q58 | varchar |  |  | SI | Homonymous Hemianopsia |
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