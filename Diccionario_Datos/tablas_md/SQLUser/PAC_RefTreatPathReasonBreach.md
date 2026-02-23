# SQLUser.PAC_RefTreatPathReasonBreach

**Schema:** SQLUser
**Columnas:** 101
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| RTPRB_RowId | bigint | PK |  | NO | - |
| ChildQ13DR | - |  |  | SI | Child Reference: Carer details |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Medical / Surgical contraindications to peritoneal... |
| Q04 | - |  |  | SI | • History of diverticulitis / inflammatory bowel d... |
| Q05 | - |  |  | SI | • Respiratory / Diaphragmatic defect |
| Q06 | - |  |  | SI | • Chronic open wounds or skin conditions |
| Q07 | - |  |  | SI | • Urine/ Faecal incontinence |
| Q08 | - |  |  | SI | • Loss of PD function/ extensive abdominal adhesio... |
| Q09 | - |  |  | SI | • Psychological or emotional unable |
| Q10 | - |  |  | SI | • Severe socio- economic difficulties |
| Q11 | - |  |  | SI | • Literal and numerical incapability |
| Q12 | - |  |  | SI | Suitability assessment attended by |
| Q14 | - |  |  | SI | Previous surgery |
| Q15 | - |  |  | SI | Any previous surgery documented that may affect pa... |
| Q16 | - |  |  | SI | Abdominal scarring |
| Q17 | - |  |  | SI | Skin folds |
| Q18 | - |  |  | SI | Hernias |
| Q19 | - |  |  | SI | Diverticulitis |
| Q20 | - |  |  | SI | Respiratory / diaphragmatic defect |
| Q21 | - |  |  | SI | Physical assessment notes |
| Q24 | - |  |  | SI | Urine / faecal incontinence |
| Q25 | - |  |  | SI | Psychologically or emotionally unstable |
| Q26 | - |  |  | SI | Diabetes |
| Q27 | - |  |  | SI | Patient states their diabetes is controlled |
| Q28 | - |  |  | SI | Notes |
| Q34 | - |  |  | SI | Accommodation type |
| Q35 | - |  |  | SI | Other accommodation type |
| Q36 | - |  |  | SI | Has own bedroom |
| Q37 | - |  |  | SI | Other residents |
| Q38 | - |  |  | SI | Number of adults in household |
| Q39 | - |  |  | SI | Number of children in household |
| Q40 | - |  |  | SI | Number of grandchildren in  household |
| Q41 | - |  |  | SI | Other resident notes |
| Q42 | - |  |  | SI | Pets in home |
| Q43 | - |  |  | SI | Bathroom location / accessibility |
| Q44 | - |  |  | SI | Power supply |
| Q45 | - |  |  | SI | Other power supply |
| Q46 | - |  |  | SI | Clean room available for storage and performing ex... |
| Q47 | - |  |  | SI | Housing notes |
| Q48 | - |  |  | SI | Assessed as able to perform Independently |
| Q49 | - |  |  | SI | Carer required |
| Q50 | - |  |  | SI | Recommendation |
| QUESAnaDR | - |  |  | SI | Anaesthesia |
| QUESAnaOperationDR | - |  |  | SI | Operation |
| QUESConsultDR | - |  |  | SI | Consult |
| QUESCopiedComments | - |  |  | SI | Copied Comments |
| QUESCopiedDate | - |  |  | SI | Copied Date |
| QUESCopiedEpDR | - |  |  | SI | Copied Episode |
| QUESCopiedSourceDR | - |  |  | SI | Copied Source DR |
| QUESCopiedTime | - |  |  | SI | Copied Time |
| QUESCopiedUserDR | - |  |  | SI | Copied User |
| QUESCreateDate | - |  |  | SI | Creation Date |
| QUESCreateTime | - |  |  | SI | Creation Time |
| QUESCreateUserDR | - |  |  | SI | Creation User |
| QUESDate | - |  |  | SI | Last Update Date |
| QUESErrorReasonDR | - |  |  | SI | Error Reason |
| QUESFHResidentDR | - |  |  | SI | Resident |
| QUESMRClinicalPathWaysDR | - |  |  | SI | Clinical Pathway |
| QUESNRCarePlanIssuesDR | - |  |  | SI | Nurse Care Plan Issues |
| QUESOEOrdExecDR | - |  |  | SI | Order Execution |
| QUESORPreanaestheticConsultDR | - |  |  | SI | Preanaesthetic Consultation |
| QUESObsEntryDR | - |  |  | SI | Observation Entry |
| QUESOperRoomDR | - |  |  | SI | Operating Room |
| QUESPAAdmDR | - |  |  | SI | Admission |
| QUESPAAdverseEventDR | - |  |  | SI | Adverse Event |
| QUESPAPatMasDR | - |  |  | SI | Patient |
| QUESPAPregnancyDR | - |  |  | SI | Pregnancy |
| QUESPAWaitingListDR | - |  |  | SI | Waiting List |
| QUESPathwayItemDR | - |  |  | SI | Pathway Item |
| QUESPrePostExamOEOrdItemDR | - |  |  | SI | Pre/Post Exam OrdItem |
| QUESRBAppointmentDR | - |  |  | SI | Appointments |
| QUESRBApptOutcomeDR | - |  |  | SI | Appointment Outcome |
| QUESRBApptSlotDR | - |  |  | SI | Appointment Slot |
| QUESReasonForCorrectionDR | - |  |  | SI | Reason for Correction |
| QUESSSUserDefWindowDR | - |  |  | SI | Questionnaire |
| QUESScore | - |  |  | SI | Score |
| QUESSecondUserDR | - |  |  | SI | Second Signature |
| QUESStatusDR | - |  |  | SI | Status |
| QUESTextResultDR | - |  |  | SI | Text Result |
| QUESTime | - |  |  | SI | Last Update Time |
| QUESTransactionDR | - |  |  | SI | Transaction |
| QUESUserDR | - |  |  | SI | Last Update User |
| RTPRB_Code | varchar |  |  | NO | Code |
| RTPRB_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| RTPRB_CreatedDate | date |  |  | SI | Created Date |
| RTPRB_CreatedTime | time |  |  | SI | Created Time |
| RTPRB_CreatedUser_DR | bigint |  | FK | SI | Created User |
| RTPRB_DateFrom | date |  |  | SI | Date From |
| RTPRB_DateTo | date |  |  | SI | Date To |
| RTPRB_Default | varchar |  |  | SI | Default |
| RTPRB_Desc | varchar |  |  | NO | Description |
| RTPRB_NationalCode | varchar |  |  | SI | National Code |
| RTPRB_Owner | varchar |  |  | SI | Owner |
| RTPRB_TTG | varchar |  |  | SI | TTG |
| RTPRB_TreatmentPathway | varchar |  |  | SI | TreatmentPathway |
| RTPRB_TreatmentStage | varchar |  |  | SI | TreatmentStage |
| RTPRB_UpdatedDate | date |  |  | SI | Updated Date |
| RTPRB_UpdatedTime | time |  |  | SI | Updated Time |
| RTPRB_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*