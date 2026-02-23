# questionnaire.QTCSSQOL

> Stroke Specific Quality of Life Scale (SS-QOL)

**Schema:** questionnaire
**Columnas:** 106
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Stroke Specific Quality of Life Scale (SS-QOL)

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | 1.&nbsp;I felt tired most of the time |
| Q04 | varchar |  |  | SI | 2.&nbsp;I had to stop and rest during the day |
| Q05 | varchar |  |  | SI | 3. I was too tired to do what I wanted to do |
| Q06 | varchar |  |  | SI | 1.&nbsp;I didn't join in activities just for fun w... |
| Q07 | varchar |  |  | SI | 2.&nbsp;I felt I was a burden to my family |
| Q08 | varchar |  |  | SI | 3.&nbsp;My physical condition interfered with my p... |
| Q09 | varchar |  |  | SI | 1.&nbsp;Did you have trouble speaking? For example... |
| Q10 | varchar |  |  | SI | 2.&nbsp;Did you have trouble speaking clearly enou... |
| Q11 | varchar |  |  | SI | 3.&nbsp;Did other people have trouble in understan... |
| Q12 | varchar |  |  | SI | 4.&nbsp;Did you have trouble finding the word you ... |
| Q13 | varchar |  |  | SI | 5.&nbsp;Did you have to repeat yourself so others ... |
| Q14 | varchar |  |  | SI | 1. Did you have trouble walking? |
| Q15 | varchar |  |  | SI | 2.&nbsp;Did you lose your balance when bending ove... |
| Q16 | varchar |  |  | SI | 3. Did you have trouble climbing stairs? |
| Q17 | varchar |  |  | SI | 4.&nbsp;Did you have to stop and rest more than yo... |
| Q18 | varchar |  |  | SI | 5.&nbsp;Did you have trouble with standing? |
| Q19 | varchar |  |  | SI | 6.&nbsp;Did you have trouble getting out of a chai... |
| Q20 | varchar |  |  | SI | 1.&nbsp;I was discouraged about my future |
| Q21 | varchar |  |  | SI | 2.&nbsp;I wasn't interested in other people or act... |
| Q22 | varchar |  |  | SI | 3. I felt withdrawn from other people |
| Q23 | varchar |  |  | SI | 4.&nbsp;I had little confidence in myself |
| Q24 | varchar |  |  | SI | 5.&nbsp;I was not interested in food |
| Q25 | varchar |  |  | SI | 1.&nbsp;I was irritable |
| Q26 | varchar |  |  | SI | 2.&nbsp;I was impatient with others |
| Q27 | varchar |  |  | SI | 3.&nbsp;My personality has changed |
| Q28 | varchar |  |  | SI | 1. Did you need help preparing food? |
| Q29 | varchar |  |  | SI | 2.&nbsp;Did you need help eating? For example, cut... |
| Q30 | varchar |  |  | SI | 3. Did you need help getting dressed? For example,... |
| Q31 | varchar |  |  | SI | 4.&nbsp;Did you need help taking a bath or a showe... |
| Q32 | varchar |  |  | SI | 5.&nbsp;Did you need help to use the toilet? |
| Q33 | varchar |  |  | SI | 1.&nbsp;I didn't go out as often as I would like. |
| Q34 | varchar |  |  | SI | 2.&nbsp;I did my hobbies and recreation for shorte... |
| Q35 | varchar |  |  | SI | 3. I didn't see as many of my friends as I would l... |
| Q36 | varchar |  |  | SI | 4. I had sex less often than I would like. |
| Q37 | varchar |  |  | SI | 5. My physical condition interfered with my social... |
| Q38 | varchar |  |  | SI | 1.&nbsp;It was hard for me to concentrate. |
| Q39 | varchar |  |  | SI | 2. I had trouble remembering things |
| Q40 | varchar |  |  | SI | 3. I had to write things down to remember them |
| Q41 | varchar |  |  | SI | 1.&nbsp;Did you have trouble writing or typing? |
| Q42 | varchar |  |  | SI | 2. Did you have trouble putting on socks? |
| Q43 | varchar |  |  | SI | 3. Did you have trouble buttoning buttons? |
| Q44 | varchar |  |  | SI | 4. Did you have trouble zipping a zipper? |
| Q45 | varchar |  |  | SI | 5. Did you have trouble opening a jar? |
| Q46 | varchar |  |  | SI | 1.&nbsp;Did you have trouble seeing the television... |
| Q47 | varchar |  |  | SI | 2. Did you have trouble reaching things because of... |
| Q48 | varchar |  |  | SI | 3. Did you have trouble seeing things off to one s... |
| Q49 | varchar |  |  | SI | 1.&nbsp;Did you have trouble doing daily work arou... |
| Q50 | varchar |  |  | SI | 2. Did you have trouble finishing jobs that you st... |
| Q51 | varchar |  |  | SI | 3. Did you have trouble doing the work you used to... |
| Q52 | varchar |  |  | SI | Notes |
| Q53 | varchar |  |  | SI | Total score |
| Q54 | varchar |  |  | SI | Williams LS, Weinberger M, Harris LE, Clark DO, Bi... |
| Q55 | varchar |  |  | SI | Higher score indicates better of quality of life |
| Q56 | varchar |  |  | SI | Should not be used in: |
| Q57 | varchar |  |  | SI | • Patients without stroke. The SS-QOL was develope... |
| Q58 | varchar |  |  | SI | • Severe stroke populations. The SS-QOL has not ye... |
| Q59 | varchar |  |  | SI | • Patients who require a proxy to complete. |
| Q60 | varchar |  |  | SI | • Should be used with caution in patients with aph... |
| Q61 | varchar |  |  | SI | Although the modified version of the scale, the SA... |
| Q62 | varchar |  |  | SI | • Not to be used in patients under 18 years. |
| Q63 | varchar |  |  | SI | The performance characteristics of this instrument... |
| Q64 | varchar |  |  | SI | The Stroke Specific Quality of Life Scale assesses... |
| Q65 | varchar |  |  | SI | 1. Did you have trouble walking? |
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