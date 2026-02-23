# SQLUser.ORC_CatheterType

**Schema:** SQLUser
**Columnas:** 68
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTHTP_RowId | bigint | PK |  | NO | - |
| CTHTP_Code | varchar |  |  | NO | Code |
| CTHTP_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| CTHTP_CreatedDate | date |  |  | SI | Created Date |
| CTHTP_CreatedTime | time |  |  | SI | Created Time |
| CTHTP_CreatedUser_DR | bigint |  | FK | SI | Created User |
| CTHTP_DateFrom | date |  |  | SI | Date From |
| CTHTP_DateTo | date |  |  | SI | Date To |
| CTHTP_Desc | varchar |  |  | NO | Description |
| CTHTP_Owner | varchar |  |  | SI | Owner |
| CTHTP_UpdatedDate | date |  |  | SI | Updated Date |
| CTHTP_UpdatedTime | time |  |  | SI | Updated Time |
| CTHTP_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Fecha |
| Q02 | - |  |  | SI | Hora |
| Q03 | - |  |  | SI | Escala Visual de Fragilidad |
| Q04 | - |  |  | SI | Puntuación de la fragilidad en una paciente con de... |
| Q05 | - |  |  | SI | • El grado de fragilidad corresponde al grado de d... |
| Q06 | - |  |  | SI | • Los síntomas comunes en la demencia leve incluye... |
| Q07 | - |  |  | SI | • En la demencia moderada, la memoria reciente est... |
| Q08 | - |  |  | SI | • En demencia severa no pueden hacer el cuidado pe... |
| Q09 | - |  |  | SI | Puntaje |
| Q10 | - |  |  | SI | Clasificación |
| Q11 | - |  |  | SI | 0 - 9 |
| Q12 | - |  |  | SI | Las puntuaciones más altas corresponden a niveles ... |
| Q13 | - |  |  | SI | La Escala de Fragilidad Clínica se introdujo en el... |
| Q14 | - |  |  | SI | el nivel general de condición física o fragilidad ... |
| Q15 | - |  |  | SI | 0 - 9: Las puntuaciones más altas corresponden a n... |
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