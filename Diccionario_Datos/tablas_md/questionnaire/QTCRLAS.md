# questionnaire.QTCRLAS

> Rancho Los Amigos Scale

**Schema:** questionnaire
**Columnas:** 93
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Rancho Los Amigos Scale

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Rancho Los Amigos Scale |
| Q02 | varchar |  |  | SI | Level 1 : No Response |
| Q03 | varchar |  |  | SI | Patient does not respond to external stimuli and a... |
| Q04 | varchar |  |  | SI | Level 2: Generalised Response |
| Q05 | varchar |  |  | SI | Patient reacts to external stimuli in nonspecific,... |
| Q06 | varchar |  |  | SI | Level 3: Localised Response |
| Q07 | varchar |  |  | SI | Patient responds specifically and inconsistently w... |
| Q08 | varchar |  |  | SI | Level 4: Confused, Agitated Response |
| Q09 | varchar |  |  | SI | Patient exhibits bizarre, nonpurposeful, incoheren... |
| Q10 | varchar |  |  | SI | Level 5: Confused, Inappropriate, Non-agitated Res... |
| Q11 | varchar |  |  | SI | Patient gives random, fragmented, and nonpurposefu... |
| Q12 | varchar |  |  | SI | complex or unstructured stimuli. Simple commands a... |
| Q13 | varchar |  |  | SI | Level 6: Confused, Appropriate Response |
| Q14 | varchar |  |  | SI | Patient gives context appropriate, goal-directed r... |
| Q15 | varchar |  |  | SI | external input for direction. There is carry-over ... |
| Q16 | varchar |  |  | SI | Level 7: Automatic, Appropriate Response |
| Q17 | varchar |  |  | SI | Patient behaves appropriately in familiar settings... |
| Q18 | varchar |  |  | SI | automatically, and shows carry-over for new learni... |
| Q19 | varchar |  |  | SI | Level 8: Purposeful, Appropriate Response |
| Q20 | varchar |  |  | SI | Patient oriented and responds to the environment b... |
| Q21 | varchar |  |  | SI | The Rancho Los Amigos Scale (RLAS), a.k.a. the Ran... |
| Q22 | varchar |  |  | SI | individuals after a closed head injury, including ... |
| Q23 | varchar |  |  | SI | After being assessed based on the LOCF, individual... |
| Q24 | varchar |  |  | SI | whereas a score of eight represents purposeful and... |
| Q25 | varchar |  |  | SI | coma. After being assessed based on individuals wi... |
| Q26 | varchar |  |  | SI | nonpurposeful manner with stereotypic and limited ... |
| Q27 | varchar |  |  | SI | but may follow simple commands for motor action. |
| Q28 | varchar |  |  | SI | behaviours, has no short-term recall, attention is... |
| Q29 | varchar |  |  | SI | memory and selective attention are impaired, and n... |
| Q30 | varchar |  |  | SI | new tasks, and recent memory problems persist. |
| Q31 | varchar |  |  | SI | rates. Patient intitiates social interactions, but... |
| Q32 | varchar |  |  | SI | abilities are decreased relative to premorbid leve... |
| Q33 | varchar |  |  | SI | a score from one to eight. A score of one represen... |
| Q34 | varchar |  |  | SI | whereas a score of eight represents purposeful and... |
| Q35 | varchar |  |  | SI | Score |
| Q36 | varchar |  |  | SI | Classification |
| Q37 | varchar |  |  | SI | Level 1 |
| Q38 | varchar |  |  | SI | No Response |
| Q39 | varchar |  |  | SI | Level 2 |
| Q40 | varchar |  |  | SI | Generalised Response |
| Q41 | varchar |  |  | SI | Level 3 |
| Q42 | varchar |  |  | SI | Localised Response |
| Q43 | varchar |  |  | SI | Level 4 |
| Q44 | varchar |  |  | SI | Confused, Agitated Response |
| Q45 | varchar |  |  | SI | Level 5 |
| Q46 | varchar |  |  | SI | Confused, Inappropriate, Non-agitated Response |
| Q47 | varchar |  |  | SI | Level 6 |
| Q48 | varchar |  |  | SI | Confused, Appropriate Response |
| Q49 | varchar |  |  | SI | Level 7 |
| Q50 | varchar |  |  | SI | Automatic, Appropriate Response |
| Q51 | varchar |  |  | SI | Level 8 |
| Q52 | varchar |  |  | SI | Purposeful, Appropriate Response |
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