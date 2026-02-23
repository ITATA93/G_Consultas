# SQLUser.PAC_UnplannedReadmission

**Schema:** SQLUser
**Columnas:** 110
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| UNPLREAD_RowId | bigint | PK |  | NO | - |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Microorganisms in a vegetation |
| Q04 | - |  |  | SI | Demonstrated by culture or histologic examination ... |
| Q05 | - |  |  | SI | Pathologic lesions |
| Q06 | - |  |  | SI | Vegetation or intracardiac abscess confirmed by hi... |
| Q07 | - |  |  | SI | Blood cultures positive for endocarditis |
| Q08 | - |  |  | SI | Typical microorganisms consistent with infective e... |
| Q09 | - |  |  | SI | single positive blood culture for Coxiella burneti... |
| Q10 | - |  |  | SI | Evidence of endocardial involvement |
| Q11 | - |  |  | SI | Echocardiogram positive for infective endocarditis... |
| Q12 | - |  |  | SI | Predisposing heart condition or injection drug use |
| Q13 | - |  |  | SI | Fever |
| Q14 | - |  |  | SI | Vascular phenomena |
| Q15 | - |  |  | SI | Major arterial emboli, septic pulmonary infarcts, ... |
| Q16 | - |  |  | SI | Immunologic phenomena |
| Q17 | - |  |  | SI | Glomerulonephritis, Osler’s nodes, Roth’s spots, a... |
| Q18 | - |  |  | SI | Microbiological evidence |
| Q19 | - |  |  | SI | Positive blood culture but does not meet a major c... |
| Q20 | - |  |  | SI | Do any of the following exclusion criteria apply? |
| Q21 | - |  |  | SI | Suspect infective endocarditis and consider the Du... |
| Q22 | - |  |  | SI | • Prolonged fever of unknown origin) |
| Q23 | - |  |  | SI | • Fever and vascular phenomena (stroke, limb ische... |
| Q24 | - |  |  | SI | • Persistently positive blood cultures (2 or more)... |
| Q25 | - |  |  | SI | • Prosthetic valves who are febrile. |
| Q26 | - |  |  | SI | • Injection drug users who are febrile. |
| Q27 | - |  |  | SI | • A pre-disposing heart condition who are febrile. |
| Q28 | - |  |  | SI | • Fever with a recent history of hospitalization. |
| Q29 | - |  |  | SI | Definite' Infective Endocarditis: |
| Q30 | - |  |  | SI | • One or more Pathologic criteria, or |
| Q31 | - |  |  | SI | • 2 major criteria, or |
| Q32 | - |  |  | SI | • 1 major and 3 minor criteria, or |
| Q33 | - |  |  | SI | • 5 minor criteria |
| Q34 | - |  |  | SI | Possible' Infective Endocarditis: |
| Q35 | - |  |  | SI | • 1 major criterion and 1 minor criterion, or |
| Q36 | - |  |  | SI | • 3 minor criterion |
| Q37 | - |  |  | SI | Rejected' Infective Endocarditis: |
| Q38 | - |  |  | SI | • Firm alternative diagnosis explaining evidence o... |
| Q39 | - |  |  | SI | • Resolution of IE symptoms with antibiotics for l... |
| Q40 | - |  |  | SI | • No pathological evidence of IE at surgery or aut... |
| Q41 | - |  |  | SI | • Does not meet criteria of 'possible', as above. |
| Q42 | - |  |  | SI | Score |
| Q43 | - |  |  | SI | Classification |
| Q44 | - |  |  | SI | ≥ 10 |
| Q45 | - |  |  | SI | Definite infective endocarditis |
| Q46 | - |  |  | SI | 6 - 9 |
| Q47 | - |  |  | SI | Possible infective endocarditis |
| Q48 | - |  |  | SI | ≤ 5 |
| Q49 | - |  |  | SI | Rejected for infective endocarditis |
| Q50 | - |  |  | SI | ≥ 10: Definite infective endocarditis |
| Q51 | - |  |  | SI | 6 - 9: Possible infective endocarditis |
| Q52 | - |  |  | SI | ≤ 5: Rejected for infective endocarditis |
| Q53 | - |  |  | SI | The Duke Criteria is a tool used to diagnose infec... |
| Q54 | - |  |  | SI | This criteria is sensitive for disease detection, ... |
| Q55 | - |  |  | SI | Rejected for infective endocarditis |
| Q56 | - |  |  | SI | Definite infective endocarditis |
| Q57 | - |  |  | SI | Possible infective endocarditis |
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
| UNPLREAD_Code | varchar |  |  | NO | Code |
| UNPLREAD_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| UNPLREAD_CreatedDate | date |  |  | SI | Created Date |
| UNPLREAD_CreatedTime | time |  |  | SI | Created Time |
| UNPLREAD_CreatedUser_DR | bigint |  | FK | SI | Created User |
| UNPLREAD_DateFrom | date |  |  | SI | Date From |
| UNPLREAD_DateTo | date |  |  | SI | Date To |
| UNPLREAD_Desc | varchar |  |  | NO | Description |
| UNPLREAD_Owner | varchar |  |  | SI | Owner |
| UNPLREAD_UpdatedDate | date |  |  | SI | Updated Date |
| UNPLREAD_UpdatedTime | time |  |  | SI | Updated Time |
| UNPLREAD_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*