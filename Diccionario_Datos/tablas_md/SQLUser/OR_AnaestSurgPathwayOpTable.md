# SQLUser.OR_AnaestSurgPathwayOpTable

**Schema:** SQLUser
**Columnas:** 76
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Pabellón Quirúrgico**. Gestión de cirugías.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| OPTAB_ParRef | varchar | PK |  | NO | OR_AnaestSurgPathway Parent Reference |
| OPTAB_Childsub | numeric |  |  | NO | Childsub |
| OPTAB_Equipment_DR | bigint |  | FK | NO |  Des Ref ORC_Equipment |
| OPTAB_RowId | varchar |  |  | NO | - |
| Q1 | - |  |  | SI | Intervention planning checklist |
| Q10 | - |  |  | SI | Glasses / Hearing aids within patients' reach |
| Q11 | - |  |  | SI | Comments |
| Q12 | - |  |  | SI | 2- Pharmacological therapy |
| Q13 | - |  |  | SI | Information given on certain medications' effect o... |
| Q14 | - |  |  | SI | Medical team aware of falls risk related to medica... |
| Q15 | - |  |  | SI | Comments |
| Q16 | - |  |  | SI | 3 - Mobility issues |
| Q17 | - |  |  | SI | Mobilisation plan in place to minimise falls risk |
| Q18 | - |  |  | SI | Mobility aids given - training given |
| Q19 | - |  |  | SI | Patient alerted not to mobilise alone |
| Q2 | - |  |  | SI | Objective: draw attention to specific falls risk a... |
| Q20 | - |  |  | SI | Patient instructed to use call bell |
| Q21 | - |  |  | SI | Patient trained on safe mobility techniques |
| Q22 | - |  |  | SI | Continence aids / Plan in place |
| Q23 | - |  |  | SI | Bed rails / Call bell within reach at night |
| Q24 | - |  |  | SI | Relatives / Caregiver presence or assistance encou... |
| Q25 | - |  |  | SI | Medical team aware of falls risk related to medica... |
| Q26 | - |  |  | SI | Comments |
| Q27 | - |  |  | SI | 4 - Post-operative risk |
| Q28 | - |  |  | SI | Patient / Relative / Caregiver instructed on calli... |
| Q29 | - |  |  | SI | Comments |
| Q3 | - |  |  | SI | Interventions: |
| Q30 | - |  |  | SI | Notes |
| Q31 | - |  |  | SI | Date |
| Q32 | - |  |  | SI | Time |
| Q4 | - |  |  | SI | 1- Cognitive / Sensory status |
| Q5 | - |  |  | SI | Falls prevention measures taken |
| Q6 | - |  |  | SI | Falls prevention measures taken - other |
| Q7 | - |  |  | SI | Patient within sight of the nursing station |
| Q8 | - |  |  | SI | Bed at lowest height |
| Q9 | - |  |  | SI | Relatives / Caregiver presence or assistance encou... |
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