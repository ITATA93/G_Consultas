# SQLUser.LBC_ClinicalCondition

**Schema:** SQLUser
**Columnas:** 76
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Laboratorio**. Parámetros del módulo de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCCLC_RowID | bigint | PK |  | NO | - |
| LBCCLC_Code | varchar |  |  | NO | Clinical Condition Code |
| LBCCLC_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LBCCLC_CreatedDate | date |  |  | SI | Created Date |
| LBCCLC_CreatedTime | time |  |  | SI | Created Time |
| LBCCLC_CreatedUser_DR | bigint |  | FK | SI | Created User |
| LBCCLC_DateFrom | date |  |  | SI | From Date |
| LBCCLC_DateTo | date |  |  | SI | To Date |
| LBCCLC_Desc | varchar |  |  | NO | Clinical Condition Description |
| LBCCLC_Owner | varchar |  |  | SI | Owner |
| LBCCLC_SpecialHandling_DR | bigint |  | FK | SI | Special Handling Instructions |
| LBCCLC_UpdatedDate | date |  |  | SI | Updated Date |
| LBCCLC_UpdatedTime | time |  |  | SI | Updated Time |
| LBCCLC_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Complete el cuestionario llenando con los valores ... |
| Q02 | - |  |  | SI | Peso (kg) |
| Q02ObsDR | - |  |  | SI | Peso (kg) DR |
| Q03 | - |  |  | SI | Talla (cm) |
| Q03ObsDR | - |  |  | SI | Talla (cm)  DR |
| Q04 | - |  |  | SI | Fecha |
| Q05 | - |  |  | SI | A. Ha comido menos por falta de apetito, problemas... |
| Q06 | - |  |  | SI | B. Pérdida reciente de peso (últimos 3 meses) |
| Q07 | - |  |  | SI | C. Movilidad |
| Q08 | - |  |  | SI | D. Ha tenido una enfermedad aguda o situación de e... |
| Q09 | - |  |  | SI | E. Problemas neuropsicológicos |
| Q11 | - |  |  | SI | IMC |
| Q12 | - |  |  | SI | F1. Índice de masa corporal (IMC) |
| Q13 | - |  |  | SI | F2. Circunferencia de la Pantorilla |
| Q14 | - |  |  | SI | Puntaje Screening  (max. 14 puntos) |
| Q15 | - |  |  | SI | 12 - 14 puntos: Estado Nutricional Normal |
| Q16 | - |  |  | SI | 8-11 puntos: Riesgo de Malnutrición |
| Q17 | - |  |  | SI | 0-7 puntos: Malnutrición |
| Q18 | - |  |  | SI | IMC |
| Q19 | - |  |  | SI | Date |
| Q20 | - |  |  | SI | El formulario de evaluación mini-nutricional es un... |
| Q21 | - |  |  | SI | Time |
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