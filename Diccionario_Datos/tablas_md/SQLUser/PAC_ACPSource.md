# SQLUser.PAC_ACPSource

**Schema:** SQLUser
**Columnas:** 100
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ACPSRC_RowId | bigint | PK |  | NO | - |
| ACPSRC_Code | varchar |  |  | NO | Code |
| ACPSRC_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| ACPSRC_CreatedDate | date |  |  | SI | Created Date |
| ACPSRC_CreatedTime | time |  |  | SI | Created Time |
| ACPSRC_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ACPSRC_DateFrom | date |  |  | SI | Date From |
| ACPSRC_DateTo | date |  |  | SI | Date To |
| ACPSRC_Desc | varchar |  |  | NO | Description |
| ACPSRC_NationalCode | varchar |  |  | SI | National Code |
| ACPSRC_Owner | varchar |  |  | SI | Owner |
| ACPSRC_UpdatedDate | date |  |  | SI | Updated Date |
| ACPSRC_UpdatedTime | time |  |  | SI | Updated Time |
| ACPSRC_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| ChildQ46DR | - |  |  | SI | Child Reference: Daily shift assessment |
| Q01 | - |  |  | SI | Insertion Reason |
| Q02 | - |  |  | SI | Explained procedure to patient and verified consen... |
| Q03 | - |  |  | SI | Prepared materials / documents / medications? |
| Q04 | - |  |  | SI | Marked / Assessed site? |
| Q05 | - |  |  | SI | Assembled equipment, verified supplies? |
| Q06 | - |  |  | SI | Positioned patient correctly? |
| Q07 | - |  |  | SI | All persons in the room had clean hands? |
| Q08 | - |  |  | SI | Skin disinfected correctly? |
| Q09 | - |  |  | SI | Patient was covered from head to toe with a steril... |
| Q10 | - |  |  | SI | Used ultrasound guidance if appropriate? |
| Q11 | - |  |  | SI | Wore a cap, mask, sterile gown and gloves? |
| Q12 | - |  |  | SI | Care provider and patient in the room wore masks? |
| Q13 | - |  |  | SI | Maintained sterile field? |
| Q14 | - |  |  | SI | Was sterile technique maintained when applying dre... |
| Q15 | - |  |  | SI | Was dressing dated? |
| Q16 | - |  |  | SI | Catheter position confirmed? |
| Q17 | - |  |  | SI | Daily review of line necessity? |
| Q18 | - |  |  | SI | Note |
| Q19 | - |  |  | SI | Name of Procedure CP |
| Q20 | - |  |  | SI | Name of Assisting CP |
| Q21 | - |  |  | SI | Name of other CP |
| Q22 | - |  |  | SI | Skin preparation |
| Q23 | - |  |  | SI | Note |
| Q24 | - |  |  | SI | Insertion approach |
| Q25 | - |  |  | SI | Checklist |
| Q26 | - |  |  | SI | Number of insertion attempts |
| Q27 | - |  |  | SI | Information |
| Q28 | - |  |  | SI | Date inserted |
| Q29 | - |  |  | SI | Time inserted |
| Q30 | - |  |  | SI | Date infection found |
| Q31 | - |  |  | SI | Time infection found |
| Q32 | - |  |  | SI | Date infection healed |
| Q33 | - |  |  | SI | Time infection healed |
| Q34 | - |  |  | SI | Date removed |
| Q35 | - |  |  | SI | Time removed |
| Q37 | - |  |  | SI | Characteristics |
| Q37ObsDR | - |  |  | SI | Characteristics DR |
| Q38 | - |  |  | SI | Material |
| Q38ObsDR | - |  |  | SI | Material DR |
| Q39 | - |  |  | SI | Drain Type |
| Q40 | - |  |  | SI | Size |
| Q41 | - |  |  | SI | Drain position |
| Q42 | - |  |  | SI | Local anaesthetic used |
| Q43 | - |  |  | SI | Localisation |
| Q44 | - |  |  | SI | Drain labelled with date inserted |
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