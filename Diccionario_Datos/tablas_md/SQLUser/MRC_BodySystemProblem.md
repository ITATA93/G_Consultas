# SQLUser.MRC_BodySystemProblem

**Schema:** SQLUser
**Columnas:** 74
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Registros Médicos**. Parámetros de historia clínica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PRO_ParRef | bigint | PK |  | NO | MRC_BodySystems Parent Reference |
| PRO_Childsub | double |  |  | NO | Childsub |
| PRO_Code | varchar |  |  | NO | Code |
| PRO_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| PRO_CreatedDate | date |  |  | SI | Created Date |
| PRO_CreatedTime | time |  |  | SI | Created Time |
| PRO_CreatedUser_DR | bigint |  | FK | SI | Created User |
| PRO_Desc | varchar |  |  | NO | Description |
| PRO_Explanation | varchar |  |  | SI | Explanation |
| PRO_RowId | varchar |  |  | NO | - |
| PRO_UpdatedDate | date |  |  | SI | Updated Date |
| PRO_UpdatedTime | time |  |  | SI | Updated Time |
| PRO_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| QC01 | - |  |  | SI | Resultado 01 |
| QC02 | - |  |  | SI | Resultado 02 |
| QC03 | - |  |  | SI | Resultado 03 |
| QC04 | - |  |  | SI | Resultado 04 |
| QC05 | - |  |  | SI | Resultado 05 |
| QC06 | - |  |  | SI | Resultado 06 |
| QC07 | - |  |  | SI | Resultado 07 |
| QC08 | - |  |  | SI | Resultado 08 |
| QC09 | - |  |  | SI | Resultado 09 |
| QC10 | - |  |  | SI | Resultado 10 |
| QC11 | - |  |  | SI | Resultado 11 |
| QC12 | - |  |  | SI | Resultado 12 |
| QC13 | - |  |  | SI | Resultado 13 |
| QC14 | - |  |  | SI | Resultado 14 |
| QOriDes | - |  |  | SI | Conversión Unidad de Medida |
| QPeso | - |  |  | SI | Peso (Kg) |
| QPesoObsDR | - |  |  | SI | Peso (Kg) DR |
| QSoluto | - |  |  | SI | Soluto (mg) |
| QSolvente | - |  |  | SI | Solvente (ml) |
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
| QUnidad | - |  |  | SI | Soluto (Unidad) |
| QValor | - |  |  | SI | Dosis Indicada |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*