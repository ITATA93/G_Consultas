# SQLUser.CT_LocRpt

**Schema:** SQLUser
**Columnas:** 167
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de Ubicaciones**. Servicios, salas, unidades del hospital.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LOCRP_CTLOC_ParRef | bigint | PK |  | NO | LOCRP Parent Reference |
| LOCRP_ChildSub | double |  |  | NO | ChildSub |
| LOCRP_CreatedDate | date |  |  | SI | Created Date |
| LOCRP_CreatedTime | time |  |  | SI | Created Time |
| LOCRP_CreatedUser_DR | bigint |  | FK | SI | Created User |
| LOCRP_DEV_DR | varchar |  | FK | SI | Des Ref to CT_Device |
| LOCRP_FMT_DR | varchar |  | FK | SI | Not Used Format |
| LOCRP_LPFMT_DR | varchar |  | FK | SI | Not Used Des Ref to CT_LPFormat |
| LOCRP_LP_DR | varchar |  | FK | SI | Not Used Des Ref to CT_LP |
| LOCRP_RP_DR | bigint |  | FK | NO | Des Ref to CTRP(CT_Modules) |
| LOCRP_RowId | varchar |  |  | NO | - |
| LOCRP_UpdatedDate | date |  |  | SI | Updated Date |
| LOCRP_UpdatedTime | time |  |  | SI | Updated Time |
| LOCRP_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Have you had any cardiac problems |
| Q01A | - |  |  | SI | Cardiac symptoms |
| Q01C | - |  |  | SI | Cardiac problems |
| Q01T | - |  |  | SI | Details |
| Q02 | - |  |  | SI | Have you ever had hypertension |
| Q02C | - |  |  | SI | Hypertension |
| Q02T | - |  |  | SI | Details |
| Q03 | - |  |  | SI | Have you had anaemia or other haematological probl... |
| Q03C | - |  |  | SI | Haematological problem |
| Q03T | - |  |  | SI | Details |
| Q04 | - |  |  | SI | Have you had thromboembolic or clotting disorders |
| Q04A1 | - |  |  | SI | Do you have a history of provoked  Venous thromboe... |
| Q04A2 | - |  |  | SI | Do you have a history of unprovoked VTE |
| Q04A3 | - |  |  | SI | Do you have a history of recurrent VTE |
| Q04A4 | - |  |  | SI | Are you using anticoagulants |
| Q04AT | - |  |  | SI | Details |
| Q04C | - |  |  | SI | Thromboembolic |
| Q04T | - |  |  | SI | Details |
| Q05 | - |  |  | SI | Have you had any blood transfusions in the past |
| Q05A1 | - |  |  | SI | Have you had a transfusion reaction |
| Q05T | - |  |  | SI | Details |
| Q06 | - |  |  | SI | Have you declined blood or blood products in the p... |
| Q06T | - |  |  | SI | Details |
| Q07 | - |  |  | SI | Have you had any respiratory diseases |
| Q07C | - |  |  | SI | Respiratory |
| Q07T | - |  |  | SI | Details |
| Q08 | - |  |  | SI | Have you had your heart and lungs listened to in t... |
| Q08T | - |  |  | SI | Details |
| Q09 | - |  |  | SI | Have you had urinary or kidney problems |
| Q09C | - |  |  | SI | Urinary |
| Q09T | - |  |  | SI | Details |
| Q10 | - |  |  | SI | Have you had any gastrointestinal problems |
| Q104 | - |  |  | SI | Endocrine problem type |
| Q105 | - |  |  | SI | If history of diabetes mellitus, please describe t... |
| Q105T | - |  |  | SI | Details |
| Q106 | - |  |  | SI | Date |
| Q107 | - |  |  | SI | Time |
| Q109 | - |  |  | SI | Have you had any diabetes mellitus problems |
| Q10C | - |  |  | SI | Gastrointestinal |
| Q10T | - |  |  | SI | Details |
| Q11 | - |  |  | SI | Have you had any endocrine problems |
| Q110 | - |  |  | SI | Diabetes mellitus problem type |
| Q111 | - |  |  | SI | Details |
| Q112 | - |  |  | SI | Have you had any other endocrine problems |
| Q113 | - |  |  | SI | Problem documentation status |
| Q11C | - |  |  | SI | Endocrine |
| Q11T | - |  |  | SI | Details |
| Q12 | - |  |  | SI | Have you had fits, epilepsy or neurological proble... |
| Q12C | - |  |  | SI | Neurological |
| Q12T | - |  |  | SI | Details |
| Q13 | - |  |  | SI | Do you have any inherited disorders |
| Q13C | - |  |  | SI | Inherited disorders |
| Q13T | - |  |  | SI | Details |
| Q14 | - |  |  | SI | Have you had any autoimmune disease |
| Q14A1 | - |  |  | SI | Drugs to suppress immune response taken in early p... |
| Q14A2 | - |  |  | SI | Currently taking drugs to suppress immune response |
| Q14A2T | - |  |  | SI | Details |
| Q14A3 | - |  |  | SI | Currently on other (non immunosuppressant) medicat... |
| Q14A3T | - |  |  | SI | Details |
| Q14C | - |  |  | SI | Autoimmune |
| Q14T | - |  |  | SI | Details |
| Q15 | - |  |  | SI | Do you have any dermatological problems |
| Q15C | - |  |  | SI | Dermatological |
| Q15T | - |  |  | SI | Details |
| Q16 | - |  |  | SI | Have you had any other medical problems in the pas... |
| Q16T | - |  |  | SI | Details |
| Q17 | - |  |  | SI | Have you had any musculoskeletal problems |
| Q17C | - |  |  | SI | Musculoskeletal |
| Q17T | - |  |  | SI | Details |
| Q18 | - |  |  | SI | Do you have any history of cancer and/or malignanc... |
| Q18C | - |  |  | SI | Cancer |
| Q18T | - |  |  | SI | Details |
| Q19 | - |  |  | SI | Have you had any gynaecological problems or operat... |
| Q19C | - |  |  | SI | Gynaecological |
| Q19T | - |  |  | SI | Details |
| Q20 | - |  |  | SI | Have you had a smear |
| Q20A1 | - |  |  | SI | When was your last smear |
| Q20A2 | - |  |  | SI | Result of last smear |
| Q20T | - |  |  | SI | Details |
| Q21 | - |  |  | SI | Have you had any surgery in the past |
| Q21A1 | - |  |  | SI | Surgery during this pregnancy |
| Q21A2 | - |  |  | SI | Recent major surgery |
| Q21C | - |  |  | SI | Surgery |
| Q21T | - |  |  | SI | Details |
| Q22 | - |  |  | SI | Have you had any problems with anaesthesia in the ... |
| Q22C | - |  |  | SI | Anaesthesia |
| Q22T | - |  |  | SI | Details |
| Q23 | - |  |  | SI | Have you had any infections |
| Q23C | - |  |  | SI | Infections |
| Q23T | - |  |  | SI | Details |
| Q24 | - |  |  | SI | Have you had an Sexually Transmitted Disease (STI) |
| Q24A1 | - |  |  | SI | Suppress STI responses |
| Q24C | - |  |  | SI | Sexually Transmitted Infections (STI) |
| Q24T | - |  |  | SI | Details |
| Q25 | - |  |  | SI | Have you had any mental health problems |
| Q25A1 | - |  |  | SI | Are you taking medication for mental health proble... |
| Q25A1T | - |  |  | SI | Details |
| Q25A2 | - |  |  | SI | Have you stopped taking medication for a mental he... |
| Q25A2T | - |  |  | SI | Details |
| Q25A3 | - |  |  | SI | Have you had a recent admission to a psychiatric u... |
| Q25A4 | - |  |  | SI | Who is treating you |
| Q25A5 | - |  |  | SI | Practitioner type |
| Q25A5T | - |  |  | SI | Details |
| Q25C | - |  |  | SI | Mental health |
| Q25T | - |  |  | SI | Details |
| Q26 | - |  |  | SI | Have you had jaundice or liver problems |
| Q26C | - |  |  | SI | Jaundice / Liver |
| Q26T | - |  |  | SI | Details |
| Q27 | - |  |  | SI | Do you have any physical disabilities |
| Q27A1 | - |  |  | SI | Are you able to self care |
| Q27A1T | - |  |  | SI | Details |
| Q27L | - |  |  | SI | Please review patient alerts and amend as appropri... |
| Q27T | - |  |  | SI | Details |
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