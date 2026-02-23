# SQLUser.CT_LocSpecialtyLoc

**Schema:** SQLUser
**Columnas:** 70
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de Ubicaciones**. Servicios, salas, unidades del hospital.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTLOCSPEC_ParRef | bigint | PK |  | NO | CT_Loc Parent Reference |
| CTLOCSPEC_Childsub | double |  |  | NO | Childsub |
| CTLOCSPEC_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| CTLOCSPEC_RowId | varchar |  |  | NO | - |
| CTLOCSPEC_Specialty_DR | bigint |  | FK | SI | Des Ref CTLOC |
| Q01 | - |  |  | SI | Motivo de Ingreso |
| Q02 | - |  |  | SI | Acompañado por: |
| Q03 | - |  |  | SI | Medio de Llegada |
| Q04 | - |  |  | SI | Otro Medio de LLegada |
| Q05 | - |  |  | SI | Nombre Contacto Emergencia |
| Q06 | - |  |  | SI | Teléfono Contacto Emergencia |
| Q07 | - |  |  | SI | Información Entregada por |
| Q08 | - |  |  | SI | Otro información entregado |
| Q09 | - |  |  | SI | Origen del Paciente |
| Q10 | - |  |  | SI | Procedencia Otro Centro Asistencial: Tiempo de Est... |
| Q11 | - |  |  | SI | Paciente Porta Brazalete Identificación |
| Q12 | - |  |  | SI | Paciente Porta Brazalete con Datos Completos y Leg... |
| Q13 | - |  |  | SI | comentario 01 |
| Q14 | - |  |  | SI | comentario 02 |
| Q15 | - |  |  | SI | Paciente Porta Brazalete de Alergias |
| Q16 | - |  |  | SI | comentario 03 |
| Q17 | - |  |  | SI | Dispositivos Artificiales |
| Q18 | - |  |  | SI | Otro Dispositivo |
| Q19 | - |  |  | SI | Dispositivos Clínicos |
| Q20 | - |  |  | SI | Otro Dispositivo Clínico |
| Q21 | - |  |  | SI | Exámenes que Trae el Paciente |
| Q22 | - |  |  | SI | Otro Examen |
| Q24 | - |  |  | SI | Información Entregada por Otro |
| Q25 | - |  |  | SI | Otro Dispositivo 2 |
| Q26 | - |  |  | SI | Otro Dispositivo 3 |
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