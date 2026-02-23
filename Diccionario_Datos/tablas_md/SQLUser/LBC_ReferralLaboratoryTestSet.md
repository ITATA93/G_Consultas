# SQLUser.LBC_ReferralLaboratoryTestSet

**Schema:** SQLUser
**Columnas:** 65
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Laboratorio**. Parámetros del módulo de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCRLTS_ParRef | bigint | PK |  | NO | Parent Reference |
| LBCRLTS_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LBCRLTS_DateFrom | date |  |  | SI | Effective date for the record |
| LBCRLTS_DateTo | date |  |  | SI | Last day the record is active  |
| LBCRLTS_ExternalTestSet | varchar |  |  | SI | External Test Set Code |
| LBCRLTS_RowID | varchar |  |  | NO | - |
| LBCRLTS_TestSet_DR | bigint |  | FK | SI | Test Set DR |
| Q01 | - |  |  | SI | Movilidad |
| Q02 | - |  |  | SI | Cuidado personal |
| Q03 | - |  |  | SI | Actividades Habituales |
| Q04 | - |  |  | SI | Dolor / Malestar |
| Q05 | - |  |  | SI | Angustia / Depresión |
| Q06 | - |  |  | SI | Mi estado de salud hoy es: |
| Q07 | - |  |  | SI | Su estado de salud hoy |
| Q08 | - |  |  | SI | Movilidad |
| Q09 | - |  |  | SI | Cuidado Personal |
| Q10 | - |  |  | SI | Actividades Habituales |
| Q11 | - |  |  | SI | Dolor / Malestar |
| Q12 | - |  |  | SI | Angustia / Depresión |
| Q13 | - |  |  | SI | Resultado Movilidad |
| Q14 | - |  |  | SI | Resultado Cuidado Personal |
| Q15 | - |  |  | SI | Resultado Actividades Habituales |
| Q16 | - |  |  | SI | Resultado Dolor / Malestar |
| Q17 | - |  |  | SI | Resultado Angustia / Depresión |
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