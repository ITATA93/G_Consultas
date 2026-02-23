# SQLUser.MR_DiagnosisAllocation

**Schema:** SQLUser
**Columnas:** 67
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Diagnósticos**. Códigos CIE-10 asociados al episodio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ALLOC_ParRef | varchar | PK |  | NO | MR_Diagnos Parent Reference |
| ALLOC_Appointment_DR | varchar |  | FK | SI | Des Ref Appointment |
| ALLOC_Childsub | double |  |  | NO | Childsub |
| ALLOC_RowId | varchar |  |  | NO | - |
| ALLOC_Transaction_DR | varchar |  | FK | SI | Des Ref Transaction |
| Q01 | - |  |  | SI | Inmunohistoquímico |
| Q02 | - |  |  | SI | Dosis |
| Q03 | - |  |  | SI | Fecha de Aplicación (Administración) |
| Q04 | - |  |  | SI | Lote |
| Q05 | - |  |  | SI | Observaciones (Comentarios) |
| Q06 | - |  |  | SI | Evento |
| Q07 | - |  |  | SI | Tiempo Transcurrido |
| Q08 | - |  |  | SI | Laboratorio |
| Q09 | - |  |  | SI | Notificación Gubernamental |
| Q10 | - |  |  | SI | Fecha de Notificación |
| Q11 | - |  |  | SI | Establecimiento de salud donde se administró la va... |
| Q12 | - |  |  | SI | Evolución del Caso |
| Q13 | - |  |  | SI | Cierre del Caso |
| Q14 | - |  |  | SI | Conducta a Seguir para Inmunización |
| Q15 | - |  |  | SI | Cuidados Médicos |
| Q16 | - |  |  | SI | Fecha de Ingreso |
| Q17 | - |  |  | SI | Fecha de Egreso |
| Q18 | - |  |  | SI | Establecimiento |
| Q19 | - |  |  | SI | Días |
| Q20 | - |  |  | SI | Horas |
| Q21 | - |  |  | SI | Minutes |
| Q22 | - |  |  | SI | Dirección |
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