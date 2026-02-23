# questionnaire.QTCRPGHA

> Respiratory Patient General Health Assessment

**Schema:** questionnaire
**Columnas:** 77
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Respiratory Patient General Health Assessment

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Cyanosis |
| Q02 | varchar |  |  | SI | Pressure areas intact |
| Q03 | varchar |  |  | SI | Water based gel in use |
| Q04 | varchar |  |  | SI | Skin assessment notes |
| Q05 | varchar |  |  | SI | Peripheral oedema present |
| Q06 | varchar |  |  | SI | Loss of sensation in peripheries |
| Q07 | varchar |  |  | SI | Peripheral oedema notes |
| Q08 | varchar |  |  | SI | Bladder |
| Q09 | varchar |  |  | SI | Bowel |
| Q10 | varchar |  |  | SI | Elimination notes |
| Q11 | varchar |  |  | SI | Mental state |
| Q12 | varchar |  |  | SI | Mental state notes |
| Q13 | varchar |  |  | SI | Hygiene |
| Q14 | varchar |  |  | SI | Requires help with hygiene |
| Q15 | varchar |  |  | SI | Hygiene help required |
| Q16 | varchar |  |  | SI | Hygiene and mobility aids in use |
| Q17 | varchar |  |  | SI | Other aids |
| Q18 | varchar |  |  | SI | Hygiene and mobility notes |
| Q19 | varchar |  |  | SI | Sleep |
| Q20 | varchar |  |  | SI | Is the patient on CPAP / BiPAP? |
| Q21 | varchar |  |  | SI | Sleep notes |
| Q22 | varchar |  |  | SI | Description of patient's diet |
| Q23 | varchar |  |  | SI | Diet texture |
| Q23ObsDR | varchar |  | FK | SI | Diet texture DR |
| Q24 | varchar |  |  | SI | Is the patient short of breath on eating? |
| Q25 | varchar |  |  | SI | Is the patient using a meal delivery service? |
| Q26 | varchar |  |  | SI | Diet notes |
| Q27 | varchar |  |  | SI | Does the patient have pain? |
| Q28 | varchar |  |  | SI | Location and description of pain |
| Q29 | varchar |  |  | SI | Pain score |
| Q29ObsDR | varchar |  | FK | SI | Pain score DR |
| Q30 | varchar |  |  | SI | Pain notes |
| Q31 | varchar |  |  | SI | Goals of care discussed with patient |
| Q32 | varchar |  |  | SI | Goals of care notes |
| Q33 | date |  |  | SI | Date |
| Q34 | time |  |  | SI | Time |
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