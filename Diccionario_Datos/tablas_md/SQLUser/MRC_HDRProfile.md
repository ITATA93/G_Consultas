# SQLUser.MRC_HDRProfile

**Schema:** SQLUser
**Columnas:** 74
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Registros Médicos**. Parámetros de historia clínica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| HDRP_ParRef | bigint | PK |  | NO | HDR config Parent Reference |
| HDRP_Chart_DR | bigint |  | FK | SI | Chart |
| HDRP_Childsub | double |  |  | NO | Childsub |
| HDRP_ClinicalProfileDR | bigint |  | FK | SI | Clinical Profile |
| HDRP_Code | varchar |  |  | NO | Code	 |
| HDRP_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| HDRP_CreatedDate | date |  |  | SI | Created Date |
| HDRP_CreatedTime | time |  |  | SI | Created Time |
| HDRP_CreatedUser_DR | bigint |  | FK | SI | Created User |
| HDRP_DateFrom | date |  |  | SI | DateFrom |
| HDRP_DateTo | date |  |  | SI | DateTo |
| HDRP_Desc | varchar |  |  | NO | Description  |
| HDRP_GraphDR | bigint |  | FK | SI | Graph Definition |
| HDRP_Owner | varchar |  |  | SI | Owner - DEPRECATED by Code Table Overrides |
| HDRP_RowId | varchar |  |  | NO | - |
| HDRP_Seq | integer |  |  | SI | DateFrom |
| HDRP_UpdatedDate | date |  |  | SI | Updated Date |
| HDRP_UpdatedTime | time |  |  | SI | Updated Time |
| HDRP_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | N° Folio |
| Q02 | - |  |  | SI | Fecha de Notificacion |
| Q03 | - |  |  | SI | Fecha de Ingestion |
| Q04 | - |  |  | SI | Hora de Ingestion |
| Q05 | - |  |  | SI | Fecha 1° Sintomas |
| Q06 | - |  |  | SI | Caso Pertenese a Brote |
| Q07 | - |  |  | SI | Alimento Sospechoso Consumido |
| Q08 | - |  |  | SI | Lugar de Consumo |
| Q09 | - |  |  | SI | Otros |
| Q10 | - |  |  | SI | Lugar de Compra |
| Q11 | - |  |  | SI | Forma de Consumo |
| Q12 | - |  |  | SI | Otros |
| Q13 | - |  |  | SI | Signos y Sintomas |
| Q14 | - |  |  | SI | Otros |
| Q15 | - |  |  | SI | Muestra |
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