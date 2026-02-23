# SQLUser.PAC_LetterType

**Schema:** SQLUser
**Columnas:** 99
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LET_RowId | bigint | PK |  | NO | - |
| LET_Code | varchar |  |  | NO | Code |
| LET_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LET_CreatedDate | date |  |  | SI | Created Date |
| LET_CreatedTime | time |  |  | SI | Created Time |
| LET_CreatedUser_DR | bigint |  | FK | SI | Created User |
| LET_DateFrom | date |  |  | SI | Date From |
| LET_DateTo | date |  |  | SI | Date To |
| LET_Desc | varchar |  |  | NO | Description |
| LET_LetterTemplate_DR | bigint |  | FK | SI | Des Ref CTLetterTemplate |
| LET_Module_DR | bigint |  | FK | SI | Des Ref PACModule |
| LET_Owner | varchar |  |  | SI | Owner |
| LET_UpdatedDate | date |  |  | SI | Updated Date |
| LET_UpdatedTime | time |  |  | SI | Updated Time |
| LET_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Gestation weeks |
| Q04 | - |  |  | SI | Time of birth |
| Q05 | - |  |  | SI | Delivery / Birth method |
| Q06 | - |  |  | SI | APGAR score 1 minute |
| Q07 | - |  |  | SI | APGAR score 5 minutes |
| Q08 | - |  |  | SI | APGAR score |
| Q09 | - |  |  | SI | Minutes |
| Q10 | - |  |  | SI | Birth length (cm) |
| Q11 | - |  |  | SI | Birth weight (g) |
| Q12 | - |  |  | SI | Birth head circumference (cm) |
| Q13 | - |  |  | SI | Maximum value of Bilirubin on |
| Q14 | - |  |  | SI | Maximum value of Bilirubin (mg/dL) |
| Q15 | - |  |  | SI | Hematocrit (%) |
| Q16 | - |  |  | SI | Neurological examination |
| Q17 | - |  |  | SI | Comment |
| Q18 | - |  |  | SI | Additional notes |
| Q19 | - |  |  | SI | The Baby Birth Details section should only be fill... |
| Q20 | - |  |  | SI | APGAR Score Index |
| Q21 | - |  |  | SI | Score |
| Q22 | - |  |  | SI | 0 |
| Q23 | - |  |  | SI | 1 |
| Q24 | - |  |  | SI | 2 |
| Q25 | - |  |  | SI | Appearance |
| Q26 | - |  |  | SI | Blue/Pale |
| Q27 | - |  |  | SI | Body pink, limbs blue |
| Q28 | - |  |  | SI | Pink |
| Q29 | - |  |  | SI | Pulse |
| Q30 | - |  |  | SI | Absent |
| Q31 | - |  |  | SI | < 100 |
| Q32 | - |  |  | SI | > 100 |
| Q33 | - |  |  | SI | Grimace |
| Q34 | - |  |  | SI | No response |
| Q35 | - |  |  | SI | Some motion |
| Q36 | - |  |  | SI | Cry |
| Q37 | - |  |  | SI | Activity |
| Q38 | - |  |  | SI | Limp |
| Q39 | - |  |  | SI | Some flexion of extremities |
| Q40 | - |  |  | SI | Well flexed |
| Q41 | - |  |  | SI | Respiration |
| Q42 | - |  |  | SI | Absent |
| Q43 | - |  |  | SI | Weak cry |
| Q44 | - |  |  | SI | Good strong cry |
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