# SQLUser.LB_QCRun

**Schema:** SQLUser
**Columnas:** 90
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio**. Módulo de laboratorio clínico.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBQCR_RowID | bigint | PK |  | NO | - |
| ChildQ39DR | - |  |  | SI | Child Reference: Antecedentes |
| LBQCR_InstrumentGroup_DR | bigint |  | FK | SI | Instrument Group |
| LBQCR_Instrument_DR | bigint |  | FK | SI | Instrument |
| LBQCR_Reagents | varchar |  |  | SI | Reagents used for this QC run |
| LBQCR_SequenceNumber | numeric |  |  | SI | Run Number |
| LBQCR_StartDate | date |  |  | SI | Start Date |
| LBQCR_StartTime | time |  |  | SI | Start Time |
| LBQCR_Status | varchar |  |  | SI | Run Status
StandardType: LabQCRunStatus |
| LBQCR_WorksheetGroup_DR | bigint |  | FK | SI | Worksheet Group |
| LBQCR_Worksheet_DR | bigint |  | FK | SI | Worksheet |
| Q01 | - |  |  | SI | RUN |
| Q02 | - |  |  | SI | Nombres |
| Q03 | - |  |  | SI | Apellido Paterno |
| Q04 | - |  |  | SI | Apellido Materno |
| Q05 | - |  |  | SI | Sexo |
| Q06 | - |  |  | SI | Fecha de Nacimiento |
| Q07 | - |  |  | SI | Edad |
| Q08 | - |  |  | SI | Dirección |
| Q09 | - |  |  | SI | Región |
| Q10 | - |  |  | SI | Ciudad/Localidad |
| Q11 | - |  |  | SI | Comuna |
| Q12 | - |  |  | SI | Teléfono |
| Q13 | - |  |  | SI | Previsión |
| Q14 | - |  |  | SI | Profesional Responsable |
| Q15 | - |  |  | SI | Región |
| Q16 | - |  |  | SI | Provincia |
| Q17 | - |  |  | SI | Comuna |
| Q18 | - |  |  | SI | Dirección |
| Q19 | - |  |  | SI | Laboratorio/Hospital |
| Q20 | - |  |  | SI | Unidad |
| Q21 | - |  |  | SI | Correo Electronico |
| Q22 | - |  |  | SI | Fono |
| Q23 | - |  |  | SI | Fax |
| Q24 | - |  |  | SI | Dirección |
| Q25 | - |  |  | SI | Región |
| Q26 | - |  |  | SI | Ciudad7Localidad |
| Q27 | - |  |  | SI | Tipo de Despacho |
| Q28 | - |  |  | SI | Comuna |
| Q29 | - |  |  | SI | Correo Laboratorio |
| Q30 | - |  |  | SI | Exámen |
| Q31 | - |  |  | SI | Fecha de la Obtención de la Muestra |
| Q32 | - |  |  | SI | Hora Obtención |
| Q33 | - |  |  | SI | Tipo de Muestra |
| Q34 | - |  |  | SI | Fecha Envío ISPCH |
| Q35 | - |  |  | SI | N° Muestra Original |
| Q36 | - |  |  | SI | Diagnóstico |
| Q37 | - |  |  | SI | Diagnóstico en Estudio |
| Q38 | - |  |  | SI | Tratamiento Antibiótico |
| Q40 | - |  |  | SI | Plan |
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