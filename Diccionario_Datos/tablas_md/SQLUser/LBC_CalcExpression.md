# SQLUser.LBC_CalcExpression

**Schema:** SQLUser
**Columnas:** 72
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Laboratorio**. Parámetros del módulo de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCCE_RowID | bigint | PK |  | NO | - |
| LBCCE_Code | varchar |  |  | NO | Code |
| LBCCE_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LBCCE_CreatedDate | date |  |  | SI | Created Date |
| LBCCE_CreatedTime | time |  |  | SI | Created Time |
| LBCCE_CreatedUser_DR | bigint |  | FK | SI | Created User |
| LBCCE_DateFrom | date |  |  | SI | Effective date for the record |
| LBCCE_DateTo | date |  |  | SI | Last day the record is active  |
| LBCCE_Desc | varchar |  |  | NO | Description |
| LBCCE_Expression | varchar |  |  | SI | Expression or constant value |
| LBCCE_Owner | varchar |  |  | SI | Owner |
| LBCCE_System | varchar |  |  | SI | System created |
| LBCCE_Units_DR | bigint |  | FK | SI | Unit of the constant value |
| LBCCE_UpdatedDate | date |  |  | SI | Updated Date |
| LBCCE_UpdatedTime | time |  |  | SI | Updated Time |
| LBCCE_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Durante las últimas semanas: |
| Q02 | - |  |  | SI | ¿Se ha sentido triste o deprimido(a) la mayor part... |
| Q03 | - |  |  | SI | ¿Ha estado desinteresad(a) o incapaz d disfrutarl ... |
| Q04 | - |  |  | SI | ¿Ha tenido problemas para dormir (Insomnio o dormi... |
| Q05 | - |  |  | SI | ¿Se ha sentido cansado(a) o con menos energía la m... |
| Q06 | - |  |  | SI | ¿Ha notado problemas de concentración o memoria, c... |
| Q07 | - |  |  | SI | ¿Ha estado mas lento(a) para hacer las cosas, casi... |
| Q08 | - |  |  | SI | ¿Ha estado tan inquieto(a) que no puede permanecer... |
| Q09 | - |  |  | SI | ¿Ha sentido que Ud. no es tan hábil o capaz como o... |
| Q10 | - |  |  | SI | ¿Se ha sentido despreciable o culpable, casi todos... |
| Q11 | - |  |  | SI | ¿Ha notado un cambio importante en el apetito? (Au... |
| Q12 | - |  |  | SI | ¿Ha notado un cambio de peso de mas de 4 kilos? (A... |
| Q13 | - |  |  | SI | ¿Ha pensado realmente que no vale la pena vivir? |
| Q14 | - |  |  | SI | ¿Ha pensado quitarse la vida? |
| Q15 | - |  |  | SI | Resultado Criterios Diagnostico Depresión |
| Q15ObsDR | - |  |  | SI | Resultado Criterios Diagnostico Depresión DR |
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