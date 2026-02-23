# SQLUser.CT_ClinicalTimeLineItem

**Schema:** SQLUser
**Columnas:** 73
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTCTLI_ParRef | bigint | PK |  | NO | - |
| CTCTLI_ClinicalProfile_DR | bigint |  | FK | SI | Reference to Clinical Profile for this Profile |
| CTCTLI_DateFrom | date |  |  | SI | Date From  |
| CTCTLI_DateTo | date |  |  | SI | Date To |
| CTCTLI_EventTimeline_DR | bigint |  | FK | SI | Reference to Event Timeline for this Profile |
| CTCTLI_Graph_DR | bigint |  | FK | SI | Reference to Graph configuration for this Profile |
| CTCTLI_ObsProfile_DR | bigint |  | FK | SI | Reference to Observation Profile for this Profile |
| CTCTLI_OrderTimeline_DR | bigint |  | FK | SI | Reference to Order Timeline for this Profile |
| CTCTLI_Owner | varchar |  |  | SI | Owner - Standard type "EditionOwnerType" |
| CTCTLI_PathwayTimeline_DR | bigint |  | FK | SI | Reference to Pathway Timeline for this Profile |
| CTCTLI_ProfileType | varchar |  |  | SI | Type |
| CTCTLI_RowID | varchar |  |  | NO | - |
| CTCTLI_Sequence | double |  |  | SI | Sequence |
| Q01 | - |  |  | SI | Fecha del Traumatismo Craneoencefálico |
| Q02 | - |  |  | SI | 1. ¿Cuál es su nombre? |
| Q03 | - |  |  | SI | ¿Cuándo nació? |
| Q04 | - |  |  | SI | ¿Dónde vive? |
| Q05 | - |  |  | SI | 2. ¿Dónde se encuentra usted ahora? Ciudad |
| Q06 | - |  |  | SI | Hospital |
| Q07 | - |  |  | SI | 3. ¿En qué fecha ingresó en este hospital? |
| Q08 | - |  |  | SI | ¿Cómo llego hasta aquí? |
| Q09 | - |  |  | SI | 4. ¿Qué es lo primero que recuerda después del acc... |
| Q10 | - |  |  | SI | ¿Puede describir con detalle lo primero que recuer... |
| Q11 | - |  |  | SI | 5. ¿Qué es lo primero que recuerda antes del accid... |
| Q12 | - |  |  | SI | ¿Puede describir con detalle lo primero que recuer... |
| Q13 | - |  |  | SI | 6. ¿Puede decirme la hora? |
| Q14 | - |  |  | SI | 7. ¿En qué día de la semana estamos? |
| Q15 | - |  |  | SI | 8. ¿En qué día del mes estamos? |
| Q16 | - |  |  | SI | 9. ¿En qué mes estamos? |
| Q17 | - |  |  | SI | 10. ¿En qué año estamos? |
| Q18 | - |  |  | SI | Puntuación total |
| Q19 | - |  |  | SI | Resultado |
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