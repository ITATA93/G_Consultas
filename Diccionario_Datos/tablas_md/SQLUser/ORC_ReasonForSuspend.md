# SQLUser.ORC_ReasonForSuspend

**Schema:** SQLUser
**Columnas:** 109
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Órdenes**. Parámetros de órdenes médicas.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SUSP_RowId | bigint | PK |  | NO | - |
| ChildQ10DR | - |  |  | SI | Child Reference: Scope Register |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Procedure type |
| Q04 | - |  |  | SI | Intravascular access established |
| Q05 | - |  |  | SI | Sedation method |
| Q06 | - |  |  | SI | Xylocaine throat spray time given |
| Q07 | - |  |  | SI | Procedure preparation comments |
| Q08 | - |  |  | SI | Rectal examination |
| Q09 | - |  |  | SI | Haemorrhoid treatment |
| Q11 | - |  |  | SI | Gastroscopy start date / time |
| Q12 | - |  |  | SI | Gastroscopy start time |
| Q13 | - |  |  | SI | Gastroscopy finish date / time |
| Q14 | - |  |  | SI | Gastroscopy finish |
| Q15 | - |  |  | SI | Lower endoscopy start date / time |
| Q16 | - |  |  | SI | Lower endoscopy start time |
| Q17 | - |  |  | SI | Lower endoscopy finish date / time |
| Q18 | - |  |  | SI | Lower endoscopy finish |
| Q19 | - |  |  | SI | Procedure start date / time |
| Q20 | - |  |  | SI | Procedure start time |
| Q21 | - |  |  | SI | Procedure end date / time |
| Q22 | - |  |  | SI | Procedure end time |
| Q24 | - |  |  | SI | Colonoscope advanced to |
| Q25 | - |  |  | SI | Reason for not reaching caecum |
| Q26 | - |  |  | SI | Colonoscope progression assistance |
| Q27 | - |  |  | SI | Withdrawal time (in minutes) |
| Q30 | - |  |  | SI | Biopsy(s) taken |
| Q31 | - |  |  | SI | Biopsy details |
| Q32 | - |  |  | SI | Diathermy used |
| Q33 | - |  |  | SI | Diathermy site |
| Q34 | - |  |  | SI | Procedural photos captured |
| Q35 | - |  |  | SI | Sphincterotomy performed |
| Q36 | - |  |  | SI | Lithotripsy |
| Q37 | - |  |  | SI | Bile duct stent inserted |
| Q39 | - |  |  | SI | Procedure comments |
| Q40 | - |  |  | SI | Diathermy pads removed |
| Q41 | - |  |  | SI | Fully awake time |
| Q42 | - |  |  | SI | Post procedure comments |
| Q43 | - |  |  | SI | Boston Bowel Preparation Score |
| Q45 | - |  |  | SI | BBPS, Left Colon |
| Q45ObsDR | - |  |  | SI | BBPS, Left Colon DR |
| Q46 | - |  |  | SI | BBPS, Right Colon |
| Q46ObsDR | - |  |  | SI | BBPS, Right Colon DR |
| Q47 | - |  |  | SI | BBPS, Transverse Colon |
| Q47ObsDR | - |  |  | SI | BBPS, Transverse Colon DR |
| Q48 | - |  |  | SI | Reference: Lai EJ, Calderwood AH, Doros G, Fix OK,... |
| Q49 | - |  |  | SI | Gastrointest Endosc 2009 |
| Q50 | - |  |  | SI | Gastroscopy Specimens & Interventions |
| Q51 | - |  |  | SI | Gastroscopy Specimens & Interventions |
| Q52 | - |  |  | SI | Lower Endoscopy Specimens & Interventions |
| Q53 | - |  |  | SI | Lower Endoscopy Specimens & Interventions |
| Q54 | - |  |  | SI | Lower Endoscopy Specimens & Interventions |
| Q55 | - |  |  | SI | Lower Endoscopy Specimens & Interventions |
| Q57 | - |  |  | SI | Scope Guide Used |
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
| SUSP_AdmCancelReason_DR | bigint |  | FK | SI | Des Ref AuxInsType |
| SUSP_Code | varchar |  |  | NO | Code |
| SUSP_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| SUSP_CreatedDate | date |  |  | SI | Created Date |
| SUSP_CreatedTime | time |  |  | SI | Created Time |
| SUSP_CreatedUser_DR | bigint |  | FK | SI | Created User |
| SUSP_DateFrom | date |  |  | SI | Date From |
| SUSP_DateTo | date |  |  | SI | Date To |
| SUSP_DefaultForAutomatic | varchar |  |  | SI | DefaultForAutomatic |
| SUSP_Desc | varchar |  |  | NO | Description |
| SUSP_Owner | varchar |  |  | SI | Owner |
| SUSP_UpdatedDate | date |  |  | SI | Updated Date |
| SUSP_UpdatedTime | time |  |  | SI | Updated Time |
| SUSP_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*