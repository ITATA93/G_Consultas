# questionnaire.QTCPNST

> Paediatric Nutrition Screening Tool

**Schema:** questionnaire
**Columnas:** 84
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Paediatric Nutrition Screening Tool

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | Has the child unintentionally lost weight lately? |
| Q04 | varchar |  |  | SI | Has the child had poor weight gain over the last f... |
| Q05 | varchar |  |  | SI | Has the child been eating / feeding less in the la... |
| Q06 | varchar |  |  | SI | Is the child obviously underweight? |
| Q07 | varchar |  |  | SI | The Paediatric Nutrition Screening Tool is intende... |
| Q08 | varchar |  |  | SI | Complete the questions by obtaining information fr... |
| Q09 | varchar |  |  | SI | 1. Has the child unintentionally lost weight latel... |
| Q10 | varchar |  |  | SI | This question identifies if the child has lost wei... |
| Q11 | varchar |  |  | SI | There are many causes of weight loss that require ... |
| Q12 | varchar |  |  | SI | ‘Lately’ can be over a time period of six months o... |
| Q13 | varchar |  |  | SI | If there is no weight history, a subjective assess... |
| Q14 | varchar |  |  | SI | 2. Has the child had poor weight gain over the las... |
| Q15 | varchar |  |  | SI | The rate of weight gain of children depends on the... |
| Q16 | varchar |  |  | SI | Take into account the child’s age when answering t... |
| Q17 | varchar |  |  | SI | 3. Has the child been eating / feeding less in the... |
| Q18 | varchar |  |  | SI | Determine if the child has reduced nutritional int... |
| Q19 | varchar |  |  | SI | Nutritional intake can be via various routes inclu... |
| Q20 | varchar |  |  | SI | Reduced nutritional intake can occur as the result... |
| Q21 | varchar |  |  | SI | 4. Is the child obviously underweight? |
| Q22 | varchar |  |  | SI | Examine the child for physical indicators of malnu... |
| Q23 | varchar |  |  | SI | Look for loss of subcutaneous fat stores such as a... |
| Q24 | varchar |  |  | SI | Protruding or prominent bones of the clavicle and ... |
| Q25 | varchar |  |  | SI | If ''yes'' to two or more of the above: |
| Q26 | varchar |  |  | SI | - refer the child for further nutrition assessment |
| Q27 | varchar |  |  | SI | - check if child is known to a dietitian |
| Q28 | varchar |  |  | SI | - measure weight and length / height |
| Q29 | varchar |  |  | SI | - commence food and fluid intake record |
| Q30 | varchar |  |  | SI | If a child does not require nutrition assessment i... |
| Q31 | varchar |  |  | SI | Rescreening should include regular weights and mon... |
| Q32 | varchar |  |  | SI | Rescreening questions can be: |
| Q33 | varchar |  |  | SI | 1. Has the child unintentionally lost weight since... |
| Q34 | varchar |  |  | SI | 2. Has the child reduced intake over the past thre... |
| Q35 | varchar |  |  | SI | Score |
| Q36 | varchar |  |  | SI | Classification |
| Q37 | varchar |  |  | SI | 0 - 1 |
| Q38 | varchar |  |  | SI | Does not meet criteria for further nutritional ass... |
| Q39 | varchar |  |  | SI | 2 - 4 |
| Q40 | varchar |  |  | SI | Further nutritional assessment recommended |
| Q41 | varchar |  |  | SI | 0 - 1: Does not meet criteria for further nutritio... |
| Q42 | varchar |  |  | SI | 2 - 4: Further nutritional assessment recommended |
| Q43 | varchar |  |  | SI | The Paediatric Nutrition Screening Tool (PNST) is ... |
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