# questionnaire.QTCFIS

> "Faecal Incontinence Scores (Wexner, 1993

**Schema:** questionnaire
**Columnas:** 78
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* "Faecal Incontinence Scores (Wexner, 1993

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | Type of incontinence |
| Q04 | varchar |  |  | SI | Solid |
| Q05 | varchar |  |  | SI | Liquid |
| Q06 | varchar |  |  | SI | Wears pads |
| Q07 | varchar |  |  | SI | Lifestyle alteration |
| Q08 | varchar |  |  | SI | Wexner Score |
| Q09 | varchar |  |  | SI | Incontinence for solid stool |
| Q10 | varchar |  |  | SI | Incontinence for liquid stool |
| Q11 | varchar |  |  | SI | Incontinence for gas |
| Q12 | varchar |  |  | SI | Alteration in lifestyle |
| Q13 | varchar |  |  | SI | Need to wear a pad or plug |
| Q14 | varchar |  |  | SI | Taking constipating medicines |
| Q15 | varchar |  |  | SI | Lack of ability to defer defecation for 15 minutes |
| Q16 | varchar |  |  | SI | Vaizey Score |
| Q17 | varchar |  |  | SI | Wexner Score |
| Q18 | varchar |  |  | SI | Vaizey Score |
| Q19 | varchar |  |  | SI | Provenance |
| Q20 | varchar |  |  | SI | Jorge JMN, Wexner SD. Etiology and management of f... |
| Q21 | varchar |  |  | SI | Vaizey CJ, Carapeti E, Cahill JA, Kamm MA. Prospec... |
| Q22 | varchar |  |  | SI | 0 = Perfect |
| Q23 | varchar |  |  | SI | 20 = Complete Incontinence |
| Q24 | varchar |  |  | SI | 0 = Perfect Continence |
| Q25 | varchar |  |  | SI | 24 = Totally Incontinent |
| Q26 | varchar |  |  | SI | Wexner Score Interpretation |
| Q27 | varchar |  |  | SI | Vaizey Score Interpretation |
| Q28 | varchar |  |  | SI | The assessment evaluates type and frequency of sto... |
| Q29 | varchar |  |  | SI | Wexner Score |
| Q30 | varchar |  |  | SI | Vaizey&nbsp;Score |
| Q31 | varchar |  |  | SI | Wexner Score |
| Q32 | varchar |  |  | SI | Vaizey Score |
| Q33 | varchar |  |  | SI | 0 = Perfect, 20 = Complete Incontinence. |
| Q34 | varchar |  |  | SI | 0 = Perfect continence, 24 = Totally Incontinence. |
| Q35 | varchar |  |  | SI | Which instrument do you wish to use? |
| Q36 | varchar |  |  | SI | Which instrument do you wish to use? |
| Q37 | varchar |  |  | SI | Gas |
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