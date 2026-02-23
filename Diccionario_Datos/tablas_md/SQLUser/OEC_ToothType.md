# SQLUser.OEC_ToothType

**Schema:** SQLUser
**Columnas:** 85
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| TOOTHT_RowId | bigint | PK |  | NO | - |
| ChildQ04DR | - |  |  | SI | Child Reference: Exposure details |
| Q01 | - |  |  | SI | Time of exposure known |
| Q02 | - |  |  | SI | Date |
| Q03 | - |  |  | SI | Time |
| Q05 | - |  |  | SI | Accidental |
| Q05N | - |  |  | SI | Note |
| Q06 | - |  |  | SI | Self inflicted |
| Q06N | - |  |  | SI | Note |
| Q09 | - |  |  | SI | Prior to arrival |
| Q10 | - |  |  | SI | Eye injury / pain |
| Q10N | - |  |  | SI | Note |
| Q11 | - |  |  | SI | Oral burns / lesions / pain |
| Q11N | - |  |  | SI | Note |
| Q15 | - |  |  | SI | Pain on swallowing |
| Q15N | - |  |  | SI | Note |
| Q17 | - |  |  | SI | Abdominal pain |
| Q17N | - |  |  | SI | Note |
| Q19 | - |  |  | SI | Dyspnea |
| Q19N | - |  |  | SI | Note |
| Q21 | - |  |  | SI | Skin exposure / burns |
| Q21N | - |  |  | SI | Note |
| Q23 | - |  |  | SI | Altered mental status |
| Q23N | - |  |  | SI | Note |
| Q25 | - |  |  | SI | Confusion |
| Q25N | - |  |  | SI | Note |
| Q27 | - |  |  | SI | Loss of consciousness |
| Q27N | - |  |  | SI | Note |
| Q29 | - |  |  | SI | Psychiatric history |
| Q30 | - |  |  | SI | Suicidal ideation |
| Q30N | - |  |  | SI | Note |
| Q32 | - |  |  | SI | Alcohol or drug abuse |
| Q32N | - |  |  | SI | Note |
| Q33 | - |  |  | SI | Hallucinations / delusions |
| Q33N | - |  |  | SI | Note |
| Q35 | - |  |  | SI | Date |
| Q36 | - |  |  | SI | Time |
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
| TOOTHT_Code | varchar |  |  | NO | Code |
| TOOTHT_CreatedDate | date |  |  | SI | Created Date |
| TOOTHT_CreatedTime | time |  |  | SI | Created Time |
| TOOTHT_CreatedUser_DR | bigint |  | FK | SI | Created User |
| TOOTHT_Desc | varchar |  |  | NO | Description |
| TOOTHT_UpdatedDate | date |  |  | SI | Updated Date |
| TOOTHT_UpdatedTime | time |  |  | SI | Updated Time |
| TOOTHT_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*