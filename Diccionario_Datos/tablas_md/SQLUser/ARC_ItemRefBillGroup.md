# SQLUser.ARC_ItemRefBillGroup

**Schema:** SQLUser
**Columnas:** 80
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Arquetipo de configuración**. Definición base del sistema. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| RFBGRP_ParRef | varchar | PK |  | NO | ARC_ItmMast Parent Reference |
| Q01 | - |  |  | SI | Fecha Realización Chequeo |
| Q02 | - |  |  | SI | Hora Realización Chequeo |
| Q03 | - |  |  | SI | Chequeo Salida Recuperación |
| Q04 | - |  |  | SI | Puntaje Escala Aldrete >= 9 puntos |
| Q05 | - |  |  | SI | Comentarios |
| Q06 | - |  |  | SI | Retiro Dispositivos Invasivos |
| Q07 | - |  |  | SI | Comentarios |
| Q08 | - |  |  | SI | Evolución Médica previa al alta |
| Q09 | - |  |  | SI | Comentarios |
| Q10 | - |  |  | SI | Chequeo entrega de pertenencias al Paciente / Acom... |
| Q11 | - |  |  | SI | Comentarios |
| Q12 | - |  |  | SI | Retiro en Silla de Ruedas |
| Q13 | - |  |  | SI | Comentarios |
| Q14 | - |  |  | SI | Informe del Procedimiento / Intervención |
| Q15 | - |  |  | SI | Comentarios |
| Q16 | - |  |  | SI | Indicaciones al Alta (Verbal o Escrita) |
| Q17 | - |  |  | SI | Comentarios |
| Q18 | - |  |  | SI | Paciente Recibe Conforme y se retira acompañado po... |
| Q19 | - |  |  | SI | Nombre |
| Q20 | - |  |  | SI | RUN |
| Q21 | - |  |  | SI | Observaciones Egreso Recuperación |
| Q22 | - |  |  | SI | Enfermera / Matrona Responsable |
| Q23 | - |  |  | SI | TENS / TONS Responsable |
| Q24 | - |  |  | SI | Indicaciones para el retiro de Biopsias |
| Q25 | - |  |  | SI | Comentarios |
| Q26 | - |  |  | SI | Entrega de Exámenes Previos al Paciente/Acompañant... |
| Q27 | - |  |  | SI | Comentarios |
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
| RFBGRP_BillGrp_DR | bigint |  | FK | SI | Des Ref ARCBillGrp |
| RFBGRP_Childsub | double |  |  | NO | Childsub |
| RFBGRP_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| RFBGRP_CreatedDate | date |  |  | SI | Created Date |
| RFBGRP_CreatedTime | time |  |  | SI | Created Time |
| RFBGRP_CreatedUser_DR | bigint |  | FK | SI | Created User |
| RFBGRP_DateFrom | date |  |  | SI | Date From |
| RFBGRP_DateTo | date |  |  | SI | Date To |
| RFBGRP_RowId | varchar |  |  | NO | - |
| RFBGRP_UpdatedDate | date |  |  | SI | Updated Date |
| RFBGRP_UpdatedTime | time |  |  | SI | Updated Time |
| RFBGRP_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*