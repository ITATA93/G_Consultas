# SQLUser.PAC_Laterality

**Schema:** SQLUser
**Columnas:** 131
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LATER_RowId | bigint | PK |  | NO | - |
| LATER_Code | varchar |  |  | NO | Code |
| LATER_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LATER_CodeTranslated | varchar |  |  | SI | - |
| LATER_CreatedDate | date |  |  | SI | Created Date |
| LATER_CreatedTime | time |  |  | SI | Created Time |
| LATER_CreatedUser_DR | bigint |  | FK | SI | Created User |
| LATER_DateFrom | date |  |  | SI | Date From |
| LATER_DateTo | date |  |  | SI | Date To |
| LATER_Desc | varchar |  |  | NO | Description |
| LATER_DescTranslated | varchar |  |  | SI | - |
| LATER_Owner | varchar |  |  | SI | Owner |
| LATER_UpdatedDate | date |  |  | SI | Updated Date |
| LATER_UpdatedTime | time |  |  | SI | Updated Time |
| LATER_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Type of assessment |
| Q04 | - |  |  | SI | Is shoulder passive range of movement restricted? |
| Q05 | - |  |  | SI | Objective measure: Flexion < 160° |
| Q06 | - |  |  | SI | Is shoulder Passive Range of Motion (PROM) worseni... |
| Q07 | - |  |  | SI | Is there shoulder pain? |
| Q08 | - |  |  | SI | Objective measure: Ritchie Articular Index Score >... |
| Q09 | - |  |  | SI | Is pain Ritchie Articular Scale > 1 and/or worseni... |
| Q10 | - |  |  | SI | Is upper arm function limited? |
| Q11 | - |  |  | SI | Objective measure: Motor Assessment Scale (upper a... |
| Q12 | - |  |  | SI | Is function static? |
| Q13 | - |  |  | SI | Is the shoulder subluxed? |
| Q14 | - |  |  | SI | Objective measure: Shoulder subluxation˜ > 10 mm |
| Q15 | - |  |  | SI | Is subluxation worsening? |
| Q16 | - |  |  | SI | Is the tone in either the elbow flexors and/or sho... |
| Q17 | - |  |  | SI | Objective measure: Tardieu scale for high tone (x ... |
| Q18 | - |  |  | SI | Is tone worsening? |
| Q19 | - |  |  | SI | Initial Assessment Guidelines |
| Q20 | - |  |  | SI | The initial hemiplegic shoulder risk assessment is... |
| Q21 | - |  |  | SI | 1. Therapist assesses passive range of motion (PRO... |
| Q22 | - |  |  | SI | 2. An individual score is determined for each comp... |
| Q23 | - |  |  | SI | 3. An overall risk score is calculated, given as a... |
| Q24 | - |  |  | SI | 4. Formulation of management plan: guided by model... |
| Q25 | - |  |  | SI | 5. Documentation is completed on the risk assessme... |
| Q26 | - |  |  | SI | Follow-up Assessment |
| Q27 | - |  |  | SI | Formal follow-up assessments are not strictly requ... |
| Q28 | - |  |  | SI | Emphasis is also placed on providing up-to-date me... |
| Q29 | - |  |  | SI | This is completed by the PT, OT or jointly, accord... |
| Q30 | - |  |  | SI | 1. Therapist reassesses PROM, pain, function, subl... |
| Q31 | - |  |  | SI | 2. Risk scores for each component are determined t... |
| Q32 | - |  |  | SI | 3. a) Management plan is reviewed: guided by the m... |
| Q33 | - |  |  | SI | 4. a) Documentation is completed in the progress n... |
| Q34 | - |  |  | SI | Inclusion / Exclusion Criteria |
| Q35 | - |  |  | SI | Inclusion criteria (use the MTAHS) |
| Q36 | - |  |  | SI | One or more of the following: |
| Q37 | - |  |  | SI | • Shoulder pain |
| Q38 | - |  |  | SI | • Shoulder subluxation |
| Q39 | - |  |  | SI | • Altered upper limb tone |
| Q40 | - |  |  | SI | • Neglect |
| Q41 | - |  |  | SI | • Reduced shoulder passive range of motion |
| Q42 | - |  |  | SI | • Limited active movement |
| Q43 | - |  |  | SI | Exclusion criteria (don’t use the MTAHS) |
| Q44 | - |  |  | SI | Isolated signs of upper limb dysfunction: |
| Q45 | - |  |  | SI | • Dyspraxia |
| Q46 | - |  |  | SI | • Incoordination |
| Q47 | - |  |  | SI | • Numbness |
| Q48 | - |  |  | SI | Scoring and Suggested Interventions |
| Q49 | - |  |  | SI | Nil Significant Risk (0) |
| Q50 | - |  |  | SI | Usual intervention as indicated by general assessm... |
| Q51 | - |  |  | SI | Low (1 – 3) |
| Q52 | - |  |  | SI | – Education of patient / family and provide educat... |
| Q53 | - |  |  | SI | – Teach appropriate self-management strategies (su... |
| Q54 | - |  |  | SI | – Upper limb task-specific training |
| Q55 | - |  |  | SI | – Monitor and review as required |
| Q56 | - |  |  | SI | High (4 – 10) |
| Q57 | - |  |  | SI | – Upper limb positioning |
| Q58 | - |  |  | SI | – Support shoulder / upper limb (e.g. pillow, tray... |
| Q59 | - |  |  | SI | – Careful upper limb handling |
| Q60 | - |  |  | SI | – Daily monitoring and therapy as required |
| Q61 | - |  |  | SI | – Education to patient and family |
| Q62 | - |  |  | SI | – Flag patient as high-risk |
| Q63 | - |  |  | SI | – Close involvement with nursing staff |
| Q64 | - |  |  | SI | – Specific interventions (e.g. air-splinting, coll... |
| Q65 | - |  |  | SI | Score |
| Q66 | - |  |  | SI | Classification |
| Q67 | - |  |  | SI | 4 – 10 |
| Q68 | - |  |  | SI | High Risk |
| Q69 | - |  |  | SI | 1 – 3 |
| Q70 | - |  |  | SI | Low Risk |
| Q71 | - |  |  | SI | 0 |
| Q72 | - |  |  | SI | Nil Significant Risk |
| Q73 | - |  |  | SI | The Management Tool for Acute Hemiplegic Shoulder ... |
| Q74 | - |  |  | SI | 0: Nil Significant Risk	 |
| Q75 | - |  |  | SI | 1 – 3: Low Risk |
| Q76 | - |  |  | SI | 4 - 10: High Risk |
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