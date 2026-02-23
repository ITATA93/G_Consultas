# SQLUser.LBC_BloodProduct

**Schema:** SQLUser
**Columnas:** 103
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Laboratorio**. Parámetros del módulo de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCBP_RowID | bigint | PK |  | NO | - |
| LBCBP_AutoRequestCollection_DR | varchar |  | FK | SI | Auto request collection specimen container
Specim... |
| LBCBP_AutoRequestTestSets | varchar |  |  | SI | Auto request test sets
Test set to be automatical... |
| LBCBP_BarcodeLabelPrintFormat_DR | bigint |  | FK | SI | Format for Printing Barcode Label Representations ... |
| LBCBP_BatchProduct | varchar |  |  | SI | Is a batch product |
| LBCBP_BloodProductGroup_DR | bigint |  | FK | NO | Blood product group |
| LBCBP_Code | varchar |  |  | NO | Code |
| LBCBP_CodeTableTags | varchar |  |  | SI | List of code table tags |
| LBCBP_Comment | varchar |  |  | SI | Comment |
| LBCBP_Cost | numeric |  |  | SI | Cost of the product |
| LBCBP_CreatedDate | date |  |  | SI | Created Date |
| LBCBP_CreatedTime | time |  |  | SI | Created Time |
| LBCBP_CreatedUser_DR | bigint |  | FK | SI | Created User |
| LBCBP_DateFrom | date |  |  | SI | Effective date for the record |
| LBCBP_DateTo | date |  |  | SI | Last day the record is active |
| LBCBP_DefaultQuantity | numeric |  |  | SI | Default quantity |
| LBCBP_DefaultReservationPeriod | integer |  |  | SI | Default reservation period |
| LBCBP_DefaultReservationPeriodUnit | varchar |  |  | SI | Default reservation period unit |
| LBCBP_Desc | varchar |  |  | NO | Description |
| LBCBP_GroupCheckRequired | varchar |  |  | SI | Requires group check |
| LBCBP_Instructions | longvarchar |  |  | SI | Instructions
HTMLRichText |
| LBCBP_Irradiated | varchar |  |  | SI | Is irradiated |
| LBCBP_IssueComment | longvarchar |  |  | SI | Issue Comment
HTMLRichText |
| LBCBP_MaximumLifeSpan | integer |  |  | SI | Maximum Life Span (from donation date/time) |
| LBCBP_MaximumLifeSpanUnit | varchar |  |  | SI | Unit of the Maximum Life Span (from donation date/... |
| LBCBP_Owner | varchar |  |  | SI | Owner |
| LBCBP_Splitable | varchar |  |  | SI | Can be split |
| LBCBP_UpdatedDate | date |  |  | SI | Updated Date |
| LBCBP_UpdatedTime | time |  |  | SI | Updated Time |
| LBCBP_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Cough score |
| Q04 | - |  |  | SI | I never cough (0) |
| Q05 | - |  |  | SI | I cough all the time (5) |
| Q06 | - |  |  | SI | Phlegm score |
| Q07 | - |  |  | SI | I have no phlegm (mucus) on my chest at all (0) |
| Q08 | - |  |  | SI | My chest is full of phlegm (mucus) (5) |
| Q09 | - |  |  | SI | Chest tightness score |
| Q10 | - |  |  | SI | My chest does not feel tight at all (0) |
| Q11 | - |  |  | SI | My chest feels very tight (5) |
| Q12 | - |  |  | SI | Shortness of breath score |
| Q13 | - |  |  | SI | When I walk up a hill or a flight of stairs I am n... |
| Q14 | - |  |  | SI | When I walk up a hill or a flight of stairs I am c... |
| Q15 | - |  |  | SI | Activities at home score |
| Q16 | - |  |  | SI | I am not limited to doing any activities at home (... |
| Q17 | - |  |  | SI | I am completely limited to doing all activities at... |
| Q18 | - |  |  | SI | Leave my home score |
| Q19 | - |  |  | SI | I am confident leaving my home despite my lung con... |
| Q20 | - |  |  | SI | I am not confident leaving my home at all because ... |
| Q21 | - |  |  | SI | Sleep score |
| Q22 | - |  |  | SI | I sleep soundly (0) |
| Q23 | - |  |  | SI | I do not sleep soundly because of my lung conditio... |
| Q24 | - |  |  | SI | Energy score |
| Q25 | - |  |  | SI | I have lots of energy (0) |
| Q26 | - |  |  | SI | I have no energy at all (5) |
| Q27 | - |  |  | SI | 0 - 40 |
| Q28 | - |  |  | SI | Higher score indicates higher impact that COPD is ... |
| Q29 | - |  |  | SI | Score |
| Q30 | - |  |  | SI | Classification |
| Q31 | - |  |  | SI | The COPD Assessment Test (CAT) is a questionnaire ... |
| Q32 | - |  |  | SI | It is designed to measure the impact of COPD on a ... |
| Q33 | - |  |  | SI | 0 - 40: Higher score indicates higher impact that ... |
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