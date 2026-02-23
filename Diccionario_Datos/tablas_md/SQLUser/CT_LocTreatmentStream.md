# SQLUser.CT_LocTreatmentStream

**Schema:** SQLUser
**Columnas:** 87
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de Ubicaciones**. Servicios, salas, unidades del hospital.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LOCTRSTR_ParRef | bigint | PK |  | NO | CT_Loc Parent Reference |
| LOCTRSTR_Childsub | double |  |  | NO | Childsub |
| LOCTRSTR_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LOCTRSTR_CreatedDate | date |  |  | SI | Created Date |
| LOCTRSTR_CreatedTime | time |  |  | SI | Created Time |
| LOCTRSTR_CreatedUser_DR | bigint |  | FK | SI | Created User |
| LOCTRSTR_DateFrom | date |  |  | SI | Date From |
| LOCTRSTR_DateTo | date |  |  | SI | Date To |
| LOCTRSTR_RowId | varchar |  |  | NO | - |
| LOCTRSTR_TreatmentStream_DR | bigint |  | FK | NO | Des Ref PAC_TreatmentStream |
| LOCTRSTR_UpdatedDate | date |  |  | SI | Updated Date |
| LOCTRSTR_UpdatedTime | time |  |  | SI | Updated Time |
| LOCTRSTR_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Gestation |
| Q04 | - |  |  | SI | Smoking in this period in this pregnancy |
| Q05 | - |  |  | SI | Did smoking cease in this period |
| Q06 | - |  |  | SI | Cessation date |
| Q07 | - |  |  | SI | Gestation age (weeks) |
| Q08 | - |  |  | SI | Average number of cigarettes smoked per day |
| Q09 | - |  |  | SI | Does your partner or another member of the househo... |
| Q10 | - |  |  | SI | Notes |
| Q11 | - |  |  | SI | Advice / Education |
| Q12 | - |  |  | SI | Advise benefits of quitting smoking for |
| Q13 | - |  |  | SI | Patient / Partner |
| Q14 | - |  |  | SI | Pregnancy |
| Q15 | - |  |  | SI | Baby |
| Q16 | - |  |  | SI | Breastfeeding |
| Q17 | - |  |  | SI | Family |
| Q18 | - |  |  | SI | Advice / Education notes |
| Q19 | - |  |  | SI | Provided Patient |
| Q20 | - |  |  | SI | Assess to quit or reduce smoking |
| Q21 | - |  |  | SI | Quit / Reduce smoking notes |
| Q22 | - |  |  | SI | Assist / Arrange education / quit plan |
| Q23 | - |  |  | SI | Quit information provided |
| Q24 | - |  |  | SI | Date quit information provided |
| Q25 | - |  |  | SI | Education / Quit plan provided |
| Q26 | - |  |  | SI | Patient provided notes |
| Q27 | - |  |  | SI | Provided Partner |
| Q28 | - |  |  | SI | Quit information provided |
| Q29 | - |  |  | SI | Date quit information provided |
| Q30 | - |  |  | SI | Education / Quit plan provided |
| Q31 | - |  |  | SI | Partner provided notes |
| Q32 | - |  |  | SI | Cessation gestation age (weeks) |
| Q33 | - |  |  | SI | Patient support notes |
| Q34 | - |  |  | SI | Partner support notes |
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