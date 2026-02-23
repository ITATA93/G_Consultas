# SQLUser.PAC_DischClassification

**Schema:** SQLUser
**Columnas:** 86
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DSCL_RowId | bigint | PK |  | NO | - |
| DSCL_Code | varchar |  |  | NO | Code |
| DSCL_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| DSCL_CreatedDate | date |  |  | SI | Created Date |
| DSCL_CreatedTime | time |  |  | SI | Created Time |
| DSCL_CreatedUser_DR | bigint |  | FK | SI | Created User |
| DSCL_DateFrom | date |  |  | SI | Date From |
| DSCL_DateTo | date |  |  | SI | Date To |
| DSCL_Deceased | varchar |  |  | SI | Deceased |
| DSCL_Default | varchar |  |  | SI | Default |
| DSCL_Desc | varchar |  |  | NO | Description |
| DSCL_IconName | varchar |  |  | SI | Icon Name |
| DSCL_IconPriority | varchar |  |  | SI | Icon Priority |
| DSCL_NationalCode | varchar |  |  | SI | NationalCode |
| DSCL_Owner | varchar |  |  | SI | Owner |
| DSCL_UpdatedDate | date |  |  | SI | Updated Date |
| DSCL_UpdatedTime | time |  |  | SI | Updated Time |
| DSCL_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| DSCL_WaitingType | varchar |  |  | SI | Waiting Type |
| Q1 | - |  |  | SI | Date |
| Q10 | - |  |  | SI | Supination: wrist / forearm pathology |
| Q11 | - |  |  | SI | Strength: average of flexion, extension, pronation... |
| Q12 | - |  |  | SI | Ulnar nerve |
| Q13 | - |  |  | SI | Patient answered questions: During the last 4 week... |
| Q14 | - |  |  | SI | How often have you had to use your other arm to do... |
| Q15 | - |  |  | SI | Has your elbow problem caused you any difficulty c... |
| Q16 | - |  |  | SI | Has your elbow problem caused you any difficulty i... |
| Q17 | - |  |  | SI | Has your elbow problem caused you any difficulty i... |
| Q18 | - |  |  | SI | Has your elbow problem caused you any difficulty i... |
| Q19 | - |  |  | SI | Has your elbow problem caused you any difficulty i... |
| Q2 | - |  |  | SI | Time |
| Q20 | - |  |  | SI | Has your elbow problem caused you any difficulty i... |
| Q21 | - |  |  | SI | How would you describe the pain from this elbow? |
| Q22 | - |  |  | SI | Has your elbow problem affected your sport and lei... |
| Q23 | - |  |  | SI | Score |
| Q24 | - |  |  | SI | For calculation of the final score, all responses ... |
| Q25 | - |  |  | SI | The higher the score the best, the lowest the scor... |
| Q26 | - |  |  | SI | The Liverpool Elbow Score was introduced as an elb... |
| Q27 | - |  |  | SI | Score caption |
| Q3 | - |  |  | SI | Sathyamoorthy P, Kemp GJ, Rawal A, Rayner V, Frost... |
| Q4 | - |  |  | SI | Clinical assessment |
| Q5 | - |  |  | SI | Flexion |
| Q6 | - |  |  | SI | Extension |
| Q7 | - |  |  | SI | Pronation |
| Q8 | - |  |  | SI | Pronation: wrist / forearm pathology |
| Q9 | - |  |  | SI | Supination |
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