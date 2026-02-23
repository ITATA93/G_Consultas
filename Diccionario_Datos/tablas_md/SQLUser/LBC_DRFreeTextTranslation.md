# SQLUser.LBC_DRFreeTextTranslation

**Schema:** SQLUser
**Columnas:** 66
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Laboratorio**. Parámetros del módulo de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCDRFTT_RowID | bigint | PK |  | NO | - |
| LBCDRFTT_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LBCDRFTT_CreatedDate | date |  |  | SI | Created Date |
| LBCDRFTT_CreatedTime | time |  |  | SI | Created Time |
| LBCDRFTT_CreatedUser_DR | bigint |  | FK | SI | Created User |
| LBCDRFTT_DateFrom | date |  |  | SI | Date From |
| LBCDRFTT_DateTo | date |  |  | SI | Date To |
| LBCDRFTT_LanguageTo_DR | bigint |  | FK | SI | Translation Language |
| LBCDRFTT_Owner | varchar |  |  | SI | Owner |
| LBCDRFTT_UpdatedDate | date |  |  | SI | Updated Date |
| LBCDRFTT_UpdatedTime | time |  |  | SI | Updated Time |
| LBCDRFTT_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | ¿Ha podido concentrarse bien en lo que hace? |
| Q02 | - |  |  | SI | ¿Sus preocupaciones le han hecho peder mucho sueño... |
| Q03 | - |  |  | SI | ¿Ha sentido que está jugando un papel útil en la v... |
| Q04 | - |  |  | SI | ¿Se ha sentido capaz de tomar decisiones? |
| Q05 | - |  |  | SI | ¿Se ha sentido constantemente agobiado o en tensió... |
| Q06 | - |  |  | SI | ¿Ha sentido que no puede superar sus dificultades? |
| Q07 | - |  |  | SI | ¿Ha sido capaz de disfrutar sus actividades normal... |
| Q08 | - |  |  | SI | ¿Ha sido capaz de hacer frente a sus problemas? |
| Q09 | - |  |  | SI | ¿Se ha sentido poco feliz y deprimido? |
| Q10 | - |  |  | SI | ¿Ha perdido confianza en sí mismo? |
| Q11 | - |  |  | SI | ¿Ha pensado que usted es una persona que no vale p... |
| Q12 | - |  |  | SI | ¿Se siente razonablemente feliz considerando todas... |
| Q13 | - |  |  | SI | Resultado cuestionario de salud de Goldberg |
| Q13ObsDR | - |  |  | SI | Resultado cuestionario de salud de Goldberg DR |
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