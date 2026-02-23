# SQLUser.MRC_ObservationItemAttrExtCodes

**Schema:** SQLUser
**Columnas:** 72
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| EXTCODE_ParRef | varchar | PK |  | NO | - |
| ChildQ16DR | - |  |  | SI | Child Reference: Ingreso de Profesional Participan... |
| EXTCODE_Childsub | double |  |  | NO | Childsub |
| EXTCODE_Code | varchar |  |  | NO | Code |
| EXTCODE_CreatedDate | date |  |  | SI | Created Date |
| EXTCODE_CreatedTime | time |  |  | SI | Created Time |
| EXTCODE_CreatedUser_DR | bigint |  | FK | SI | Created User |
| EXTCODE_DateFrom | date |  |  | SI | Active Date From for new Observation Entries |
| EXTCODE_DateTo | date |  |  | SI | Active Date To for new Observation Entries |
| EXTCODE_Desc | varchar |  |  | NO | Description |
| EXTCODE_Generated | varchar |  |  | SI | ExtCodes has been used in previous data - Code can... |
| EXTCODE_RowId | varchar |  |  | NO | - |
| EXTCODE_UpdatedDate | date |  |  | SI | Updated Date |
| EXTCODE_UpdatedTime | time |  |  | SI | Updated Time |
| EXTCODE_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Fecha Ronda(s) |
| Q02 | - |  |  | SI | Tipo de Ronda |
| Q03 | - |  |  | SI | Cantidad de Rondas |
| Q04 | - |  |  | SI | Médico |
| Q05 | - |  |  | SI | Dentista |
| Q06 | - |  |  | SI | Enfermera |
| Q07 | - |  |  | SI | Matrona |
| Q08 | - |  |  | SI | Nutricionista |
| Q09 | - |  |  | SI | Tec. Paramédico |
| Q10 | - |  |  | SI | Asistente Social |
| Q11 | - |  |  | SI | Psicólogo |
| Q12 | - |  |  | SI | Otros |
| Q13 | - |  |  | SI | N° traslado de profesionales compra de servicio |
| Q14 | - |  |  | SI | Sin Compra de Servicio |
| Q15 | - |  |  | SI | Por Compra de Servicio |
| Q16Q1 | - |  |  | SI | Tipo de Profesional |
| QHR | - |  |  | SI | Establecimiento |
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