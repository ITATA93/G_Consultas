# SQLUser.LBC_QCReviewType

**Schema:** SQLUser
**Columnas:** 69
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCQCRT_RowID | bigint | PK |  | NO | - |
| LBCQCRT_Code | varchar |  |  | SI | Code |
| LBCQCRT_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LBCQCRT_CreatedDate | date |  |  | SI | Created Date |
| LBCQCRT_CreatedTime | time |  |  | SI | Created Time |
| LBCQCRT_CreatedUser_DR | bigint |  | FK | SI | Created User |
| LBCQCRT_DateFrom | date |  |  | SI | Date From |
| LBCQCRT_DateTo | date |  |  | SI | Date To |
| LBCQCRT_Desc | varchar |  |  | SI | Description |
| LBCQCRT_Owner | varchar |  |  | SI | Owner |
| LBCQCRT_UpdatedDate | date |  |  | SI | Updated Date |
| LBCQCRT_UpdatedTime | time |  |  | SI | Updated Time |
| LBCQCRT_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Fecha de última menstruación (regla): |
| Q02 | - |  |  | SI | Durante el último año la menstruación me llega: |
| Q03 | - |  |  | SI | El sangrado de mi menstruación es: |
| Q04 | - |  |  | SI | Uso pastillas anticonceptivas |
| Q05 | - |  |  | SI | Uso otras hormonas |
| Q06 | - |  |  | SI | Estoy operada para no tener más hijos |
| Q07 | - |  |  | SI | Tengo útero |
| Q08 | - |  |  | SI | Tengo ovarios (al menos uno) |
| Q09 | - |  |  | SI | Tengo pareja |
| Q10 | - |  |  | SI | Tengo actividad sexual |
| Q11 | - |  |  | SI | Uso antidepresivos o remedios para dormir |
| Q12 | - |  |  | SI | Uso remedios para la diabetes |
| Q13 | - |  |  | SI | Uso remedios para la presión arterial |
| Q14 | - |  |  | SI | Estoy en control en otros programas de mi consulto... |
| Q15 | - |  |  | SI | ¿En cuál/cuáles? |
| Q16 | - |  |  | SI | Paciente Bajo Terapia Hormonal de Reemplazo? [REM] |
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