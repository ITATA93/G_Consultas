# SQLUser.MRC_PhyESystem

**Schema:** SQLUser
**Columnas:** 77
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Registros Médicos**. Parámetros de historia clínica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTPhyE_ParRef | bigint | PK |  | NO | Parent Reference |
| CQ10 | - |  |  | SI | (null) |
| CQ11 | - |  |  | SI | (null) |
| CQ12 | - |  |  | SI | (null) |
| CQ13 | - |  |  | SI | (null) |
| CQ14 | - |  |  | SI | (null) |
| CQ15 | - |  |  | SI | (null) |
| CQ9 | - |  |  | SI | (null) |
| CTPhyE_Childsub | double |  |  | NO | Childsub |
| CTPhyE_Code | varchar |  |  | SI | Code |
| CTPhyE_CodeTableTags | varchar |  |  | SI | Code Table Tags |
| CTPhyE_CreatedDate | date |  |  | SI | Created Date |
| CTPhyE_CreatedTime | time |  |  | SI | Created Time |
| CTPhyE_CreatedUser_DR | bigint |  | FK | SI | Created User |
| CTPhyE_DateFrom | date |  |  | SI | Date From |
| CTPhyE_DateTo | date |  |  | SI | Date To |
| CTPhyE_Desc | varchar |  |  | SI | Description |
| CTPhyE_RowId | varchar |  |  | NO | - |
| CTPhyE_Sequence | integer |  |  | SI | Sequence |
| CTPhyE_UpdatedDate | date |  |  | SI | Updated Date |
| CTPhyE_UpdatedTime | time |  |  | SI | Updated Time |
| CTPhyE_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q1 | - |  |  | SI | Estudios |
| Q10 | - |  |  | SI | Conocimiento Diagnostico |
| Q11 | - |  |  | SI | Creyente |
| Q12 | - |  |  | SI | Red Social |
| Q13 | - |  |  | SI | Actitud del Paciente |
| Q14 | - |  |  | SI | Actitud de la familia |
| Q15 | - |  |  | SI | Condicion del Paciente |
| Q2 | - |  |  | SI | Diagnostico |
| Q3 | - |  |  | SI | Fecha de Ingreso |
| Q4 | - |  |  | SI | Actividad |
| Q5 | - |  |  | SI | Hijos |
| Q6 | - |  |  | SI | Foco Conflicto |
| Q7 | - |  |  | SI | Evaluación Cognitiva |
| Q8 | - |  |  | SI | Apgar Familiar |
| Q9 | - |  |  | SI | Depresión |
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