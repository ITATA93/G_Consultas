# SQLUser.PAC_AdmSource

**Schema:** SQLUser
**Columnas:** 93
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ADSOU_RowId | bigint | PK |  | NO | - |
| ADSOU_AdmReason | varchar |  |  | SI | AdmReason |
| ADSOU_AgeFrom | double |  |  | SI | Age From |
| ADSOU_AgeTo | double |  |  | SI | Age To |
| ADSOU_AgeType | varchar |  |  | SI | AgeType |
| ADSOU_CareType | varchar |  |  | SI | CareType |
| ADSOU_Code | varchar |  |  | SI | Admission Source Code |
| ADSOU_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| ADSOU_CreatedDate | date |  |  | SI | Created Date |
| ADSOU_CreatedTime | time |  |  | SI | Created Time |
| ADSOU_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ADSOU_DateFrom | date |  |  | SI | Date From |
| ADSOU_DateTo | date |  |  | SI | Date To |
| ADSOU_Desc | varchar |  |  | SI | Admission Source Description |
| ADSOU_EpisodeType | varchar |  |  | SI | Episode Type |
| ADSOU_InpatAdmType | varchar |  |  | SI | InpatAdmType |
| ADSOU_IntentReadmit | varchar |  |  | SI | IntentReadmit |
| ADSOU_NationalCode | varchar |  |  | SI | National Code |
| ADSOU_Owner | varchar |  |  | SI | Owner |
| ADSOU_QualificationStatus | varchar |  |  | SI | Qualification Status CT codes |
| ADSOU_RcFlag | varchar |  |  | SI | Archived Flag |
| ADSOU_ReasonForCritCareTransfer | varchar |  |  | SI | Reason For Crit Care Transfer |
| ADSOU_TransferSource | varchar |  |  | SI | Transfer Source |
| ADSOU_UpdatedDate | date |  |  | SI | Updated Date |
| ADSOU_UpdatedTime | time |  |  | SI | Updated Time |
| ADSOU_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | History of chest pain |
| Q02 | - |  |  | SI | Electrocardiogram (ECG) |
| Q03 | - |  |  | SI | Age |
| Q04 | - |  |  | SI | Risk factors for atherosclerotic disease	 |
| Q05 | - |  |  | SI | Troponin |
| Q06 | - |  |  | SI | Risk factors for atherosclerotic disease include:	 |
| Q07 | - |  |  | SI | Hypercholesterolemia, hypertension, diabetes melli... |
| Q08 | - |  |  | SI | Score |
| Q09 | - |  |  | SI | 0-3 holds a risk of 2.5% for an adverse outcome an... |
| Q10 | - |  |  | SI | 4-6 supports that immediate discharge is not an op... |
| Q11 | - |  |  | SI | ≥7 holds a risk of 72.7% and implies early aggress... |
| Q12 | - |  |  | SI | The HEART score is a tool for evaluating patients ... |
| Q13 | - |  |  | SI | treated as an acute coronary syndrome (ACS) awaiti... |
| Q14 | - |  |  | SI | Provides information that can correctly place pati... |
| Q15 | - |  |  | SI | Suspicious history of chest pain includes:	 |
| Q16 | - |  |  | SI | Retrosternal pain, pressure, radiation to jaw/left... |
| Q17 | - |  |  | SI | Low risk features of chest pain include: well loca... |
| Q18 | - |  |  | SI | 0 - 3 supports early discharge	 |
| Q19 | - |  |  | SI | 4 - 6 supports admission for clinical observation ... |
| Q20 | - |  |  | SI | ≥ 7 supports early invasive strategies for aggress... |
| Q21 | - |  |  | SI | Date |
| Q22 | - |  |  | SI | Time |
| Q23 | - |  |  | SI | Suspicious history of chest pain includes: |
| Q24 | - |  |  | SI | Risk factors for atherosclerotic disease: |
| Q25 | - |  |  | SI | Score interpretation: |
| Q26 | - |  |  | SI | Provenance Details |
| Q27 | - |  |  | SI | Source: Six AJ, Backus BE, Kelder JC. Chest pain i... |
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