# questionnaire.QTCECVPOL

> External Cephalic Version (ECV) Procedure

**Schema:** questionnaire
**Columnas:** 99
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* External Cephalic Version (ECV) Procedure

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | This form is intended to be used for single pregna... |
| Q04 | varchar |  |  | SI | This form is intended for nulliparous patients at ... |
| Q05 | varchar |  |  | SI | Gravida |
| Q06 | varchar |  |  | SI | Para |
| Q07 | numeric |  |  | SI | Gestation |
| Q08 | varchar |  |  | SI | weeks |
| Q09 | numeric |  |  | SI | Gestation (days) |
| Q10 | varchar |  |  | SI | days |
| Q11 | varchar |  |  | SI | Blood group - Rhesus |
| Q12 | varchar |  |  | SI | Blood group - Rhesus |
| Q14 | varchar |  |  | SI | Were maternal observations normal pre-ECV |
| Q15 | varchar |  |  | SI | Normal maternal observation pre-ECV notes |
| Q16 | varchar |  |  | SI | Was the cardiotocograph (CTG) normal pre-ECV |
| Q17 | varchar |  |  | SI | CTG normal pre-ECV notes |
| Q18 | varchar |  |  | SI | Is patient eligible for ECV |
| Q19 | varchar |  |  | SI | Patient eligible for ECV notes |
| Q20 | varchar |  |  | SI | Has ECV information been provided to the patient |
| Q21 | varchar |  |  | SI | Type of ECV information provided |
| Q22 | varchar |  |  | SI | Patient consent been gained |
| Q23 | varchar |  |  | SI | Patient consent notes |
| Q24 | varchar |  |  | SI | Has the patient been fasted |
| Q25 | varchar |  |  | SI | Fasted notes |
| Q26 | date |  |  | SI | Last food intake |
| Q27 | time |  |  | SI | Last food intake |
| Q28 | varchar |  |  | SI | Last food intake notes |
| Q29 | date |  |  | SI | Last fluid intake |
| Q30 | time |  |  | SI | Last fluid intake |
| Q31 | varchar |  |  | SI | Last fluid intake notes |
| Q32 | varchar |  |  | SI | Has a tocolytic been administered |
| Q33 | varchar |  |  | SI | Tocolytic notes |
| Q34 | varchar |  |  | SI | Pre-procedure notes |
| Q35 | varchar |  |  | SI | Procedure performed by |
| Q36 | varchar |  |  | SI | Role |
| Q37 | varchar |  |  | SI | Assistance provided by |
| Q38 | varchar |  |  | SI | Role |
| Q39 | time |  |  | SI | ECV start time |
| Q40 | time |  |  | SI | ECV end time |
| Q41 | varchar |  |  | SI | ECV outcome |
| Q42 | varchar |  |  | SI | Other presentation, if applicable |
| Q43 | numeric |  |  | SI | Number of attempts |
| Q44 | varchar |  |  | SI | Complications details |
| Q45 | varchar |  |  | SI | Specify other complication details |
| Q46 | varchar |  |  | SI | Complication notes |
| Q47 | varchar |  |  | SI | Are maternal observations normal post-ECV |
| Q48 | varchar |  |  | SI | Maternal observations normal post-ECV notes |
| Q49 | varchar |  |  | SI | Is the cardiotocograph (CTG) normal post-ECV |
| Q50 | varchar |  |  | SI | CTC normal post-ECV notes |
| Q51 | varchar |  |  | SI | Has Anti-D been administered |
| Q52 | varchar |  |  | SI | Anti-D administered notes |
| Q53 | varchar |  |  | SI | Post-procedures notes |
| Q54 | varchar |  |  | SI | Birth plan, if cephalic |
| Q55 | varchar |  |  | SI | Birth plan, if breech |
| Q56 | varchar |  |  | SI | Follow-up plan |
| Q57 | varchar |  |  | SI | Gravida |
| Q58 | varchar |  |  | SI | Para |
| Q59 | varchar |  |  | SI | Blood group - Rhesus |
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