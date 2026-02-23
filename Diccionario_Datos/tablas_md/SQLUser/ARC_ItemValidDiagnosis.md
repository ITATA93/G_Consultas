# SQLUser.ARC_ItemValidDiagnosis

**Schema:** SQLUser
**Columnas:** 71
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Arquetipo de configuración**. Definición base del sistema. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| VALD_ParRef | varchar | PK |  | NO | ARC_ItmMast Parent Reference |
| Q01 | - |  |  | SI | Clasificación ASA |
| Q02 | - |  |  | SI | Problemas en Vías Aéreas |
| Q03 | - |  |  | SI | Cuáles |
| Q04 | - |  |  | SI | Anestesia / Sedación Previa |
| Q05 | - |  |  | SI | Complicaciones en Sedación Previa |
| Q06 | - |  |  | SI | Cuáles |
| Q07 | - |  |  | SI | Ayuno |
| Q08 | - |  |  | SI | horas |
| Q09 | - |  |  | SI | Brazalete Si |
| Q10 | - |  |  | SI | Se instala Catéter Venoso Periférico Central (CVPC... |
| Q11 | - |  |  | SI | N° de Intentos |
| Q12 | - |  |  | SI | Ubicación |
| Q13 | - |  |  | SI | Fecha |
| Q14 | - |  |  | SI | Hora |
| Q15 | - |  |  | SI | Responsable |
| Q16 | - |  |  | SI | Otros |
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
| VALD_Childsub | double |  |  | NO | Childsub |
| VALD_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| VALD_CreatedDate | date |  |  | SI | Created Date |
| VALD_CreatedTime | time |  |  | SI | Created Time |
| VALD_CreatedUser_DR | bigint |  | FK | SI | Created User |
| VALD_DateFrom | date |  |  | SI | Date From |
| VALD_DateTo | date |  |  | SI | Date To |
| VALD_EpisodeType | varchar |  |  | SI | Episode Type |
| VALD_ICD_DR | bigint |  | FK | SI | Des Ref MRCICDDx |
| VALD_PostOffice_DR | bigint |  | FK | SI | Des Ref ARCPostOffice |
| VALD_RowId | varchar |  |  | NO | - |
| VALD_UpdatedDate | date |  |  | SI | Updated Date |
| VALD_UpdatedTime | time |  |  | SI | Updated Time |
| VALD_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*