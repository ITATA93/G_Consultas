# SQLUser.ORC_OperationCategory

**Schema:** SQLUser
**Columnas:** 89
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Órdenes**. Parámetros de órdenes médicas.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CATEG_RowId | bigint | PK |  | NO | - |
| CATEG_Code | varchar |  |  | NO | Code |
| CATEG_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| CATEG_CreatedDate | date |  |  | SI | Created Date |
| CATEG_CreatedTime | time |  |  | SI | Created Time |
| CATEG_CreatedUser_DR | bigint |  | FK | SI | Created User |
| CATEG_DateFrom | date |  |  | SI | DateFrom |
| CATEG_DateTo | date |  |  | SI | DateTo |
| CATEG_Desc | varchar |  |  | NO | Description |
| CATEG_Owner | varchar |  |  | SI | Owner |
| CATEG_Questionnaire_DR | bigint |  | FK | SI | Des Ref Questionnaire |
| CATEG_UpdatedDate | date |  |  | SI | Updated Date |
| CATEG_UpdatedTime | time |  |  | SI | Updated Time |
| CATEG_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Brought in by |
| Q02 | - |  |  | SI | From |
| Q03 | - |  |  | SI | From (other) |
| Q04 | - |  |  | SI | Accompanied by family |
| Q05 | - |  |  | SI | Initial Assessment |
| Q06 | - |  |  | SI | Mental status |
| Q06ObsDR | - |  |  | SI | Mental status DR |
| Q07 | - |  |  | SI | Behaviour |
| Q07ObsDR | - |  |  | SI | Behaviour DR |
| Q08 | - |  |  | SI | Skin |
| Q08ObsDR | - |  |  | SI | Skin DR |
| Q09 | - |  |  | SI | Head - Wounds |
| Q09ObsDR | - |  |  | SI | Head - Wounds DR |
| Q10 | - |  |  | SI | Pupil Reaction (R) |
| Q10ObsDR | - |  |  | SI | Pupil Reaction (R) DR |
| Q11 | - |  |  | SI | Pupil Reaction (L) |
| Q11ObsDR | - |  |  | SI | Pupil Reaction (L) DR |
| Q12 | - |  |  | SI | Chest - Wounds |
| Q12ObsDR | - |  |  | SI | Chest - Wounds DR |
| Q13 | - |  |  | SI | Chest - Paradoxical movements |
| Q13ObsDR | - |  |  | SI | Chest - Paradoxical movements DR |
| Q14 | - |  |  | SI | Breath sounds (R) |
| Q14ObsDR | - |  |  | SI | Breath sounds (R) DR |
| Q15 | - |  |  | SI | Breath sounds (L) |
| Q15ObsDR | - |  |  | SI | Breath sounds (L) DR |
| Q16 | - |  |  | SI | Abdomen - Wounds |
| Q16ObsDR | - |  |  | SI | Abdomen - Wounds DR |
| Q17 | - |  |  | SI | Abdomen distended |
| Q17ObsDR | - |  |  | SI | Abdomen distended DR |
| Q18 | - |  |  | SI | Abdomen bowel sounds |
| Q18ObsDR | - |  |  | SI | Abdomen bowel sounds DR |
| Q19 | - |  |  | SI | Abdomen - Rigidity |
| Q19ObsDR | - |  |  | SI | Abdomen - Rigidity DR |
| Q20 | - |  |  | SI | Extremities - Wounds / deformities |
| Q20ObsDR | - |  |  | SI | Extremities - Wounds / deformities DR |
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