# SQLUser.MRC_MedStat

**Schema:** SQLUser
**Columnas:** 80
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Registros Médicos**. Parámetros de historia clínica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| MRCMS_RowId | bigint | PK |  | NO | - |
| MRCMS_CreatedDate | date |  |  | SI | Created Date |
| MRCMS_CreatedTime | time |  |  | SI | Created Time |
| MRCMS_CreatedUser_DR | bigint |  | FK | SI | Created User |
| MRCMS_Desc | varchar |  |  | SI | Description |
| MRCMS_Status | varchar |  |  | SI | Status |
| MRCMS_UpdatedDate | date |  |  | SI | Updated Date |
| MRCMS_UpdatedTime | time |  |  | SI | Updated Time |
| MRCMS_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Postura |
| Q02 | - |  |  | SI | Alineación |
| Q03 | - |  |  | SI | Plano Sagital |
| Q04 | - |  |  | SI | Plano Frontal |
| Q05 | - |  |  | SI | Plano Transversal |
| Q06 | - |  |  | SI | Base de Apoyo |
| Q07 | - |  |  | SI | Reacciones de Equilibrio |
| Q08 | - |  |  | SI | Reacciones de Enderezamiento |
| Q09 | - |  |  | SI | Transferencias |
| Q10 | - |  |  | SI | Giros Decúbitos |
| Q11 | - |  |  | SI | Sedestación |
| Q12 | - |  |  | SI | Cuatro Apoyos |
| Q13 | - |  |  | SI | Bipedestación |
| Q14 | - |  |  | SI | Marcha |
| Q15 | - |  |  | SI | Pruebas Especiales |
| Q16 | - |  |  | SI | Apreciación Diagnósticas Kinésicas |
| Q17 | - |  |  | SI | postura obs |
| Q18 | - |  |  | SI | Alineación obs |
| Q19 | - |  |  | SI | Plano Sagital obs |
| Q20 | - |  |  | SI | Plano Frontal obs |
| Q21 | - |  |  | SI | Plano Transversal obs |
| Q22 | - |  |  | SI | Base de Apoyo obs |
| Q23 | - |  |  | SI | Reacciones de Equilibrio obs |
| Q24 | - |  |  | SI | Reacciones de Enderezamiento obs |
| Q25 | - |  |  | SI | Transferencias obs |
| Q26 | - |  |  | SI | Giros Decúbitos obs |
| Q27 | - |  |  | SI | Sedentación obs |
| Q28 | - |  |  | SI | Cuatro Apoyos obs |
| Q29 | - |  |  | SI | Bipedestación obs |
| Q30 | - |  |  | SI | Marcha obs |
| Q31 | - |  |  | SI | Evaluación Intermedia |
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