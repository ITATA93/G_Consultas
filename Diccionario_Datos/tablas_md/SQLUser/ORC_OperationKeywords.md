# SQLUser.ORC_OperationKeywords

**Schema:** SQLUser
**Columnas:** 75
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Órdenes**. Parámetros de órdenes médicas.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| KEYW_ParRef | bigint | PK |  | NO | ORC_Operation Parent Reference |
| KEYW_Childsub | double |  |  | NO | Childsub |
| KEYW_Name | varchar |  |  | SI | Name |
| KEYW_RowId | varchar |  |  | NO | - |
| Q01 | - |  |  | SI | Activity |
| Q02 | - |  |  | SI | Mechanical circulatory support type |
| Q03 | - |  |  | SI | Cannulation type |
| Q04 | - |  |  | SI | Arterial Site |
| Q05 | - |  |  | SI | Arterial cannula size |
| Q06 | - |  |  | SI | Venous site |
| Q07 | - |  |  | SI | Others |
| Q08 | - |  |  | SI | Venous cannula size |
| Q09 | - |  |  | SI | Veno-venous in venous site |
| Q10 | - |  |  | SI | Veno-venous in venous cannula size |
| Q11 | - |  |  | SI | Veno-venous out venous site |
| Q12 | - |  |  | SI | Veno-venous out venous cannula size |
| Q13 | - |  |  | SI | Oxygenator type |
| Q14 | - |  |  | SI | ECMO insertion date |
| Q15 | - |  |  | SI | ECMO insertion time |
| Q16 | - |  |  | SI | ECMO discontinuation date |
| Q17 | - |  |  | SI | ECMO discontinuation time |
| Q18 | - |  |  | SI | ECMO know, insertion date |
| Q19 | - |  |  | SI | RVAD, inflow cannula site |
| Q20 | - |  |  | SI | RVAD, inflow cannula size |
| Q21 | - |  |  | SI | RVAD, outflow cannula site |
| Q22 | - |  |  | SI | RVAD, outflow cannula size |
| Q23 | - |  |  | SI | LVAD, inflow cannula site |
| Q24 | - |  |  | SI | LVAD, inflow cannula size |
| Q25 | - |  |  | SI | LVAD, outflow cannula site |
| Q26 | - |  |  | SI | LVAD, outflow cannula size |
| Q27 | - |  |  | SI | ECMO known, date of insertion |
| Q28 | - |  |  | SI | Procedure preparation |
| Q29 | - |  |  | SI | Sterile field |
| Q30 | - |  |  | SI | MBP compliance |
| Q31 | - |  |  | SI | Non compliant MBP |
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