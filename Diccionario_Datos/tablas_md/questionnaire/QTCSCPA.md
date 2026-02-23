# questionnaire.QTCSCPA

> Psychosocial Assessment

**Schema:** questionnaire
**Columnas:** 91
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Psychosocial Assessment

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Religious status |
| Q02 | bigint |  |  | SI | Description of family system, networks and support... |
| Q02TxtOnly | bigint |  |  | SI | Description of family system, networks and support... |
| Q03 | bigint |  |  | SI | Formal support / services involved |
| Q03TxtOnly | bigint |  |  | SI | Formal support / services involved Plain Text Only |
| Q04 | varchar |  |  | SI | Case manager |
| Q05 | varchar |  |  | SI | Case manager details |
| Q06 | varchar |  |  | SI | Aged Care Assessment Service details (ACAS) |
| Q07 | varchar |  |  | SI | Financial circumstances |
| Q08 | varchar |  |  | SI | Financial notes |
| Q09 | varchar |  |  | SI | Legal issues |
| Q10 | varchar |  |  | SI | Current living situation |
| Q11 | varchar |  |  | SI | Status: housing stable |
| Q12 | varchar |  |  | SI | Mental health state |
| Q13 | varchar |  |  | SI | Mental health state details |
| Q14 | varchar |  |  | SI | Carer issues |
| Q15 | varchar |  |  | SI | Carer issues details |
| Q16 | varchar |  |  | SI | Threat to person (self or others) |
| Q17 | varchar |  |  | SI | Threat to person (self or others) details |
| Q18 | varchar |  |  | SI | Other risk assessment |
| Q19 | varchar |  |  | SI | Other risk assessment details |
| Q20 | varchar |  |  | SI | Other |
| Q21 | varchar |  |  | SI | Other details |
| Q22 | bigint |  |  | SI | Identified strengths / resources of patient (inter... |
| Q22TxtOnly | bigint |  |  | SI | Identified strengths / resources of patient (inter... |
| Q23 | bigint |  |  | SI | Summary / Recommendations / Discharge plan |
| Q23TxtOnly | bigint |  |  | SI | Summary / Recommendations / Discharge plan Plain T... |
| Q24 | varchar |  |  | SI | Religious status |
| Q25 | date |  |  | SI | Date |
| Q26 | time |  |  | SI | Time |
| Q27 | varchar |  |  | SI | Support services / Care arrangements type |
| Q28 | varchar |  |  | SI | Support services details |
| Q29 | varchar |  |  | SI | Current informal supports |
| Q30 | varchar |  |  | SI | Notes |
| Q31 | varchar |  |  | SI | Main source of income (not for people less than 16... |
| Q32 | varchar |  |  | SI | Other living situation |
| Q33 | varchar |  |  | SI | Usual living arrangements |
| Q34 | varchar |  |  | SI | Usual living arrangement details |
| Q35 | varchar |  |  | SI | Current occupation |
| Q36 | varchar |  |  | SI | Current / Previous occupation |
| Q37 | varchar |  |  | SI | Carer responsibilities for others |
| Q38 | varchar |  |  | SI | Patient have pets requiring care |
| Q39 | varchar |  |  | SI | Pet details |
| Q40 | varchar |  |  | SI | Any significant stresses impacting on daily life a... |
| Q41 | varchar |  |  | SI | Stressor details |
| Q42 | varchar |  |  | SI | Cultural considerations |
| Q43 | varchar |  |  | SI | Cultural consideration details |
| Q44 | varchar |  |  | SI | Notes |
| Q45 | varchar |  |  | SI | Income details |
| Q46 | varchar |  |  | SI | Carer responsibilities for others details |
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