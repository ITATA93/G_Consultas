# SQLUser.PA_Complaints

**Schema:** SQLUser
**Columnas:** 86
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PACM_RowId | bigint | PK |  | NO | - |
| PACM_CTLOC_DR | bigint |  | FK | SI | Des Ref CTLOC |
| PACM_Category_DR | bigint |  | FK | SI | Des Ref Category |
| PACM_ChangesDetails | varchar |  |  | SI | Changes Details |
| PACM_ComplaintHandler | bigint |  |  | SI | Des Ref User |
| PACM_DateComplaint | date |  |  | SI | Date Complaint |
| PACM_DateNextAction | date |  |  | SI | Target Date for Next Action |
| PACM_DateResolved | date |  |  | SI | Date Resolved |
| PACM_Details | varchar |  |  | SI | Details |
| PACM_Keyword | varchar |  |  | SI | Keyword |
| PACM_MadeTo | bigint |  |  | SI | Des Ref User |
| PACM_PAADM_DR | bigint |  | FK | SI | Des Ref PAADM |
| PACM_Person_DR | bigint |  | FK | SI | Des Ref Person |
| PACM_Priority_DR | bigint |  | FK | SI | Des Ref Priority |
| PACM_RecordedUser_DR | bigint |  | FK | SI | Des Ref RecordedUser |
| PACM_Relation_DR | bigint |  | FK | SI | Des Ref Relation |
| PACM_ReportedBy | varchar |  |  | SI | Reported By |
| PACM_Status_DR | bigint |  | FK | SI | Des Ref Status |
| PACM_Type | varchar |  |  | SI | Type |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Cannula Insertion Site |
| Q03ObsDR | - |  |  | SI | Cannula Insertion Site DR |
| Q04 | - |  |  | SI | VIP score checks |
| Q05 | - |  |  | SI | Score |
| Q06 | - |  |  | SI | Classification |
| Q07 | - |  |  | SI | 0: |
| Q08 | - |  |  | SI | No signs of phlebitis - OBSERVE CANNULA |
| Q09 | - |  |  | SI | 1: |
| Q10 | - |  |  | SI | Possible first signs - OBSERVE CANNULA |
| Q11 | - |  |  | SI | 2: |
| Q12 | - |  |  | SI | Early stage of phlebitis - RESITE CANNULA |
| Q13 | - |  |  | SI | 3: |
| Q14 | - |  |  | SI | Mid-stage of phlebitis - RESITE CANNULA | CONSIDER... |
| Q15 | - |  |  | SI | 4: |
| Q16 | - |  |  | SI | Advanced stage of phlebitis or start of thrombophl... |
| Q17 | - |  |  | SI | 5: |
| Q18 | - |  |  | SI | Advanced stage of thrombophlebitis – RESITE CANNUL... |
| Q19 | - |  |  | SI | The Visual Infusion Phlebitis (VIP) scoring tool a... |
| Q20 | - |  |  | SI | 0: No signs of phlebitis - OBSERVE CANNULA |
| Q21 | - |  |  | SI | 1: Possible first signs - OBSERVE CANNULA |
| Q22 | - |  |  | SI | 2: Early stage of phlebitis - RESITE CANNULA |
| Q23 | - |  |  | SI | 3: Mid-stage of phlebitis - RESITE CANNULA | CONSI... |
| Q24 | - |  |  | SI | 4: Advanced stage of phlebitis or start of thrombo... |
| Q25 | - |  |  | SI | 5:&nbsp |
| Q26 | - |  |  | SI | Gallant P and Schultz AA (2006) Evaluation of a vi... |
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