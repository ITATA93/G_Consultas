# SQLUser.ARC_ReasonForClaimDenial

**Schema:** SQLUser
**Columnas:** 89
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Arquetipo de configuración**. Definición base del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| REACLDEN_RowId | bigint | PK |  | NO | - |
| Q01 | - |  |  | SI | EVALUACIÓN SENSITIVA |
| Q02 | - |  |  | SI | Superficial |
| Q03 | - |  |  | SI | Comentario |
| Q04 | - |  |  | SI | Profundo |
| Q05 | - |  |  | SI | Comentario |
| Q06 | - |  |  | SI | Combinada |
| Q07 | - |  |  | SI | Comentario |
| Q08 | - |  |  | SI | TRATAMIENTO ORTÉSICO |
| Q09 | - |  |  | SI | Material |
| Q10 | - |  |  | SI | Comentario |
| Q11 | - |  |  | SI | Zona |
| Q12 | - |  |  | SI | Gran quemado (GES) |
| Q13 | - |  |  | SI | Comentario |
| Q14 | - |  |  | SI | Manejo sensorial |
| Q15 | - |  |  | SI | Indicaciones Diurno |
| Q16 | - |  |  | SI | Detalles Indicaciones&nbsp |
| Q17 | - |  |  | SI | Indicaciones Nocturno |
| Q18 | - |  |  | SI | Detalles Indicaciones Nocturno |
| Q19 | - |  |  | SI | MANEJO DE CICATRIZ |
| Q20 | - |  |  | SI | Clasificación |
| Q21 | - |  |  | SI | Comentario |
| Q22 | - |  |  | SI | Gran quemado (GES) |
| Q23 | - |  |  | SI | Comentario |
| Q24 | - |  |  | SI | Localización |
| Q25 | - |  |  | SI | Comentario |
| Q26 | - |  |  | SI | Manejo sensorial |
| Q27 | - |  |  | SI | Tratamiento compresivo |
| Q28 | - |  |  | SI | Comentario |
| Q29 | - |  |  | SI | Indicaciones |
| Q30 | - |  |  | SI | ADAPTACIONES |
| Q31 | - |  |  | SI | Alimentación |
| Q32 | - |  |  | SI | Arreglo personal |
| Q33 | - |  |  | SI | Baño (higiene mayor) |
| Q34 | - |  |  | SI | Vestuario (cuerpo superior) |
| Q35 | - |  |  | SI | Vestuario (cuerpo inferior) |
| Q36 | - |  |  | SI | Modificación AATT |
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
| REACLDEN_Code | varchar |  |  | NO | Code |
| REACLDEN_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| REACLDEN_CreatedDate | date |  |  | SI | Created Date |
| REACLDEN_CreatedTime | time |  |  | SI | Created Time |
| REACLDEN_CreatedUser_DR | bigint |  | FK | SI | Created User |
| REACLDEN_DateFrom | date |  |  | SI | Date From |
| REACLDEN_DateTo | date |  |  | SI | Date To |
| REACLDEN_Desc | varchar |  |  | NO | Description |
| REACLDEN_Owner | varchar |  |  | SI | Owner |
| REACLDEN_UpdatedDate | date |  |  | SI | Updated Date |
| REACLDEN_UpdatedTime | time |  |  | SI | Updated Time |
| REACLDEN_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*