# SQLUser.PAC_WaitingListGroups

**Schema:** SQLUser
**Columnas:** 92
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| WLG_RowId | bigint | PK |  | NO | - |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Discharge Criteria |
| Q04 | - |  |  | SI | Heart rate - within +/- 20% pre-operative value |
| Q05 | - |  |  | SI | Respiratory rate - within +/- 20% pre-operative va... |
| Q06 | - |  |  | SI | Blood pressure - within +/- 20% pre-operative valu... |
| Q07 | - |  |  | SI | Post-op care instructions provided |
| Q08 | - |  |  | SI | Alert and oriented (At pre-anaesthetic level) |
| Q09 | - |  |  | SI | Minimal nausea and tolerating food / oral fluids |
| Q10 | - |  |  | SI | Pain controlled with oral analgesia |
| Q11 | - |  |  | SI | Voided |
| Q12 | - |  |  | SI | Intravenous access removed |
| Q13 | - |  |  | SI | Adult supervision at discharge |
| Q14 | - |  |  | SI | Discharge checklist completed |
| Q15 | - |  |  | SI | Safely mobilising |
| Q16 | - |  |  | SI | Wound - minimal discharge (post op) |
| Q17 | - |  |  | SI | Other (Specify) |
| Q18 | - |  |  | SI | Follow Up |
| Q19 | - |  |  | SI | Follow up method |
| Q20 | - |  |  | SI | Follow up method note |
| Q21 | - |  |  | SI | Patient informed how to re-engage with hospital sy... |
| Q22 | - |  |  | SI | Script sent to pharmacy |
| Q23 | - |  |  | SI | Medications supplied to patient |
| Q24 | - |  |  | SI | Script given to patient for outside pharmacy |
| Q25 | - |  |  | SI | Community health referral |
| Q26 | - |  |  | SI | Discharge summary given to patient |
| Q27 | - |  |  | SI | Medical certificate given to patient and/or carer |
| Q28 | - |  |  | SI | I confirm that all the discharge criteria have bee... |
| Q29 | - |  |  | SI | Reason patient not discharged using criteria led d... |
| Q30 | - |  |  | SI | Other (Specify) |
| Q31 | - |  |  | SI | Guidelines |
| Q32 | - |  |  | SI | How to initiate criteria led discharge (CLD) for a... |
| Q33 | - |  |  | SI | CLD aims to facilitate timely and clinical appropr... |
| Q34 | - |  |  | SI | All patients should be considered for criteria led... |
| Q35 | - |  |  | SI | • Surgical patient criteria led discharge form to ... |
| Q36 | - |  |  | SI | • The surgeon is to document the criteria led disc... |
| Q37 | - |  |  | SI | • If a post-operation review by the surgeon is req... |
| Q38 | - |  |  | SI | • Discharge scripts, discharge summaries, sick cer... |
| Q39 | - |  |  | SI | • Senior nurse to document assessment made for dis... |
| Q40 | - |  |  | SI | Note: If nursing staff are in any doubt they are t... |
| Q41 | - |  |  | SI | Discharge checklist - ensure all are complete prio... |
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
| WLG_Code | varchar |  |  | NO | Code |
| WLG_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| WLG_CreatedDate | date |  |  | SI | Created Date |
| WLG_CreatedTime | time |  |  | SI | Created Time |
| WLG_CreatedUser_DR | bigint |  | FK | SI | Created User |
| WLG_Desc | varchar |  |  | NO | Description |
| WLG_Owner | varchar |  |  | SI | Owner |
| WLG_UpdatedDate | date |  |  | SI | Updated Date |
| WLG_UpdatedTime | time |  |  | SI | Updated Time |
| WLG_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*