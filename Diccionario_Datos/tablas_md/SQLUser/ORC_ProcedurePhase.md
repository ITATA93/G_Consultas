# SQLUser.ORC_ProcedurePhase

**Schema:** SQLUser
**Columnas:** 121
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Órdenes**. Parámetros de órdenes médicas.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PROCPH_RowId | bigint | PK |  | NO | - |
| ChildQ11DR | - |  |  | SI | Child Reference: Target Bolus Regimen |
| PROCPH_Code | varchar |  |  | NO | Code |
| PROCPH_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| PROCPH_CreatedDate | date |  |  | SI | Created Date |
| PROCPH_CreatedTime | time |  |  | SI | Created Time |
| PROCPH_CreatedUser_DR | bigint |  | FK | SI | Created User |
| PROCPH_DateFrom | date |  |  | SI | Date From |
| PROCPH_DateTo | date |  |  | SI | Date To |
| PROCPH_Desc | varchar |  |  | NO | Description |
| PROCPH_Owner | varchar |  |  | SI | Owner |
| PROCPH_UpdatedDate | date |  |  | SI | Updated Date |
| PROCPH_UpdatedTime | time |  |  | SI | Updated Time |
| PROCPH_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Enteral feeding regimen |
| Q02 | - |  |  | SI | Is the patient at risk of refeeding syndrome? |
| Q03 | - |  |  | SI | Feed is initiated slowly as per instructions and n... |
| Q04 | - |  |  | SI | Please refer to the “Refeeding Syndrome in Adults ... |
| Q05 | - |  |  | SI | Location |
| Q06 | - |  |  | SI | Other |
| Q07 | - |  |  | SI | Feed name |
| Q08 | - |  |  | SI | Feeding regimen |
| Q10 | - |  |  | SI | From (date) |
| Q12 | - |  |  | SI | Method of delivery |
| Q13 | - |  |  | SI | Commence at |
| Q14 | - |  |  | SI | Increase by |
| Q15 | - |  |  | SI | Every |
| Q16 | - |  |  | SI | Target rate of |
| Q17 | - |  |  | SI | Total feed per day of |
| Q18 | - |  |  | SI | Times of feeding |
| Q19 | - |  |  | SI | Water flush |
| Q20 | - |  |  | SI | Water flush |
| Q21 | - |  |  | SI | Water flush text |
| Q22 | - |  |  | SI | every |
| Q23 | - |  |  | SI | Water flush 2 |
| Q24 | - |  |  | SI | Water flush 2 text |
| Q25 | - |  |  | SI | Also flush with at least 50mL before and after eac... |
| Q26 | - |  |  | SI | Monitoring gastric residual volume (aspirates) |
| Q27 | - |  |  | SI | Date |
| Q28 | - |  |  | SI | Monitoring gastric residual volume (aspirates) 2 |
| Q29 | - |  |  | SI | Date |
| Q30 | - |  |  | SI | Comments |
| Q31 | - |  |  | SI | Total nutrition provided at target rate |
| Q32 | - |  |  | SI | Energy |
| Q33 | - |  |  | SI | Protein |
| Q34 | - |  |  | SI | Other |
| Q35 | - |  |  | SI | Fluid from feed |
| Q36 | - |  |  | SI | Fluid from flushes |
| Q37 | - |  |  | SI | Total fluids |
| Q38 | - |  |  | SI | Dietitian |
| Q39 | - |  |  | SI | Date |
| Q40 | - |  |  | SI | Signature |
| Q40UDt | - |  |  | SI | Signature Last Updated Date |
| Q40UTm | - |  |  | SI | Signature Last Updated Time |
| Q41 | - |  |  | SI | Pager no / Phone no |
| Q42 | - |  |  | SI | mL/hr |
| Q43 | - |  |  | SI | mL/hr every |
| Q44 | - |  |  | SI | hrs, as tolerated, until, |
| Q45 | - |  |  | SI | mL/hr (total feed per day of |
| Q46 | - |  |  | SI | mL) |
| Q47 | - |  |  | SI | mL every |
| Q48 | - |  |  | SI | hours |
| Q49 | - |  |  | SI | Feeding regimen |
| Q50 | - |  |  | SI | Tube type / diameter |
| Q51 | - |  |  | SI | mL pre and post feeding |
| Q52 | - |  |  | SI | KJ/day |
| Q53 | - |  |  | SI | g/day |
| Q54 | - |  |  | SI | /day |
| Q55 | - |  |  | SI | mL/day |
| Q56 | - |  |  | SI | mL/day |
| Q57 | - |  |  | SI | mL/day |
| Q58 | - |  |  | SI | Other |
| Q59 | - |  |  | SI | Monitoring gastric residual volume (aspirates) |
| Q60 | - |  |  | SI | Monitoring gastric residual volume (aspirates) 2 |
| Q61 | - |  |  | SI | Status of enteral feeding regimen |
| Q62 | - |  |  | SI | Reason for voiding |
| Q63 | - |  |  | SI | Voided by |
| Q64 | - |  |  | SI | Void date |
| Q65 | - |  |  | SI | Void time |
| Q66 | - |  |  | SI | Date |
| Q67 | - |  |  | SI | Time |
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