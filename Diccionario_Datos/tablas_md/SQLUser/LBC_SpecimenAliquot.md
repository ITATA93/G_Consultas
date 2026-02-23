# SQLUser.LBC_SpecimenAliquot

**Schema:** SQLUser
**Columnas:** 77
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Laboratorio**. Parámetros del módulo de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCSPA_ParRef | bigint | PK |  | NO | Parent Specimen DR |
| LBCSPA_AliquotContainer_DR | bigint |  | FK | SI | Aliqout Container |
| LBCSPA_Aliquot_DR | bigint |  | FK | NO | Aliqout Specimen |
| LBCSPA_Code | varchar |  |  | SI | Code |
| LBCSPA_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LBCSPA_DateFrom | date |  |  | SI | Date Active From |
| LBCSPA_DateTo | date |  |  | SI | Date Active To |
| LBCSPA_DefaultAliquot | varchar |  |  | SI | Default Aliquot Flag
Destinguishes between a aliq... |
| LBCSPA_DefaultVolume | double |  |  | SI | Default volume of a default aliquot |
| LBCSPA_Desc | varchar |  |  | SI | Description |
| LBCSPA_DisassociateTestSet | varchar |  |  | SI | Flag to indicate that the aliquot will disassociat... |
| LBCSPA_RowID | varchar |  |  | NO | - |
| Q01 | - |  |  | SI | Lugar de Realización de Visita de Enfermería Preop... |
| Q02 | - |  |  | SI | Fecha Realización Visita de Enfermería Preoperator... |
| Q03 | - |  |  | SI | Hora Realización Visita Enfermería Preoperatoria |
| Q04 | - |  |  | SI | Presentación y Recepción de EU |
| Q05 | - |  |  | SI | Revisión de Antecedentes Generales (Ingreso de EU,... |
| Q06 | - |  |  | SI | Nivel Compromiso de Conciencia |
| Q07 | - |  |  | SI | Limitaciones Sensitivo/ Motoras |
| Q08 | - |  |  | SI | Datos Generales de la Cirugía( monitorización, ind... |
| Q09 | - |  |  | SI | Recepción de Examenes e Imaginología (placas cd,et... |
| Q10 | - |  |  | SI | Recepción de Examenes e Imaginologia |
| Q11 | - |  |  | SI | Resuelve Consultas de Paciente y/o Familia |
| Q12 | - |  |  | SI | Procedencia del Paciente |
| Q13 | - |  |  | SI | Motivo de Atraso Preoperatorio (si corresponde) |
| Q14 | - |  |  | SI | Recepción de Examenes e Imagenología (placas cd,et... |
| Q15 | - |  |  | SI | Otros Procedencia |
| Q16 | - |  |  | SI | comentario uno |
| Q17 | - |  |  | SI | comentario dos |
| Q18 | - |  |  | SI | comentario tres |
| Q19 | - |  |  | SI | comentario cuatro |
| Q20 | - |  |  | SI | comentario cinco |
| Q21 | - |  |  | SI | El paciente refiere Alergias |
| Q22 | - |  |  | SI | Comentario |
| Q23 | - |  |  | SI | El paciente refiere Ayuno |
| Q24 | - |  |  | SI | Comentario |
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