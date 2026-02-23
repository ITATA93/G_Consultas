# SQLUser.LBC_DiffCounter

**Schema:** SQLUser
**Columnas:** 97
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Laboratorio**. Parámetros del módulo de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCDC_RowID | bigint | PK |  | NO | - |
| LBCDC_Code | varchar |  |  | NO | Code	 |
| LBCDC_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LBCDC_CreatedDate | date |  |  | SI | Created Date |
| LBCDC_CreatedTime | time |  |  | SI | Created Time |
| LBCDC_CreatedUser_DR | bigint |  | FK | SI | Created User |
| LBCDC_DateFrom | date |  |  | SI | Effective date for the record |
| LBCDC_DateTo | date |  |  | SI | Last day the record is active  |
| LBCDC_Desc | varchar |  |  | NO | Description  |
| LBCDC_Mode | varchar |  |  | SI | Counter Type
Standard type (LabCounterMode) to in... |
| LBCDC_Owner | varchar |  |  | SI | Owner |
| LBCDC_Queue_DR | bigint |  | FK | SI | Assign to Queue
The Validation Queue that would b... |
| LBCDC_RequestTestSet_DR | bigint |  | FK | SI | Request Test Set
A single test set that would be ... |
| LBCDC_SecurityGroups | varchar |  |  | SI | Security Groups
A list of security groups can use... |
| LBCDC_SpeciesBreed_DR | varchar |  | FK | SI | Species Breed |
| LBCDC_Species_DR | bigint |  | FK | SI | Species |
| LBCDC_SubjectType_DR | bigint |  | FK | SI | Subject Type |
| LBCDC_TriggerTestSets | varchar |  |  | SI | Trigger Test Sets
A list of Test Sets trigger the... |
| LBCDC_UpdatedDate | date |  |  | SI | Updated Date |
| LBCDC_UpdatedTime | time |  |  | SI | Updated Time |
| LBCDC_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Heart |
| Q04 | - |  |  | SI | Vascular |
| Q05 | - |  |  | SI | Haematopoietic |
| Q06 | - |  |  | SI | Respiratory |
| Q07 | - |  |  | SI | Eyes, ears, nose, throat, and larynx |
| Q08 | - |  |  | SI | Upper gastrointestinal |
| Q09 | - |  |  | SI | Lower gastrointestinal |
| Q10 | - |  |  | SI | Liver |
| Q11 | - |  |  | SI | Renal |
| Q12 | - |  |  | SI | Genitourinary |
| Q13 | - |  |  | SI | Musculoskeletal or integument |
| Q14 | - |  |  | SI | Neurological |
| Q15 | - |  |  | SI | Endocrine or metabolic, and breast |
| Q16 | - |  |  | SI | Psychiatric illness |
| Q17 | - |  |  | SI | Scoring |
| Q18 | - |  |  | SI | Total Number of Categories Endorsed |
| Q19 | - |  |  | SI | Total Score |
| Q20 | - |  |  | SI | Severity Index: (Total Score / Total Number of Cat... |
| Q21 | - |  |  | SI | Number of Categories at Level 3 Severity |
| Q22 | - |  |  | SI | Number of Categories at Level 4 Severity |
| Q23 | - |  |  | SI | Refer to the scoring to see if patient's total sco... |
| Q24 | - |  |  | SI | Guidelines |
| Q25 | - |  |  | SI | Rating strategy |
| Q26 | - |  |  | SI | 0 - No problem |
| Q27 | - |  |  | SI | 1 - Current mild problem OR past significant probl... |
| Q28 | - |  |  | SI | 2 - Moderate disability or mobility OR requires fi... |
| Q29 | - |  |  | SI | 3 - Severe OR constant significant disability OR u... |
| Q30 | - |  |  | SI | 4 - Extremely severe OR immediate treatment requir... |
| Q31 | - |  |  | SI | Provenance |
| Q32 | - |  |  | SI | Reference |
| Q33 | - |  |  | SI | Miller MD, Paradis CF, Houck PR, Mazumdar S, Stack... |
| Q34 | - |  |  | SI | Psychiatry Res 1992 |
| Q35 | - |  |  | SI | Cumulative Illness Rating Scale-Geriatric (CIRS-G)... |
| Q36 | - |  |  | SI | Refer to the scoring to see if patient's total sco... |
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