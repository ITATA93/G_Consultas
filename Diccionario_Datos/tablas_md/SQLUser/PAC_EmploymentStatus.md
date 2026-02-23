# SQLUser.PAC_EmploymentStatus

**Schema:** SQLUser
**Columnas:** 79
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Estados posibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| EMPLST_RowId | bigint | PK |  | NO | - |
| EMPLST_Code | varchar |  |  | NO | Code |
| EMPLST_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| EMPLST_CodeTranslated | varchar |  |  | SI | Code Translated (Computed) |
| EMPLST_CreatedDate | date |  |  | SI | Created Date |
| EMPLST_CreatedTime | time |  |  | SI | Created Time |
| EMPLST_CreatedUser_DR | bigint |  | FK | SI | Created User |
| EMPLST_DateFrom | date |  |  | SI | Date From |
| EMPLST_DateTo | date |  |  | SI | Date To |
| EMPLST_Desc | varchar |  |  | NO | Description |
| EMPLST_DescTranslated | varchar |  |  | SI | Description Translated (Computed) |
| EMPLST_NationCode | varchar |  |  | SI | National Code |
| EMPLST_Owner | varchar |  |  | SI | Owner |
| EMPLST_UpdatedDate | date |  |  | SI | Updated Date |
| EMPLST_UpdatedTime | time |  |  | SI | Updated Time |
| EMPLST_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Paciente esta intubado (a) |
| Q02 | - |  |  | SI | Objetivo de la evaluación |
| Q03 | - |  |  | SI | Puntuación Objetiva |
| Q04 | - |  |  | SI | Alerta |
| Q05 | - |  |  | SI | Calma / Agitación |
| Q06 | - |  |  | SI | Respuesta respiratoria (solo en niños&nbsp |
| Q07 | - |  |  | SI | Llanto (sólo en niños&nbsp |
| Q08 | - |  |  | SI | Movimiento fisico |
| Q09 | - |  |  | SI | Tono muscular |
| Q10 | - |  |  | SI | Tensión facial |
| Q11 | - |  |  | SI | La Escala COMFORT mide varios parámetros para dete... |
| Q12 | - |  |  | SI | 6 - 10 |
| Q13 | - |  |  | SI | 11 - 15 |
| Q14 | - |  |  | SI | 16 - 22 |
| Q15 | - |  |  | SI | 23 - 40 |
| Q16 | - |  |  | SI | Amarillo |
| Q17 | - |  |  | SI | Azul |
| Q18 | - |  |  | SI | Verde |
| Q19 | - |  |  | SI | Red |
| Q20 | - |  |  | SI | Puntaje |
| Q21 | - |  |  | SI | Classification |
| Q22 | - |  |  | SI | Fecha |
| Q23 | - |  |  | SI | Hora |
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