# SQLUser.CT_PackageItem

**Schema:** SQLUser
**Columnas:** 86
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ITM_ParRef | bigint | PK |  | NO | Parent Reference |
| ITM_Childsub | double |  |  | NO | Childsub |
| ITM_Excluded | bit |  |  | SI | Item excluded of released content of package |
| ITM_ReferenceClass | varchar |  |  | SI | Class name of content object reference |
| ITM_ReferenceId | varchar |  |  | SI | ID of content object reference |
| ITM_RelatedItem_DR | varchar |  | FK | SI | Related package item reference |
| ITM_RowId | varchar |  |  | NO | - |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Age |
| Q04 | - |  |  | SI | Age must be between 20 to 79 |
| Q05 | - |  |  | SI | Sex |
| Q06 | - |  |  | SI | Race |
| Q07 | - |  |  | SI | Systolic blood pressure (mm Hg) |
| Q07ObsDR | - |  |  | SI | Systolic blood pressure (mm Hg) DR |
| Q08 | - |  |  | SI | Value must be between 90 to 200 |
| Q09 | - |  |  | SI | Diastolic blood pressure (mm Hg) |
| Q09ObsDR | - |  |  | SI | Diastolic blood pressure (mm Hg) DR |
| Q10 | - |  |  | SI | Value must be between 60 to 130 |
| Q11 | - |  |  | SI | Total cholesterol (mg/dL) |
| Q12 | - |  |  | SI | Value must be between 130 to 320 |
| Q13 | - |  |  | SI | HDL cholesterol (mg/dL) |
| Q14 | - |  |  | SI | Value must be between 20 to 100 |
| Q15 | - |  |  | SI | LDL cholesterol (mg/dL) |
| Q16 | - |  |  | SI | Value must be between 30 to 300 |
| Q17 | - |  |  | SI | History of diabetes? |
| Q18 | - |  |  | SI | Smoker? |
| Q19 | - |  |  | SI | How long ago did patient quit smoking? |
| Q20 | - |  |  | SI | On hypertension treatment? |
| Q21 | - |  |  | SI | On a statin? |
| Q22 | - |  |  | SI | On aspirin therapy? |
| Q23 | - |  |  | SI | https://tools.acc.org/ascvd-risk-estimator-plus/#!... |
| Q24 | - |  |  | SI | Current 10-year Atherosclerotic Cardiovascular Dis... |
| Q25 | - |  |  | SI | Lifetime Atherosclerotic Cardiovascular Disease Ri... |
| Q26 | - |  |  | SI | Optimal Atherosclerotic Cardiovascular Disease Ris... |
| Q27 | - |  |  | SI | The Atherosclerotic Cardiovascular Disease Risk Es... |
| Q28 | - |  |  | SI | making to optimize care and lower risk for atheros... |
| Q29 | - |  |  | SI | • Atherosclerotic Cardiovascular Disease (ASCVD) r... |
| Q30 | - |  |  | SI | • The atherosclerotic cardiovascular disease (ASCV... |
| Q31 | - |  |  | SI | Calculator should only be used for primary prevent... |
| Q32 | - |  |  | SI | Values entered in this field should be only values... |
| Q33 | - |  |  | SI | This value is only calculated for patients between... |
| Q34 | - |  |  | SI | Current 10-year ASCVD risk % as follow: The follow... |
| Q35 | - |  |  | SI | Current 10-year Atherosclerotic Cardiovascular Dis... |
| Q36 | - |  |  | SI | Lifetime Atherosclerotic Cardiovascular Disease Ri... |
| Q37 | - |  |  | SI | Optimal Atherosclerotic Cardiovascular Disease Ris... |
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