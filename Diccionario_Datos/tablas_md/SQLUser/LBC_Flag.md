# SQLUser.LBC_Flag

**Schema:** SQLUser
**Columnas:** 72
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Laboratorio**. Parámetros del módulo de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCF_RowID | bigint | PK |  | NO | - |
| LBCF_Code | varchar |  |  | NO | Code |
| LBCF_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LBCF_Colour | varchar |  |  | SI | Colour |
| LBCF_CreatedDate | date |  |  | SI | Created Date |
| LBCF_CreatedTime | time |  |  | SI | Created Time |
| LBCF_CreatedUser_DR | bigint |  | FK | SI | Created User |
| LBCF_DateFrom | date |  |  | SI | Date From |
| LBCF_DateTo | date |  |  | SI | Date To |
| LBCF_Desc | varchar |  |  | NO | Description |
| LBCF_ExcludeFromElectronicIssue | varchar |  |  | SI | Exclude from Electronic Issue |
| LBCF_Owner | varchar |  |  | SI | Owner |
| LBCF_Rank | numeric |  |  | SI | Rank of the flag, lowest rank will be displayed fi... |
| LBCF_Type | varchar |  |  | SI | Type
Standardtype: LabInstrumentFlag |
| LBCF_UpdatedDate | date |  |  | SI | Updated Date |
| LBCF_UpdatedTime | time |  |  | SI | Updated Time |
| LBCF_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Clasificación Herida Operatoria: |
| Q02 | - |  |  | SI | Otro |
| Q03 | - |  |  | SI | Especialidad: |
| Q04 | - |  |  | SI | Tipo de ASA: |
| Q05 | - |  |  | SI | Diagnóstico Preoperatorio: |
| Q06 | - |  |  | SI | Diagnóstico Postoperatorio: |
| Q07 | - |  |  | SI | Prioridad del Caso quirúrgico: |
| Q08 | - |  |  | SI | Otro |
| Q09 | - |  |  | SI | Aislamiento Pabellón |
| Q10 | - |  |  | SI | Motivo Atraso (si, corresponde): |
| Q11 | - |  |  | SI | Otro |
| Q12 | - |  |  | SI | Motivo de Atraso /Sí, corresponde) |
| Q13 | - |  |  | SI | Otro |
| Q14 | - |  |  | SI | Otros |
| Q15 | - |  |  | SI | Otro Motivo de Atraso |
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