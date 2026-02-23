# SQLUser.IN_IsTrfItm

**Schema:** SQLUser
**Columnas:** 161
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Incidentes**. Registro de eventos adversos.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| INITI_INIT_ParRef | bigint | PK |  | NO | INIT Par Ref |
| INITI_AckQty | double |  |  | SI | Acknowledge Quantity |
| INITI_CTUOM_DR | bigint |  | FK | NO | Des Ref to UOM |
| INITI_ChildSub | numeric |  |  | NO | INITI ChildSub (NewKey) |
| INITI_DateAcknow | date |  |  | SI | Date Acknowledged |
| INITI_INCLB_DR | varchar |  | FK | NO | Des Ref to INCLB |
| INITI_INRQI_DR | varchar |  | FK | SI | Des Ref to INRQI |
| INITI_Qty | double |  |  | NO | Transfer/Issue Quantity |
| INITI_ReasonAckLess_DR | bigint |  | FK | SI | Des Ref ReasonAckLess |
| INITI_RequestCreated | varchar |  |  | SI | Request Created For This Item |
| INITI_ReturnDate | date |  |  | SI | Date to be Returned (Loan Items) |
| INITI_RowId | varchar |  |  | NO | - |
| INITI_ScanFlag | varchar |  |  | SI | Scan Flag |
| INITI_SupplyLocStorageBin_DR | varchar |  | FK | SI | Des Ref CTLocStorageBin |
| INITI_TimeAcknow | time |  |  | SI | Time Acknowledged |
| INITI_ToLoc_DR | bigint |  | FK | SI | Des Ref to CTLOC |
| INITI_TransferToStorageBin_DR | varchar |  | FK | SI | Des Ref CTLocStorageBin |
| INITI_Type | varchar |  |  | NO | Transfer Type |
| INITI_UCost | double |  |  | SI | Transfer/Issue Unit Cost |
| INITI_UserAck_DR | bigint |  | FK | SI | Des REf UserAck_DR |
| Q01 | - |  |  | SI | Date of Assessment |
| Q02 | - |  |  | SI | Speech Pathologist |
| Q03 | - |  |  | SI | Three Identifiers Checked |
| Q04 | - |  |  | SI | Referral Trigger |
| Q05 | - |  |  | SI | A) Receptive Language |
| Q06 | - |  |  | SI | Following Commands |
| Q07 | - |  |  | SI | 1 Stage |
| Q08 | - |  |  | SI | 1 Stage |
| Q09 | - |  |  | SI | 2 Stage |
| Q10 | - |  |  | SI | 2 Stage |
| Q100 | - |  |  | SI | /4 |
| Q101 | - |  |  | SI | /1 |
| Q11 | - |  |  | SI | 3 Stage |
| Q12 | - |  |  | SI | 3 Stage |
| Q13 | - |  |  | SI | Comparatives |
| Q14 | - |  |  | SI | Comparative Relationships |
| Q15 | - |  |  | SI | Comparative Relationships (Notes) |
| Q16 | - |  |  | SI | Complex Grammar |
| Q17 | - |  |  | SI | Sentence Level Comprehension |
| Q18 | - |  |  | SI | Sentence Level Comprehension (Notes) |
| Q19 | - |  |  | SI | B) Expressive Language |
| Q20 | - |  |  | SI | Naming |
| Q21 | - |  |  | SI | Naming Objects |
| Q22 | - |  |  | SI | Naming Objects |
| Q23 | - |  |  | SI | Naming Pictures |
| Q24 | - |  |  | SI | Naming Pictures |
| Q25 | - |  |  | SI | Providing Factual Information |
| Q26 | - |  |  | SI | Name |
| Q27 | - |  |  | SI | Address |
| Q28 | - |  |  | SI | General Statement (eg weather) |
| Q29 | - |  |  | SI | Verbal Reasoning |
| Q30 | - |  |  | SI | Using Narrative |
| Q31 | - |  |  | SI | Sequencing |
| Q32 | - |  |  | SI | Sentence Structure |
| Q33 | - |  |  | SI | Content |
| Q34 | - |  |  | SI | C) Reading |
| Q35 | - |  |  | SI | Reading Aloud |
| Q36 | - |  |  | SI | Single Word |
| Q37 | - |  |  | SI | Phrase |
| Q38 | - |  |  | SI | Factual Comprehension |
| Q39 | - |  |  | SI | Sentence |
| Q40 | - |  |  | SI | Paragraph |
| Q41 | - |  |  | SI | Inferential Comprehension |
| Q42 | - |  |  | SI | Paragraph |
| Q43 | - |  |  | SI | D) Writing |
| Q44 | - |  |  | SI | Automatic |
| Q45 | - |  |  | SI | Name |
| Q46 | - |  |  | SI | Address |
| Q47 | - |  |  | SI | Numbers |
| Q48 | - |  |  | SI | Single Words (List Writing) |
| Q49 | - |  |  | SI | Number of Words Written |
| Q50 | - |  |  | SI | Relevance |
| Q51 | - |  |  | SI | Spelling |
| Q52 | - |  |  | SI | Legibility |
| Q53 | - |  |  | SI | Sentence |
| Q54 | - |  |  | SI | Number of Words in Sentence |
| Q55 | - |  |  | SI | Relevance |
| Q56 | - |  |  | SI | Spelling |
| Q57 | - |  |  | SI | Legibility |
| Q58 | - |  |  | SI | Grammar |
| Q59 | - |  |  | SI | E) Pragmatics |
| Q60 | - |  |  | SI | Non-verbal |
| Q61 | - |  |  | SI | Intonation |
| Q62 | - |  |  | SI | Facial Expression |
| Q63 | - |  |  | SI | Eye Contact |
| Q64 | - |  |  | SI | Gestures |
| Q65 | - |  |  | SI | Conversational Skills |
| Q66 | - |  |  | SI | Initiation |
| Q67 | - |  |  | SI | Turn Taking |
| Q68 | - |  |  | SI | Verbosity |
| Q69 | - |  |  | SI | Linguistic Context |
| Q70 | - |  |  | SI | Topic Maintenance |
| Q71 | - |  |  | SI | Presupposition |
| Q72 | - |  |  | SI | Referencing Skills |
| Q73 | - |  |  | SI | Organisation of Narrative |
| Q74 | - |  |  | SI | Organisation |
| Q75 | - |  |  | SI | Completeness |
| Q76 | - |  |  | SI | F) Cognitive Observation |
| Q77 | - |  |  | SI | Alertness |
| Q78 | - |  |  | SI | Orientation |
| Q79 | - |  |  | SI | Insight |
| Q80 | - |  |  | SI | Motivation |
| Q81 | - |  |  | SI | Initiation |
| Q82 | - |  |  | SI | Attention |
| Q83 | - |  |  | SI | Speed of Processing |
| Q84 | - |  |  | SI | Organisation / Planning |
| Q85 | - |  |  | SI | Problem Solving |
| Q86 | - |  |  | SI | New Learning |
| Q87 | - |  |  | SI | Auditory Memory |
| Q88 | - |  |  | SI | Fatigue |
| Q89 | - |  |  | SI | Able to Communicate Healthcare Needs |
| Q90 | - |  |  | SI | Able to Communicate Healthcare Needs (Notes) |
| Q91 | - |  |  | SI | Impression |
| Q92 | - |  |  | SI | Plan |
| Q93 | - |  |  | SI | /3 |
| Q94 | - |  |  | SI | /3 |
| Q95 | - |  |  | SI | /3 |
| Q96 | - |  |  | SI | /4 |
| Q97 | - |  |  | SI | /6 |
| Q98 | - |  |  | SI | /4 |
| Q99 | - |  |  | SI | /5 |
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