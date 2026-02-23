# questionnaire.QTCEANSIEHA

**Schema:** questionnaire
**Columnas:** 68
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Cuestionario/Formulario**. Plantilla de evaluación clínica estructurada.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CQQ01 | varchar | PK |  | SI | - |
| CQQ02 | varchar | PK |  | SI | - |
| CQQ03 | varchar | PK |  | SI | - |
| CQQ04 | varchar | PK |  | SI | - |
| CQQ05 | varchar | PK |  | SI | - |
| CQQ06 | varchar | PK |  | SI | - |
| CQQ07 | varchar | PK |  | SI | - |
| CQQ08 | varchar | PK |  | SI | - |
| CQQ09 | varchar | PK |  | SI | - |
| CQQ10 | varchar | PK |  | SI | - |
| CQQ11 | varchar | PK |  | SI | - |
| CQQ12 | varchar | PK |  | SI | - |
| CQQ13 | varchar | PK |  | SI | - |
| CQQ14 | varchar | PK |  | SI | - |
| ID | bigint | PK |  | NO | - |
| QQ01 | varchar | PK |  | SI | 1. Estado de ánimo ansioso |
| QQ02 | varchar | PK |  | SI | 2. Tensión |
| QQ03 | varchar | PK |  | SI | 3. Temores |
| QQ04 | varchar | PK |  | SI | 4. Insomnio |
| QQ05 | varchar | PK |  | SI | 5. Intelectual |
| QQ06 | varchar | PK |  | SI | 6. Estado de ánimo deprimido |
| QQ07 | varchar | PK |  | SI | 7. Sïntomas somáticos musculares |
| QQ08 | varchar | PK |  | SI | 8. Síntomas somáticos sensoriales |
| QQ09 | varchar | PK |  | SI | 9. Síntomas cardiovasculares |
| QQ10 | varchar | PK |  | SI | 10. Síntomas respiratorios |
| QQ11 | varchar | PK |  | SI | 11. Síntomas gastrointestinales |
| QQ12 | varchar | PK |  | SI | 12. Síntomas genitourinarios |
| QQ13 | varchar | PK |  | SI | 13. Síntomas autónomos |
| QQ14 | varchar | PK |  | SI | 14. Comportamiento en la entrevista (General y Fis... |
| QQ15 | varchar | PK |  | SI | Puntaje Ansiedad Psíquica |
| QQ16 | varchar | PK |  | SI | Puntaje Ansiedad Somática |
| QUESAnaDR | varchar | PK | FK | SI | Anaesthesia |
| QUESAnaOperationDR | varchar | PK | FK | SI | Operation |
| QUESConsultDR | varchar | PK | FK | SI | Consult |
| QUESCopiedComments | varchar | PK |  | SI | Copied Comments |
| QUESCopiedDate | date | PK |  | SI | Copied Date |
| QUESCopiedEpDR | bigint | PK | FK | SI | Copied Episode |
| QUESCopiedSourceDR | bigint | PK | FK | SI | Copied Source DR |
| QUESCopiedTime | time | PK |  | SI | Copied Time |
| QUESCopiedUserDR | bigint | PK | FK | SI | Copied User |
| QUESCreateDate | date | PK |  | SI | Creation Date |
| QUESCreateTime | time | PK |  | SI | Creation Time |
| QUESCreateUserDR | bigint | PK | FK | SI | Creation User |
| QUESDate | date | PK |  | SI | Last Update Date |
| QUESErrorReasonDR | bigint | PK | FK | SI | Error Reason |
| QUESFHResidentDR | bigint | PK | FK | SI | Resident |
| QUESMRClinicalPathWaysDR | varchar | PK | FK | SI | Clinical Pathway |
| QUESNRCarePlanIssuesDR | varchar | PK | FK | SI | Nurse Care Plan Issues |
| QUESOEOrdExecDR | varchar | PK | FK | SI | Order Execution |
| QUESORPreanaestheticConsultDR | bigint | PK | FK | SI | Preanaesthetic Consultation |
| QUESObsEntryDR | varchar | PK | FK | SI | Observation Entry |
| QUESOperRoomDR | bigint | PK | FK | SI | Operating Room |
| QUESPAAdmDR | bigint | PK | FK | SI | Admission |
| QUESPAPatMasDR | bigint | PK | FK | SI | Patient |
| QUESPAPregnancyDR | bigint | PK | FK | SI | Pregnancy |
| QUESPAWaitingListDR | bigint | PK | FK | SI | Waiting List |
| QUESPathwayItemDR | varchar | PK | FK | SI | Pathway Item |
| QUESPrePostExamOEOrdItemDR | varchar | PK | FK | SI | Pre/Post Exam OrdItem |
| QUESRBAppointmentDR | varchar | PK | FK | SI | Appointments |
| QUESRBApptOutcomeDR | varchar | PK | FK | SI | Appointment Outcome |
| QUESReasonForCorrectionDR | bigint | PK | FK | SI | Reason for Correction |
| QUESSSUserDefWindowDR | bigint | PK | FK | SI | Questionnaire |
| QUESScore | varchar | PK |  | SI | Score |
| QUESStatusDR | bigint | PK | FK | SI | Status |
| QUESTextResultDR | bigint | PK | FK | SI | Text Result |
| QUESTime | time | PK |  | SI | Last Update Time |
| QUESTransactionDR | varchar | PK | FK | SI | Transaction |
| QUESUserDR | bigint | PK | FK | SI | Last Update User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*