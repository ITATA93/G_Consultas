# SQLUser.PAC_SnomedCrossMaps

**Schema:** SQLUser
**Columnas:** 69
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SNOCM_ParRef | bigint | PK |  | NO | PAC_SnomedCrossMapSets Parent Reference |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Type of echocardiogram |
| Q04 | - |  |  | SI | Indication for focused echocardiogram |
| Q05 | - |  |  | SI | Image quality |
| Q06 | - |  |  | SI | Left ventricle size |
| Q07 | - |  |  | SI | Left ventricle function |
| Q08 | - |  |  | SI | Right ventricle size |
| Q09 | - |  |  | SI | Right ventricle function |
| Q10 | - |  |  | SI | Pericardial fluids present? |
| Q11 | - |  |  | SI | Tamponade present? |
| Q12 | - |  |  | SI | Findings suggestive of hypovolaemia? |
| Q13 | - |  |  | SI | Is formal imaging indicated? |
| Q14 | - |  |  | SI | Conclusion |
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
| SNOCM_Childsub | double |  |  | NO | Childsub |
| SNOCM_CreatedDate | date |  |  | SI | Created Date |
| SNOCM_CreatedTime | time |  |  | SI | Created Time |
| SNOCM_CreatedUser_DR | bigint |  | FK | SI | Created User |
| SNOCM_MapConceptID_DR | bigint |  | FK | SI | Des Ref SnomedConcept |
| SNOCM_MapExpression | varchar |  |  | SI | MapExpression |
| SNOCM_MapOption | varchar |  |  | SI | MapOption |
| SNOCM_MapPriority | varchar |  |  | SI | MapPriority |
| SNOCM_MapRule | varchar |  |  | SI | MapRule |
| SNOCM_MapTargetID_DR | bigint |  | FK | SI | Des Ref SnomedCrossMapTargets |
| SNOCM_RowId | varchar |  |  | NO | - |
| SNOCM_UpdatedDate | date |  |  | SI | Updated Date |
| SNOCM_UpdatedTime | time |  |  | SI | Updated Time |
| SNOCM_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*