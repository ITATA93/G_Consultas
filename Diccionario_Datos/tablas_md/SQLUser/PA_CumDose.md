# SQLUser.PA_CumDose

**Schema:** SQLUser
**Columnas:** 82
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CUMD_ParRef | bigint | PK |  | NO | PA_PatMas Parent Reference |
| CUMD_Childsub | double |  |  | NO | Childsub |
| CUMD_Ingredient_DR | bigint |  | FK | SI | Des Ref PHCIngredient |
| CUMD_RowId | varchar |  |  | NO | - |
| CUMD_TotalDose | double |  |  | SI | Total Dose  |
| CUMD_UOM_DR | bigint |  | FK | SI | Des Ref CTUOM |
| Q01 | - |  |  | SI | Test date |
| Q02 | - |  |  | SI | Test time |
| Q03 | - |  |  | SI | A - Sedation Phase |
| Q04 | - |  |  | SI | Injection time |
| Q05 | - |  |  | SI | The expressive language score during counting |
| Q06 | - |  |  | SI | Memory registration |
| Q07 | - |  |  | SI | Token comprehension test score |
| Q08 | - |  |  | SI | Confrontation naming |
| Q09 | - |  |  | SI | Reading |
| Q10 | - |  |  | SI | B - Recovery and Recall Phase (10 min post-injecti... |
| Q11 | - |  |  | SI | If language impairment present, continue to test r... |
| Q12 | - |  |  | SI | Time of recovery |
| Q13 | - |  |  | SI | Demonstrate return of 5/5 power |
| Q14 | - |  |  | SI | Absence of pronator drift |
| Q15 | - |  |  | SI | Demonstrate normal language functions |
| Q16 | - |  |  | SI | Ask for spontaneous recall |
| Q17 | - |  |  | SI | /8 |
| Q18 | - |  |  | SI | Give clues |
| Q19 | - |  |  | SI | Conclusion |
| Q20 | - |  |  | SI | Repetition |
| Q21 | - |  |  | SI | A - Sedation Phase |
| Q22 | - |  |  | SI | The expressive language score during counting |
| Q23 | - |  |  | SI | Memory registration |
| Q24 | - |  |  | SI | Token comprehension test score |
| Q25 | - |  |  | SI | Confrontation Naming |
| Q26 | - |  |  | SI | Repetition |
| Q27 | - |  |  | SI | Reading |
| Q28 | - |  |  | SI | B- Recovery and Recall Phase (10 min post-injectio... |
| Q29 | - |  |  | SI | If language impairment present, continue to test r... |
| Q30 | - |  |  | SI | Time of recovery |
| Q31 | - |  |  | SI | Demonstrate return of 5/5 power |
| Q32 | - |  |  | SI | Absence of pronator drift |
| Q33 | - |  |  | SI | Demonstrate normal language functions |
| Q34 | - |  |  | SI | Ask for spontaneous recall |
| Q35 | - |  |  | SI | /8 |
| Q36 | - |  |  | SI | Give clues |
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