# SQLUser.MRC_ObservationGroupItems

**Schema:** SQLUser
**Columnas:** 94
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ITM_ParRef | bigint | PK |  | NO | MRC_ObservationGroup Parent Reference |
| ITM_Childsub | double |  |  | NO | Childsub |
| ITM_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| ITM_CreatedDate | date |  |  | SI | Created Date |
| ITM_CreatedTime | time |  |  | SI | Created Time |
| ITM_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ITM_EndDate | date |  |  | SI | End Date |
| ITM_GraphingMarkSize | double |  |  | SI | Graphing Mark Size |
| ITM_NotInUse | double |  |  | SI | Not In Use |
| ITM_ObsItem_DR | bigint |  | FK | SI | Des Ref Observ Item |
| ITM_Owner | varchar |  |  | SI | Owner - DEPRECATED by Code Table Overrides |
| ITM_RowId | varchar |  |  | NO | - |
| ITM_RowPosition | double |  |  | SI | Row Position in Table |
| ITM_StartDate | date |  |  | SI | Start Date |
| ITM_SuspendedByDefault | varchar |  |  | SI | Suspended by Default |
| ITM_UpdatedDate | date |  |  | SI | Updated Date |
| ITM_UpdatedTime | time |  |  | SI | Updated Time |
| ITM_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| ITM_YAxisOnGraph | varchar |  |  | SI | Y Axis On Graph |
| Q01 | - |  |  | SI | Fecha de Notificación |
| Q02 | - |  |  | SI | N° Correlativo del Caso |
| Q03 | - |  |  | SI | N° Caso |
| Q04 | - |  |  | SI | Lugar de Ocurrencia de la Intoxicación |
| Q05 | - |  |  | SI | Otro |
| Q06 | - |  |  | SI | Nombre |
| Q07 | - |  |  | SI | C |
| Q08 | - |  |  | SI | Dirección |
| Q09 | - |  |  | SI | Comuna |
| Q10 | - |  |  | SI | Localidad |
| Q11 | - |  |  | SI | Fono |
| Q12 | - |  |  | SI | Nombre del Empleador |
| Q13 | - |  |  | SI | Fono |
| Q14 | - |  |  | SI | Tipo de Exposición |
| Q15 | - |  |  | SI | Actividad al momento de la exposición |
| Q16 | - |  |  | SI | Otro |
| Q17 | - |  |  | SI | Nombre 1 |
| Q18 | - |  |  | SI | Nombre 2 |
| Q19 | - |  |  | SI | Desconocido |
| Q20 | - |  |  | SI | Fecha primeros síntomas |
| Q21 | - |  |  | SI | Hora |
| Q22 | - |  |  | SI | Localizado |
| Q23 | - |  |  | SI | Sistémico |
| Q24 | - |  |  | SI | Otros |
| Q25 | - |  |  | SI | Vía de Exposición |
| Q26 | - |  |  | SI | Test de Colinesterasa |
| Q27 | - |  |  | SI | Resultado |
| Q28 | - |  |  | SI | Test de Colinesterasa 2 |
| Q29 | - |  |  | SI | Cuál? |
| Q30 | - |  |  | SI | No Corresponde |
| Q31 | - |  |  | SI | Destino del Intoxicado |
| Q32 | - |  |  | SI | Licencia o Reposo Médico |
| Q33 | - |  |  | SI | N° Días |
| Q34 | - |  |  | SI | Este Caso es parte de un brote |
| Q35 | - |  |  | SI | N° Probable de casos |
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