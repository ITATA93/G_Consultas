# SQLUser.GLC_CC

**Schema:** SQLUser
**Columnas:** 119
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Contabilidad General (GL)**. Libro mayor y asientos contables.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| GLCCC_RowId | bigint | PK |  | NO | - |
| ChildQ25DR | - |  |  | SI | Child Reference: Catheter position corrected / wit... |
| GLCCC_CoCode_DR | bigint |  | FK | SI | Des Ref to CTCO |
| GLCCC_Code | varchar |  |  | NO | Cost Center |
| GLCCC_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| GLCCC_CreatedDate | date |  |  | SI | Created Date |
| GLCCC_CreatedTime | time |  |  | SI | Created Time |
| GLCCC_CreatedUser_DR | bigint |  | FK | SI | Created User |
| GLCCC_Desc | varchar |  |  | NO | Description |
| GLCCC_Owner | varchar |  |  | SI | Owner |
| GLCCC_RcFlag | varchar |  |  | SI | Archived Flag |
| GLCCC_UpdatedDate | date |  |  | SI | Updated Date |
| GLCCC_UpdatedTime | time |  |  | SI | Updated Time |
| GLCCC_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Activity |
| Q04 | - |  |  | SI | Central venous catheter present |
| Q05 | - |  |  | SI | Insertion date and time |
| Q06 | - |  |  | SI | Insertion time |
| Q07 | - |  |  | SI | Procedure type |
| Q08 | - |  |  | SI | Access type |
| Q09 | - |  |  | SI | Number of lumens |
| Q10 | - |  |  | SI | Laterality |
| Q11 | - |  |  | SI | Site |
| Q12 | - |  |  | SI | Catheter size |
| Q13 | - |  |  | SI | Antibiotic coated line used |
| Q14 | - |  |  | SI | Reason for insertion |
| Q15 | - |  |  | SI | Patient identified |
| Q16 | - |  |  | SI | Insertion unit |
| Q17 | - |  |  | SI | Performing provider |
| Q18 | - |  |  | SI | Assisting in insertion |
| Q19 | - |  |  | SI | Procedure preparation |
| Q20 | - |  |  | SI | Maximal sterile barrier precautions compliance |
| Q21 | - |  |  | SI | Non - Compliant maximal sterile barrier precaution... |
| Q22 | - |  |  | SI | Procedure result |
| Q23 | - |  |  | SI | Number of attempts |
| Q24 | - |  |  | SI | Catheter position correction required |
| Q26 | - |  |  | SI | Radio - graphic confirmation done |
| Q27 | - |  |  | SI | Catheter tip confirmation site |
| Q28 | - |  |  | SI | Comment |
| Q29 | - |  |  | SI | Catheter insertion bundle |
| Q30 | - |  |  | SI | Explained procedure to patient and verified consen... |
| Q31 | - |  |  | SI | Comment |
| Q32 | - |  |  | SI | Catheter insertion bundle |
| Q33 | - |  |  | SI | Explained procedure to patient and verified consen... |
| Q34 | - |  |  | SI | Prepared materials / documents / medications? |
| Q35 | - |  |  | SI | Marked / assessed site? |
| Q36 | - |  |  | SI | Assembled equipment, verified supplies? |
| Q37 | - |  |  | SI | Positioned patient correctly? |
| Q38 | - |  |  | SI | All persons in the room had clean hands? |
| Q39 | - |  |  | SI | Skin disinfected correctly? |
| Q40 | - |  |  | SI | Patient was covered from head to toe with a steril... |
| Q41 | - |  |  | SI | Used ultrasound guidance if appropriate? |
| Q42 | - |  |  | SI | Wore a cap, mask, sterile gown and gloves? |
| Q43 | - |  |  | SI | Care provider and patient in the room wore masks? |
| Q44 | - |  |  | SI | Maintained sterile field? |
| Q45 | - |  |  | SI | Was sterile technique maintained when applying dre... |
| Q46 | - |  |  | SI | Was dressing dated? |
| Q47 | - |  |  | SI | Catheter position confirmed? |
| Q50 | - |  |  | SI | Central venous catheter line care bundle |
| Q53 | - |  |  | SI | Catheter tunnel / porta cath |
| Q54 | - |  |  | SI | Catheter tunnel status |
| Q55 | - |  |  | SI | Tunnel exit site / port pocket |
| Q56 | - |  |  | SI | Tunnel cath anchor suture removed |
| Q57 | - |  |  | SI | Port needle type |
| Q58 | - |  |  | SI | Accessing port |
| Q59 | - |  |  | SI | Accessing port reason |
| Q61 | - |  |  | SI | Discontinue date and time |
| Q62 | - |  |  | SI | Discontinue time |
| Q63 | - |  |  | SI | Care provider discontinued the line |
| Q64 | - |  |  | SI | Discontinue reason |
| Q65 | - |  |  | SI | Unexpected events |
| Q66 | - |  |  | SI | Discontinue result |
| Q67 | - |  |  | SI | Direct pressure applied duration |
| Q68 | - |  |  | SI | Total days of insertion |
| Q69 | - |  |  | SI | Comment |
| Q70 | - |  |  | SI | Lumen characteristics |
| Q71 | - |  |  | SI | Catheter length (cm) |
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