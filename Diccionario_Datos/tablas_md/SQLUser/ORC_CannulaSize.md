# SQLUser.ORC_CannulaSize

**Schema:** SQLUser
**Columnas:** 147
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Órdenes**. Parámetros de órdenes médicas.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CANSIZ_RowId | bigint | PK |  | NO | - |
| CANSIZ_Code | varchar |  |  | NO | Code |
| CANSIZ_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| CANSIZ_CreatedDate | date |  |  | SI | Created Date |
| CANSIZ_CreatedTime | time |  |  | SI | Created Time |
| CANSIZ_CreatedUser_DR | bigint |  | FK | SI | Created User |
| CANSIZ_DateFrom | date |  |  | SI | Date From |
| CANSIZ_DateTo | date |  |  | SI | Date To |
| CANSIZ_Desc | varchar |  |  | NO | Description |
| CANSIZ_Owner | varchar |  |  | SI | Owner |
| CANSIZ_UpdatedDate | date |  |  | SI | Updated Date |
| CANSIZ_UpdatedTime | time |  |  | SI | Updated Time |
| CANSIZ_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Testing and Confirmation of Brain Stem Death |
| Q02 | - |  |  | SI | Date and Time of 1st set of tests |
| Q03 | - |  |  | SI | Time 1st set |
| Q04 | - |  |  | SI | Date and Time of 2nd set of tests |
| Q05 | - |  |  | SI | Time 2nd set |
| Q06 | - |  |  | SI | Pre-conditions |
| Q07 | - |  |  | SI | Dr A |
| Q07a | - |  |  | SI | Dr A |
| Q07b | - |  |  | SI | Dr A |
| Q07c | - |  |  | SI | Dr A |
| Q07d | - |  |  | SI | Dr A |
| Q08 | - |  |  | SI | Dr B |
| Q08a | - |  |  | SI | Dr B |
| Q08b | - |  |  | SI | Dr B |
| Q08c | - |  |  | SI | Dr B |
| Q08d | - |  |  | SI | Dr B |
| Q09 | - |  |  | SI | Primary Diagnosis |
| Q09a | - |  |  | SI | Primary Diagnosis |
| Q10 | - |  |  | SI | Evidence of irreversible brain damage |
| Q10a | - |  |  | SI | Evidence of irreversible brain damage |
| Q11 | - |  |  | SI | Exclusion of reversible causes of coma and apnoea |
| Q12 | - |  |  | SI | Coma due to depressant drugs? |
| Q12a | - |  |  | SI | Coma due to depressant drugs? |
| Q13 | - |  |  | SI | Body temperature 34 degrees centigrade or less? |
| Q13a | - |  |  | SI | Body temperature 34 degrees centigrade or less? |
| Q14 | - |  |  | SI | Coma due to circulatory, metabolic or endocrine di... |
| Q14a | - |  |  | SI | Coma due to circulatory, metabolic or endocrine di... |
| Q15 | - |  |  | SI | Apnoea due to neuromuscular blocking agents, other... |
| Q15a | - |  |  | SI | Apnoea due to neuromuscular blocking agents, other... |
| Q16 | - |  |  | SI | Tests for absence of brain stem reflexes |
| Q17a | - |  |  | SI | Test 1 |
| Q17b | - |  |  | SI | Test 1 |
| Q17c | - |  |  | SI | Test 1 |
| Q17d | - |  |  | SI | Test 1 |
| Q18a | - |  |  | SI | Test 2 |
| Q18b | - |  |  | SI | Test 2 |
| Q18c | - |  |  | SI | Test 2 |
| Q18d | - |  |  | SI | Test 2 |
| Q19a | - |  |  | SI | Do the pupils react to light? |
| Q19b | - |  |  | SI | Do the pupils react to light? |
| Q19c | - |  |  | SI | Do the pupils react to light? |
| Q19d | - |  |  | SI | Do the pupils react to light? |
| Q20a | - |  |  | SI | Are there corneal reflexes? |
| Q20b | - |  |  | SI | Are there corneal reflexes? |
| Q20c | - |  |  | SI | Are there corneal reflexes? |
| Q20d | - |  |  | SI | Are there corneal reflexes? |
| Q21a | - |  |  | SI | Is there movement on application of supraorbital p... |
| Q21b | - |  |  | SI | Is there movement on application of supraorbital p... |
| Q21c | - |  |  | SI | Is there movement on application of supraorbital p... |
| Q21d | - |  |  | SI | Is there movement on application of supraorbital p... |
| Q22a | - |  |  | SI | Is there a cough reflex? |
| Q22b | - |  |  | SI | Is there a cough reflex? |
| Q22c | - |  |  | SI | Is there a cough reflex? |
| Q22d | - |  |  | SI | Is there a cough reflex? |
| Q23a | - |  |  | SI | Is there eye movement on caloric testing? |
| Q23b | - |  |  | SI | Is there eye movement on caloric testing? |
| Q23c | - |  |  | SI | Is there eye movement on caloric testing? |
| Q23d | - |  |  | SI | Is there eye movement on caloric testing? |
| Q24 | - |  |  | SI | Apnoea Test |
| Q25a | - |  |  | SI | Have the recommendations concerning apnoea testing... |
| Q25b | - |  |  | SI | Have the recommendations concerning apnoea testing... |
| Q25c | - |  |  | SI | Have the recommendations concerning apnoea testing... |
| Q25d | - |  |  | SI | Have the recommendations concerning apnoea testing... |
| Q26a | - |  |  | SI | Pre test PaCO2 (kPa) |
| Q26b | - |  |  | SI | Pre test PaCO2 (kPa) |
| Q26c | - |  |  | SI | Pre test PaCO2 (kPa) |
| Q26d | - |  |  | SI | Pre test PaCO2 (kPa) |
| Q27a | - |  |  | SI | Post test PaCO2 (kPa) |
| Q27b | - |  |  | SI | Post test PaCO2 (kPa) |
| Q27c | - |  |  | SI | Post test PaCO2 (kPa) |
| Q27d | - |  |  | SI | Post test PaCO2 (kPa) |
| Q28a | - |  |  | SI | Post test pH |
| Q28b | - |  |  | SI | Post test pH |
| Q28c | - |  |  | SI | Post test pH |
| Q28d | - |  |  | SI | Post test pH |
| Q29a | - |  |  | SI | Pre test pH |
| Q29b | - |  |  | SI | Pre test pH |
| Q29c | - |  |  | SI | Pre test pH |
| Q29d | - |  |  | SI | Pre test pH |
| Q30a | - |  |  | SI | Were there any respiratory movements seen? |
| Q30b | - |  |  | SI | Were there any respiratory movements seen? |
| Q30c | - |  |  | SI | Were there any respiratory movements seen? |
| Q30d | - |  |  | SI | Were there any respiratory movements seen? |
| Q31 | - |  |  | SI | Completion of diagnosis |
| Q32a | - |  |  | SI | Are you satisfied that death has been confirmed du... |
| Q32b | - |  |  | SI | Are you satisfied that death has been confirmed du... |
| Q33a | - |  |  | SI | Ancillary investigations or variance from recommen... |
| Q33b | - |  |  | SI | Ancillary investigations or variance from recommen... |
| Q34a | - |  |  | SI | Dr Name |
| Q34b | - |  |  | SI | Dr Name |
| Q35a | - |  |  | SI | Grade |
| Q35b | - |  |  | SI | Grade |
| Q37a | - |  |  | SI | Dr Registration Number |
| Q37b | - |  |  | SI | Dr Registration Number |
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