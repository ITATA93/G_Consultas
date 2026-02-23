# SQLUser.INC_ReasonForAdjustment

**Schema:** SQLUser
**Columnas:** 81
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Incidentes**. Reportes de eventos adversos.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ADJ_RowId | bigint | PK |  | NO | - |
| ADJ_Code | varchar |  |  | NO | Code |
| ADJ_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| ADJ_CreatedDate | date |  |  | SI | Created Date |
| ADJ_CreatedTime | time |  |  | SI | Created Time |
| ADJ_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ADJ_Desc | varchar |  |  | NO | Description |
| ADJ_Owner | varchar |  |  | SI | Owner |
| ADJ_UpdatedDate | date |  |  | SI | Updated Date |
| ADJ_UpdatedTime | time |  |  | SI | Updated Time |
| ADJ_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Father / Mother's name |
| Q02 | - |  |  | SI | This scale enables you to indicate the kinds of pr... |
| Q03 | - |  |  | SI | My child wets the bed |
| Q04 | - |  |  | SI | My child hits other children |
| Q05 | - |  |  | SI | My child runs away from home |
| Q06 | - |  |  | SI | My child disobeys me |
| Q07 | - |  |  | SI | My child tells lies |
| Q08 | - |  |  | SI | My child steals things from others |
| Q09 | - |  |  | SI | My child screams very loudly |
| Q10 | - |  |  | SI | My child bites other children |
| Q11 | - |  |  | SI | My child hits me when I try to administer discipli... |
| Q12 | - |  |  | SI | My child demands constant attention |
| Q13 | - |  |  | SI | My child is afraid of other children |
| Q14 | - |  |  | SI | My child is afraid of strangers |
| Q15 | - |  |  | SI | My child has nightmare |
| Q16 | - |  |  | SI | My child misbehaves when we go out |
| Q17 | - |  |  | SI | My child will not let me out of his or her sight |
| Q18 | - |  |  | SI | My child is very timid or shy |
| Q19 | - |  |  | SI | My child is destructive |
| Q20 | - |  |  | SI | My child has temper tantrums |
| Q21 | - |  |  | SI | My child has accidents or gets hurt |
| Q22 | - |  |  | SI | My child bangs his or her head or engages in other... |
| Q23 | - |  |  | SI | Physician signature |
| Q23UDt | - |  |  | SI | Physician signature Last Updated Date |
| Q23UTm | - |  |  | SI | Physician signature Last Updated Time |
| Q24 | - |  |  | SI | 19 - 38: Potential behavioral anomalies |
| Q25 | - |  |  | SI | 39 - 76: Behavioral anomalies |
| Q26 | - |  |  | SI | 77 - 100: Critical behavioral anomalies |
| Q27 | - |  |  | SI | Date |
| Q28 | - |  |  | SI | Time |
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