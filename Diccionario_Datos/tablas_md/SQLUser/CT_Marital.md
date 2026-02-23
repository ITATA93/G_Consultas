# SQLUser.CT_Marital

**Schema:** SQLUser
**Columnas:** 140
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTMAR_RowId | bigint | PK |  | NO | - |
| CQ01 | - |  |  | SI | (null) |
| CQ010 | - |  |  | SI | (null) |
| CQ011 | - |  |  | SI | (null) |
| CQ012 | - |  |  | SI | (null) |
| CQ013 | - |  |  | SI | (null) |
| CQ014 | - |  |  | SI | (null) |
| CQ015 | - |  |  | SI | (null) |
| CQ016 | - |  |  | SI | (null) |
| CQ017 | - |  |  | SI | (null) |
| CQ018 | - |  |  | SI | (null) |
| CQ019 | - |  |  | SI | (null) |
| CQ02 | - |  |  | SI | (null) |
| CQ020 | - |  |  | SI | (null) |
| CQ021 | - |  |  | SI | (null) |
| CQ022 | - |  |  | SI | (null) |
| CQ023 | - |  |  | SI | (null) |
| CQ024 | - |  |  | SI | (null) |
| CQ025 | - |  |  | SI | (null) |
| CQ026 | - |  |  | SI | (null) |
| CQ027 | - |  |  | SI | (null) |
| CQ028 | - |  |  | SI | (null) |
| CQ029 | - |  |  | SI | (null) |
| CQ03 | - |  |  | SI | (null) |
| CQ030 | - |  |  | SI | (null) |
| CQ031 | - |  |  | SI | (null) |
| CQ032 | - |  |  | SI | (null) |
| CQ033 | - |  |  | SI | (null) |
| CQ034 | - |  |  | SI | (null) |
| CQ04 | - |  |  | SI | (null) |
| CQ044 | - |  |  | SI | (null) |
| CQ05 | - |  |  | SI | (null) |
| CQ06 | - |  |  | SI | (null) |
| CQ07 | - |  |  | SI | (null) |
| CQ08 | - |  |  | SI | (null) |
| CQ09 | - |  |  | SI | (null) |
| CTMAR_Code | varchar |  |  | NO | Code |
| CTMAR_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| CTMAR_CodeTranslated | varchar |  |  | SI | Code Translated (Computed) |
| CTMAR_CreatedDate | date |  |  | SI | Created Date |
| CTMAR_CreatedTime | time |  |  | SI | Created Time |
| CTMAR_CreatedUser_DR | bigint |  | FK | SI | Created User |
| CTMAR_DateFrom | date |  |  | SI | Date From |
| CTMAR_DateTo | date |  |  | SI | Date To |
| CTMAR_Desc | varchar |  |  | NO | Description |
| CTMAR_DescTranslated | varchar |  |  | SI | Description Translated (Computed) |
| CTMAR_Owner | varchar |  |  | SI | Owner |
| CTMAR_PRS2 | varchar |  |  | SI | PRS2 |
| CTMAR_UpdatedDate | date |  |  | SI | Updated Date |
| CTMAR_UpdatedTime | time |  |  | SI | Updated Time |
| CTMAR_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Heart Rate Ventricular Response |
| Q010 | - |  |  | SI | PaCO2 |
| Q011 | - |  |  | SI | Urine output in L per day |
| Q012 | - |  |  | SI | Serum BUN in mg/dL |
| Q013 | - |  |  | SI | Serum Creatinine in mg/dL |
| Q014 | - |  |  | SI | Serum Amylase in IU |
| Q015 | - |  |  | SI | Serum Albumin in g/dL |
| Q016 | - |  |  | SI | Total Bilirubin in mg/dL |
| Q017 | - |  |  | SI | Alkaline Phosphate in IU |
| Q018 | - |  |  | SI | SGOT |
| Q019 | - |  |  | SI | Anergy by skin testing |
| Q02 | - |  |  | SI | Mean Arterial Pessure |
| Q020 | - |  |  | SI | Hematocrit in percent |
| Q021 | - |  |  | SI | WBC |
| Q022 | - |  |  | SI | Platelet count |
| Q023 | - |  |  | SI | Prothrombin time in secs greater than control |
| Q024 | - |  |  | SI | CSF positive culture |
| Q025 | - |  |  | SI | Blood Culture positive |
| Q026 | - |  |  | SI | Fungal Culture positive |
| Q027 | - |  |  | SI | Rectal temperature in C |
| Q028 | - |  |  | SI | Serum Calcium |
| Q029 | - |  |  | SI | Serum Glucose |
| Q03 | - |  |  | SI | Right Artial Pressure ot Central Venous Pressure |
| Q030 | - |  |  | SI | Serum Sodium |
| Q031 | - |  |  | SI | Serum Potassium |
| Q032 | - |  |  | SI | Serum Bicarbonate |
| Q033 | - |  |  | SI | Serum Osmolarity |
| Q034 | - |  |  | SI | Glasgow Coma Score |
| Q035 | - |  |  | SI | Cardiovascular Status |
| Q036 | - |  |  | SI | Respiratory Status |
| Q037 | - |  |  | SI | Renal Status |
| Q038 | - |  |  | SI | Gastrointestinal Status |
| Q039 | - |  |  | SI | Hematological Status |
| Q04 | - |  |  | SI | Evidence of Acute MI |
| Q040 | - |  |  | SI | Septic Status |
| Q041 | - |  |  | SI | Metabolic Status |
| Q042 | - |  |  | SI | Neurological Status |
| Q043 | - |  |  | SI | APACHE Score |
| Q044 | - |  |  | SI | Pre-Admission Health Status |
| Q045 | - |  |  | SI | D Severe restriction of activity due to disease |
| Q046 | - |  |  | SI | C chronic disease producing serious but not incapc... |
| Q047 | - |  |  | SI | B mild to moderate limitation in activity because ... |
| Q048 | - |  |  | SI | A prior good heatlh with no functional limitations |
| Q05 | - |  |  | SI | ECG Arrhythmias |
| Q06 | - |  |  | SI | Serum lactate in mg/dL |
| Q07 | - |  |  | SI | Arterial pH |
| Q08 | - |  |  | SI | Respiratory Rate Nonventilated |
| Q09 | - |  |  | SI | P(A-a) O2 with FIO2 = 1.0 |
| Q49 | - |  |  | SI | The  Acute Physiology and Chronic Health Evaluatio... |
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