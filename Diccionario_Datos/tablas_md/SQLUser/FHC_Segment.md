# SQLUser.FHC_Segment

**Schema:** SQLUser
**Columnas:** 89
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Hogar/Familia**. Parámetros de entorno familiar.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| FHCS_RowId | bigint | PK |  | NO | - |
| FHCS_Code | varchar |  |  | NO | Segment Code |
| FHCS_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| FHCS_CreatedDate | date |  |  | SI | Created Date |
| FHCS_CreatedTime | time |  |  | SI | Created Time |
| FHCS_CreatedUser_DR | bigint |  | FK | SI | Created User |
| FHCS_DateFrom | date |  |  | NO | Date From |
| FHCS_DateTo | date |  |  | SI | Date To |
| FHCS_Desc | varchar |  |  | NO | Segment Description |
| FHCS_NationalCode | varchar |  |  | SI | National Code |
| FHCS_Owner | varchar |  |  | SI | Owner |
| FHCS_UpdatedDate | date |  |  | SI | Updated Date |
| FHCS_UpdatedTime | time |  |  | SI | Updated Time |
| FHCS_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Reason for catheter insertion |
| Q02 | - |  |  | SI | Aseptic procedure followed for catheter insertion |
| Q03 | - |  |  | SI | Hand hygiene before procedure |
| Q04 | - |  |  | SI | Catheter insertion kit with sterile gloves, cleans... |
| Q05 | - |  |  | SI | Catheter inserted by trained staff |
| Q06 | - |  |  | SI | During procedure |
| Q07 | - |  |  | SI | After the procedure |
| Q08 | - |  |  | SI | Complies with hand hygiene requirement |
| Q09 | - |  |  | SI | Catheter needs to be reviewed daily |
| Q10 | - |  |  | SI | Promptly remove when not needed |
| Q11 | - |  |  | SI | Catheter secured in place |
| Q12 | - |  |  | SI | Closed drainage system |
| Q13 | - |  |  | SI | Maintain unobstructed flow, keep collection bag be... |
| Q14 | - |  |  | SI | Daily cleansing of meatal surface with soap and wa... |
| Q15 | - |  |  | SI | Provide individual clean collection container at t... |
| Q16 | - |  |  | SI | Before procedure |
| Q17 | - |  |  | SI | Comments |
| Q18 | - |  |  | SI | Other reason |
| Q19 | - |  |  | SI | Procedure |
| Q20 | - |  |  | SI | Urinary catheter |
| Q20ObsDR | - |  |  | SI | Urinary catheter DR |
| Q21 | - |  |  | SI | Catheter in situ from ward |
| Q22 | - |  |  | SI | Catheter inserted in theatre	 |
| Q23 | - |  |  | SI | Lot number	 |
| Q24 | - |  |  | SI | Catheter Pathway 	 |
| Q25 | - |  |  | SI | Operation |
| Q26 | - |  |  | SI | Catheter insertion date |
| Q27 | - |  |  | SI | Catheter insertion time |
| Q28 | - |  |  | SI | Catheter removal date |
| Q29 | - |  |  | SI | Catheter removal time |
| Q30 | - |  |  | SI | Total catheter days |
| Q31 | - |  |  | SI | Catheter removal type |
| Q32 | - |  |  | SI | Date |
| Q33 | - |  |  | SI | Time |
| Q34 | - |  |  | SI | Total catheter days |
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