# SQLUser.CT_CareProvDateRange

**Schema:** SQLUser
**Columnas:** 90
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de Profesionales**. Médicos y personal de salud.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CPDR_RowId | bigint | PK |  | NO | - |
| CPDR_AllFrom | varchar |  |  | SI | All From |
| CPDR_AllTo | varchar |  |  | SI | All To |
| CPDR_CCFrom | varchar |  |  | SI | CC From |
| CPDR_CCTo | varchar |  |  | SI | CC To |
| CPDR_CTCP_DR | bigint |  | FK | NO | Des Ref User |
| CPDR_CreatedDate | date |  |  | SI | Created Date |
| CPDR_CreatedTime | time |  |  | SI | Created Time |
| CPDR_CreatedUser_DR | bigint |  | FK | SI | Created User |
| CPDR_DiagFrom | varchar |  |  | SI | Diag From |
| CPDR_DiagTo | varchar |  |  | SI | Diag To |
| CPDR_EvoFrom | varchar |  |  | SI | EvoFrom |
| CPDR_EvoTo | varchar |  |  | SI | Evo To |
| CPDR_FixeddateRange | varchar |  |  | SI | Fixed date Range |
| CPDR_OFFrom | varchar |  |  | SI | OF From |
| CPDR_OFTo | varchar |  |  | SI | OF To |
| CPDR_PEFrom | varchar |  |  | SI | PE From |
| CPDR_PETo | varchar |  |  | SI | PE To |
| CPDR_PIFrom | varchar |  |  | SI | PI From |
| CPDR_PITo | varchar |  |  | SI | PI To |
| CPDR_ProcFrom | varchar |  |  | SI | Procedure From |
| CPDR_ProcTo | varchar |  |  | SI | Procedure To |
| CPDR_ROSFrom | varchar |  |  | SI | ROS From |
| CPDR_ROSTo | varchar |  |  | SI | ROS To |
| CPDR_ReFrom | varchar |  |  | SI | ReFrom |
| CPDR_ReTo | varchar |  |  | SI | ReTo |
| CPDR_ResFrom | varchar |  |  | SI | Res From |
| CPDR_ResTo | varchar |  |  | SI | Res To |
| CPDR_SCPT_All | varchar |  |  | SI | SCPT_All |
| CPDR_SCPT_CC | varchar |  |  | SI | SCPT_CC |
| CPDR_SCPT_Diag | varchar |  |  | SI | SCPT Diag |
| CPDR_SCPT_Evolution | varchar |  |  | SI | SCPT Evolution |
| CPDR_SCPT_Obj | varchar |  |  | SI | SCPT_Obj |
| CPDR_SCPT_PhysExam | varchar |  |  | SI | SCPT PhysExam |
| CPDR_SCPT_PresIllness | varchar |  |  | SI | SCPT PresIllness |
| CPDR_SCPT_Review | varchar |  |  | SI | SCPT Review |
| CPDR_SCPT_RiskEval | varchar |  |  | SI | SCPT RiskEval |
| CPDR_SCPT_Subj | varchar |  |  | SI | SCPT Subj |
| CPDR_SCPT_Transfer | varchar |  |  | SI | SCPT Transfer |
| CPDR_SFFrom | varchar |  |  | SI | SF From |
| CPDR_SFTo | varchar |  |  | SI | SF To |
| CPDR_TNFrom | varchar |  |  | SI | TN From |
| CPDR_TNTo | varchar |  |  | SI | TN To |
| CPDR_UpdatedDate | date |  |  | SI | Updated Date |
| CPDR_UpdatedTime | time |  |  | SI | Updated Time |
| CPDR_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | RTMAVRowID |
| Q02 | - |  |  | SI | Nombre Funcionario |
| Q03 | - |  |  | SI | RUN Funcionario |
| Q04 | - |  |  | SI | Nombre Reporte |
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