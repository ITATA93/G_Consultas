# SQLUser.ARC_ItemQuestion

**Schema:** SQLUser
**Columnas:** 74
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Arquetipo de configuración**. Definición base del sistema. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUES_ParRef | varchar | PK |  | NO | ARC_ItmMast Parent Reference |
| Q01 | - |  |  | SI | Fecha Ingreso |
| Q02 | - |  |  | SI | Fecha Inicio Delirium |
| Q03 | - |  |  | SI | 1. Comienzo agudo y curso fluctuante |
| Q04 | - |  |  | SI | ¿Ha observado un cambio agudo en el estado mental ... |
| Q05 | - |  |  | SI | 2. Alteración de la atención |
| Q06 | - |  |  | SI | ¿El paciente se distrae con facilidad o tiene difi... |
| Q07 | - |  |  | SI | 3. Pensamiento desorganizado |
| Q08 | - |  |  | SI | ¿El paciente manifiesta ideas o conversaciones inc... |
| Q09 | - |  |  | SI | 4. Alteración del nivel de conciencia |
| Q10 | - |  |  | SI | ¿Está alterado el nivel de conciencia del paciente... |
| Q11 | - |  |  | SI | Hiperalerta (vigilante, hiperreactivo) |
| Q12 | - |  |  | SI | Somnoliento (se duerme con facilidad) |
| Q13 | - |  |  | SI | Estupor (responde a estímulos verbales) |
| Q14 | - |  |  | SI | Coma |
| Q15 | - |  |  | SI | Resultado |
| Q16 | - |  |  | SI | Reevaluar |
| Q17 | - |  |  | SI | Evaluador |
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
| QUES_Childsub | double |  |  | NO | Childsub |
| QUES_ClinicalDetails | varchar |  |  | SI | ClinicalDetails |
| QUES_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| QUES_CreatedDate | date |  |  | SI | Created Date |
| QUES_CreatedTime | time |  |  | SI | Created Time |
| QUES_CreatedUser_DR | bigint |  | FK | SI | Created User |
| QUES_DateFrom | date |  |  | SI | Date From |
| QUES_DateTo | date |  |  | SI | Date To |
| QUES_ForSpecCollection | varchar |  |  | SI | ForSpecimenCollection  |
| QUES_HospitalCT_DR | bigint |  | FK | SI | Hospital CT des ref |
| QUES_Mandatory | varchar |  |  | SI | Mandatory |
| QUES_Question_DR | bigint |  | FK | SI | Des Ref Question |
| QUES_RowId | varchar |  |  | NO | - |
| QUES_UpdatedDate | date |  |  | SI | Updated Date |
| QUES_UpdatedTime | time |  |  | SI | Updated Time |
| QUES_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*