# questionnaire.QTCPENAT

> Pediatric Nausea Assessment Tool (PeNAT)

**Schema:** questionnaire
**Columnas:** 101
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Pediatric Nausea Assessment Tool (PeNAT)

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q1 | date |  |  | SI | Date |
| Q10 | varchar |  |  | SI | Two standards are developed for administering the ... |
| Q11 | varchar |  |  | SI | Group 1: children receiving chemotherapy. |
| Q12 | varchar |  |  | SI | Group 2: children receiving cancer chemotherapy be... |
| Q13 | varchar |  |  | SI | Group 3: children with cancer who were not receivi... |
| Q14 | varchar |  |  | SI | Determine from the parent(s) what terms their fami... |
| Q15 | varchar |  |  | SI | To the child: |
| Q16 | varchar |  |  | SI | Have you ever thrown up (use family term above) be... |
| Q17 | varchar |  |  | SI | If yes, how did your tummy feel just before you th... |
| Q18 | varchar |  |  | SI |  We call that feeling nausea or being nauseous. In... |
| Q19 | varchar |  |  | SI | If no, have you ever felt like you were going to t... |
| Q2 | time |  |  | SI | Time |
| Q20 | varchar |  |  | SI | If yes, how did your tummy feel then? |
| Q21 | varchar |  |  | SI |  We call that feeling nausea or being nauseous. In... |
| Q22 | varchar |  |  | SI | FOR GROUP 1: |
| Q23 | varchar |  |  | SI | Some children who get chemo feel nauseous (use fam... |
| Q24 | varchar |  |  | SI | If child says no nausea, show faces A and B. |
| Q25 | varchar |  |  | SI |  Some children who get chemo feel no nausea (use f... |
| Q26 | varchar |  |  | SI |  Point to each face at the appropriate time and us... |
| Q27 | varchar |  |  | SI |  Which child is more like you right now? |
| Q28 | varchar |  |  | SI | If child says some nausea, show faces C and D. |
| Q29 | varchar |  |  | SI |   Some children who get chemo feel some nausea (us... |
| Q3 | varchar |  |  | SI | Which face is more like you right now? |
| Q30 | varchar |  |  | SI |  Point to each face at the appropriate time and us... |
| Q31 | varchar |  |  | SI |  Which child is more like you right now? |
| Q32 | varchar |  |  | SI | FOR GROUPS 2 & 3: |
| Q33 | varchar |  |  | SI | Some children feel nauseous (use family term) and ... |
| Q34 | varchar |  |  | SI | If child says no nausea, show faces A and B. |
| Q35 | varchar |  |  | SI |  Some children feel no nausea (use family term) at... |
| Q36 | varchar |  |  | SI |  Point to each face at the appropriate time and us... |
| Q37 | varchar |  |  | SI |  Which child is more like you right now? |
| Q38 | varchar |  |  | SI | If child says some nausea, show faces C and D. |
| Q39 | varchar |  |  | SI |  Some children feel some nausea (use family term),... |
| Q4 | varchar |  |  | SI | Image |
| Q40 | varchar |  |  | SI |  Point to each face at the appropriate time and us... |
| Q41 | varchar |  |  | SI |  Which child is more like you right now? |
| Q42 | varchar |  |  | SI | Introduction script - children 9 to 18 years |
| Q43 | varchar |  |  | SI | The following script is to ensure that children un... |
| Q44 | varchar |  |  | SI | Two standards are developed for administering the ... |
| Q45 | varchar |  |  | SI | Group 1: children receiving chemotherapy. |
| Q46 | varchar |  |  | SI | Group 2: children receiving cancer chemotherapy be... |
| Q47 | varchar |  |  | SI | Group 3: children with cancer who were not receivi... |
| Q48 | varchar |  |  | SI | Determine from the parent(s) what terms their fami... |
| Q49 | varchar |  |  | SI | To the child: |
| Q50 | varchar |  |  | SI | Have you ever thrown up (use family term above) be... |
| Q51 | varchar |  |  | SI | If yes, how did your tummy feel just before you th... |
| Q52 | varchar |  |  | SI |  We call that feeling nausea or being nauseous. In... |
| Q53 | varchar |  |  | SI | If no, have you ever felt like you were going to t... |
| Q54 | varchar |  |  | SI | If yes, how did your tummy feel then? |
| Q55 | varchar |  |  | SI |  We call that feeling nausea or being nauseous. In... |
| Q56 | varchar |  |  | SI | FOR GROUP 1: |
| Q57 | varchar |  |  | SI | Some children who get chemo feel nauseous (use fam... |
| Q58 | varchar |  |  | SI | These faces show children who feel no nausea at al... |
| Q59 | varchar |  |  | SI | Point to each face at the appropriate time. Which ... |
| Q60 | varchar |  |  | SI | FOR GROUPS 2 & 3: |
| Q61 | varchar |  |  | SI | Some children feel nauseous (use family term) and ... |
| Q62 | varchar |  |  | SI | These faces show children who feel no nausea at al... |
| Q63 | varchar |  |  | SI | Point to each face at the appropriate time. Which ... |
| Q8 | varchar |  |  | SI | Introduction script - children 4 to 8 years |
| Q9 | varchar |  |  | SI | The following script is to ensure that children un... |
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