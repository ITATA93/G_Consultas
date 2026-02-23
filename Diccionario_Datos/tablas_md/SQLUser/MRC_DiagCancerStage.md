# SQLUser.MRC_DiagCancerStage

**Schema:** SQLUser
**Columnas:** 131
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Registros Médicos**. Parámetros de historia clínica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DIACS_RowId | bigint | PK |  | NO | - |
| DIACS_Code | varchar |  |  | NO | Code |
| DIACS_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| DIACS_CreatedDate | date |  |  | SI | Created Date |
| DIACS_CreatedTime | time |  |  | SI | Created Time |
| DIACS_CreatedUser_DR | bigint |  | FK | SI | Created User |
| DIACS_DateFrom | date |  |  | SI | Date From |
| DIACS_DateTo | date |  |  | SI | Date To |
| DIACS_Desc | varchar |  |  | NO | Description |
| DIACS_Owner | varchar |  |  | SI | Owner |
| DIACS_UpdatedDate | date |  |  | SI | Updated Date |
| DIACS_UpdatedTime | time |  |  | SI | Updated Time |
| DIACS_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Actividades Masivas: 1 condón por persona |
| Q02 | - |  |  | SI | Nombre Institución /ONG’s Responsable Actividad |
| Q03 | - |  |  | SI | Nombre Persona Realiza Reporte |
| Q04 | - |  |  | SI | Período Comprende Reporte |
| Q05 | - |  |  | SI | Período Comprende Reporte |
| Q06 | - |  |  | SI | Distribución |
| Q07 | - |  |  | SI | Nombre Actividad |
| Q08 | - |  |  | SI | Nombre Actividad |
| Q09 | - |  |  | SI | Nombre Actividad |
| Q10 | - |  |  | SI | Fecha |
| Q11 | - |  |  | SI | Fecha |
| Q12 | - |  |  | SI | Fecha |
| Q13 | - |  |  | SI | N° Personas Alcanzadas |
| Q14 | - |  |  | SI | N° Personas Alcanzadas |
| Q15 | - |  |  | SI | N° Personas Alcanzadas |
| Q16 | - |  |  | SI | Sexo y Rango Etareo |
| Q17 | - |  |  | SI | 15 - 19 |
| Q18 | - |  |  | SI | H |
| Q19 | - |  |  | SI | H |
| Q20 | - |  |  | SI | H |
| Q21 | - |  |  | SI | H |
| Q22 | - |  |  | SI | M |
| Q23 | - |  |  | SI | M |
| Q24 | - |  |  | SI | M |
| Q25 | - |  |  | SI | M |
| Q26 | - |  |  | SI | Trans |
| Q27 | - |  |  | SI | Trans |
| Q28 | - |  |  | SI | Trans |
| Q29 | - |  |  | SI | Trans |
| Q30 | - |  |  | SI | 20 - 24 |
| Q31 | - |  |  | SI | H |
| Q32 | - |  |  | SI | H |
| Q33 | - |  |  | SI | H |
| Q34 | - |  |  | SI | H |
| Q35 | - |  |  | SI | M |
| Q36 | - |  |  | SI | M |
| Q37 | - |  |  | SI | M |
| Q38 | - |  |  | SI | M |
| Q39 | - |  |  | SI | Trans |
| Q40 | - |  |  | SI | Trans |
| Q41 | - |  |  | SI | Trans |
| Q42 | - |  |  | SI | Trans |
| Q43 | - |  |  | SI | 25 - 29 |
| Q44 | - |  |  | SI | H |
| Q45 | - |  |  | SI | H |
| Q46 | - |  |  | SI | H |
| Q47 | - |  |  | SI | H |
| Q48 | - |  |  | SI | M |
| Q49 | - |  |  | SI | M |
| Q50 | - |  |  | SI | M |
| Q51 | - |  |  | SI | M |
| Q52 | - |  |  | SI | Trans |
| Q53 | - |  |  | SI | Trans |
| Q54 | - |  |  | SI | Trans |
| Q55 | - |  |  | SI | Trans |
| Q56 | - |  |  | SI | 30 y Más |
| Q57 | - |  |  | SI | H |
| Q58 | - |  |  | SI | H |
| Q59 | - |  |  | SI | H |
| Q60 | - |  |  | SI | H |
| Q61 | - |  |  | SI | M |
| Q62 | - |  |  | SI | M |
| Q63 | - |  |  | SI | M |
| Q64 | - |  |  | SI | M |
| Q65 | - |  |  | SI | Trans |
| Q66 | - |  |  | SI | Trans |
| Q67 | - |  |  | SI | Trans |
| Q68 | - |  |  | SI | Trans |
| Q69 | - |  |  | SI | Total Cantidad de Condones Entregados |
| Q70 | - |  |  | SI | Total Cantidad de Condones Entregados |
| Q71 | - |  |  | SI | Total Cantidad de Condones Entregados |
| Q72 | - |  |  | SI | Total Cantidad de Condones Entregados |
| Q73 | - |  |  | SI | Total Lubricantes |
| Q74 | - |  |  | SI | Total Lubricantes |
| Q75 | - |  |  | SI | Total Lubricantes |
| Q76 | - |  |  | SI | Total Lubricantes |
| Q77 | - |  |  | SI | Observaciones |
| Q78 | - |  |  | SI | N° Personas Alcanzadas |
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