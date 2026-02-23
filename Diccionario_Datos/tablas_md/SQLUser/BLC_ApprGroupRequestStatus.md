# SQLUser.BLC_ApprGroupRequestStatus

**Schema:** SQLUser
**Columnas:** 78
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Estados posibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| APGRPRST_RowId | bigint | PK |  | NO | - |
| APGRPRST_Code | varchar |  |  | NO | Code |
| APGRPRST_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| APGRPRST_CreatedDate | date |  |  | SI | Created Date |
| APGRPRST_CreatedTime | time |  |  | SI | Created Time |
| APGRPRST_CreatedUser_DR | bigint |  | FK | SI | Created User |
| APGRPRST_DateFrom | date |  |  | SI | Date From |
| APGRPRST_DateTo | date |  |  | SI | Date To |
| APGRPRST_Desc | varchar |  |  | NO | Description |
| APGRPRST_InitialStatus | varchar |  |  | SI | Initial Status |
| APGRPRST_NoEditAllowed | varchar |  |  | SI | No Edit Allowed |
| APGRPRST_Owner | varchar |  |  | SI | Owner |
| APGRPRST_UpdatedDate | date |  |  | SI | Updated Date |
| APGRPRST_UpdatedTime | time |  |  | SI | Updated Time |
| APGRPRST_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Antes de la realización del procedimiento |
| Q02 | - |  |  | SI | 1. El endoscopista repasa con el paciente: Procedi... |
| Q03 | - |  |  | SI | 2. Consentimiento informado, contiene: |
| Q04 | - |  |  | SI | Datos completos del paciente y firma |
| Q05 | - |  |  | SI | Procedimiento a realizar |
| Q06 | - |  |  | SI | Beneficios y potenciales complicaciones |
| Q07 | - |  |  | SI | Nombre y firma del médico |
| Q08 | - |  |  | SI | Fecha del procedimiento |
| Q09 | - |  |  | SI | 3. El médico conoce antecedentes mórbidos del paci... |
| Q10 | - |  |  | SI | 4. El endoscopista y la enfermera confirman verbal... |
| Q11 | - |  |  | SI | Identificación del paciente |
| Q12 | - |  |  | SI | Procedimiento a realizar |
| Q13 | - |  |  | SI | Posibilidad de Biopsia y/u otro examen |
| Q14 | - |  |  | SI | Endoscopio desinfectado (DAN) |
| Q15 | - |  |  | SI | 5. Enfermería Chequea: |
| Q16 | - |  |  | SI | Posición correcta del paciente (DLI) |
| Q17 | - |  |  | SI | Pulsioxímetro instalado y en funcionamiento |
| Q18 | - |  |  | SI | Acceso venoso y/o equipo fleboclisis preparado |
| Q19 | - |  |  | SI | Sistema de succión, aire e irrigación |
| Q20 | - |  |  | SI | Captura de imágenes comprobados |
| Q21 | - |  |  | SI | Fecha Evaluación |
| Q22 | - |  |  | SI | Hora Evaluación |
| Q23 | - |  |  | SI | Responsable del registro |
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