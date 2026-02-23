# SQLUser.INC_GdRecType

**Schema:** SQLUser
**Columnas:** 80
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| INCGR_RowId | bigint | PK |  | NO | - |
| INCGR_Code | varchar |  |  | NO | Good Receive Code |
| INCGR_CreatedDate | date |  |  | SI | Created Date |
| INCGR_CreatedTime | time |  |  | SI | Created Time |
| INCGR_CreatedUser_DR | bigint |  | FK | SI | Created User |
| INCGR_Desc | varchar |  |  | NO | Description |
| INCGR_InvFlag | varchar |  |  | NO | Item Flag |
| INCGR_UpdatedDate | date |  |  | SI | Updated Date |
| INCGR_UpdatedTime | time |  |  | SI | Updated Time |
| INCGR_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Type of catheter |
| Q01ObsDR | - |  |  | SI | Type of catheter DR |
| Q02 | - |  |  | SI | Localisation of catheter |
| Q02ObsDR | - |  |  | SI | Localisation of catheter DR |
| Q03 | - |  |  | SI | Characteristics of catheter |
| Q03ObsDR | - |  |  | SI | Characteristics of catheter DR |
| Q04 | - |  |  | SI | Insertion reason |
| Q05 | - |  |  | SI | Explained procedure to patient and verified consen... |
| Q06 | - |  |  | SI | Prepared materials / documents / medications? |
| Q07 | - |  |  | SI | Marked / Assessed site? |
| Q08 | - |  |  | SI | Assembled equipment, verified supplies? |
| Q09 | - |  |  | SI | Positioned patient correctly? |
| Q10 | - |  |  | SI | All persons in the room had clean hands? |
| Q11 | - |  |  | SI | Skin disinfected correctly? |
| Q12 | - |  |  | SI | Patient was covered from head to toe with a steril... |
| Q13 | - |  |  | SI | Used ultrasound guidance if appropriate? |
| Q14 | - |  |  | SI | Wore a cap, mask, sterile gown and gloves? |
| Q15 | - |  |  | SI | Care provider and patient in the room wore masks? |
| Q16 | - |  |  | SI | Maintained sterile field? |
| Q17 | - |  |  | SI | Was sterile technique maintained when applying dre... |
| Q18 | - |  |  | SI | Was dressing dated? |
| Q19 | - |  |  | SI | Catheter position confirmed? |
| Q20 | - |  |  | SI | Daily review of line necessity? |
| Q21 | - |  |  | SI | Note |
| Q22 | - |  |  | SI | Name of Procedure CP |
| Q23 | - |  |  | SI | Name of Assisting CP |
| Q24 | - |  |  | SI | Name of other CP |
| Q25 | - |  |  | SI | Number of insertion attempts |
| Q26 | - |  |  | SI | Assessment date |
| Q27 | - |  |  | SI | Assessment time |
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