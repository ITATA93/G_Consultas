# questionnaire.QTCMHMSE

> Mental State Examination (MSE)

**Schema:** questionnaire
**Columnas:** 79
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Mental State Examination (MSE)

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Appearance	 |
| Q02 | varchar |  |  | SI | Appearance comment |
| Q03 | varchar |  |  | SI | Behaviour |
| Q04 | varchar |  |  | SI | Posture |
| Q05 | varchar |  |  | SI | Facial expression |
| Q06 | varchar |  |  | SI | General movements |
| Q07 | varchar |  |  | SI | Quality of speech	 |
| Q08 | varchar |  |  | SI | Relationship with interviewer |
| Q09 | varchar |  |  | SI | Behaviour comments	 |
| Q10 | varchar |  |  | SI | Mood and affect	 |
| Q11 | varchar |  |  | SI | Emotion	 |
| Q12 | varchar |  |  | SI | Predominant mood |
| Q13 | varchar |  |  | SI | Emotion comments	 |
| Q14 | varchar |  |  | SI | Thinking / Cognition	 |
| Q15 | varchar |  |  | SI | Perception |
| Q16 | varchar |  |  | SI | Perception comments	 |
| Q17 | varchar |  |  | SI | Intellectual functioning |
| Q18 | varchar |  |  | SI | Orientation |
| Q19 | varchar |  |  | SI | Insight	 |
| Q20 | varchar |  |  | SI | Judgement	 |
| Q21 | varchar |  |  | SI | Memory |
| Q22 | varchar |  |  | SI | Thought content |
| Q23 | varchar |  |  | SI | Thought processes	 |
| Q24 | varchar |  |  | SI | Thinking / Cognition comments	 |
| Q25 | varchar |  |  | SI | The evaluation of mental status, both in the clini... |
| Q26 | varchar |  |  | SI | Many aspects of mental status, cognition, and beha... |
| Q27 | varchar |  |  | SI | attention, response latency, ability to answer que... |
| Q28 | varchar |  |  | SI | These observations, in conjunction along with any ... |
| Q29 | varchar |  |  | SI | The clinical history supplements the other portion... |
| Q30 | varchar |  |  | SI | Interpretation of both cognitive performance and b... |
| Q31 | varchar |  |  | SI | Other important information that can be obtained t... |
| Q32 | varchar |  |  | SI | and interpersonal relationships. |
| Q33 | varchar |  |  | SI | As patients may have limited insight into their co... |
| Q34 | varchar |  |  | SI | The clinical interview also allows the examiner to... |
| Q35 | varchar |  |  | SI | The collection of information that is relatively m... |
| Q36 | varchar |  |  | SI | In turn, the comfort level established during the ... |
| Q37 | varchar |  |  | SI | Teng, E. MD, PhD. (2018, July 13). The mental stat... |
| Q38 | varchar |  |  | SI | www.uptodate.com/contents/the-mental-status-examin... |
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