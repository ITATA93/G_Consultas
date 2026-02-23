# SQLUser.PA_Employee

**Schema:** SQLUser
**Columnas:** 76
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| EPE_ParRef | bigint | PK |  | NO | PA_PatMas Parent Reference |
| EPE_Childsub | double |  |  | NO | Childsub |
| EPE_DateFrom | date |  |  | SI | Date of Discount From |
| EPE_DateTo | date |  |  | SI | Date of Discount To |
| EPE_DiscType_DR | bigint |  | FK | SI | Des Ref to Discount Type |
| EPE_EmplNo | varchar |  |  | SI | Employee Number |
| EPE_EmplType_DR | bigint |  | FK | SI | Des Ref to Employee Type |
| EPE_Loc_DR | varchar |  | FK | SI | Not Used (Department) Des Ref to CTEML |
| EPE_PAPER_DR | bigint |  | FK | SI | Des Ref to PAPER |
| EPE_Relation_DR | bigint |  | FK | SI | Des Ref to CTRelation |
| EPE_RowId | varchar |  |  | NO | - |
| Q01 | - |  |  | SI | Worker Name2 |
| Q02 | - |  |  | SI | Initial Assessment Date |
| Q03 | - |  |  | SI | Sources of Information |
| Q04 | - |  |  | SI | Social/Family Profile |
| Q06 | - |  |  | SI | Formal Support/Services Involved |
| Q07 | - |  |  | SI | Financial Circumstances |
| Q08 | - |  |  | SI | Legal Issues |
| Q09 | - |  |  | SI | Current Living Situation |
| Q10 | - |  |  | SI | Status: Housing Stable* |
| Q11 | - |  |  | SI | Adjustment to Current Situation |
| Q12 | - |  |  | SI | Mental Health State |
| Q13 | - |  |  | SI | Carer Issues |
| Q14 | - |  |  | SI | Threat to Person (Self or Others) * |
| Q15 | - |  |  | SI | Other Risk Assessment * |
| Q16 | - |  |  | SI | Other |
| Q17 | - |  |  | SI | Indentified Strengths/Resources of Patient |
| Q18 | - |  |  | SI | Summary/Recommentations/Discharge Plan |
| Q19 | - |  |  | SI | (*Coping Skills/Status |
| Q20 | - |  |  | SI | (Internal or External |
| Q21 | - |  |  | SI | (Goals/Plans |
| Q21A | - |  |  | SI | Resources |
| Q22 | - |  |  | SI | (Description of Family System, Marital Status, |
| Q22A | - |  |  | SI | Friends, Social Networks Spiritualty, Informal Sup... |
| Q23 | - |  |  | SI | Legal / Financial |
| Q25 | - |  |  | SI | date |
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