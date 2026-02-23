# questionnaire.QTEST01

> TEST01

**Schema:** questionnaire
**Columnas:** 66
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Cuestionario/Formulario**. Plantilla de evaluación clínica estructurada. *(TEST01)*

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Worker Name2 |
| Q02 | date |  |  | SI | Initial Assessment Date |
| Q03 | varchar |  |  | SI | Sources of Information |
| Q04 | varchar |  |  | SI | Social/Family Profile |
| Q06 | varchar |  |  | SI | Formal Support/Services Involved |
| Q07 | varchar |  |  | SI | Financial Circumstances |
| Q08 | varchar |  |  | SI | Legal Issues |
| Q09 | varchar |  |  | SI | Current Living Situation |
| Q10 | varchar |  |  | SI | Status: Housing Stable* |
| Q11 | varchar |  |  | SI | Adjustment to Current Situation |
| Q12 | varchar |  |  | SI | Mental Health State |
| Q13 | varchar |  |  | SI | Carer Issues |
| Q14 | varchar |  |  | SI | Threat to Person (Self or Others) * |
| Q15 | varchar |  |  | SI | Other Risk Assessment * |
| Q16 | varchar |  |  | SI | Other |
| Q17 | varchar |  |  | SI | Indentified Strengths/Resources of Patient |
| Q18 | varchar |  |  | SI | Summary/Recommentations/Discharge Plan |
| Q19 | varchar |  |  | SI | (*Coping Skills/Status; Cognition; Resources Inter... |
| Q20 | varchar |  |  | SI | (Internal or External; Social or Emotional) |
| Q21 | varchar |  |  | SI | (Goals/Plans; Information given to Patient/Family; |
| Q21A | varchar |  |  | SI | Resources; Referrals; Priority) |
| Q22 | varchar |  |  | SI | (Description of Family System, Marital Status, |
| Q22A | varchar |  |  | SI | Friends, Social Networks Spiritualty, Informal Sup... |
| Q23 | varchar |  |  | SI | Legal / Financial |
| Q25 | date |  |  | SI | date |
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