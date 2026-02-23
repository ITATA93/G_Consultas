# SQLUser.AR_HICInHospitalClaim

**Schema:** SQLUser
**Columnas:** 80
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Cuentas por Cobrar (AR)**. Facturación y cobranza de pacientes.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| IHC_RowID | bigint | PK |  | NO | - |
| IHC_ErrorDetails | varchar |  |  | SI | Error details 
TrakCare internal error details |
| IHC_FundStatusCode | varchar |  |  | SI | Funds PVF assessment result code. |
| IHC_PatientBill_DR | bigint |  | FK | SI | Patient bill of the claim |
| IHC_ProcessStatusCode | varchar |  |  | SI | Code to indicate the processing status of the clai... |
| IHC_ReportStatusCode | varchar |  |  | SI | Code to indicate the report status
PROCESSING 
I... |
| IHC_StatusCode | varchar |  |  | SI | HIC Status Code
1716 - the Hub is acknowledging t... |
| IHC_TransactionID | varchar |  |  | SI | Transaction ID
A unique identifier maintained thr... |
| IHC_TransmissionDate | date |  |  | SI | Date of transmission |
| IHC_TransmissionTime | time |  |  | SI | Time of transmission |
| IHC_TransmissionUser_DR | bigint |  | FK | SI | Transmitting user |
| Q01 | - |  |  | SI | Hora Ingreso |
| Q02 | - |  |  | SI | Valoración General |
| Q03 | - |  |  | SI | Temporalidad Recuperación |
| Q04 | - |  |  | SI | Estado mental / Emocional |
| Q05 | - |  |  | SI | Otro |
| Q06 | - |  |  | SI | Nivel Sedación |
| Q07 | - |  |  | SI | Vía Aérea |
| Q08 | - |  |  | SI | Otro |
| Q09 | - |  |  | SI | Respiración |
| Q10 | - |  |  | SI | Otro |
| Q11 | - |  |  | SI | Cardiaco |
| Q12 | - |  |  | SI | Otro |
| Q13 | - |  |  | SI | Estado de la Piel |
| Q14 | - |  |  | SI | Prevención Caídas |
| Q15 | - |  |  | SI | Cama Baja |
| Q16 | - |  |  | SI | Comentarios |
| Q17 | - |  |  | SI | Barandas en Alto |
| Q18 | - |  |  | SI | Comentarios |
| Q19 | - |  |  | SI | Paciente Vigilado |
| Q20 | - |  |  | SI | Comentarios |
| Q21 | - |  |  | SI | Freno Activado |
| Q22 | - |  |  | SI | Comentarios |
| Q23 | - |  |  | SI | Timbre a Mano |
| Q24 | - |  |  | SI | Comentarios |
| Q25 | - |  |  | SI | Observaciones Generales |
| Q26 | - |  |  | SI | Uso de Medidas de Sujeción |
| Q27 | - |  |  | SI | Comentarios |
| Q28 | - |  |  | SI | Levantar Asistido |
| Q29 | - |  |  | SI | Comentarios |
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