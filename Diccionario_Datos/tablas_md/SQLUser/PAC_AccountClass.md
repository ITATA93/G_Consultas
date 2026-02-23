# SQLUser.PAC_AccountClass

**Schema:** SQLUser
**Columnas:** 112
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ACCL_RowId | bigint | PK |  | NO | - |
| ACCL_AccomType | varchar |  |  | SI | AccomType |
| ACCL_CareType | varchar |  |  | SI | CareType |
| ACCL_CasePaymentRate | double |  |  | SI | Case Payment Rate |
| ACCL_Code | varchar |  |  | SI | Code |
| ACCL_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| ACCL_CreatedDate | date |  |  | SI | Created Date |
| ACCL_CreatedTime | time |  |  | SI | Created Time |
| ACCL_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ACCL_DateFrom | date |  |  | SI | Date From |
| ACCL_DateTo | date |  |  | SI | Date To |
| ACCL_Default | varchar |  |  | SI | Default |
| ACCL_Desc | varchar |  |  | SI | Description |
| ACCL_FundingSource | varchar |  |  | SI | FundingSource |
| ACCL_Owner | varchar |  |  | SI | Owner |
| ACCL_UnqualifiedAdm | varchar |  |  | SI | Unqualified Adm |
| ACCL_UpdatedDate | date |  |  | SI | Updated Date |
| ACCL_UpdatedTime | time |  |  | SI | Updated Time |
| ACCL_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Age |
| Q02 | - |  |  | SI | Systolic Blood Pressure (SBP) |
| Q03 | - |  |  | SI | Heart Rate (HR) |
| Q04 | - |  |  | SI | Serum Creatinine (sCr) |
| Q05 | - |  |  | SI | Congestive Heart Failure (CHF) killip class |
| Q06 | - |  |  | SI | Other risk factors |
| Q07 | - |  |  | SI | Score |
| Q08 | - |  |  | SI | Classification |
| Q09 | - |  |  | SI | Total GRACE Score (1 to 372 points) |
| Q10 | - |  |  | SI | Score predicts in hospital and 6 month risk of dea... |
| Q11 | - |  |  | SI | Non-ST Elevation Acute Coronary Syndrome |
| Q12 | - |  |  | SI | <109 |
| Q13 | - |  |  | SI | Low risk - Mortality <1% (Mortality in the hospita... |
| Q14 | - |  |  | SI | 109 - 140 |
| Q15 | - |  |  | SI | Intermediate risk - Mortality 1-3% (Mortality in t... |
| Q16 | - |  |  | SI | >140 |
| Q17 | - |  |  | SI | High risk - Mortality >3% (Mortality in the hospit... |
| Q18 | - |  |  | SI | <89 |
| Q19 | - |  |  | SI | Low risk - Mortality <3% (Mortality at 6 months) |
| Q20 | - |  |  | SI | 89 - 118 |
| Q21 | - |  |  | SI | Intermediate risk - Mortality 3-8% (Mortality at 6... |
| Q22 | - |  |  | SI | >118 |
| Q23 | - |  |  | SI | High risk - Mortality >8% (Mortality at 6 months) |
| Q24 | - |  |  | SI | ST-Elevation Acute Coronary Syndrome |
| Q25 | - |  |  | SI | <126 |
| Q26 | - |  |  | SI | Low risk - Mortality <2% (Mortality in the hospita... |
| Q27 | - |  |  | SI | 126 - 154 |
| Q28 | - |  |  | SI | Intermediate risk - Mortality 2-5% (Mortality in t... |
| Q29 | - |  |  | SI | >154 |
| Q30 | - |  |  | SI | High risk - Mortality >5% (Mortality in the hospit... |
| Q31 | - |  |  | SI | <100 |
| Q32 | - |  |  | SI | Low risk - Mortality <4.5% (Mortality at 6 months) |
| Q33 | - |  |  | SI | 100 - 127 |
| Q34 | - |  |  | SI | Intermediate risk - Mortality 4.5-11% (Mortality a... |
| Q35 | - |  |  | SI | >127 |
| Q36 | - |  |  | SI | High risk -Mortality >11% (Mortality at 6 months) |
| Q37 | - |  |  | SI | <109: Low risk - Mortality <1% (Mortality in the h... |
| Q38 | - |  |  | SI | 109 - 140: Intermediate risk - Mortality 1-3% (Mor... |
| Q39 | - |  |  | SI | >140: High risk - Mortality >3% (Mortality in the ... |
| Q40 | - |  |  | SI | <89: Low risk - Mortality <3% (Mortality at 6 mont... |
| Q41 | - |  |  | SI | 89 - 118: Intermediate risk - Mortality 3-8% (Mort... |
| Q42 | - |  |  | SI | >118: High risk - Mortality >8% (Mortality at 6 mo... |
| Q43 | - |  |  | SI | <126: Low risk - Mortality <2% (Mortality in the h... |
| Q44 | - |  |  | SI | 126 - 154: Intermediate risk - Mortality 2-5% (Mor... |
| Q45 | - |  |  | SI | >154: High risk - Mortality >5% (Mortality in the ... |
| Q46 | - |  |  | SI | <100: Low risk - Mortality <4.5% (Mortality at 6 m... |
| Q47 | - |  |  | SI | 100 - 127: Intermediate risk - Mortality 4.5-11% (... |
| Q48 | - |  |  | SI | >127: High risk -Mortality >11% (Mortality at 6 mo... |
| Q49 | - |  |  | SI | Global Registry of Acute Coronary Events (GRACE) V... |
| Q50 | - |  |  | SI | The total GRACE Score is from 1 to 372 points. The... |
| Q51 | - |  |  | SI | Please find the interpretation of the score below |
| Q52 | - |  |  | SI | Date |
| Q53 | - |  |  | SI | Time |
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

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*