# questionnaire.QTCPPST

> Adult Pre Procedure Screening Tool

**Schema:** questionnaire
**Columnas:** 100
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Adult Pre Procedure Screening Tool

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | Does the patient still require / want the surgery |
| Q04 | varchar |  |  | SI | Reason |
| Q05 | varchar |  |  | SI | Surgical team informed |
| Q06 | varchar |  |  | SI | Theatre schedulers informed |
| Q07 | varchar |  |  | SI | Patient allergies checked and recorded as appropri... |
| Q08 | varchar |  |  | SI | Any changes in condition since completion of last ... |
| Q09 | varchar |  |  | SI | What has changed |
| Q10 | varchar |  |  | SI | Notes |
| Q11 | varchar |  |  | SI | Is the patient currently well |
| Q12 | varchar |  |  | SI | Details of illness |
| Q13 | varchar |  |  | SI | Discussed with anaesthetist |
| Q14 | varchar |  |  | SI | Theatre schedulers notified and pre-admission clin... |
| Q15 | varchar |  |  | SI | Infection status confirmed with patient and docume... |
| Q16 | varchar |  |  | SI | Weight recorded and checked with patient |
| Q17 | varchar |  |  | SI | Schedulers informed to book day of surgery admissi... |
| Q18 | varchar |  |  | SI | Patient's skin is intact – free from cuts, scratch... |
| Q19 | varchar |  |  | SI | Skin condition notes |
| Q20 | varchar |  |  | SI | Patient’s medications have been confirmed |
| Q21 | varchar |  |  | SI | Has the patient recently started taking any new me... |
| Q22 | varchar |  |  | SI | Is the patient on anticoagulants |
| Q23 | varchar |  |  | SI | Vitamins or natural supplements have been discusse... |
| Q24 | varchar |  |  | SI | Transport for admission and discharge has been arr... |
| Q25 | varchar |  |  | SI | Somebody is available to assist with activities of... |
| Q26 | varchar |  |  | SI | Comment |
| Q27 | varchar |  |  | SI | Admission |
| Q28 | varchar |  |  | SI | Admission time confirmed |
| Q29 | date |  |  | SI | Expected admission date |
| Q30 | time |  |  | SI | Expected admission time |
| Q31 | varchar |  |  | SI | Patient informed of admission location |
| Q32 | varchar |  |  | SI | Morning medication discussed |
| Q33 | varchar |  |  | SI | Fasting time instructions given |
| Q34 | varchar |  |  | SI | Pre-Operative |
| Q35 | varchar |  |  | SI | Patient journey explained |
| Q36 | varchar |  |  | SI | Expected length of stay discussed |
| Q37 | varchar |  |  | SI | Day case |
| Q38 | varchar |  |  | SI | Admit full care |
| Q39 | varchar |  |  | SI | Patient informed waiting times are variable |
| Q40 | varchar |  |  | SI | Showering discussed - prior to surgery |
| Q41 | varchar |  |  | SI | Shaving discussed – use caution to prevent cuts |
| Q42 | varchar |  |  | SI | Skin care discussed - avoiding cuts etc |
| Q43 | varchar |  |  | SI | Nails discussed -  all nail polish and acrylic / g... |
| Q44 | varchar |  |  | SI | Valuables discussed - jewellery to be removed and ... |
| Q45 | varchar |  |  | SI | Discharge Restrictions / Requirements |
| Q46 | varchar |  |  | SI | Driving restriction |
| Q47 | varchar |  |  | SI | Lifting restriction |
| Q48 | varchar |  |  | SI | Post-operative visit required |
| Q49 | varchar |  |  | SI | Household chores restriction |
| Q50 | varchar |  |  | SI | Pre-prepared foods required |
| Q51 | varchar |  |  | SI | Responsible adult available for 24 hours for a day... |
| Q52 | varchar |  |  | SI | Name of responsible adult |
| Q53 | varchar |  |  | SI | Contact details of responsible adult |
| Q54 | varchar |  |  | SI | Reviewed by Nursing / Medical Staff |
| Q55 | varchar |  |  | SI | Suitable for anaesthetic review on day of procedur... |
| Q56 | varchar |  |  | SI | Requires referral to anaesthetic assessment |
| Q57 | varchar |  |  | SI | Patient requires specialist anaesthetic assessment |
| Q58 | varchar |  |  | SI | Comments |
| Q59 | varchar |  |  | SI | Infectious status comment |
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