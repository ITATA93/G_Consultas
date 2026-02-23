# questionnaire.QCLXXPSENDO

> Pausa Endoscópica : Pre

**Schema:** questionnaire
**Columnas:** 64
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Pausa Endoscópica : Pre

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Antes de la realización del procedimiento |
| Q02 | varchar |  |  | SI | 1. El endoscopista repasa con el paciente: Procedi... |
| Q03 | varchar |  |  | SI | 2. Consentimiento informado, contiene: |
| Q04 | varchar |  |  | SI | Datos completos del paciente y firma |
| Q05 | varchar |  |  | SI | Procedimiento a realizar |
| Q06 | varchar |  |  | SI | Beneficios y potenciales complicaciones |
| Q07 | varchar |  |  | SI | Nombre y firma del médico |
| Q08 | varchar |  |  | SI | Fecha del procedimiento |
| Q09 | varchar |  |  | SI | 3. El médico conoce antecedentes mórbidos del paci... |
| Q10 | varchar |  |  | SI | 4. El endoscopista y la enfermera confirman verbal... |
| Q11 | varchar |  |  | SI | Identificación del paciente |
| Q12 | varchar |  |  | SI | Procedimiento a realizar |
| Q13 | varchar |  |  | SI | Posibilidad de Biopsia y/u otro examen |
| Q14 | varchar |  |  | SI | Endoscopio desinfectado (DAN) |
| Q15 | varchar |  |  | SI | 5. Enfermería Chequea: |
| Q16 | varchar |  |  | SI | Posición correcta del paciente (DLI) |
| Q17 | varchar |  |  | SI | Pulsioxímetro instalado y en funcionamiento |
| Q18 | varchar |  |  | SI | Acceso venoso y/o equipo fleboclisis preparado |
| Q19 | varchar |  |  | SI | Sistema de succión, aire e irrigación |
| Q20 | varchar |  |  | SI | Captura de imágenes comprobados |
| Q21 | date |  |  | SI | Fecha Evaluación |
| Q22 | time |  |  | SI | Hora Evaluación |
| Q23 | varchar |  |  | SI | Responsable del registro |
| QUESAnaDR | varchar |  | FK | SI | Anaesthesia |
| QUESAnaOperationDR | varchar |  | FK | SI | Operation |
| QUESConsultDR | varchar |  | FK | SI | Consult |
| QUESCopiedComments | varchar |  |  | SI | Copied Comments |
| QUESCopiedDate | date |  |  | SI | Copied Date |
| QUESCopiedEpDR | bigint |  | FK | SI | Copied Episode |
| QUESCopiedSourceDR | bigint |  | FK | SI | Copied Source DR |
| QUESCopiedTime | time |  |  | SI | Copied Time |
| QUESCopiedUserDR | bigint |  | FK | SI | Copied User |
| QUESCreateDate | date |  |  | SI | Creation Date |
| QUESCreateTime | time |  |  | SI | Creation Time |
| QUESCreateUserDR | bigint |  | FK | SI | Creation User |
| QUESDate | date |  |  | SI | Last Update Date |
| QUESErrorReasonDR | bigint |  | FK | SI | Error Reason |
| QUESFHResidentDR | bigint |  | FK | SI | Resident |
| QUESMRClinicalPathWaysDR | varchar |  | FK | SI | Clinical Pathway |
| QUESNRCarePlanIssuesDR | varchar |  | FK | SI | Nurse Care Plan Issues |
| QUESOEOrdExecDR | varchar |  | FK | SI | Order Execution |
| QUESORPreanaestheticConsultDR | bigint |  | FK | SI | Preanaesthetic Consultation |
| QUESObsEntryDR | varchar |  | FK | SI | Observation Entry |
| QUESOperRoomDR | bigint |  | FK | SI | Operating Room |
| QUESPAAdmDR | bigint |  | FK | SI | Admission |
| QUESPAAdverseEventDR | varchar |  | FK | SI | Adverse Event |
| QUESPAPatMasDR | bigint |  | FK | SI | Patient |
| QUESPAPregnancyDR | bigint |  | FK | SI | Pregnancy |
| QUESPAWaitingListDR | bigint |  | FK | SI | Waiting List |
| QUESPathwayItemDR | varchar |  | FK | SI | Pathway Item |
| QUESPrePostExamOEOrdItemDR | varchar |  | FK | SI | Pre/Post Exam OrdItem |
| QUESRBAppointmentDR | varchar |  | FK | SI | Appointments |
| QUESRBApptOutcomeDR | varchar |  | FK | SI | Appointment Outcome |
| QUESRBApptSlotDR | varchar |  | FK | SI | Appointment Slot |
| QUESReasonForCorrectionDR | bigint |  | FK | SI | Reason for Correction |
| QUESSSUserDefWindowDR | bigint |  | FK | SI | Questionnaire |
| QUESScore | varchar |  |  | SI | Score |
| QUESSecondUserDR | bigint |  | FK | SI | Second Signature |
| QUESStatusDR | bigint |  | FK | SI | Status |
| QUESTextResultDR | bigint |  | FK | SI | Text Result |
| QUESTime | time |  |  | SI | Last Update Time |
| QUESTransactionDR | varchar |  | FK | SI | Transaction |
| QUESUserDR | bigint |  | FK | SI | Last Update User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*