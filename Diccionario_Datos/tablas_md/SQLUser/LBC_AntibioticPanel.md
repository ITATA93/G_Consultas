# SQLUser.LBC_AntibioticPanel

**Schema:** SQLUser
**Columnas:** 75
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Laboratorio**. Parámetros del módulo de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCAP_RowID | bigint | PK |  | NO | - |
| LBCAP_Code | varchar |  |  | SI | Code |
| LBCAP_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LBCAP_CreatedDate | date |  |  | SI | Created Date |
| LBCAP_CreatedTime | time |  |  | SI | Created Time |
| LBCAP_CreatedUser_DR | bigint |  | FK | SI | Created User |
| LBCAP_DateFrom | date |  |  | SI | Date From |
| LBCAP_DateTo | date |  |  | SI | Date To |
| LBCAP_Desc | varchar |  |  | SI | Description |
| LBCAP_Owner | varchar |  |  | SI | Owner |
| LBCAP_UpdatedDate | date |  |  | SI | Updated Date |
| LBCAP_UpdatedTime | time |  |  | SI | Updated Time |
| LBCAP_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q1 | - |  |  | SI | Registered nurse to complete |
| Q10 | - |  |  | SI | Metabolic exercise test score indicative of reduce... |
| Q11 | - |  |  | SI | Polypharmacy |
| Q12 | - |  |  | SI | Multiple comorbidities |
| Q13 | - |  |  | SI | Appears frail upon visual assessment |
| Q14 | - |  |  | SI | If yes to any, please complete clinical frailty sc... |
| Q15 | - |  |  | SI | Clinical frailty score |
| Q16 | - |  |  | SI | Scores < 5 - provide advice on how to improve modi... |
| Q17 | - |  |  | SI | Score ≥ 5 - refer to anaesthetist for further revi... |
| Q18 | - |  |  | SI | Has the patient made any legal decisions regarding... |
| Q19 | - |  |  | SI | If yes please detail |
| Q2 | - |  |  | SI | Is the patient safe to be nursed in a single room? |
| Q20 | - |  |  | SI | Additional risk assessments completed (please deta... |
| Q21 | - |  |  | SI | Date |
| Q22 | - |  |  | SI | Time |
| Q3 | - |  |  | SI | If no, please detail |
| Q4 | - |  |  | SI | Does the patient meet any of the following conside... |
| Q5 | - |  |  | SI | Age > 65 yrs |
| Q6 | - |  |  | SI | High risk of falls |
| Q7 | - |  |  | SI | Poor nutritional assessment |
| Q8 | - |  |  | SI | Poor skin integrity / high risk of pressure ulcers |
| Q9 | - |  |  | SI | Displaying signs of declining / reduced cognitive ... |
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