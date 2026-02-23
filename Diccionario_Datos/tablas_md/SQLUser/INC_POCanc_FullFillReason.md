# SQLUser.INC_POCanc_FullFillReason

**Schema:** SQLUser
**Columnas:** 103
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Incidentes**. Reportes de eventos adversos.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CFR_RowId | bigint | PK |  | NO | - |
| CFR_Code | varchar |  |  | NO | Code |
| CFR_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| CFR_CreatedDate | date |  |  | SI | Created Date |
| CFR_CreatedTime | time |  |  | SI | Created Time |
| CFR_CreatedUser_DR | bigint |  | FK | SI | Created User |
| CFR_Desc | varchar |  |  | NO | Description |
| CFR_Owner | varchar |  |  | SI | Owner |
| CFR_UpdatedDate | date |  |  | SI | Updated Date |
| CFR_UpdatedTime | time |  |  | SI | Updated Time |
| CFR_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| ChildQ52DR | - |  |  | SI | Child Reference: Daily assessment |
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
| Q19 | - |  |  | SI | Chest drain position confirmed? |
| Q20 | - |  |  | SI | Daily review of chest drain necessity? |
| Q21 | - |  |  | SI | Note |
| Q22 | - |  |  | SI | Name of procedure CP |
| Q23 | - |  |  | SI | Name of assisting CP |
| Q24 | - |  |  | SI | Name of other CP |
| Q25 | - |  |  | SI | Skin preparation |
| Q25a | - |  |  | SI | Note |
| Q26 | - |  |  | SI | Insertion approach |
| Q27 | - |  |  | SI | Checklist |
| Q28 | - |  |  | SI | Number of insertion attempts |
| Q30 | - |  |  | SI | Information |
| Q31 | - |  |  | SI | Date inserted |
| Q32 | - |  |  | SI | Time inserted |
| Q33 | - |  |  | SI | Date infection found |
| Q34 | - |  |  | SI | Time infection found |
| Q35 | - |  |  | SI | Date infection heal up |
| Q36 | - |  |  | SI | Time infection heal up |
| Q37 | - |  |  | SI | Date removed |
| Q38 | - |  |  | SI | Time removed |
| Q41N | - |  |  | SI | Note chest drain |
| Q41S | - |  |  | SI | Size |
| Q42 | - |  |  | SI | Chest drain type |
| Q46 | - |  |  | SI | Characteristics |
| Q46ObsDR | - |  |  | SI | Characteristics DR |
| Q47 | - |  |  | SI | Material |
| Q47ObsDR | - |  |  | SI | Material DR |
| Q48 | - |  |  | SI | Position |
| Q48ObsDR | - |  |  | SI | Position DR |
| Q49 | - |  |  | SI | Total days of insertion |
| Q50 | - |  |  | SI | Chest drain labelled with date inserted |
| Q51 | - |  |  | SI | Chest drain labelled with name and change due |
| Q53 | - |  |  | SI | Date |
| Q54 | - |  |  | SI | Time |
| Q70 | - |  |  | SI | Insertion site |
| Q70N | - |  |  | SI | Note |
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