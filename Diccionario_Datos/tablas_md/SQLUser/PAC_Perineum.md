# SQLUser.PAC_Perineum

**Schema:** SQLUser
**Columnas:** 105
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PERIN_RowId | bigint | PK |  | NO | - |
| PERIN_Code | varchar |  |  | NO | Code |
| PERIN_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| PERIN_CreatedDate | date |  |  | SI | Created Date |
| PERIN_CreatedTime | time |  |  | SI | Created Time |
| PERIN_CreatedUser_DR | bigint |  | FK | SI | Created User |
| PERIN_DateFrom | date |  |  | SI | Date From |
| PERIN_DateTo | date |  |  | SI | Date To |
| PERIN_Desc | varchar |  |  | NO | Description |
| PERIN_NationalCode | varchar |  |  | SI | National code |
| PERIN_Owner | varchar |  |  | SI | Owner |
| PERIN_UpdatedDate | date |  |  | SI | Updated Date |
| PERIN_UpdatedTime | time |  |  | SI | Updated Time |
| PERIN_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q1 | - |  |  | SI | Anaesthetic Care |
| Q10 | - |  |  | SI | Care During Procedure |
| Q11 | - |  |  | SI | Correct techniques for moving patient adopted and ... |
| Q12 | - |  |  | SI | Patient positioned safely for surgery |
| Q13 | - |  |  | SI | Pre procedure - where possible the patients pressu... |
| Q14 | - |  |  | SI | Please document any findings on the relevant risk ... |
| Q15 | - |  |  | SI | Positional aids used (if applicable) |
| Q16 | - |  |  | SI | Pressure reducing aids used (if applicable) |
| Q17 | - |  |  | SI | Warming device used (if applicable) |
| Q18 | - |  |  | SI | Free flow oxygen administered beneath eye drape |
| Q19 | - |  |  | SI | Pulse oximetry in situ and recordings normal for p... |
| Q2 | - |  |  | SI | Temperature minimum 36 degrees Celsius on arrival |
| Q20 | - |  |  | SI | Blood pressure recorded prior to procedure commenc... |
| Q21 | - |  |  | SI | Skin preparation used (if applicable) |
| Q22 | - |  |  | SI | Eye drape in use |
| Q23 | - |  |  | SI | Irrigation fluid used |
| Q24 | - |  |  | SI | Volume of irrigation fluid used |
| Q25 | - |  |  | SI | Sutures |
| Q26 | - |  |  | SI | Please detail |
| Q27 | - |  |  | SI | Dressing |
| Q28 | - |  |  | SI | If other, please detail |
| Q29 | - |  |  | SI | Additional local anaesthetic required |
| Q3 | - |  |  | SI | Pellet removed |
| Q30 | - |  |  | SI | Please detail |
| Q31 | - |  |  | SI | Phaco machine readings |
| Q32 | - |  |  | SI | Power |
| Q33 | - |  |  | SI | Phaco time |
| Q34 | - |  |  | SI | Lens implant details |
| Q35 | - |  |  | SI | Lens type |
| Q36 | - |  |  | SI | Dioptre |
| Q37 | - |  |  | SI | Detail additional intraoperative medications given |
| Q38 | - |  |  | SI | Bipolar diathermy used |
| Q39 | - |  |  | SI | Post Procedure Care |
| Q4 | - |  |  | SI | Type of anaesthetic |
| Q40 | - |  |  | SI | Post procedure - where possible the patients press... |
| Q41 | - |  |  | SI | If yes, please detail on relevant assessments |
| Q42 | - |  |  | SI | Item count completed and correct |
| Q43 | - |  |  | SI | Perioperative sign off completed |
| Q44 | - |  |  | SI | Post operative observations stable compared to bas... |
| Q45 | - |  |  | SI | Additional comments |
| Q46 | - |  |  | SI | Patient transferred to recovery |
| Q47 | - |  |  | SI | Handover given to ongoing care provider |
| Q48 | - |  |  | SI | Theatre practitioner |
| Q49 | - |  |  | SI | Recovery / ward nurse |
| Q5 | - |  |  | SI | Eye drops administered as prescribed |
| Q50 | - |  |  | SI | Date |
| Q51 | - |  |  | SI | Time |
| Q6 | - |  |  | SI | Right eye (please detail) |
| Q7 | - |  |  | SI | Left eye (please detail) |
| Q8 | - |  |  | SI | Eye area cleaned as per protocol |
| Q9 | - |  |  | SI | Additional comments |
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