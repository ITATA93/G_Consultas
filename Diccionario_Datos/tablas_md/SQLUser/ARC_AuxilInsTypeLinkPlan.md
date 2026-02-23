# SQLUser.ARC_AuxilInsTypeLinkPlan

**Schema:** SQLUser
**Columnas:** 74
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Arquetipo de configuración**. Definición base del sistema. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LINK_ParRef | bigint | PK |  | NO | ARC_AuxilInsurType Parent Reference |
| LINK_AuxInsType_DR | bigint |  | FK | SI | Des Ref AuxInsType |
| LINK_Childsub | double |  |  | NO | Childsub |
| LINK_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LINK_CreatedDate | date |  |  | SI | Created Date |
| LINK_CreatedTime | time |  |  | SI | Created Time |
| LINK_CreatedUser_DR | bigint |  | FK | SI | Created User |
| LINK_InsType_DR | bigint |  | FK | SI | Des Ref InsType |
| LINK_RowId | varchar |  |  | NO | - |
| LINK_UpdatedDate | date |  |  | SI | Updated Date |
| LINK_UpdatedTime | time |  |  | SI | Updated Time |
| LINK_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Edad Corregida |
| Q02 | - |  |  | SI | Timpanometría (Derecha) |
| Q03 | - |  |  | SI | Timpanometría (Izquierda) |
| Q04 | - |  |  | SI | Emisiones Otoacústicas (OAEs) |
| Q05 | - |  |  | SI | Emisiones Otoacústicas Transitorias (TEOAE) |
| Q06 | - |  |  | SI | Derecho |
| Q07 | - |  |  | SI | Izquierdo |
| Q08 | - |  |  | SI | Emisiones Otoacústicas Producto de Distorsión (DPO... |
| Q09 | - |  |  | SI | Derecho |
| Q10 | - |  |  | SI | Izquierdo |
| Q11 | - |  |  | SI | Respuesta Auditiva en Estado Estable (ASSR) |
| Q12 | - |  |  | SI | Derecho |
| Q13 | - |  |  | SI | Izquierdo |
| Q14 | - |  |  | SI | Potencial Evocado Auditivo Automatizado del Tronco... |
| Q15 | - |  |  | SI | Derecho |
| Q16 | - |  |  | SI | Izquierdo |
| Q17 | - |  |  | SI | Respuesta Auditiva del Tronco Cerebral (ABR) |
| Q18 | - |  |  | SI | Derecho |
| Q19 | - |  |  | SI | Izquierdo |
| Q20 | - |  |  | SI | Comentarios |
| Q21 | - |  |  | SI | Recomendaciones |
| Q22 | - |  |  | SI | Presenta Factores de Riesgo |
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