# SQLUser.PA_ORAnaestAdditStaffSnapshot

**Schema:** SQLUser
**Columnas:** 63
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PAAAS_ParRef | bigint | PK |  | NO | PA_ORAnaestSnapshot Parent Reference |
| PAAAS_CPLocation_DR | bigint |  | FK | SI | Des Resf CT_Loc |
| PAAAS_CareProvType | varchar |  |  | SI | [DEPRECATED]Deprecated in TrakCare T2017.2+ and re... |
| PAAAS_CareProv_DR | varchar |  | FK | SI | Des Ref CT_CareProv |
| PAAAS_ChildSub | double |  |  | NO | Childsub |
| PAAAS_EndDate | date |  |  | SI | End Date |
| PAAAS_EndTime | time |  |  | SI | End Time |
| PAAAS_NonCPAttendeeDetails | varchar |  |  | SI | Non CP Attendee Details |
| PAAAS_OperatingStaffRole_DR | bigint |  | FK | SI | Des Ref ORC_OperatingStaffRole |
| PAAAS_Operation_DR | bigint |  | FK | SI | Des Ref ORC_Operation |
| PAAAS_Remarks | varchar |  |  | SI | Remarks |
| PAAAS_RowId | varchar |  |  | NO | - |
| PAAAS_ShiftNumber | varchar |  |  | SI | Shift Number |
| PAAAS_StartDate | date |  |  | SI | Start Date |
| PAAAS_StartTime | time |  |  | SI | Start Time |
| PAAAS_StatePPP_DR | bigint |  | FK | SI | Des Ref PAC_StatePPP |
| Q01 | - |  |  | SI | Sextante 1 |
| Q02 | - |  |  | SI | Sextante 2 |
| Q03 | - |  |  | SI | Sextante 3 |
| Q04 | - |  |  | SI | Sextante 4 |
| Q05 | - |  |  | SI | Sextante&nbsp |
| Q06 | - |  |  | SI | Sextante 6 |
| Q07 | - |  |  | SI | Total Sextantes |
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