# SQLUser.PAC_ReferralEligibilityRule

**Schema:** SQLUser
**Columnas:** 70
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| REFELIGRL_RowId | bigint | PK |  | NO | - |
| Q1 | - |  |  | SI | Date |
| Q10 | - |  |  | SI | Leukocytosis &gt |
| Q11 | - |  |  | SI | Neutrophilia (absolute neutrophil count &gt |
| Q12 | - |  |  | SI | Provenance |
| Q13 | - |  |  | SI | Samuel M. Pediatric appendicitis score. J Pediatr ... |
| Q14 | - |  |  | SI | Goldman RD, Carter S, Stephens D, Antoon R, Mounst... |
| Q15 | - |  |  | SI | The Paediatric Appendicitis Score is a diagnostic ... |
| Q2 | - |  |  | SI | Time |
| Q3 | - |  |  | SI | Sign / Symptom |
| Q4 | - |  |  | SI | Nausea / vomiting |
| Q5 | - |  |  | SI | Anorexia |
| Q6 | - |  |  | SI | Migration of pain to right lower quaderant (RLQ) |
| Q7 | - |  |  | SI | Temperature >38 °C (100.4 °F) |
| Q8 | - |  |  | SI | Right lower quadrant pain with coughing / hopping ... |
| Q9 | - |  |  | SI | Right lower quadrant tenderness to palpation |
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
| REFELIGRL_Code | varchar |  |  | NO | Code |
| REFELIGRL_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| REFELIGRL_CreatedDate | date |  |  | SI | Created Date |
| REFELIGRL_CreatedTime | time |  |  | SI | Created Time |
| REFELIGRL_CreatedUser_DR | bigint |  | FK | SI | Created User |
| REFELIGRL_DateFrom | date |  |  | SI | Date From |
| REFELIGRL_DateTo | date |  |  | SI | Date To |
| REFELIGRL_Desc | varchar |  |  | NO | Description |
| REFELIGRL_NationalCode | varchar |  |  | SI | National Code |
| REFELIGRL_Owner | varchar |  |  | SI | Owner |
| REFELIGRL_Subregion_DR | bigint |  | FK | SI | Subregion |
| REFELIGRL_UpdatedDate | date |  |  | SI | Updated Date |
| REFELIGRL_UpdatedTime | time |  |  | SI | Updated Time |
| REFELIGRL_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*