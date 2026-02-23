# SQLUser.LBC_Procedure

**Schema:** SQLUser
**Columnas:** 85
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Laboratorio**. Parámetros del módulo de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCPR_RowID | bigint | PK |  | NO | - |
| LBCPR_Autocomplete | varchar |  |  | SI | Autocomplete
Indicates that this procedure is aut... |
| LBCPR_BillingMode | varchar |  |  | SI | Billing Mode |
| LBCPR_Code | varchar |  |  | SI | Code |
| LBCPR_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LBCPR_ComplexityScore | numeric |  |  | SI | Complexity Score |
| LBCPR_CreatedDate | date |  |  | SI | Created Date |
| LBCPR_CreatedTime | time |  |  | SI | Created Time |
| LBCPR_CreatedUser_DR | bigint |  | FK | SI | Created User |
| LBCPR_CreatesMaterial | varchar |  |  | SI | Creates Material
Indicates that this procedure wi... |
| LBCPR_DateFrom | date |  |  | SI | Date From |
| LBCPR_DateTo | date |  |  | SI | Date To |
| LBCPR_Desc | varchar |  |  | SI | Description |
| LBCPR_IndirectCost | numeric |  |  | SI | Procedure Indirect Cost |
| LBCPR_Notes | longvarchar |  |  | SI | Notes
HTMLRichText |
| LBCPR_Owner | varchar |  |  | SI | Owner |
| LBCPR_PostAnalytical | varchar |  |  | SI | Postanalytical Flag
Indicates that this procedure... |
| LBCPR_Primary | varchar |  |  | SI | Primary
Indicates that this procedure is performe... |
| LBCPR_SOPCode | varchar |  |  | SI | SOP Code |
| LBCPR_Type | varchar |  |  | SI | Procedure Type |
| LBCPR_UpdatedDate | date |  |  | SI | Updated Date |
| LBCPR_UpdatedTime | time |  |  | SI | Updated Time |
| LBCPR_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| LBCPR_Workload | integer |  |  | SI | Procedure WorkLoad |
| Q01 | - |  |  | SI | Nivel de Conciencia |
| Q02 | - |  |  | SI | Detalle |
| Q03 | - |  |  | SI | Dificultad para hablar |
| Q04 | - |  |  | SI | Detalle |
| Q05 | - |  |  | SI | Idioma |
| Q06 | - |  |  | SI | Detalle |
| Q07 | - |  |  | SI | Alteracion de la percepcion visual |
| Q08 | - |  |  | SI | Gafas/Lentillas |
| Q09 | - |  |  | SI | Alteracion de la percepcion auditiva |
| Q10 | - |  |  | SI | Protesis |
| Q11 | - |  |  | SI | Desorientacion temporo-espacial |
| Q12 | - |  |  | SI | Perdida de memoria |
| Q13 | - |  |  | SI | Alteracion del proceso de pensamiento |
| Q14 | - |  |  | SI | Sexualidad |
| Q15 | - |  |  | SI | Metodos Anticonceptivos |
| Q16 | - |  |  | SI | Adecuado para la edad |
| Q17 | - |  |  | SI | Especificar |
| Q18 | - |  |  | SI | Objetivo Registro |
| Q19 | - |  |  | SI | Diagnóstico 1 |
| Q20 | - |  |  | SI | Diagnóstico 2 |
| Q21 | - |  |  | SI | Conclusión |
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