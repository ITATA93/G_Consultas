# questionnaire.QTCBRMT

> Bed Rails Risk Matrix Tool

**Schema:** questionnaire
**Columnas:** 85
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Bed Rails Risk Matrix Tool

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q1 | varchar |  |  | SI | Please note, this tool is to help support you in y... |
| Q10 | varchar |  |  | SI | Is there a risk of any part of the patients body b... |
| Q11 | varchar |  |  | SI | Use bedrails with caution.  Use professional and c... |
| Q12 | varchar |  |  | SI | Mental status |
| Q13 | varchar |  |  | SI | Mobility |
| Q14 | varchar |  |  | SI | Consider use of low beds where the patient is conf... |
| Q15 | varchar |  |  | SI | Is low bed appropriate |
| Q16 | varchar |  |  | SI | If no, give reason |
| Q17 | varchar |  |  | SI | Discussed with |
| Q18 | varchar |  |  | SI | Relationship |
| Q19 | varchar |  |  | SI | Relative / Carers views |
| Q2 | varchar |  |  | SI | Is the patient likely to fall out of bed? |
| Q20 | varchar |  |  | SI | Outcome of the assessment |
| Q21 | varchar |  |  | SI | Bedrails used |
| Q22 | varchar |  |  | SI | Rationale for decision |
| Q23 | date |  |  | SI | Date |
| Q24 | time |  |  | SI | Time |
| Q25 | varchar |  |  | SI | Evaluation comments and variation |
| Q26 | varchar |  |  | SI | Bed rails are used to prevent patients from fallin... |
| Q27 | varchar |  |  | SI | Score |
| Q28 | varchar |  |  | SI | Classification |
| Q29 | varchar |  |  | SI | 7 - 7 |
| Q3 | varchar |  |  | SI | Is the patient likely to be injured in a fall from... |
| Q30 | varchar |  |  | SI | 8 - 10 |
| Q31 | varchar |  |  | SI | 11 - 11 |
| Q32 | varchar |  |  | SI | 12 - 12 |
| Q33 | varchar |  |  | SI | 13 - 13 |
| Q34 | varchar |  |  | SI | 14 - 14 |
| Q35 | varchar |  |  | SI | 15 - 17 |
| Q36 | varchar |  |  | SI | 18 - 18 |
| Q37 | varchar |  |  | SI | Use bed rails with caution |
| Q38 | varchar |  |  | SI | Bed rails recommended |
| Q39 | varchar |  |  | SI | Bed rails not recommended |
| Q4 | varchar |  |  | SI | Will the patient be anxious if bedrails are not in... |
| Q40 | varchar |  |  | SI | Use bed rails with caution |
| Q41 | varchar |  |  | SI | Bed rails recommended |
| Q42 | varchar |  |  | SI | Not applicable |
| Q43 | varchar |  |  | SI | Bed rails not recommended |
| Q44 | varchar |  |  | SI | Not applicable |
| Q5 | varchar |  |  | SI | Would the bedrails stop the patient from being ind... |
| Q6 | varchar |  |  | SI | Is the patient likely to climb over the bedrails? |
| Q7 | varchar |  |  | SI | Could the patient injure themselves on the bedrail... |
| Q8 | varchar |  |  | SI | Will the use of bedrails cause the patient distres... |
| Q9 | varchar |  |  | SI | Is the bedrail suitable for the bed and mattress? |
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