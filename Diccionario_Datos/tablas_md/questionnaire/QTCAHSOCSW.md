# questionnaire.QTCAHSOCSW

> Social Work Assessment

**Schema:** questionnaire
**Columnas:** 66
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Social Work Assessment

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Worker name |
| Q02 | date |  |  | SI | Initial assessment date |
| Q03 | varchar |  |  | SI | Sources of information |
| Q04 | varchar |  |  | SI | Social / Family profile |
| Q06 | varchar |  |  | SI | Formal support / Services involved |
| Q07 | varchar |  |  | SI | Financial circumstances |
| Q08 | varchar |  |  | SI | Legal issues |
| Q09 | varchar |  |  | SI | Current living situation |
| Q10 | varchar |  |  | SI | Status: Housing stable* |
| Q11 | varchar |  |  | SI | Adjustment to current situation |
| Q12 | varchar |  |  | SI | Mental health state |
| Q13 | varchar |  |  | SI | Carer issues |
| Q14 | varchar |  |  | SI | Threat to Person (Self or Others) * |
| Q15 | varchar |  |  | SI | Other risk assessment * |
| Q16 | varchar |  |  | SI | Other |
| Q17 | varchar |  |  | SI | Indentified strengths / Resources of patient |
| Q18 | varchar |  |  | SI | Summary / Recommentations / Discharge plan |
| Q19 | varchar |  |  | SI | (*Coping Skills / Status; Cognition; Resources Int... |
| Q20 | varchar |  |  | SI | (Internal or External; Social or Emotional) |
| Q21 | varchar |  |  | SI | (Goals / Plans; Information given to patient / fam... |
| Q21A | varchar |  |  | SI | Resources; Referrals; Priority) |
| Q22 | varchar |  |  | SI | (Description of family system, marital status, |
| Q22A | varchar |  |  | SI | Friends, Social networks spiritualty, Informal sup... |
| Q23 | varchar |  |  | SI | Legal / Financial |
| Q25 | varchar |  |  | SI | Current living situation |
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