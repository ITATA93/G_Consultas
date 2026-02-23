# SQLUser.PAC_FetalMonitoringMethods

**Schema:** SQLUser
**Columnas:** 91
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| FMM_RowId | bigint | PK |  | NO | - |
| FMM_Code | varchar |  |  | NO | Code |
| FMM_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| FMM_CreatedDate | date |  |  | SI | Created Date |
| FMM_CreatedTime | time |  |  | SI | Created Time |
| FMM_CreatedUser_DR | bigint |  | FK | SI | Created User |
| FMM_DateFrom | date |  |  | SI | Date From |
| FMM_DateTo | date |  |  | SI | Date To |
| FMM_Desc | varchar |  |  | NO | Description |
| FMM_Owner | varchar |  |  | SI | Owner |
| FMM_UpdatedDate | date |  |  | SI | Updated Date |
| FMM_UpdatedTime | time |  |  | SI | Updated Time |
| FMM_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Appearance	 |
| Q02 | - |  |  | SI | Appearance comment |
| Q03 | - |  |  | SI | Behaviour |
| Q04 | - |  |  | SI | Posture |
| Q05 | - |  |  | SI | Facial expression |
| Q06 | - |  |  | SI | General movements |
| Q07 | - |  |  | SI | Quality of speech	 |
| Q08 | - |  |  | SI | Relationship with interviewer |
| Q09 | - |  |  | SI | Behaviour comments	 |
| Q10 | - |  |  | SI | Mood and affect	 |
| Q11 | - |  |  | SI | Emotion	 |
| Q12 | - |  |  | SI | Predominant mood |
| Q13 | - |  |  | SI | Emotion comments	 |
| Q14 | - |  |  | SI | Thinking / Cognition	 |
| Q15 | - |  |  | SI | Perception |
| Q16 | - |  |  | SI | Perception comments	 |
| Q17 | - |  |  | SI | Intellectual functioning |
| Q18 | - |  |  | SI | Orientation |
| Q19 | - |  |  | SI | Insight	 |
| Q20 | - |  |  | SI | Judgement	 |
| Q21 | - |  |  | SI | Memory |
| Q22 | - |  |  | SI | Thought content |
| Q23 | - |  |  | SI | Thought processes	 |
| Q24 | - |  |  | SI | Thinking / Cognition comments	 |
| Q25 | - |  |  | SI | The evaluation of mental status, both in the clini... |
| Q26 | - |  |  | SI | Many aspects of mental status, cognition, and beha... |
| Q27 | - |  |  | SI | attention, response latency, ability to answer que... |
| Q28 | - |  |  | SI | These observations, in conjunction along with any ... |
| Q29 | - |  |  | SI | The clinical history supplements the other portion... |
| Q30 | - |  |  | SI | Interpretation of both cognitive performance and b... |
| Q31 | - |  |  | SI | Other important information that can be obtained t... |
| Q32 | - |  |  | SI | and interpersonal relationships. |
| Q33 | - |  |  | SI | As patients may have limited insight into their co... |
| Q34 | - |  |  | SI | The clinical interview also allows the examiner to... |
| Q35 | - |  |  | SI | The collection of information that is relatively m... |
| Q36 | - |  |  | SI | In turn, the comfort level established during the ... |
| Q37 | - |  |  | SI | Teng, E. MD, PhD. (2018, July 13). The mental stat... |
| Q38 | - |  |  | SI | www.uptodate.com/contents/the-mental-status-examin... |
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