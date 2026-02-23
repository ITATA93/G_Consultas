# SQLUser.ARC_ReceiptType

**Schema:** SQLUser
**Columnas:** 84
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Arquetipo de configuración**. Definición base del sistema. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| RECT_RowId | bigint | PK |  | NO | - |
| ChildQ18DR | - |  |  | SI | Child Reference: Motivo de consulta según adolesce... |
| Q01 | - |  |  | SI | Acompañante |
| Q02 | - |  |  | SI | Otro acompañante |
| Q03 | - |  |  | SI | Estudios |
| Q04 | - |  |  | SI | Grado Curso |
| Q05 | - |  |  | SI | Estado Civil |
| Q06 | - |  |  | SI | Peso |
| Q06ObsDR | - |  |  | SI | Peso DR |
| Q07 | - |  |  | SI | Talla |
| Q07ObsDR | - |  |  | SI | Talla DR |
| Q08 | - |  |  | SI | DE |
| Q09 | - |  |  | SI | Perímetro Cintura |
| Q09ObsDR | - |  |  | SI | Perímetro Cintura DR |
| Q10 | - |  |  | SI | IMC |
| Q11 | - |  |  | SI | Presión Arterial Sistólica |
| Q11ObsDR | - |  |  | SI | Presión Arterial Sistólica DR |
| Q12 | - |  |  | SI | Presión Arterial Diastólica |
| Q12ObsDR | - |  |  | SI | Presión Arterial Diastólica DR |
| Q13 | - |  |  | SI | Fecha última menstruación |
| Q14 | - |  |  | SI | No contesta |
| Q15 | - |  |  | SI | Tanner con Foto |
| Q16 | - |  |  | SI | Tanner Mamas |
| Q16ObsDR | - |  |  | SI | Tanner Mamas DR |
| Q17 | - |  |  | SI | Tanner Genitales |
| Q17ObsDR | - |  |  | SI | Tanner Genitales DR |
| Q20 | - |  |  | SI | Cambios Relevantes / Observaciones |
| Q21 | - |  |  | SI | Detección de riesgo |
| Q22 | - |  |  | SI | Diagnóstico Integral |
| Q23 | - |  |  | SI | Indicaciones e Interconsultas |
| Q24 | - |  |  | SI | Fecha próxima visita |
| Q25 | - |  |  | SI | DE (IMC) |
| Q26 | - |  |  | SI | Conoce fecha de última menstruación |
| Q27 | - |  |  | SI | Especificar otro Riesgo |
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
| RECT_Code | varchar |  |  | NO | Code |
| RECT_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| RECT_CreatedDate | date |  |  | SI | Created Date |
| RECT_CreatedTime | time |  |  | SI | Created Time |
| RECT_CreatedUser_DR | bigint |  | FK | SI | Created User |
| RECT_Desc | varchar |  |  | NO | Description |
| RECT_Owner | varchar |  |  | SI | Owner |
| RECT_UpdatedDate | date |  |  | SI | Updated Date |
| RECT_UpdatedTime | time |  |  | SI | Updated Time |
| RECT_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*