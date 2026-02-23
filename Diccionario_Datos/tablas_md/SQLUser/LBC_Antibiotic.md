# SQLUser.LBC_Antibiotic

**Schema:** SQLUser
**Columnas:** 98
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Laboratorio**. Parámetros del módulo de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCANT_RowID | bigint | PK |  | NO | - |
| CQ004 | - |  |  | SI | (null) |
| CQ024 | - |  |  | SI | (null) |
| LBCANT_AgeMax | double |  |  | SI | Maximum age for antibiotic |
| LBCANT_AgeMin | double |  |  | SI | Minimum age for antibiotic |
| LBCANT_AntibioticClass_DR | bigint |  | FK | SI | Antibiotic Class |
| LBCANT_Code | varchar |  |  | SI | Code |
| LBCANT_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LBCANT_CreatedDate | date |  |  | SI | Created Date |
| LBCANT_CreatedTime | time |  |  | SI | Created Time |
| LBCANT_CreatedUser_DR | bigint |  | FK | SI | Created User |
| LBCANT_DateFrom | date |  |  | SI | Effective date for the record |
| LBCANT_DateTo | date |  |  | SI | Last day the record is active  |
| LBCANT_Desc | varchar |  |  | SI | Description |
| LBCANT_NotForPregnantFlag | varchar |  |  | SI | Not for Pregnant Flag |
| LBCANT_OXOID_Code | varchar |  |  | SI | OXOID Code |
| LBCANT_Owner | varchar |  |  | SI | Owner |
| LBCANT_Sequence | double |  |  | SI | Display Sequence |
| LBCANT_SexAllowed | varchar |  |  | SI | Allowed for Sex |
| LBCANT_UpdatedDate | date |  |  | SI | Updated Date |
| LBCANT_UpdatedTime | time |  |  | SI | Updated Time |
| LBCANT_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q001 | - |  |  | SI | Fecha |
| Q002 | - |  |  | SI | Nombre Completo Acompañante |
| Q003 | - |  |  | SI | RUT Acompañante |
| Q004 | - |  |  | SI | Autorización para que se practiquen Exámenes Corpo... |
| Q005 | - |  |  | SI | Motivo de Negativa de Realización de Examen |
| Q006 | - |  |  | SI | Procedimiento |
| Q007 | - |  |  | SI | Fecha |
| Q008 | - |  |  | SI | Hora |
| Q009 | - |  |  | SI | Descripción de Especie |
| Q010 | - |  |  | SI | Unidad Policial |
| Q011 | - |  |  | SI | Levantada por |
| Q012 | - |  |  | SI | N° de paciente |
| Q013 | - |  |  | SI | RUT |
| Q014 | - |  |  | SI | Cargo |
| Q015 | - |  |  | SI | Observaciones Indicadas por el Fiscal |
| Q016 | - |  |  | SI | De |
| Q017 | - |  |  | SI | Fecha |
| Q018 | - |  |  | SI | Nombre (Grado) |
| Q019 | - |  |  | SI | RUT |
| Q020 | - |  |  | SI | Motivo de Traslado |
| Q021 | - |  |  | SI | Para (Estado Especie) |
| Q022 | - |  |  | SI | De (Estado Especie) |
| Q023 | - |  |  | SI | Hora (Estado Especie) |
| Q024 | - |  |  | SI | ¿Víctima es Menor de Edad? |
| Q025 | - |  |  | SI | Para 2 |
| Q026 | - |  |  | SI | De |
| Q027 | - |  |  | SI | Hora 2 |
| Q028 | - |  |  | SI | Para 3 |
| Q029 | - |  |  | SI | De 3 |
| Q030 | - |  |  | SI | Hora 3 |
| Q031 | - |  |  | SI | De 4 |
| Q032 | - |  |  | SI | Para 4 |
| Q033 | - |  |  | SI | Hora 4 |
| Q034 | - |  |  | SI | De 5 |
| Q035 | - |  |  | SI | Para 5 |
| Q036 | - |  |  | SI | Hora 5 |
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