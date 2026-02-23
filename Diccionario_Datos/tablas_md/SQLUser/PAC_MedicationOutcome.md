# SQLUser.PAC_MedicationOutcome

**Schema:** SQLUser
**Columnas:** 101
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| MEDOUTC_RowId | bigint | PK |  | NO | - |
| MEDOUTC_Code | varchar |  |  | NO | Code |
| MEDOUTC_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| MEDOUTC_Color | varchar |  |  | SI | Color |
| MEDOUTC_CreatedDate | date |  |  | SI | Created Date |
| MEDOUTC_CreatedTime | time |  |  | SI | Created Time |
| MEDOUTC_CreatedUser_DR | bigint |  | FK | SI | Created User |
| MEDOUTC_Desc | varchar |  |  | NO | Description |
| MEDOUTC_Owner | varchar |  |  | SI | Owner |
| MEDOUTC_Type | varchar |  |  | SI | Type |
| MEDOUTC_UpdatedDate | date |  |  | SI | Updated Date |
| MEDOUTC_UpdatedTime | time |  |  | SI | Updated Time |
| MEDOUTC_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Items |
| Q04 | - |  |  | SI | Variance |
| Q05 | - |  |  | SI | Patient seen by the anaesthetist and anaesthetic a... |
| Q06 | - |  |  | SI | Variance |
| Q07 | - |  |  | SI | Consent completed and patient confirms understandi... |
| Q08 | - |  |  | SI | Variance |
| Q09 | - |  |  | SI | Baseline observations taken for vital signs and ne... |
| Q10 | - |  |  | SI | Variance |
| Q11 | - |  |  | SI | Nursing history completed |
| Q12 | - |  |  | SI | Variance |
| Q13 | - |  |  | SI | Usual bowel/bladder habits are documented |
| Q14 | - |  |  | SI | Variance |
| Q15 | - |  |  | SI | 12 lead electrocardiogram performed and reviewed a... |
| Q16 | - |  |  | SI | Variance |
| Q17 | - |  |  | SI | Ordered blood tests completed and reviewed |
| Q18 | - |  |  | SI | Variance |
| Q19 | - |  |  | SI | Baseline height and weight recorded |
| Q20 | - |  |  | SI | Variance |
| Q21 | - |  |  | SI | Education provided on fasting time prior to proced... |
| Q22 | - |  |  | SI | Variance |
| Q23 | - |  |  | SI | Education provided for pre-op washes and patient g... |
| Q24 | - |  |  | SI | Variance |
| Q25 | - |  |  | SI | Skin assessed for sores or fungal infection |
| Q26 | - |  |  | SI | Variance |
| Q27 | - |  |  | SI | Patient provided education regarding, expected len... |
| Q28 | - |  |  | SI | Variance |
| Q29 | - |  |  | SI | Patient provided with an information brochure |
| Q30 | - |  |  | SI | Variance |
| Q31 | - |  |  | SI | Determine discharge home capability and identify p... |
| Q32 | - |  |  | SI | Variance |
| Q33 | - |  |  | SI | Referrals to allied health services as necessary |
| Q34 | - |  |  | SI | Other referral details |
| Q35 | - |  |  | SI | Variance |
| Q36 | - |  |  | SI | Variance |
| Q37 | - |  |  | SI | Variance |
| Q38 | - |  |  | SI | Variance |
| Q39 | - |  |  | SI | Variance |
| Q40 | - |  |  | SI | Variance |
| Q41 | - |  |  | SI | Variance |
| Q42 | - |  |  | SI | Variance |
| Q43 | - |  |  | SI | Variance |
| Q44 | - |  |  | SI | Variance |
| Q45 | - |  |  | SI | Variance |
| Q46 | - |  |  | SI | Variance |
| Q47 | - |  |  | SI | Variance |
| Q48 | - |  |  | SI | Variance |
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