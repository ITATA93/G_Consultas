# SQLUser.MRC_ObjectiveOutcomePat

**Schema:** SQLUser
**Columnas:** 72
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Registros Médicos**. Parámetros de historia clínica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| OBJPAT_RowId | bigint | PK |  | NO | - |
| ChildQ09DR | - |  |  | SI | Child Reference: Acuerdos y Responsables de cada i... |
| OBJPAT_Code | varchar |  |  | NO | Code |
| OBJPAT_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| OBJPAT_CreatedDate | date |  |  | SI | Created Date |
| OBJPAT_CreatedTime | time |  |  | SI | Created Time |
| OBJPAT_CreatedUser_DR | bigint |  | FK | SI | Created User |
| OBJPAT_DateFrom | date |  |  | SI | DateFrom |
| OBJPAT_DateTo | date |  |  | SI | DateTo |
| OBJPAT_Desc | varchar |  |  | NO | Description |
| OBJPAT_Owner | varchar |  |  | SI | Owner |
| OBJPAT_UpdatedDate | date |  |  | SI | Updated Date |
| OBJPAT_UpdatedTime | time |  |  | SI | Updated Time |
| OBJPAT_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | CESFAM |
| Q02 | - |  |  | SI | Territorio |
| Q03 | - |  |  | SI | Fecha |
| Q04 | - |  |  | SI | Riesgo Familiar |
| Q04ObsDR | - |  |  | SI | Riesgo Familiar DR |
| Q05 | - |  |  | SI | Caso Indice |
| Q06 | - |  |  | SI | Responsables |
| Q07 | - |  |  | SI | Motivo |
| Q10 | - |  |  | SI | Objetivos |
| Q11 | - |  |  | SI | Actividades |
| Q12 | - |  |  | SI | Tiempo de intervención |
| Q13 | - |  |  | SI | Observaciones |
| Q14 | - |  |  | SI | Inclusión Social |
| Q15 | - |  |  | SI | Trabajo |
| Q16 | - |  |  | SI | Escuela |
| Q17 | - |  |  | SI | Grupos Sociales |
| Q18 | - |  |  | SI | Organizaciones |
| Q19 | - |  |  | SI | Otras. Especifique: |
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