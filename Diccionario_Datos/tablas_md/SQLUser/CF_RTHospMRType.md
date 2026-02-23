# SQLUser.CF_RTHospMRType

**Schema:** SQLUser
**Columnas:** 63
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| MRTYPE_ParRef | bigint | PK |  | NO | CF_RT Parent Reference |
| ChildQ13DR | - |  |  | SI | Child Reference: Administración de Medicamentos |
| MRTYPE_Childsub | double |  |  | NO | Childsub |
| MRTYPE_DateFrom | date |  |  | SI | Date From |
| MRTYPE_DateTo | date |  |  | SI | Date To |
| MRTYPE_Hospital_DR | bigint |  | FK | SI | Des Ref Hospital |
| MRTYPE_MRType_DR | bigint |  | FK | SI | Des Ref MRType |
| MRTYPE_RowId | varchar |  |  | NO | - |
| MRTYPE_Volume_DR | varchar |  | FK | SI | Des Ref Volume |
| Q01 | - |  |  | SI | Cirugía / Procedimiento |
| Q02 | - |  |  | SI | Detalles Procedimiento / Cirugía Menor a Realizar |
| Q03 | - |  |  | SI | Especialidad Cirugía / Procedimiento |
| Q04 | - |  |  | SI | Hora Inicio Programada |
| Q05 | - |  |  | SI | Hora Inicio Real |
| Q06 | - |  |  | SI | Hora Término |
| Q07 | - |  |  | SI | Paciente Acompañado |
| Q08 | - |  |  | SI | Biopsia |
| Q09 | - |  |  | SI | Nº Frascos |
| Q10 | - |  |  | SI | Otros Exámenes |
| Q11 | - |  |  | SI | Comentarios |
| Q12 | - |  |  | SI | Observaciones / Comentarios |
| Q14 | - |  |  | SI | Vía de Administración |
| Q16 | - |  |  | SI | Fecha Inicio Programada |
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