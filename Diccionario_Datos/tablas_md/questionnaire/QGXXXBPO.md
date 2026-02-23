# questionnaire.QGXXXBPO

> Blood Products Order and Pre-transfusion Checklist

**Schema:** questionnaire
**Columnas:** 89
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Blood Products Order and Pre-transfusion Checklist

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Medical Pre-transfusion Checklist |
| Q02 | varchar |  |  | SI | Reviewed patient's clinical record |
| Q03 | varchar |  |  | SI | Patient assessment |
| Q04 | varchar |  |  | SI | Patient IV access |
| Q05 | varchar |  |  | SI | Pre-transfusion blood sample ordered |
| Q06 | varchar |  |  | SI | Valid group and hold |
| Q07 | varchar |  |  | SI | Valid cross match |
| Q08 | varchar |  |  | SI | Procedure explained to patient / guardian |
| Q09 | varchar |  |  | SI | Valid consent from patient / guardian |
| Q10 | varchar |  |  | SI | Special requirements |
| Q11 | varchar |  |  | SI | Blood product |
| Q12 | varchar |  |  | SI | Dose / Volume / Rate |
| Q13 | varchar |  |  | SI | Route |
| Q14 | varchar |  |  | SI | Blood group |
| Q15 | varchar |  |  | SI | Blood warmer required |
| Q16 | numeric |  |  | SI | Temperature (Celcius) |
| Q17 | varchar |  |  | SI | Indication for use |
| Q18 | varchar |  |  | SI | Premedication (if applicable) ordered in medicatio... |
| Q19 | varchar |  |  | SI | Completed documentation in patients clinical recor... |
| Q20 | varchar |  |  | SI | Accredited practioner name |
| Q21 | date |  |  | SI | Date ordered |
| Q22 | varchar |  |  | SI | Nursing Pre-Transfusion Checklist |
| Q23 | varchar |  |  | SI | Reviewed patient's clinical record (including obse... |
| Q24 | varchar |  |  | SI | Patient assessment (Must notify if assessment find... |
| Q25 | varchar |  |  | SI | Patient IV access |
| Q26 | varchar |  |  | SI | Valid consent available and verified with patient ... |
| Q27 | varchar |  |  | SI | Valid group and hold |
| Q28 | varchar |  |  | SI | Valid cross match available |
| Q29 | varchar |  |  | SI | Procedure explained to patient / guardian |
| Q30 | varchar |  |  | SI | Confirmed patient identity with patient / guardian... |
| Q31 | varchar |  |  | SI | Confirmed patient identity with patient / guardian... |
| Q32 | varchar |  |  | SI | Confirmed patient identity with patient / guardian... |
| Q33 | varchar |  |  | SI | Premedication administered as charted |
| Q34 | varchar |  |  | SI | Completed documentation in patients clinical recor... |
| Q35 | varchar |  |  | SI | Completed documentation in patients clinical recor... |
| Q36 | varchar |  |  | SI | Care provider 1 |
| Q37 | varchar |  |  | SI | Care provider 2 |
| Q38 | varchar |  |  | SI | Unit / Batch number |
| Q39 | date |  |  | SI | Expiration date |
| Q40 | varchar |  |  | SI | Pre-transfusion blood sample ordered |
| Q41 | varchar |  |  | SI | Valid group and hold |
| Q42 | varchar |  |  | SI | Valid cross match |
| Q43 | varchar |  |  | SI | Valid group and hold |
| Q44 | varchar |  |  | SI | Valid cross match available |
| Q45 | varchar |  |  | SI | Premedication administered as charted |
| Q46 | varchar |  |  | SI | Blood group |
| Q47 | date |  |  | SI | Date |
| Q48 | time |  |  | SI | Time |
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