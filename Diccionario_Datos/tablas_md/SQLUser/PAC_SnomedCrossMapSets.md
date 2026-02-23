# SQLUser.PAC_SnomedCrossMapSets

**Schema:** SQLUser
**Columnas:** 99
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SNOCMS_RowId | bigint | PK |  | NO | - |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Has the child unintentionally lost weight lately? |
| Q04 | - |  |  | SI | Has the child had poor weight gain over the last f... |
| Q05 | - |  |  | SI | Has the child been eating / feeding less in the la... |
| Q06 | - |  |  | SI | Is the child obviously underweight? |
| Q07 | - |  |  | SI | The Paediatric Nutrition Screening Tool is intende... |
| Q08 | - |  |  | SI | Complete the questions by obtaining information fr... |
| Q09 | - |  |  | SI | 1. Has the child unintentionally lost weight latel... |
| Q10 | - |  |  | SI | This question identifies if the child has lost wei... |
| Q11 | - |  |  | SI | There are many causes of weight loss that require ... |
| Q12 | - |  |  | SI | ‘Lately’ can be over a time period of six months o... |
| Q13 | - |  |  | SI | If there is no weight history, a subjective assess... |
| Q14 | - |  |  | SI | 2. Has the child had poor weight gain over the las... |
| Q15 | - |  |  | SI | The rate of weight gain of children depends on the... |
| Q16 | - |  |  | SI | Take into account the child’s age when answering t... |
| Q17 | - |  |  | SI | 3. Has the child been eating / feeding less in the... |
| Q18 | - |  |  | SI | Determine if the child has reduced nutritional int... |
| Q19 | - |  |  | SI | Nutritional intake can be via various routes inclu... |
| Q20 | - |  |  | SI | Reduced nutritional intake can occur as the result... |
| Q21 | - |  |  | SI | 4. Is the child obviously underweight? |
| Q22 | - |  |  | SI | Examine the child for physical indicators of malnu... |
| Q23 | - |  |  | SI | Look for loss of subcutaneous fat stores such as a... |
| Q24 | - |  |  | SI | Protruding or prominent bones of the clavicle and ... |
| Q25 | - |  |  | SI | If ''yes'' to two or more of the above: |
| Q26 | - |  |  | SI | - refer the child for further nutrition assessment |
| Q27 | - |  |  | SI | - check if child is known to a dietitian |
| Q28 | - |  |  | SI | - measure weight and length / height |
| Q29 | - |  |  | SI | - commence food and fluid intake record |
| Q30 | - |  |  | SI | If a child does not require nutrition assessment i... |
| Q31 | - |  |  | SI | Rescreening should include regular weights and mon... |
| Q32 | - |  |  | SI | Rescreening questions can be: |
| Q33 | - |  |  | SI | 1. Has the child unintentionally lost weight since... |
| Q34 | - |  |  | SI | 2. Has the child reduced intake over the past thre... |
| Q35 | - |  |  | SI | Score |
| Q36 | - |  |  | SI | Classification |
| Q37 | - |  |  | SI | 0 - 1 |
| Q38 | - |  |  | SI | Does not meet criteria for further nutritional ass... |
| Q39 | - |  |  | SI | 2 - 4 |
| Q40 | - |  |  | SI | Further nutritional assessment recommended |
| Q41 | - |  |  | SI | 0 - 1: Does not meet criteria for further nutritio... |
| Q42 | - |  |  | SI | 2 - 4: Further nutritional assessment recommended |
| Q43 | - |  |  | SI | The Paediatric Nutrition Screening Tool (PNST) is ... |
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
| SNOCMS_CreatedDate | date |  |  | SI | Created Date |
| SNOCMS_CreatedTime | time |  |  | SI | Created Time |
| SNOCMS_CreatedUser_DR | bigint |  | FK | SI | Created User |
| SNOCMS_MapSetID | varchar |  |  | SI | MapSetID |
| SNOCMS_MapSetName | varchar |  |  | SI | MapSetName |
| SNOCMS_MapSetRealmID | varchar |  |  | SI | MapSetRealmID |
| SNOCMS_MapSetRuleType | varchar |  |  | SI | MapSetRuleType |
| SNOCMS_MapSetSchemeID | varchar |  |  | SI | MapSetSchemeID |
| SNOCMS_MapSetSchemeName | varchar |  |  | SI | MapSetSchemeName |
| SNOCMS_MapSetSchemeVersion | varchar |  |  | SI | MapSetSchemeVersion |
| SNOCMS_MapSetSeparator | varchar |  |  | SI | MapSetSeparator |
| SNOCMS_MapSetType | varchar |  |  | SI | MapSetType |
| SNOCMS_UpdatedDate | date |  |  | SI | Updated Date |
| SNOCMS_UpdatedTime | time |  |  | SI | Updated Time |
| SNOCMS_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*