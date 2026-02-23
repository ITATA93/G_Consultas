# SQLUser.CT_NFMICategDepPayor

**Schema:** SQLUser
**Columnas:** 64
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PA_ParRef | varchar | PK |  | NO | CT_NFMI_CategDepart Parent Reference |
| PA_Amt | double |  |  | SI | Amt |
| PA_Childsub | double |  |  | NO | Childsub |
| PA_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| PA_CreatedDate | date |  |  | SI | Created Date |
| PA_CreatedTime | time |  |  | SI | Created Time |
| PA_CreatedUser_DR | bigint |  | FK | SI | Created User |
| PA_Date | date |  |  | SI | Date |
| PA_InsType_DR | bigint |  | FK | SI | Des Ref InsType |
| PA_RowId | varchar |  |  | NO | - |
| PA_UpdatedDate | date |  |  | SI | Updated Date |
| PA_UpdatedTime | time |  |  | SI | Updated Time |
| PA_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| PA_Weight | double |  |  | SI | Weight |
| Q01 | - |  |  | SI | ¿Está satisfecho con la ayuda que recibe de su fam... |
| Q02 | - |  |  | SI | ¿Está satisfecha con la forma en que su familia di... |
| Q03 | - |  |  | SI | ¿Encuentra que su familia acepta sus deseos de hac... |
| Q04 | - |  |  | SI | ¿Está de acuerdo con la forma en que su familia ex... |
| Q05 | - |  |  | SI | ¿Está satisfecha con la cantidad de tiempo que ust... |
| Q09 | - |  |  | SI | Resultado APGAR Familiar |
| Q09ObsDR | - |  |  | SI | Resultado APGAR Familiar DR |
| QApoyo | - |  |  | SI | 0 a 3: Disfunción Severa - Necesidad de Apoyo Inme... |
| QEvaluar | - |  |  | SI | 4 a 6: Probable Disfunción -  Evaluar. Verifique G... |
| QFuncionalidad | - |  |  | SI | 7 a 10: Funcionalidad Normal - No Requiere Interve... |
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