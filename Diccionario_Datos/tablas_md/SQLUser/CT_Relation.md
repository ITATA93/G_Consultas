# SQLUser.CT_Relation

**Schema:** SQLUser
**Columnas:** 77
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTRLT_RowId | bigint | PK |  | NO | - |
| CTRLT_Code | varchar |  |  | NO | Code |
| CTRLT_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| CTRLT_CodeTranslated | varchar |  |  | SI | Code Translated (Computed) |
| CTRLT_CreatedDate | date |  |  | SI | Created Date |
| CTRLT_CreatedTime | time |  |  | SI | Created Time |
| CTRLT_CreatedUser_DR | bigint |  | FK | SI | Created User |
| CTRLT_CutOffAge | double |  |  | SI | CutOffAge |
| CTRLT_DateFrom | date |  |  | SI | Date From |
| CTRLT_DateTo | date |  |  | SI | Date To |
| CTRLT_DefFemaleRelationship_DR | bigint |  | FK | SI | Default Female Relationship |
| CTRLT_DefMaleRelationship_DR | bigint |  | FK | SI | Default Male Relationship |
| CTRLT_Desc | varchar |  |  | NO | Description |
| CTRLT_DescTranslated | varchar |  |  | SI | Description Translated (Computed) |
| CTRLT_Generation | varchar |  |  | SI | Relationship Generation |
| CTRLT_Owner | varchar |  |  | SI | Owner |
| CTRLT_UpdatedDate | date |  |  | SI | Updated Date |
| CTRLT_UpdatedTime | time |  |  | SI | Updated Time |
| CTRLT_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q06 | - |  |  | SI | Date |
| Q07 | - |  |  | SI | Time |
| Q08 | - |  |  | SI | 0 - 15 |
| Q09 | - |  |  | SI | Vaginal atrophy |
| Q1 | - |  |  | SI | Elasticity |
| Q10 | - |  |  | SI | 16 - 25 |
| Q11 | - |  |  | SI | No vaginal atrophy |
| Q12 | - |  |  | SI | Vaginal health index is used to evaluate vaginal w... |
| Q13 | - |  |  | SI | 0 - 15: Vaginal atrophy |
| Q14 | - |  |  | SI | 16 - 25: No vaginal atrophy |
| Q15 | - |  |  | SI | Score |
| Q16 | - |  |  | SI | Classification |
| Q17 | - |  |  | SI | Bachmann GA, Notelovitz M, Gonzalez SJ. et al.  Va... |
| Q18 | - |  |  | SI | Bachmann GA, Notelovitz M, Kelly SJ et al (1992) L... |
| Q2 | - |  |  | SI | Fluid volume |
| Q3 | - |  |  | SI | pH |
| Q4 | - |  |  | SI | Epithelial integrity |
| Q5 | - |  |  | SI | Moisture (coating) |
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