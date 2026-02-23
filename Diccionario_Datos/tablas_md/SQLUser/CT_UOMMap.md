# SQLUser.CT_UOMMap

**Schema:** SQLUser
**Columnas:** 262
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTMAP_RowID | bigint | PK |  | NO | - |
| CTMAP_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| CTMAP_CreatedDate | date |  |  | SI | Created Date |
| CTMAP_CreatedTime | time |  |  | SI | Created Time |
| CTMAP_CreatedUser_DR | bigint |  | FK | SI | Created User |
| CTMAP_DateFrom | date |  |  | SI | Date From |
| CTMAP_DateTo | date |  |  | SI | Date To |
| CTMAP_ExternalSystem | varchar |  |  | SI | ExternalSystem |
| CTMAP_FrUOM_DR | bigint |  | FK | SI | Des Ref to CTUOM |
| CTMAP_Owner | varchar |  |  | SI | Owner |
| CTMAP_ToUOM_DR | bigint |  | FK | SI | Des Ref to CTUOM |
| CTMAP_UpdatedDate | date |  |  | SI | Updated Date |
| CTMAP_UpdatedTime | time |  |  | SI | Updated Time |
| CTMAP_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Date and time 1st set of tests completed |
| Q02 | - |  |  | SI | Time 1st set of tests completed |
| Q03 | - |  |  | SI | Date and time 2nd set of tests completed |
| Q04 | - |  |  | SI | Time 2nd set of tests completed |
| Q05 | - |  |  | SI | Preconditions |
| Q06a | - |  |  | SI | Dr A |
| Q06b | - |  |  | SI | Dr A |
| Q06c | - |  |  | SI | Dr A |
| Q06d | - |  |  | SI | Dr A |
| Q06e | - |  |  | SI | Dr A |
| Q07a | - |  |  | SI | Cause of permanent loss of brain function |
| Q07b | - |  |  | SI | Cause of permanent loss of brain function |
| Q08a | - |  |  | SI | Evidence of irreversible brain damage |
| Q08b | - |  |  | SI | Evidence of irreversible brain damage |
| Q09 | - |  |  | SI | Reversible Causes of Coma and Apnoea |
| Q100 | - |  |  | SI | Do the pupils react to light? |
| Q101 | - |  |  | SI | Are there corneal reflexes? |
| Q102 | - |  |  | SI | Are there corneal reflexes? |
| Q103 | - |  |  | SI | Reflex response to pain in the trigeminal distribu... |
| Q104 | - |  |  | SI | Reflex response to pain in the trigeminal distribu... |
| Q105 | - |  |  | SI | Is there a gag reflex? |
| Q106 | - |  |  | SI | Is there a gag reflex? |
| Q107 | - |  |  | SI | Is there a cough (tracheal) reflex? |
| Q108 | - |  |  | SI | Is there a cough (tracheal) reflex? |
| Q109 | - |  |  | SI | Is there eye movement on caloric testing? |
| Q10a | - |  |  | SI | Dr B |
| Q10b | - |  |  | SI | Dr B |
| Q10c | - |  |  | SI | Dr B |
| Q10d | - |  |  | SI | Dr B |
| Q10e | - |  |  | SI | Dr B |
| Q110 | - |  |  | SI | Is there eye movement on caloric testing? |
| Q111 | - |  |  | SI | Have the recommendations concerning apnoea testing... |
| Q112 | - |  |  | SI | Have the recommendations concerning apnoea testing... |
| Q113 | - |  |  | SI | Pre test PaCO2 (kPa) |
| Q114 | - |  |  | SI | Pre test PaCO2 (kPa) |
| Q115 | - |  |  | SI | Pre test pH |
| Q116 | - |  |  | SI | Pre test pH |
| Q117 | - |  |  | SI | Post test PaCO2 (kPa) |
| Q118 | - |  |  | SI | Post test PaCO2 (kPa) |
| Q119 | - |  |  | SI | Post test pH |
| Q11a | - |  |  | SI | Depressant or sedative drugs? |
| Q11b | - |  |  | SI | Depressant or sedative drugs? |
| Q120 | - |  |  | SI | Post test pH |
| Q121 | - |  |  | SI | Were there any respiratory movements seen? |
| Q122 | - |  |  | SI | Were there any respiratory movements seen? |
| Q123 | - |  |  | SI | Is there cerebral perfusion? |
| Q124 | - |  |  | SI | Are you satisfied that death has been confirmed du... |
| Q125 | - |  |  | SI | Ancillary investigation or variance from recommend... |
| Q126 | - |  |  | SI | Dr Name |
| Q127 | - |  |  | SI | Grade |
| Q128 | - |  |  | SI | Dr Registration Number |
| Q129 | - |  |  | SI | Do the pupils react to light? |
| Q12a | - |  |  | SI | Hypothermia |
| Q12b | - |  |  | SI | Hypothermia |
| Q130 | - |  |  | SI | Are there corneal reflexes? |
| Q131 | - |  |  | SI | Reflex response to pain in the trigeminal distribu... |
| Q132 | - |  |  | SI | Is there a gag reflex? |
| Q133 | - |  |  | SI | Is there a cough (tracheal) reflex? |
| Q134 | - |  |  | SI | Is there eye movement on caloric testing? |
| Q135 | - |  |  | SI | Have the recommendations concerning apnoea testing... |
| Q136 | - |  |  | SI | Pre test PaCO2 (kPa) |
| Q137 | - |  |  | SI | Pre test pH |
| Q138 | - |  |  | SI | Post test PaCO2 (kPa) |
| Q139 | - |  |  | SI | Post test pH |
| Q13a | - |  |  | SI | Metabolic / Endocrine disturbance |
| Q13b | - |  |  | SI | Metabolic / Endocrine disturbance |
| Q140 | - |  |  | SI | Were there any respiratory movements seen? |
| Q141 | - |  |  | SI | Date and time of death is the time of the end of t... |
| Q14a | - |  |  | SI | Apnoea due to neuromuscular blocking agents, other... |
| Q14b | - |  |  | SI | Apnoea due to neuromuscular blocking agents, other... |
| Q15 | - |  |  | SI | Test for Absence of Brain Stem Reflexes |
| Q16a | - |  |  | SI | Test 1 |
| Q16b | - |  |  | SI | Test 1 |
| Q16c | - |  |  | SI | Test 1 |
| Q16d | - |  |  | SI | Test 1 |
| Q17a | - |  |  | SI | Test 2 |
| Q17b | - |  |  | SI | Test 2 |
| Q17c | - |  |  | SI | Test 2 |
| Q17d | - |  |  | SI | Test 2 |
| Q18a | - |  |  | SI | Do the pupils react to light? |
| Q18b | - |  |  | SI | Do the pupils react to light? |
| Q18c | - |  |  | SI | Do the pupils react to light? |
| Q18d | - |  |  | SI | Do the pupils react to light? |
| Q19a | - |  |  | SI | Are there corneal reflexes? |
| Q19b | - |  |  | SI | Are there corneal reflexes? |
| Q19c | - |  |  | SI | Are there corneal reflexes? |
| Q19d | - |  |  | SI | Are there corneal reflexes? |
| Q20a | - |  |  | SI | Reflex response to pain in the trigeminal distribu... |
| Q20b | - |  |  | SI | Reflex response to pain in the trigeminal distribu... |
| Q20c | - |  |  | SI | Reflex response to pain in the trigeminal distribu... |
| Q20d | - |  |  | SI | Reflex response to pain in the trigeminal distribu... |
| Q21a | - |  |  | SI | Is there a cough (tracheal) reflex? |
| Q21b | - |  |  | SI | Is there a cough (tracheal) reflex? |
| Q21c | - |  |  | SI | Is there a cough (tracheal) reflex? |
| Q21d | - |  |  | SI | Is there a cough (tracheal) reflex? |
| Q22a | - |  |  | SI | Is there eye movement on caloric testing? |
| Q22b | - |  |  | SI | Is there eye movement on caloric testing? |
| Q22c | - |  |  | SI | Is there eye movement on caloric testing? |
| Q22d | - |  |  | SI | Is there eye movement on caloric testing? |
| Q23 | - |  |  | SI | Apnoea Test |
| Q24a | - |  |  | SI | Have the recommendations concerning apnoea testing... |
| Q24b | - |  |  | SI | Have the recommendations concerning apnoea testing... |
| Q24c | - |  |  | SI | Have the recommendations concerning apnoea testing... |
| Q24d | - |  |  | SI | Have the recommendations concerning apnoea testing... |
| Q25a | - |  |  | SI | Pre test PaCO2 (kPa) |
| Q25b | - |  |  | SI | Pre test PaCO2 (kPa) |
| Q25c | - |  |  | SI | Pre test PaCO2 (kPa) |
| Q25d | - |  |  | SI | Pre test PaCO2 (kPa) |
| Q26a | - |  |  | SI | Post test PaCO2 (kPa) |
| Q26b | - |  |  | SI | Post test PaCO2 (kPa) |
| Q26c | - |  |  | SI | Post test PaCO2 (kPa) |
| Q26d | - |  |  | SI | Post test PaCO2 (kPa) |
| Q27a | - |  |  | SI | Pre test pH |
| Q27b | - |  |  | SI | Pre test pH |
| Q27c | - |  |  | SI | Pre test pH |
| Q27d | - |  |  | SI | Pre test pH |
| Q28a | - |  |  | SI | Post test pH |
| Q28b | - |  |  | SI | Post test pH |
| Q28c | - |  |  | SI | Post test pH |
| Q28d | - |  |  | SI | Post test pH |
| Q29a | - |  |  | SI | Were there any respiratory movements seen? |
| Q29b | - |  |  | SI | Were there any respiratory movements seen? |
| Q29c | - |  |  | SI | Were there any respiratory movements seen? |
| Q29d | - |  |  | SI | Were there any respiratory movements seen? |
| Q30 | - |  |  | SI | Outcome |
| Q31a | - |  |  | SI | Are you satisfied that death has been confirmed du... |
| Q31b | - |  |  | SI | Are you satisfied that death has been confirmed du... |
| Q32a | - |  |  | SI | Ancillary investigation or variance from recommend... |
| Q32b | - |  |  | SI | Ancillary investigation or variance from recommend... |
| Q33a | - |  |  | SI | Dr Name |
| Q33b | - |  |  | SI | Dr Name |
| Q34a | - |  |  | SI | Grade |
| Q34b | - |  |  | SI | Grade |
| Q36a | - |  |  | SI | Dr Registration Number |
| Q36b | - |  |  | SI | Dr Registration Number |
| Q37a | - |  |  | SI | Is there a gag reflex? |
| Q37b | - |  |  | SI | Is there a gag reflex? |
| Q37c | - |  |  | SI | Is there a gag reflex? |
| Q37d | - |  |  | SI | Is there a gag reflex? |
| Q40a | - |  |  | SI | Neuromuscular function is intact |
| Q40b | - |  |  | SI | Neuromuscular function is intact |
| Q41a | - |  |  | SI | It is possible to examine the brain-stem reflexes ... |
| Q41b | - |  |  | SI | It is possible to examine the brain-stem reflexes ... |
| Q42a | - |  |  | SI | It is possible to perform apnoea testing |
| Q42b | - |  |  | SI | It is possible to perform apnoea testing |
| Q43a | - |  |  | SI | Specify temperature (°C) |
| Q43b | - |  |  | SI | Specify temperature (°C) |
| Q44a | - |  |  | SI | Hypotension |
| Q44b | - |  |  | SI | Hypotension |
| Q45a | - |  |  | SI | Neuromuscular blocking agents |
| Q45b | - |  |  | SI | Neuromuscular blocking agents |
| Q46a | - |  |  | SI | Other reversible causes |
| Q46b | - |  |  | SI | Other reversible causes |
| Q47a | - |  |  | SI | Other reversible cause details |
| Q47b | - |  |  | SI | Other reversible cause details |
| Q49 | - |  |  | SI | Dr A |
| Q50 | - |  |  | SI | Dr B |
| Q51a | - |  |  | SI | Date and time of pre test observation period |
| Q51b | - |  |  | SI | Date and time of pre test observation period |
| Q52a | - |  |  | SI | Time of pre test observation period |
| Q52b | - |  |  | SI | Time of pre test observation period |
| Q53a | - |  |  | SI | Date and time of pre test observation period |
| Q53b | - |  |  | SI | Date and time 1st set of tests completed |
| Q54a | - |  |  | SI | Time of pre test observation period |
| Q54b | - |  |  | SI | Time 1st set of tests completed |
| Q55b | - |  |  | SI | Date and time of pre test observation period |
| Q56b | - |  |  | SI | Time of pre test observation period |
| Q57 | - |  |  | SI | Date and time 2nd set of tests completed |
| Q58 | - |  |  | SI | Time 2nd set of tests completed |
| Q61 | - |  |  | SI | Prior to the brain perfusion study, the patient ha... |
| Q62 | - |  |  | SI | Imaging modality used to confirm cerebral perfusio... |
| Q63 | - |  |  | SI | Other imaging modality |
| Q64 | - |  |  | SI | Dr A |
| Q65 | - |  |  | SI | Dr B |
| Q66a | - |  |  | SI | Is there cerebral perfusion? |
| Q66b | - |  |  | SI | Is there cerebral perfusion? |
| Q68 | - |  |  | SI | Prior to neurological determination of death ensur... |
| Q69 | - |  |  | SI | tracheal reflex and apparent apnoea on a ventilato... |
| Q70 | - |  |  | SI | When the cause of brain injury is hypoxia-ischaemi... |
| Q71 | - |  |  | SI | following rewarming to 35°C after >6 hours of hypo... |
| Q72 | - |  |  | SI | Date and time of death is the time of the end of t... |
| Q73 | - |  |  | SI | Date |
| Q74 | - |  |  | SI | Time |
| Q75 | - |  |  | SI | Dummy 1 |
| Q76 | - |  |  | SI | Dummy 2 |
| Q77 | - |  |  | SI | Dummy 3 |
| Q78 | - |  |  | SI | Cause of permanent loss of brain function |
| Q79 | - |  |  | SI | Evidence of irreversible brain damage |
| Q80 | - |  |  | SI | Neuromuscular function is intact |
| Q81 | - |  |  | SI | It is possible to examine the brain-stem reflexes ... |
| Q82 | - |  |  | SI | It is possible to perform apnoea testing |
| Q83 | - |  |  | SI | Depressant or sedative drugs |
| Q84 | - |  |  | SI | Hypothermia |
| Q85 | - |  |  | SI | Specify temperature (°C) |
| Q86 | - |  |  | SI | Hypotension |
| Q87 | - |  |  | SI | Metabolic / Endocrine disturbance |
| Q88 | - |  |  | SI | Neuromuscular blocking agents |
| Q89 | - |  |  | SI | Other reversible causes |
| Q90 | - |  |  | SI | Other reversible cause details |
| Q91 | - |  |  | SI | Date and time of pre test observation period |
| Q92 | - |  |  | SI | Time of pre test observation period |
| Q93 | - |  |  | SI | Date and time 1st set of tests completed |
| Q94 | - |  |  | SI | Date and time 1st set of tests completed |
| Q95 | - |  |  | SI | Date and time of pre test observation period |
| Q96 | - |  |  | SI | Time of pre test observation period |
| Q97 | - |  |  | SI | Date and time 2nd set of tests completed |
| Q98 | - |  |  | SI | Time 2nd set of tests completed |
| Q99 | - |  |  | SI | Do the pupils react to light? |
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