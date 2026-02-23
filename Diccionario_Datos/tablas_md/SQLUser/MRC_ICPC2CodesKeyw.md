# SQLUser.MRC_ICPC2CodesKeyw

**Schema:** SQLUser
**Columnas:** 64
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Registros Médicos**. Parámetros de historia clínica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| KEYW_ICPC2_ParRef | bigint | PK |  | NO | Des Ref to ICPC2 |
| ChildQ01DR | - |  |  | SI | Child Reference: Evaluación de Movilidad |
| KEYW_Childsub | numeric |  |  | NO | KEYW Childsub (NewKey) |
| KEYW_CreatedDate | date |  |  | SI | Created Date |
| KEYW_CreatedTime | time |  |  | SI | Created Time |
| KEYW_CreatedUser_DR | bigint |  | FK | SI | Created User |
| KEYW_Name | varchar |  |  | SI | Name |
| KEYW_RowId | varchar |  |  | NO | - |
| KEYW_UpdatedDate | date |  |  | SI | Updated Date |
| KEYW_UpdatedTime | time |  |  | SI | Updated Time |
| KEYW_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q02 | - |  |  | SI | Pruebas Especiales |
| Q03 | - |  |  | SI | Diagnóstico Kinésico Funcional |
| Q04 | - |  |  | SI | Objetivo General |
| Q05 | - |  |  | SI | Objetivos Específicos |
| Q06 | - |  |  | SI | Objetivos Operacionales (Técnicas Kinésicas) |
| Q07 | - |  |  | SI | Profesional Evaluador |
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
| Qa | - |  |  | SI | Movimiento |
| Qb | - |  |  | SI | Tipo |
| Qc | - |  |  | SI | Segmento |
| Qd | - |  |  | SI | Lateralidad |
| Qe | - |  |  | SI | ROM |
| Qf | - |  |  | SI | Fuerza |
| Qg | - |  |  | SI | EVA |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*