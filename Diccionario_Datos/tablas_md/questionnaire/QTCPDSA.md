# questionnaire.QTCPDSA

> Peritoneal Dialysis Suitability Assessment

**Schema:** questionnaire
**Columnas:** 83
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Peritoneal Dialysis Suitability Assessment

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | Medical / Surgical contraindications to peritoneal... |
| Q04 | varchar |  |  | SI | • History of diverticulitis / inflammatory bowel d... |
| Q05 | varchar |  |  | SI | • Respiratory / Diaphragmatic defect |
| Q06 | varchar |  |  | SI | • Chronic open wounds or skin conditions |
| Q07 | varchar |  |  | SI | • Urine/ Faecal incontinence |
| Q08 | varchar |  |  | SI | • Loss of PD function/ extensive abdominal adhesio... |
| Q09 | varchar |  |  | SI | • Psychological or emotional unable |
| Q10 | varchar |  |  | SI | • Severe socio- economic difficulties |
| Q11 | varchar |  |  | SI | • Literal and numerical incapability |
| Q12 | varchar |  |  | SI | Suitability assessment attended by |
| Q14 | varchar |  |  | SI | Previous surgery |
| Q15 | varchar |  |  | SI | Any previous surgery documented that may affect pa... |
| Q16 | varchar |  |  | SI | Abdominal scarring |
| Q17 | varchar |  |  | SI | Skin folds |
| Q18 | varchar |  |  | SI | Hernias |
| Q19 | varchar |  |  | SI | Diverticulitis |
| Q20 | varchar |  |  | SI | Respiratory / diaphragmatic defect |
| Q21 | varchar |  |  | SI | Physical assessment notes |
| Q24 | varchar |  |  | SI | Urine / faecal incontinence |
| Q25 | varchar |  |  | SI | Psychologically or emotionally unstable |
| Q26 | varchar |  |  | SI | Diabetes |
| Q27 | varchar |  |  | SI | Patient states their diabetes is controlled |
| Q28 | varchar |  |  | SI | Notes |
| Q34 | varchar |  |  | SI | Accommodation type |
| Q35 | varchar |  |  | SI | Other accommodation type |
| Q36 | varchar |  |  | SI | Has own bedroom |
| Q37 | varchar |  |  | SI | Other residents |
| Q38 | numeric |  |  | SI | Number of adults in household |
| Q39 | numeric |  |  | SI | Number of children in household |
| Q40 | numeric |  |  | SI | Number of grandchildren in  household |
| Q41 | varchar |  |  | SI | Other resident notes |
| Q42 | varchar |  |  | SI | Pets in home |
| Q43 | varchar |  |  | SI | Bathroom location / accessibility |
| Q44 | varchar |  |  | SI | Power supply |
| Q45 | varchar |  |  | SI | Other power supply |
| Q46 | varchar |  |  | SI | Clean room available for storage and performing ex... |
| Q47 | varchar |  |  | SI | Housing notes |
| Q48 | varchar |  |  | SI | Assessed as able to perform Independently |
| Q49 | varchar |  |  | SI | Carer required |
| Q50 | varchar |  |  | SI | Recommendation |
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