# questionnaire.QGXXXMANMH

> Antenatal medical history

**Schema:** questionnaire
**Columnas:** 154
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Antenatal medical history

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Have you had any cardiac problems |
| Q01A | varchar |  |  | SI | Cardiac symptoms |
| Q01C | varchar |  |  | SI | Cardiac problems |
| Q01T | varchar |  |  | SI | Details |
| Q02 | varchar |  |  | SI | Have you ever had hypertension |
| Q02C | varchar |  |  | SI | Hypertension |
| Q02T | varchar |  |  | SI | Details |
| Q03 | varchar |  |  | SI | Have you had anaemia or other haematological probl... |
| Q03C | varchar |  |  | SI | Haematological problem |
| Q03T | varchar |  |  | SI | Details |
| Q04 | varchar |  |  | SI | Have you had thromboembolic or clotting disorders |
| Q04A1 | varchar |  |  | SI | Do you have a history of provoked  Venous thromboe... |
| Q04A2 | varchar |  |  | SI | Do you have a history of unprovoked VTE |
| Q04A3 | varchar |  |  | SI | Do you have a history of recurrent VTE |
| Q04A4 | varchar |  |  | SI | Are you using anticoagulants |
| Q04AT | varchar |  |  | SI | Details |
| Q04C | varchar |  |  | SI | Thromboembolic |
| Q04T | varchar |  |  | SI | Details |
| Q05 | varchar |  |  | SI | Have you had any blood transfusions in the past |
| Q05A1 | varchar |  |  | SI | Have you had a transfusion reaction |
| Q05T | varchar |  |  | SI | Details |
| Q06 | varchar |  |  | SI | Have you declined blood or blood products in the p... |
| Q06T | varchar |  |  | SI | Details |
| Q07 | varchar |  |  | SI | Have you had any respiratory diseases |
| Q07C | varchar |  |  | SI | Respiratory |
| Q07T | varchar |  |  | SI | Details |
| Q08 | varchar |  |  | SI | Have you had your heart and lungs listened to in t... |
| Q08T | varchar |  |  | SI | Details |
| Q09 | varchar |  |  | SI | Have you had urinary or kidney problems |
| Q09C | varchar |  |  | SI | Urinary |
| Q09T | varchar |  |  | SI | Details |
| Q10 | varchar |  |  | SI | Have you had any gastrointestinal problems |
| Q104 | varchar |  |  | SI | Endocrine problem type |
| Q105 | varchar |  |  | SI | If history of diabetes mellitus, please describe t... |
| Q105T | varchar |  |  | SI | Details |
| Q106 | date |  |  | SI | Date |
| Q107 | time |  |  | SI | Time |
| Q109 | varchar |  |  | SI | Have you had any diabetes mellitus problems |
| Q10C | varchar |  |  | SI | Gastrointestinal |
| Q10T | varchar |  |  | SI | Details |
| Q11 | varchar |  |  | SI | Have you had any endocrine problems |
| Q110 | varchar |  |  | SI | Diabetes mellitus problem type |
| Q111 | varchar |  |  | SI | Details |
| Q112 | varchar |  |  | SI | Have you had any other endocrine problems |
| Q113 | varchar |  |  | SI | Problem documentation status |
| Q11C | varchar |  |  | SI | Endocrine |
| Q11T | varchar |  |  | SI | Details |
| Q12 | varchar |  |  | SI | Have you had fits, epilepsy or neurological proble... |
| Q12C | varchar |  |  | SI | Neurological |
| Q12T | varchar |  |  | SI | Details |
| Q13 | varchar |  |  | SI | Do you have any inherited disorders |
| Q13C | varchar |  |  | SI | Inherited disorders |
| Q13T | varchar |  |  | SI | Details |
| Q14 | varchar |  |  | SI | Have you had any autoimmune disease |
| Q14A1 | varchar |  |  | SI | Drugs to suppress immune response taken in early p... |
| Q14A2 | varchar |  |  | SI | Currently taking drugs to suppress immune response |
| Q14A2T | varchar |  |  | SI | Details |
| Q14A3 | varchar |  |  | SI | Currently on other (non immunosuppressant) medicat... |
| Q14A3T | varchar |  |  | SI | Details |
| Q14C | varchar |  |  | SI | Autoimmune |
| Q14T | varchar |  |  | SI | Details |
| Q15 | varchar |  |  | SI | Do you have any dermatological problems |
| Q15C | varchar |  |  | SI | Dermatological |
| Q15T | varchar |  |  | SI | Details |
| Q16 | varchar |  |  | SI | Have you had any other medical problems in the pas... |
| Q16T | varchar |  |  | SI | Details |
| Q17 | varchar |  |  | SI | Have you had any musculoskeletal problems |
| Q17C | varchar |  |  | SI | Musculoskeletal |
| Q17T | varchar |  |  | SI | Details |
| Q18 | varchar |  |  | SI | Do you have any history of cancer and/or malignanc... |
| Q18C | varchar |  |  | SI | Cancer |
| Q18T | varchar |  |  | SI | Details |
| Q19 | varchar |  |  | SI | Have you had any gynaecological problems or operat... |
| Q19C | varchar |  |  | SI | Gynaecological |
| Q19T | varchar |  |  | SI | Details |
| Q20 | varchar |  |  | SI | Have you had a smear |
| Q20A1 | varchar |  |  | SI | When was your last smear |
| Q20A2 | varchar |  |  | SI | Result of last smear |
| Q20T | varchar |  |  | SI | Details |
| Q21 | varchar |  |  | SI | Have you had any surgery in the past |
| Q21A1 | varchar |  |  | SI | Surgery during this pregnancy |
| Q21A2 | varchar |  |  | SI | Recent major surgery |
| Q21C | varchar |  |  | SI | Surgery |
| Q21T | varchar |  |  | SI | Details |
| Q22 | varchar |  |  | SI | Have you had any problems with anaesthesia in the ... |
| Q22C | varchar |  |  | SI | Anaesthesia |
| Q22T | varchar |  |  | SI | Details |
| Q23 | varchar |  |  | SI | Have you had any infections |
| Q23C | varchar |  |  | SI | Infections |
| Q23T | varchar |  |  | SI | Details |
| Q24 | varchar |  |  | SI | Have you had an Sexually Transmitted Disease (STI) |
| Q24A1 | bit |  |  | SI | Suppress STI responses |
| Q24C | varchar |  |  | SI | Sexually Transmitted Infections (STI) |
| Q24T | varchar |  |  | SI | Details |
| Q25 | varchar |  |  | SI | Have you had any mental health problems |
| Q25A1 | varchar |  |  | SI | Are you taking medication for mental health proble... |
| Q25A1T | varchar |  |  | SI | Details |
| Q25A2 | varchar |  |  | SI | Have you stopped taking medication for a mental he... |
| Q25A2T | varchar |  |  | SI | Details |
| Q25A3 | varchar |  |  | SI | Have you had a recent admission to a psychiatric u... |
| Q25A4 | varchar |  |  | SI | Who is treating you |
| Q25A5 | varchar |  |  | SI | Practitioner type |
| Q25A5T | varchar |  |  | SI | Details |
| Q25C | varchar |  |  | SI | Mental health |
| Q25T | varchar |  |  | SI | Details |
| Q26 | varchar |  |  | SI | Have you had jaundice or liver problems |
| Q26C | varchar |  |  | SI | Jaundice / Liver |
| Q26T | varchar |  |  | SI | Details |
| Q27 | varchar |  |  | SI | Do you have any physical disabilities |
| Q27A1 | varchar |  |  | SI | Are you able to self care |
| Q27A1T | varchar |  |  | SI | Details |
| Q27L | varchar |  |  | SI | Please review patient alerts and amend as appropri... |
| Q27T | varchar |  |  | SI | Details |
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