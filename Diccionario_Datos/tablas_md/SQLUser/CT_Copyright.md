# SQLUser.CT_Copyright

**Schema:** SQLUser
**Columnas:** 73
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| COPYR_RowId | bigint | PK |  | NO | - |
| COPYR_Code | varchar |  |  | NO | Code |
| COPYR_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| COPYR_CreatedDate | date |  |  | SI | Created Date |
| COPYR_CreatedTime | time |  |  | SI | Created Time |
| COPYR_CreatedUser_DR | bigint |  | FK | SI | Created User |
| COPYR_DateFrom | date |  |  | SI | Date From |
| COPYR_DateTo | date |  |  | SI | Date To |
| COPYR_Desc | varchar |  |  | NO | Description |
| COPYR_FileName | varchar |  |  | SI | FileName  |
| COPYR_Owner | varchar |  |  | SI | Owner |
| COPYR_StreamData | bigint |  |  | SI | - |
| COPYR_Text | varchar |  |  | SI | Copyright Text |
| COPYR_UpdatedDate | date |  |  | SI | Updated Date |
| COPYR_UpdatedTime | time |  |  | SI | Updated Time |
| COPYR_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| COPYR_websysDocument | bigint |  |  | SI | websysDocument |
| Q01 | - |  |  | SI | Esfera del Reloj |
| Q02 | - |  |  | SI | Manecillas del Reloj |
| Q03 | - |  |  | SI | Números del Reloj |
| Q04 | - |  |  | SI | Test del Reloj a la Copia (TRC) |
| Q05 | - |  |  | SI | Esfera del Reloj - Copia |
| Q06 | - |  |  | SI | Manecillas del Reloj - Copia |
| Q07 | - |  |  | SI | Números del Reloj - Copia |
| Q08 | - |  |  | SI | Test del Reloj a la Orden (TRO) |
| Q09 | - |  |  | SI | Puntaje |
| Q10 | - |  |  | SI | Puntaje |
| Q11 | - |  |  | SI | 0 - 6: Positivo |
| Q12 | - |  |  | SI | &gt |
| Q13 | - |  |  | SI | 0 - 8: Positivo |
| Q14 | - |  |  | SI | &gt |
| Q15 | - |  |  | SI | Resultado |
| Q16 | - |  |  | SI | Resultado |
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