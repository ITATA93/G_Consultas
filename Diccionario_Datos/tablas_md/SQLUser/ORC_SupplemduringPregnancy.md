# SQLUser.ORC_SupplemduringPregnancy

**Schema:** SQLUser
**Columnas:** 88
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Órdenes**. Parámetros de órdenes médicas.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SUDUPR_RowId | bigint | PK |  | NO | - |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Surgical consent completed as per policy |
| Q04 | - |  |  | SI | Anaesthetic consent completed as per policy |
| Q05 | - |  |  | SI | Last food date / time |
| Q06 | - |  |  | SI | Last food time |
| Q07 | - |  |  | SI | Last fluid date / time |
| Q08 | - |  |  | SI | Last fluid time |
| Q09 | - |  |  | SI | Allergy / Sensitivity status confirmed |
| Q10 | - |  |  | SI | Blood results present |
| Q11 | - |  |  | SI | Relevant previous investigation results available |
| Q12 | - |  |  | SI | Patient is a diabetic |
| Q13 | - |  |  | SI | Blood glucose level |
| Q13ObsDR | - |  |  | SI | Blood glucose level DR |
| Q14 | - |  |  | SI | mmol/L |
| Q15 | - |  |  | SI | Pre medication administered as charted |
| Q16 | - |  |  | SI | Routine medications given |
| Q17 | - |  |  | SI | As required medications available |
| Q18 | - |  |  | SI | Bowel preparation completed |
| Q19 | - |  |  | SI | Bowel preparation results |
| Q20 | - |  |  | SI | Is patient ready for procedure |
| Q21 | - |  |  | SI | Actions taken if not ready |
| Q22 | - |  |  | SI | Possible pregnancy or breastfeeding |
| Q23 | - |  |  | SI | Implantable electrical device |
| Q24 | - |  |  | SI | Implantable device comments |
| Q25 | - |  |  | SI | Metal in body |
| Q26 | - |  |  | SI | Metal in body details |
| Q27 | - |  |  | SI | Indwelling catheter / drains in situ |
| Q28 | - |  |  | SI | Orientated to time / place / person |
| Q28ObsDR | - |  |  | SI | Orientated to time / place / person DR |
| Q29 | - |  |  | SI | Special requirements |
| Q30 | - |  |  | SI | Impairments |
| Q31 | - |  |  | SI | Impairments (Other) |
| Q32 | - |  |  | SI | Patient aids |
| Q33 | - |  |  | SI | Patient aids (Other) |
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
| SUDUPR_Code | varchar |  |  | NO | Code |
| SUDUPR_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| SUDUPR_CreatedDate | date |  |  | SI | Created Date |
| SUDUPR_CreatedTime | time |  |  | SI | Created Time |
| SUDUPR_CreatedUser_DR | bigint |  | FK | SI | Created User |
| SUDUPR_DateFrom | date |  |  | SI | Date From |
| SUDUPR_DateTo | date |  |  | SI | Date To |
| SUDUPR_Desc | varchar |  |  | NO | Description |
| SUDUPR_Owner | varchar |  |  | SI | Owner |
| SUDUPR_UpdatedDate | date |  |  | SI | Updated Date |
| SUDUPR_UpdatedTime | time |  |  | SI | Updated Time |
| SUDUPR_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*