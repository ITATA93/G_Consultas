# SQLUser.LBC_InstrumentReagent

**Schema:** SQLUser
**Columnas:** 83
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Laboratorio**. Parámetros del módulo de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCINR_ParRef | bigint | PK |  | NO | Parent instrument DR |
| ChildQ26DR | - |  |  | SI | Child Reference: Tratamiento |
| LBCINR_CodeTableTags | varchar |  |  | SI | List of code table tags |
| LBCINR_CreatedDate | date |  |  | SI | Created Date |
| LBCINR_CreatedTime | time |  |  | SI | Created Time |
| LBCINR_CreatedUser_DR | bigint |  | FK | SI | Created User |
| LBCINR_DateFrom | date |  |  | SI | Effective date for the record |
| LBCINR_DateTo | date |  |  | SI | Last day the record is active |
| LBCINR_Mandatory | varchar |  |  | SI | Mandatory |
| LBCINR_Reagent_DR | bigint |  | FK | NO | Reagent |
| LBCINR_RowID | varchar |  |  | NO | - |
| LBCINR_UpdatedDate | date |  |  | SI | Updated Date |
| LBCINR_UpdatedTime | time |  |  | SI | Updated Time |
| LBCINR_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Folio N° |
| Q02 | - |  |  | SI | Tipo de Accidente |
| Q03 | - |  |  | SI | Fecha Accidente |
| Q04 | - |  |  | SI | Fecha Denuncia |
| Q05 | - |  |  | SI | Animal Mordedor |
| Q06 | - |  |  | SI | Otro |
| Q07 | - |  |  | SI | Ignora Domicilio |
| Q08 | - |  |  | SI | Animal Vago |
| Q09 | - |  |  | SI | Muerto / Sacrificado |
| Q10 | - |  |  | SI | Tamaño |
| Q11 | - |  |  | SI | Color |
| Q12 | - |  |  | SI | Domicilio Animal |
| Q13 | - |  |  | SI | Poblacion |
| Q14 | - |  |  | SI | Comuna |
| Q15 | - |  |  | SI | Ciudad |
| Q16 | - |  |  | SI | Telefono |
| Q17 | - |  |  | SI | Derivado SEREMI |
| Q18 | - |  |  | SI | Fecha de la Observacion |
| Q19 | - |  |  | SI | Condiciones del Animal a la Observacion |
| Q20 | - |  |  | SI | Signos de la Enfermedad |
| Q21 | - |  |  | SI | Observacion |
| Q22 | - |  |  | SI | Nombre y Firma del Funcionario |
| Q23 | - |  |  | SI | Envio Informe a Consultorio de Origen |
| Q24 | - |  |  | SI | Indicación de Vacuna |
| Q25 | - |  |  | SI | Fecha Inicio Tratamiento |
| Q27 | - |  |  | SI | Nombre del Consultorio |
| Q28 | - |  |  | SI | Cuantificador accidente |
| Q29 | - |  |  | SI | Localidad |
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
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*