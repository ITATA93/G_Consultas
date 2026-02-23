# questionnaire.QTCMTAHS

> Management Tool for Acute Hemiplegic Shoulder (MTAHS)

**Schema:** questionnaire
**Columnas:** 117
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Management Tool for Acute Hemiplegic Shoulder (MTAHS)

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | Type of assessment |
| Q04 | varchar |  |  | SI | Is shoulder passive range of movement restricted? |
| Q05 | varchar |  |  | SI | Objective measure: Flexion < 160°; External rotati... |
| Q06 | varchar |  |  | SI | Is shoulder Passive Range of Motion (PROM) worseni... |
| Q07 | varchar |  |  | SI | Is there shoulder pain? |
| Q08 | varchar |  |  | SI | Objective measure: Ritchie Articular Index Score >... |
| Q09 | varchar |  |  | SI | Is pain Ritchie Articular Scale > 1 and/or worseni... |
| Q10 | varchar |  |  | SI | Is upper arm function limited? |
| Q11 | varchar |  |  | SI | Objective measure: Motor Assessment Scale (upper a... |
| Q12 | varchar |  |  | SI | Is function static? |
| Q13 | varchar |  |  | SI | Is the shoulder subluxed? |
| Q14 | varchar |  |  | SI | Objective measure: Shoulder subluxation˜ > 10 mm |
| Q15 | varchar |  |  | SI | Is subluxation worsening? |
| Q16 | varchar |  |  | SI | Is the tone in either the elbow flexors and/or sho... |
| Q17 | varchar |  |  | SI | Objective measure: Tardieu scale for high tone (x ... |
| Q18 | varchar |  |  | SI | Is tone worsening? |
| Q19 | varchar |  |  | SI | Initial Assessment Guidelines |
| Q20 | varchar |  |  | SI | The initial hemiplegic shoulder risk assessment is... |
| Q21 | varchar |  |  | SI | 1. Therapist assesses passive range of motion (PRO... |
| Q22 | varchar |  |  | SI | 2. An individual score is determined for each comp... |
| Q23 | varchar |  |  | SI | 3. An overall risk score is calculated, given as a... |
| Q24 | varchar |  |  | SI | 4. Formulation of management plan: guided by model... |
| Q25 | varchar |  |  | SI | 5. Documentation is completed on the risk assessme... |
| Q26 | varchar |  |  | SI | Follow-up Assessment |
| Q27 | varchar |  |  | SI | Formal follow-up assessments are not strictly requ... |
| Q28 | varchar |  |  | SI | Emphasis is also placed on providing up-to-date me... |
| Q29 | varchar |  |  | SI | This is completed by the PT, OT or jointly, accord... |
| Q30 | varchar |  |  | SI | 1. Therapist reassesses PROM, pain, function, subl... |
| Q31 | varchar |  |  | SI | 2. Risk scores for each component are determined t... |
| Q32 | varchar |  |  | SI | 3. a) Management plan is reviewed: guided by the m... |
| Q33 | varchar |  |  | SI | 4. a) Documentation is completed in the progress n... |
| Q34 | varchar |  |  | SI | Inclusion / Exclusion Criteria |
| Q35 | varchar |  |  | SI | Inclusion criteria (use the MTAHS) |
| Q36 | varchar |  |  | SI | One or more of the following: |
| Q37 | varchar |  |  | SI | • Shoulder pain |
| Q38 | varchar |  |  | SI | • Shoulder subluxation |
| Q39 | varchar |  |  | SI | • Altered upper limb tone |
| Q40 | varchar |  |  | SI | • Neglect |
| Q41 | varchar |  |  | SI | • Reduced shoulder passive range of motion |
| Q42 | varchar |  |  | SI | • Limited active movement |
| Q43 | varchar |  |  | SI | Exclusion criteria (don’t use the MTAHS) |
| Q44 | varchar |  |  | SI | Isolated signs of upper limb dysfunction: |
| Q45 | varchar |  |  | SI | • Dyspraxia |
| Q46 | varchar |  |  | SI | • Incoordination |
| Q47 | varchar |  |  | SI | • Numbness |
| Q48 | varchar |  |  | SI | Scoring and Suggested Interventions |
| Q49 | varchar |  |  | SI | Nil Significant Risk (0) |
| Q50 | varchar |  |  | SI | Usual intervention as indicated by general assessm... |
| Q51 | varchar |  |  | SI | Low (1 – 3) |
| Q52 | varchar |  |  | SI | – Education of patient / family and provide educat... |
| Q53 | varchar |  |  | SI | – Teach appropriate self-management strategies (su... |
| Q54 | varchar |  |  | SI | – Upper limb task-specific training |
| Q55 | varchar |  |  | SI | – Monitor and review as required |
| Q56 | varchar |  |  | SI | High (4 – 10) |
| Q57 | varchar |  |  | SI | – Upper limb positioning; and place positioning ch... |
| Q58 | varchar |  |  | SI | – Support shoulder / upper limb (e.g. pillow, tray... |
| Q59 | varchar |  |  | SI | – Careful upper limb handling |
| Q60 | varchar |  |  | SI | – Daily monitoring and therapy as required |
| Q61 | varchar |  |  | SI | – Education to patient and family |
| Q62 | varchar |  |  | SI | – Flag patient as high-risk |
| Q63 | varchar |  |  | SI | – Close involvement with nursing staff |
| Q64 | varchar |  |  | SI | – Specific interventions (e.g. air-splinting, coll... |
| Q65 | varchar |  |  | SI | Score |
| Q66 | varchar |  |  | SI | Classification |
| Q67 | varchar |  |  | SI | 4 – 10 |
| Q68 | varchar |  |  | SI | High Risk |
| Q69 | varchar |  |  | SI | 1 – 3 |
| Q70 | varchar |  |  | SI | Low Risk |
| Q71 | varchar |  |  | SI | 0 |
| Q72 | varchar |  |  | SI | Nil Significant Risk |
| Q73 | varchar |  |  | SI | The Management Tool for Acute Hemiplegic Shoulder ... |
| Q74 | varchar |  |  | SI | 0: Nil Significant Risk	 |
| Q75 | varchar |  |  | SI | 1 – 3: Low Risk |
| Q76 | varchar |  |  | SI | 4 - 10: High Risk |
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