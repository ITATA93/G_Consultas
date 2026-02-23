# SQLUser.MRC_CareEventType

**Schema:** SQLUser
**Columnas:** 70
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CAREVTTYP_RowId | bigint | PK |  | NO | - |
| CAREVTTYP_Code | varchar |  |  | SI | Code |
| CAREVTTYP_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| CAREVTTYP_CreatedDate | date |  |  | SI | Created Date |
| CAREVTTYP_CreatedTime | time |  |  | SI | Created Time |
| CAREVTTYP_CreatedUser_DR | bigint |  | FK | SI | Created User |
| CAREVTTYP_DateFrom | date |  |  | SI | DateFrom |
| CAREVTTYP_DateTo | date |  |  | SI | DateTo |
| CAREVTTYP_Desc | varchar |  |  | SI | Description |
| CAREVTTYP_Owner | varchar |  |  | SI | Owner |
| CAREVTTYP_Period | varchar |  |  | SI | Period Event |
| CAREVTTYP_UpdatedDate | date |  |  | SI | Updated Date |
| CAREVTTYP_UpdatedTime | time |  |  | SI | Updated Time |
| CAREVTTYP_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| QIDXD | - |  |  | SI | Datos de Indice |
| QIDXT | - |  |  | SI | Tipo de Indice |
| QL | - |  |  | SI | L |
| QM | - |  |  | SI | M |
| QP10 | - |  |  | SI | Cota Inferior Percentil 10 |
| QP25 | - |  |  | SI | Cota Inferior Percentil 25 |
| QP3 | - |  |  | SI | Cota Inferior Percentil 3 |
| QP5 | - |  |  | SI | Cota Inferior Percentil 5 |
| QP50 | - |  |  | SI | Cota Inferior Percentil 50 |
| QP75 | - |  |  | SI | Cota Inferior Percentil 75 |
| QP85 | - |  |  | SI | Cota Inferior Percentil 85 |
| QP90 | - |  |  | SI | Cota Inferior Percentil 90 |
| QP95 | - |  |  | SI | Cota Inferior Percentil 95 |
| QP97 | - |  |  | SI | Cota Inferior Percentil 97 |
| QS | - |  |  | SI | S |
| QSEX | - |  |  | SI | Sexo |
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