# SQLUser.ARC_PayorApprovalDiag

**Schema:** SQLUser
**Columnas:** 68
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Pagos**. Tarifas y facturación.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PAD_RowId | bigint | PK |  | NO | - |
| PAD_Code | varchar |  |  | SI | Code |
| PAD_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| PAD_CreatedDate | date |  |  | SI | Created Date |
| PAD_CreatedTime | time |  |  | SI | Created Time |
| PAD_CreatedUser_DR | bigint |  | FK | SI | Created User |
| PAD_DateFrom | date |  |  | NO | Date From |
| PAD_DateTo | date |  |  | SI | Date To |
| PAD_Desc | varchar |  |  | SI | Description |
| PAD_Owner | varchar |  |  | SI | Owner |
| PAD_UpdatedDate | date |  |  | SI | Updated Date |
| PAD_UpdatedTime | time |  |  | SI | Updated Time |
| PAD_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Número de sesión |
| Q02 | - |  |  | SI | Fecha |
| Q03 | - |  |  | SI | ¿Trae inhalador y aerocámara?	 |
| Q04 | - |  |  | SI | ¿Ha ingerido alimentos o líquidos durante la últim... |
| Q05 | - |  |  | SI | ¿Uso de musculatura accesoria? |
| Q06 | - |  |  | SI | ¿Cuál? |
| Q07 | - |  |  | SI | Saturación O2 |
| Q07ObsDR | - |  |  | SI | Saturación O2 DR |
| Q08 | - |  |  | SI | Temperatura Axilar |
| Q08ObsDR | - |  |  | SI | Temperatura Axilar DR |
| Q09 | - |  |  | SI | Frecuencia Respiratoria |
| Q09ObsDR | - |  |  | SI | Frecuencia Respiratoria DR |
| Q10 | - |  |  | SI | Frecuencia Cardíaca |
| Q10ObsDR | - |  |  | SI | Frecuencia Cardíaca DR |
| Q11 | - |  |  | SI | Evolución Diaria |
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