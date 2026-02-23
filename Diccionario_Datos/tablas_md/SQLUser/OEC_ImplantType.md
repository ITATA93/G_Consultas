# SQLUser.OEC_ImplantType

**Schema:** SQLUser
**Columnas:** 119
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| IMPL_RowId | bigint | PK |  | NO | - |
| IMPL_Code | varchar |  |  | NO | Code |
| IMPL_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| IMPL_CreatedDate | date |  |  | SI | Created Date |
| IMPL_CreatedTime | time |  |  | SI | Created Time |
| IMPL_CreatedUser_DR | bigint |  | FK | SI | Created User |
| IMPL_DateFrom | date |  |  | SI | DateFrom |
| IMPL_DateTo | date |  |  | SI | DateTo |
| IMPL_Desc | varchar |  |  | NO | Description |
| IMPL_Owner | varchar |  |  | SI | Owner |
| IMPL_UpdatedDate | date |  |  | SI | Updated Date |
| IMPL_UpdatedTime | time |  |  | SI | Updated Time |
| IMPL_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Normal in Right Eye |
| Q02 | - |  |  | SI | Normal in Left Eye |
| Q03 | - |  |  | SI | Notes |
| Q04 | - |  |  | SI | Normal in Right Eye |
| Q05 | - |  |  | SI | Normal in Left Eye |
| Q06 | - |  |  | SI | Notes |
| Q07 | - |  |  | SI | Clarity |
| Q08 | - |  |  | SI | Clarity 2 |
| Q09 | - |  |  | SI | Right Eye |
| Q10 | - |  |  | SI | Left Eye |
| Q11 | - |  |  | SI | KPS |
| Q12 | - |  |  | SI | KPS 2 |
| Q13 | - |  |  | SI | Notes |
| Q14 | - |  |  | SI | Anterior Chamber |
| Q15 | - |  |  | SI | Right Eye |
| Q16 | - |  |  | SI | Left Eye |
| Q17 | - |  |  | SI | Depth |
| Q18 | - |  |  | SI | Depth |
| Q19 | - |  |  | SI | Notes |
| Q20 | - |  |  | SI | Cells |
| Q21 | - |  |  | SI | Cells 2 |
| Q22 | - |  |  | SI | Flare |
| Q23 | - |  |  | SI | Flare 2 |
| Q24 | - |  |  | SI | Pupils / Iris |
| Q25 | - |  |  | SI | Normal condition |
| Q26 | - |  |  | SI | Normal conditin 2 |
| Q27 | - |  |  | SI | Right Eye |
| Q28 | - |  |  | SI | Left Eye |
| Q29 | - |  |  | SI | desc |
| Q30 | - |  |  | SI | desc 2 |
| Q31 | - |  |  | SI | Notes |
| Q32 | - |  |  | SI | Lens |
| Q33 | - |  |  | SI | Right Eye |
| Q34 | - |  |  | SI | Left Eye |
| Q35 | - |  |  | SI | Lens conditions |
| Q36 | - |  |  | SI | Lens conditions 2 |
| Q37 | - |  |  | SI | Vitreous |
| Q38 | - |  |  | SI | Right Eye |
| Q39 | - |  |  | SI | Left Eye |
| Q40 | - |  |  | SI | Conditions |
| Q41 | - |  |  | SI | conditions 2 |
| Q42 | - |  |  | SI | Notes |
| Q43 | - |  |  | SI | Retina |
| Q44 | - |  |  | SI | Right Eye |
| Q45 | - |  |  | SI | Left Eye |
| Q46 | - |  |  | SI | Condition |
| Q47 | - |  |  | SI | conditions 2 |
| Q48 | - |  |  | SI | Notes |
| Q49 | - |  |  | SI | Optic Nerve |
| Q50 | - |  |  | SI | Right Eye |
| Q51 | - |  |  | SI | Left Eye |
| Q52 | - |  |  | SI | Conditions |
| Q53 | - |  |  | SI | condition 2 |
| Q54 | - |  |  | SI | Notes |
| Q55 | - |  |  | SI | Uveitis Assessment |
| Q56 | - |  |  | SI | Onset |
| Q57 | - |  |  | SI | Course |
| Q58 | - |  |  | SI | Duration |
| Q59 | - |  |  | SI | Pathology |
| Q60 | - |  |  | SI | Laterality |
| Q61 | - |  |  | SI | Diagnosis |
| Q62 | - |  |  | SI | Anatomical |
| Q63 | - |  |  | SI | Etiological |
| Q64 | - |  |  | SI | Image |
| Q65 | - |  |  | SI | Conditions |
| Q66 | - |  |  | SI | Conditions |
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