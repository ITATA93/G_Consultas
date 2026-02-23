# SQLUser.ARC_PayorNotes

**Schema:** SQLUser
**Columnas:** 66
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Pagos**. Tarifas y facturación.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PAYNOTES_RowId | bigint | PK |  | NO | - |
| PAYNOTES_Code | varchar |  |  | NO | Code |
| PAYNOTES_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| PAYNOTES_CreatedDate | date |  |  | SI | Created Date |
| PAYNOTES_CreatedTime | time |  |  | SI | Created Time |
| PAYNOTES_CreatedUser_DR | bigint |  | FK | SI | Created User |
| PAYNOTES_DateFrom | date |  |  | SI | Date From |
| PAYNOTES_DateTo | date |  |  | SI | Date To |
| PAYNOTES_Desc | varchar |  |  | NO | Description |
| PAYNOTES_Note | varchar |  |  | SI | Comment |
| PAYNOTES_Owner | varchar |  |  | SI | Owner |
| PAYNOTES_UpdatedDate | date |  |  | SI | Updated Date |
| PAYNOTES_UpdatedTime | time |  |  | SI | Updated Time |
| PAYNOTES_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | 1. MARCHA EN SUPERFICIE PLANA |
| Q02 | - |  |  | SI | 2. CAMBIO EN LA VELOCIDAD DE LA MARCHA |
| Q03 | - |  |  | SI | 3. MARCHA CON GIROS HORIZONTALES DE LA CABEZA |
| Q04 | - |  |  | SI | 4. MARCHA CON GIROS VERTICALES DE LA CABEZA |
| Q05 | - |  |  | SI | 5. MARCHA Y GIRO SOBRE SU EJE |
| Q06 | - |  |  | SI | 6. MARCHA SOBRE OBSTÁCULO |
| Q07 | - |  |  | SI | 7. MARCHA EN TANDEM |
| Q08 | - |  |  | SI | 8. MARCHA CON LOS OJOS CERRADOS |
| Q09 | - |  |  | SI | 9. MARCHA HACIA ATRÁS |
| Q10 | - |  |  | SI | 10. USO DE ESCALERAS |
| Q11 | - |  |  | SI | Fecha Evaluación |
| Q12 | - |  |  | SI | Hora Evaluación |
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