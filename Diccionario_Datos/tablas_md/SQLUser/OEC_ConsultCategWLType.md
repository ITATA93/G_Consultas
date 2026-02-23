# SQLUser.OEC_ConsultCategWLType

**Schema:** SQLUser
**Columnas:** 87
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| WLT_ParRef | bigint | PK |  | NO | OEC_ConsultCateg Parent Reference |
| Q01 | - |  |  | SI | Pupils |
| Q02 | - |  |  | SI | Right Eye |
| Q03 | - |  |  | SI | Left Eye |
| Q04 | - |  |  | SI | Dim |
| Q05 | - |  |  | SI | Dim 2 |
| Q06 | - |  |  | SI | Light |
| Q07 | - |  |  | SI | Light 2 |
| Q08 | - |  |  | SI | Near ` |
| Q09 | - |  |  | SI | Near 2 |
| Q10 | - |  |  | SI | APD |
| Q11 | - |  |  | SI | APD 2 |
| Q12 | - |  |  | SI | Adnexa |
| Q13 | - |  |  | SI | Ptosis |
| Q14 | - |  |  | SI | Right Eye |
| Q15 | - |  |  | SI | Left Eye |
| Q16 | - |  |  | SI | PF |
| Q17 | - |  |  | SI | PF 2 |
| Q18 | - |  |  | SI | LF |
| Q19 | - |  |  | SI | LF 2 |
| Q20 | - |  |  | SI | MRD |
| Q21 | - |  |  | SI | MRD 2 |
| Q22 | - |  |  | SI | Orbicularis weakness |
| Q23 | - |  |  | SI | Fatigability |
| Q24 | - |  |  | SI | Proptosis |
| Q25 | - |  |  | SI | Exophthalmometer |
| Q26 | - |  |  | SI | Exophthalmometer 2 |
| Q27 | - |  |  | SI | Lid lag |
| Q28 | - |  |  | SI | Fundus |
| Q29 | - |  |  | SI | Neuro Exam |
| Q30 | - |  |  | SI | Orbicularis weakness |
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
| WLT_CTLOC_DR | bigint |  | FK | SI | Des Ref CTLOC |
| WLT_Childsub | double |  |  | NO | Childsub |
| WLT_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| WLT_CreatedDate | date |  |  | SI | Created Date |
| WLT_CreatedTime | time |  |  | SI | Created Time |
| WLT_CreatedUser_DR | bigint |  | FK | SI | Created User |
| WLT_DateFrom | date |  |  | SI | DateFrom |
| WLT_DateTo | date |  |  | SI | DateTo |
| WLT_Hospital_DR | bigint |  | FK | SI | Des Ref Hospital |
| WLT_Recall | double |  |  | SI | Recall |
| WLT_RecallPeriod | varchar |  |  | SI | Recall Period |
| WLT_RowId | varchar |  |  | NO | - |
| WLT_UpdatedDate | date |  |  | SI | Updated Date |
| WLT_UpdatedTime | time |  |  | SI | Updated Time |
| WLT_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| WLT_WaitLisType_DR | bigint |  | FK | SI | Des Ref WaitLisType |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*