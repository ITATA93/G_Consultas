# questionnaire.QTCAUSTOMSS

> AusTOMs - Speech Pathology

**Schema:** questionnaire
**Columnas:** 108
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* AusTOMs - Speech Pathology

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Session |
| Q02 | varchar |  |  | SI | Scale |
| Q03 | varchar |  |  | SI | Speech |
| Q04 | varchar |  |  | SI | Language |
| Q05 | varchar |  |  | SI | Voice |
| Q06 | varchar |  |  | SI | Fluency |
| Q07 | varchar |  |  | SI | Cognitive-communication |
| Q08 | varchar |  |  | SI | Swallowing |
| Q09 | varchar |  |  | SI | Impairment |
| Q10 | varchar |  |  | SI | Activity Limitation |
| Q11 | numeric |  |  | SI | Speech impairment |
| Q12 | numeric |  |  | SI | Language impairment |
| Q13 | numeric |  |  | SI | Voice impairment |
| Q14 | numeric |  |  | SI | Fluency impairment |
| Q15 | numeric |  |  | SI | Cognitive-communication impairment |
| Q16 | numeric |  |  | SI | Swallowing impairment |
| Q17 | numeric |  |  | SI | Speech activity limitation |
| Q18 | numeric |  |  | SI | Language activity limitation |
| Q19 | numeric |  |  | SI | Voice activity limitation |
| Q20 | numeric |  |  | SI | Fluency activity limitation |
| Q21 | numeric |  |  | SI | Cognitive-communication activity limitation |
| Q22 | numeric |  |  | SI | Swallowing activity limitation |
| Q23 | numeric |  |  | SI | Participation restriction |
| Q24 | numeric |  |  | SI | Distress / Wellbeing |
| Q25 | numeric |  |  | SI | Carer distress / wellbeing |
| Q26 | varchar |  |  | SI | General comments |
| Q27 | varchar |  |  | SI | IMPAIRMENT OF EITHER STRUCTURE OR FUNCTION (AS APP... |
| Q28 | varchar |  |  | SI | Impairments are problems in body structure (anatom... |
| Q29 | varchar |  |  | SI | 0 The most severe presentation of impairment |
| Q30 | varchar |  |  | SI | 1 Severe presentation of this impairment |
| Q31 | varchar |  |  | SI | 2 Moderate / Severe presentation |
| Q32 | varchar |  |  | SI | 3 Moderate presentation |
| Q33 | varchar |  |  | SI | 4 Mild presentation |
| Q34 | varchar |  |  | SI | 5 No impairment of structure or function |
| Q35 | varchar |  |  | SI | ACTIVITY LIMITATION (AS APPROPRIATE TO AGE) |
| Q36 | varchar |  |  | SI | Activity limitation results from the difficulty in... |
| Q37 | varchar |  |  | SI | 0 Complete difficulty |
| Q38 | varchar |  |  | SI | 1 Severe difficulty |
| Q39 | varchar |  |  | SI | 2 Moderate / severe difficulty |
| Q40 | varchar |  |  | SI | 3 Moderate difficulty |
| Q41 | varchar |  |  | SI | 4 Mild difficulty |
| Q42 | varchar |  |  | SI | 5 No difficulty |
| Q43 | varchar |  |  | SI | PARTICIPATION RESTRICTION (AS APPROPRIATE TO AGE) |
| Q44 | varchar |  |  | SI | Participation restrictions are difficulties the in... |
| Q45 | varchar |  |  | SI | Clinicians should ask themselves: “given their pro... |
| Q46 | varchar |  |  | SI | 0 Unable to fulfill social, work, educational or f... |
| Q47 | varchar |  |  | SI | 1 Severe difficulties in fulfilling social, work, ... |
| Q48 | varchar |  |  | SI | Can only rarely reach potential with maximum assis... |
| Q49 | varchar |  |  | SI | 2 Moderately severe difficulties in fulfilling soc... |
| Q50 | varchar |  |  | SI | Limited involvement in decision-making. Control ov... |
| Q51 | varchar |  |  | SI | Usually reaches potential with maximum assistance. |
| Q52 | varchar |  |  | SI | 3 Moderate difficulties in fulfilling social, work... |
| Q53 | varchar |  |  | SI | Control over environment in more than one setting.... |
| Q54 | varchar |  |  | SI | 4 Mild difficulties in fulfilling social, work, ed... |
| Q55 | varchar |  |  | SI | Reaches potential with little assistance. |
| Q56 | varchar |  |  | SI | 5 No difficulties in fulfilling social, work, educ... |
| Q57 | varchar |  |  | SI | Control over environment in all settings. Reaches ... |
| Q58 | varchar |  |  | SI | DISTRESS / WELLBEING (AS APPROPRIATE TO AGE): |
| Q59 | varchar |  |  | SI | The level of concern experienced by the individual... |
| Q60 | varchar |  |  | SI | 0 High and consistent levels of distress or concer... |
| Q61 | varchar |  |  | SI | 1 Severe concern, becomes distressed or concerned ... |
| Q62 | varchar |  |  | SI | 2 Moderately severe concern. Frequent emotional en... |
| Q63 | varchar |  |  | SI | 3 Moderate concern. May be able to manage emotions... |
| Q64 | varchar |  |  | SI | 4 Mild concern. Able to manage emotions in most si... |
| Q65 | varchar |  |  | SI | 5 Able to cope with most situations. Accepts and u... |
| Q66 | date |  |  | SI | Date |
| Q67 | time |  |  | SI | Time |
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