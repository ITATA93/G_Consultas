# questionnaire.QTCOMAT

> Oral Mucositis Assessment Tool

**Schema:** questionnaire
**Columnas:** 96
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Oral Mucositis Assessment Tool

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | Assess the patient’s oral cavity and their ability... |
| Q04 | varchar |  |  | SI | Voice |
| Q05 | varchar |  |  | SI | Swallow |
| Q06 | varchar |  |  | SI | Mucous membranes |
| Q07 | varchar |  |  | SI | Saliva |
| Q08 | varchar |  |  | SI | Tongue |
| Q09 | varchar |  |  | SI | Lips |
| Q10 | varchar |  |  | SI | Gums |
| Q11 | varchar |  |  | SI | Teeth / Dentures |
| Q12 | varchar |  |  | SI | Ability to maintain nutrition |
| Q13 | varchar |  |  | SI | Analgesic requirements |
| Q14 | varchar |  |  | SI | Evidence of infection |
| Q15 | varchar |  |  | SI | Taste |
| Q16 | varchar |  |  | SI | Self care assessments |
| Q17 | varchar |  |  | SI | Patient has head and neck cancer or receiving high... |
| Q18 | varchar |  |  | SI | Score |
| Q19 | varchar |  |  | SI | Documentation of the oral mucosa pertaining to can... |
| Q20 | varchar |  |  | SI | Assess and identify the risks of oral complication... |
| Q21 | varchar |  |  | SI | Assessment score |
| Q22 | varchar |  |  | SI | Intervention level |
| Q23 | varchar |  |  | SI | Assessment |
| Q24 | varchar |  |  | SI | Frequency of mouth care |
| Q25 | varchar |  |  | SI | Analgesia |
| Q26 | varchar |  |  | SI | 13 - 20 |
| Q27 | varchar |  |  | SI | Level 1 |
| Q28 | varchar |  |  | SI | At least once daily |
| Q29 | varchar |  |  | SI | 4 times a day |
| Q30 | varchar |  |  | SI | As required |
| Q31 | varchar |  |  | SI | 21 - 26 |
| Q32 | varchar |  |  | SI | Level 2 |
| Q33 | varchar |  |  | SI | At least twice daily |
| Q34 | varchar |  |  | SI | 2 to 4 hourly |
| Q35 | varchar |  |  | SI | Regular and breakthrough |
| Q36 | varchar |  |  | SI | 27 - 39 |
| Q37 | varchar |  |  | SI | Level 3 |
| Q38 | varchar |  |  | SI | At least 8 hourly (each shift) |
| Q39 | varchar |  |  | SI | 1 to 2 hourly |
| Q40 | varchar |  |  | SI | Regular and breakthrough or continuous and breakth... |
| Q41 | varchar |  |  | SI | Nursing interventions |
| Q42 | varchar |  |  | SI | Level 1 interventions |
| Q43 | varchar |  |  | SI | • Brush teeth or dentures after each meal and befo... |
| Q44 | varchar |  |  | SI | • Dentures should be removed when the patient is a... |
| Q45 | varchar |  |  | SI | • Rinse with sodium bicarbonate or salt water for ... |
| Q46 | varchar |  |  | SI | • Keep lips lubricated, e.g. with lip balm or lip ... |
| Q47 | varchar |  |  | SI | Level 2 interventions in addition to level 1 |
| Q48 | varchar |  |  | SI | • Increase the frequency of level 1 interventions ... |
| Q49 | varchar |  |  | SI | • Refer to dietician |
| Q50 | varchar |  |  | SI | • Provide regular analgesia as required |
| Q51 | varchar |  |  | SI | • Any ulcerations and visible infection should be ... |
| Q52 | varchar |  |  | SI | Level 3 interventions in addition to level 2 |
| Q53 | varchar |  |  | SI | • Increase the frequency of level 2 interventions ... |
| Q54 | varchar |  |  | SI | • Use sponge sticks instead of soft toothbrush |
| Q55 | varchar |  |  | SI | • Medical review |
| QUESAnaDR | varchar |  | FK | SI | Anaesthesia |
| QUESAnaOperationDR | varchar |  | FK | SI | Operation |
| QUESConsultDR | varchar |  | FK | SI | Consult |
| QUESCopiedComments | varchar |  |  | SI | Copied Comments |
| QUESCopiedDate | date |  |  | SI | Copied Date |
| QUESCopiedEpDR | bigint |  | FK | SI | Copied Episode |
| QUESCopiedSourceDR | bigint |  | FK | SI | Copied Source DR |
| QUESCopiedTime | time |  |  | SI | Copied Time |
| QUESCopiedUserDR | bigint |  | FK | SI | Copied User |
| QUESCreateDate | date |  |  | SI | Creation Date |
| QUESCreateTime | time |  |  | SI | Creation Time |
| QUESCreateUserDR | bigint |  | FK | SI | Creation User |
| QUESDate | date |  |  | SI | Last Update Date |
| QUESErrorReasonDR | bigint |  | FK | SI | Error Reason |
| QUESFHResidentDR | bigint |  | FK | SI | Resident |
| QUESMRClinicalPathWaysDR | varchar |  | FK | SI | Clinical Pathway |
| QUESNRCarePlanIssuesDR | varchar |  | FK | SI | Nurse Care Plan Issues |
| QUESOEOrdExecDR | varchar |  | FK | SI | Order Execution |
| QUESORPreanaestheticConsultDR | bigint |  | FK | SI | Preanaesthetic Consultation |
| QUESObsEntryDR | varchar |  | FK | SI | Observation Entry |
| QUESOperRoomDR | bigint |  | FK | SI | Operating Room |
| QUESPAAdmDR | bigint |  | FK | SI | Admission |
| QUESPAAdverseEventDR | varchar |  | FK | SI | Adverse Event |
| QUESPAPatMasDR | bigint |  | FK | SI | Patient |
| QUESPAPregnancyDR | bigint |  | FK | SI | Pregnancy |
| QUESPAWaitingListDR | bigint |  | FK | SI | Waiting List |
| QUESPathwayItemDR | varchar |  | FK | SI | Pathway Item |
| QUESPrePostExamOEOrdItemDR | varchar |  | FK | SI | Pre/Post Exam OrdItem |
| QUESRBAppointmentDR | varchar |  | FK | SI | Appointments |
| QUESRBApptOutcomeDR | varchar |  | FK | SI | Appointment Outcome |
| QUESRBApptSlotDR | varchar |  | FK | SI | Appointment Slot |
| QUESReasonForCorrectionDR | bigint |  | FK | SI | Reason for Correction |
| QUESSSUserDefWindowDR | bigint |  | FK | SI | Questionnaire |
| QUESScore | varchar |  |  | SI | Score |
| QUESSecondUserDR | bigint |  | FK | SI | Second Signature |
| QUESStatusDR | bigint |  | FK | SI | Status |
| QUESTextResultDR | bigint |  | FK | SI | Text Result |
| QUESTime | time |  |  | SI | Last Update Time |
| QUESTransactionDR | varchar |  | FK | SI | Transaction |
| QUESUserDR | bigint |  | FK | SI | Last Update User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*