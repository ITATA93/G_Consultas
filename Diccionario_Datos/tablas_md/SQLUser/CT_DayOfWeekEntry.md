# SQLUser.CT_DayOfWeekEntry

**Schema:** SQLUser
**Columnas:** 98
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DOWE_RowId1 | double | PK |  | NO | - |
| DOWE_Checked1 | varchar |  |  | NO | Checked1 |
| DOWE_Checked2 | varchar |  |  | NO | Checked2 |
| DOWE_Checked3 | varchar |  |  | NO | Checked3 |
| DOWE_Checked4 | varchar |  |  | NO | Checked4 |
| DOWE_Checked5 | varchar |  |  | NO | Checked5 |
| DOWE_Checked6 | varchar |  |  | NO | Checked6 |
| DOWE_Checked7 | varchar |  |  | NO | Checked7 |
| DOWE_CreatedDate | date |  |  | SI | Created Date |
| DOWE_CreatedTime | time |  |  | SI | Created Time |
| DOWE_CreatedUser_DR | bigint |  | FK | SI | Created User |
| DOWE_Day1 | varchar |  |  | NO | Day 1 |
| DOWE_Day2 | varchar |  |  | NO | Day 2 |
| DOWE_Day3 | varchar |  |  | NO | Day 3 |
| DOWE_Day4 | varchar |  |  | NO | Day 4 |
| DOWE_Day5 | varchar |  |  | NO | Day 5 |
| DOWE_Day6 | varchar |  |  | NO | Day 6 |
| DOWE_Day7 | varchar |  |  | NO | Day 7 |
| DOWE_RowId | double |  |  | NO | DOWE Row ID |
| DOWE_Seq1 | numeric |  |  | NO | Sequence 1 |
| DOWE_Seq2 | numeric |  |  | NO | Sequence 2 |
| DOWE_Seq3 | numeric |  |  | NO | Sequence 3 |
| DOWE_Seq4 | numeric |  |  | NO | Sequence 4 |
| DOWE_Seq5 | numeric |  |  | NO | Sequence 5 |
| DOWE_Seq6 | numeric |  |  | NO | Sequence 6 |
| DOWE_Seq7 | numeric |  |  | NO | Sequence 7 |
| DOWE_UpdatedDate | date |  |  | SI | Updated Date |
| DOWE_UpdatedTime | time |  |  | SI | Updated Time |
| DOWE_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| DOWE_Weekend1 | varchar |  |  | SI | Weekend1 |
| DOWE_Weekend2 | varchar |  |  | SI | Weekend2 |
| DOWE_Weekend3 | varchar |  |  | SI | Weekend3 |
| DOWE_Weekend4 | varchar |  |  | SI | Weekend4 |
| DOWE_Weekend5 | varchar |  |  | SI | Weekend5 |
| DOWE_Weekend6 | varchar |  |  | SI | Weekend6 |
| DOWE_Weekend7 | varchar |  |  | SI | Weekend7 |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Remember, yes, a change indicates that there has b... |
| Q04 | - |  |  | SI | Problems with judgement (e.g., falls for scams, ba... |
| Q05 | - |  |  | SI | Reduced interest in hobbies / activities |
| Q06 | - |  |  | SI | Repeats questions, stories, or statements |
| Q07 | - |  |  | SI | Trouble learning how to use a tool, appliance, or ... |
| Q08 | - |  |  | SI | Forgets correct month or year |
| Q09 | - |  |  | SI | Difficulty handling complicated financial affairs ... |
| Q10 | - |  |  | SI | Difficulty remembering appointments |
| Q11 | - |  |  | SI | Consistent problems with thinking and/or memory |
| Q12 | - |  |  | SI | Total AD8 score |
| Q13 | - |  |  | SI | Cut points |
| Q14 | - |  |  | SI | 0 to 1 |
| Q15 | - |  |  | SI | 2 or greater |
| Q16 | - |  |  | SI | Normal cognition |
| Q17 | - |  |  | SI | Cognitive impairment is likely to be present |
| Q18 | - |  |  | SI | Provenance details |
| Q19 | - |  |  | SI | The eight-item informant interview to differentiat... |
| Q20 | - |  |  | SI | Reference: galvin je, roe cm, powlishta kk, et al.... |
| Q21 | - |  |  | SI | The Eight-item Informant Interview to Differentiat... |
| Q22 | - |  |  | SI | Total AD8 score |
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