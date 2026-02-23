# SQLUser.ORC_DiscrepanciesinCount

**Schema:** SQLUser
**Columnas:** 162
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Órdenes**. Parámetros de órdenes médicas.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DIINCO_RowId | bigint | PK |  | NO | - |
| DIINCO_Code | varchar |  |  | NO | Code |
| DIINCO_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| DIINCO_CreatedDate | date |  |  | SI | Created Date |
| DIINCO_CreatedTime | time |  |  | SI | Created Time |
| DIINCO_CreatedUser_DR | bigint |  | FK | SI | Created User |
| DIINCO_DateFrom | date |  |  | SI | Date From |
| DIINCO_DateTo | date |  |  | SI | Date To |
| DIINCO_Desc | varchar |  |  | NO | Description |
| DIINCO_Owner | varchar |  |  | SI | Owner |
| DIINCO_UpdatedDate | date |  |  | SI | Updated Date |
| DIINCO_UpdatedTime | time |  |  | SI | Updated Time |
| DIINCO_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Disease activity score (DAS28) |
| Q04 | - |  |  | SI | Total number of tender joints (0&nbsp |
| Q05 | - |  |  | SI | Total number of swollen joints (0&nbsp |
| Q06 | - |  |  | SI | C-reactive protein (CRP) (mg/L) |
| Q07 | - |  |  | SI | ESR (mm/h) |
| Q08 | - |  |  | SI | General health |
| Q09 | - |  |  | SI | Rate your general health between best possible (10... |
| Q10 | - |  |  | SI | DAS-28 ESR Score |
| Q100 | - |  |  | SI | PIP, Third, Right |
| Q101 | - |  |  | SI | PIP, Third, Left |
| Q102 | - |  |  | SI | PIP, Fourth, Right |
| Q103 | - |  |  | SI | PIP, Fourth, Left |
| Q104 | - |  |  | SI | Knee, Right |
| Q105 | - |  |  | SI | Knee, Left |
| Q106 | - |  |  | SI | (1) based on the Ritchie Index, the number of swol... |
| Q107 | - |  |  | SI | And the patient’s general health assessed on a vis... |
| Q108 | - |  |  | SI | Thus creating the DAS28 score and this, in turn, w... |
| Q109 | - |  |  | SI | Arthritis and Rheumatism: Official Journal of the ... |
| Q11 | - |  |  | SI | DAS-28 CRP Score |
| Q12 | - |  |  | SI | Right |
| Q13 | - |  |  | SI | Left |
| Q14 | - |  |  | SI | Shoulder |
| Q15 | - |  |  | SI | Shoulder |
| Q16 | - |  |  | SI | Elbow |
| Q17 | - |  |  | SI | Elbow |
| Q18 | - |  |  | SI | Wrist |
| Q19 | - |  |  | SI | Wrist |
| Q20 | - |  |  | SI | MCP - Thumb |
| Q21 | - |  |  | SI | MCP - Thumb |
| Q22 | - |  |  | SI | MCP - First |
| Q23 | - |  |  | SI | MCP - First |
| Q24 | - |  |  | SI | MCP - Second |
| Q25 | - |  |  | SI | MCP - Second |
| Q26 | - |  |  | SI | MCP - Third |
| Q27 | - |  |  | SI | MCP - Third |
| Q28 | - |  |  | SI | MCP - Fourth |
| Q29 | - |  |  | SI | MCP - Fourth |
| Q30 | - |  |  | SI | PIP - Thumb |
| Q31 | - |  |  | SI | PIP - Thumb |
| Q32 | - |  |  | SI | PIP - First |
| Q33 | - |  |  | SI | PIP - First |
| Q34 | - |  |  | SI | PIP - Second |
| Q35 | - |  |  | SI | PIP - Second |
| Q36 | - |  |  | SI | PIP - Third |
| Q37 | - |  |  | SI | PIP - Third |
| Q38 | - |  |  | SI | PIP - Fourth |
| Q39 | - |  |  | SI | PIP - Fourth |
| Q40 | - |  |  | SI | Knee |
| Q41 | - |  |  | SI | Knee |
| Q42 | - |  |  | SI | *MCP - Metacarpophalangeal |
| Q43 | - |  |  | SI | *PIP - Proximal interphalangeal |
| Q44 | - |  |  | SI | Shoulder, Right |
| Q45 | - |  |  | SI | Shoulder, Left |
| Q46 | - |  |  | SI | Elbow, Right |
| Q47 | - |  |  | SI | Elbow, Left |
| Q48 | - |  |  | SI | Wrist, Right |
| Q49 | - |  |  | SI | Wrist, Left |
| Q50 | - |  |  | SI | MCP, Thumb, Right |
| Q51 | - |  |  | SI | MCP, Thumb, Left |
| Q52 | - |  |  | SI | MCP, First, Right |
| Q53 | - |  |  | SI | MCP, First, Left |
| Q54 | - |  |  | SI | MCP, Second, Right |
| Q55 | - |  |  | SI | MCP, Second, Left |
| Q56 | - |  |  | SI | MCP, Third, Right |
| Q57 | - |  |  | SI | MCP, Third, Left |
| Q58 | - |  |  | SI | MCP, Fourth, Right |
| Q59 | - |  |  | SI | MCP, Fourth, Left |
| Q60 | - |  |  | SI | PIP, Thumb, Right |
| Q61 | - |  |  | SI | PIP, Thumb, Left |
| Q62 | - |  |  | SI | PIP, First, Right |
| Q63 | - |  |  | SI | PIP, First, Left |
| Q64 | - |  |  | SI | PIP, Second, Right |
| Q65 | - |  |  | SI | PIP, Second, Left |
| Q66 | - |  |  | SI | PIP, Third, Right |
| Q67 | - |  |  | SI | PIP, Third, Left |
| Q68 | - |  |  | SI | PIP, Fourth, Right |
| Q69 | - |  |  | SI | PIP, Fourth, Left |
| Q70 | - |  |  | SI | Knee, Right |
| Q71 | - |  |  | SI | Knee, Left |
| Q72 | - |  |  | SI | The Disease Activity Score (DAS) for patient with ... |
| Q73 | - |  |  | SI | The DAS was modified in 1995 by limiting the numbe... |
| Q74 | - |  |  | SI | Van der Heijde DM, van't Hof MA, Van Riel PL, et a... |
| Q75 | - |  |  | SI | Prevoo ML, Van'T Hof M, Kuper HH, et al,. Modified... |
| Q76 | - |  |  | SI | Fransen J, Welsing PM, De Keijzer RM, Van Riel PL.... |
| Q77 | - |  |  | SI | A scoring tool used to describe the severity of rh... |
| Q78 | - |  |  | SI | Shoulder, Right |
| Q79 | - |  |  | SI | Shoulder, Left |
| Q80 | - |  |  | SI | Elbow, Right |
| Q81 | - |  |  | SI | Elbow, Left |
| Q82 | - |  |  | SI | Wrist, Right |
| Q83 | - |  |  | SI | Wrist, Left |
| Q84 | - |  |  | SI | MCP, Thumb, Right |
| Q85 | - |  |  | SI | MCP, Thumb, Left |
| Q86 | - |  |  | SI | MCP, First, Right |
| Q87 | - |  |  | SI | MCP, First, Left |
| Q88 | - |  |  | SI | MCP, Second, Right |
| Q89 | - |  |  | SI | MCP, Second, Left |
| Q90 | - |  |  | SI | MCP, Third, Right |
| Q91 | - |  |  | SI | MCP, Third, Left |
| Q92 | - |  |  | SI | MCP, Fourth, Right |
| Q93 | - |  |  | SI | MCP, Fourth, Left |
| Q94 | - |  |  | SI | PIP, Thumb, Right |
| Q95 | - |  |  | SI | PIP, Thumb, Left |
| Q96 | - |  |  | SI | PIP, First, Right |
| Q97 | - |  |  | SI | PIP, First, Left |
| Q98 | - |  |  | SI | PIP, Second, Right |
| Q99 | - |  |  | SI | PIP, Second, Left |
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