# questionnaire.QTCRDC

> Revised Duke Criteria (Li) for Infective Endocarditis

**Schema:** questionnaire
**Columnas:** 98
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Revised Duke Criteria (Li) for Infective Endocarditis

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | Microorganisms in a vegetation |
| Q04 | varchar |  |  | SI | Demonstrated by culture or histologic examination ... |
| Q05 | varchar |  |  | SI | Pathologic lesions |
| Q06 | varchar |  |  | SI | Vegetation or intracardiac abscess confirmed by hi... |
| Q07 | varchar |  |  | SI | Blood cultures positive for endocarditis |
| Q08 | varchar |  |  | SI | Typical microorganisms consistent with infective e... |
| Q09 | varchar |  |  | SI | single positive blood culture for Coxiella burneti... |
| Q10 | varchar |  |  | SI | Evidence of endocardial involvement |
| Q11 | varchar |  |  | SI | Echocardiogram positive for infective endocarditis... |
| Q12 | varchar |  |  | SI | Predisposing heart condition or injection drug use |
| Q13 | varchar |  |  | SI | Fever |
| Q14 | varchar |  |  | SI | Vascular phenomena |
| Q15 | varchar |  |  | SI | Major arterial emboli, septic pulmonary infarcts, ... |
| Q16 | varchar |  |  | SI | Immunologic phenomena |
| Q17 | varchar |  |  | SI | Glomerulonephritis, Osler’s nodes, Roth’s spots, a... |
| Q18 | varchar |  |  | SI | Microbiological evidence |
| Q19 | varchar |  |  | SI | Positive blood culture but does not meet a major c... |
| Q20 | varchar |  |  | SI | Do any of the following exclusion criteria apply? |
| Q21 | varchar |  |  | SI | Suspect infective endocarditis and consider the Du... |
| Q22 | varchar |  |  | SI | • Prolonged fever of unknown origin) |
| Q23 | varchar |  |  | SI | • Fever and vascular phenomena (stroke, limb ische... |
| Q24 | varchar |  |  | SI | • Persistently positive blood cultures (2 or more)... |
| Q25 | varchar |  |  | SI | • Prosthetic valves who are febrile. |
| Q26 | varchar |  |  | SI | • Injection drug users who are febrile. |
| Q27 | varchar |  |  | SI | • A pre-disposing heart condition who are febrile. |
| Q28 | varchar |  |  | SI | • Fever with a recent history of hospitalization. |
| Q29 | varchar |  |  | SI | 'Definite' Infective Endocarditis: |
| Q30 | varchar |  |  | SI | • One or more Pathologic criteria, or |
| Q31 | varchar |  |  | SI | • 2 major criteria, or |
| Q32 | varchar |  |  | SI | • 1 major and 3 minor criteria, or |
| Q33 | varchar |  |  | SI | • 5 minor criteria |
| Q34 | varchar |  |  | SI | 'Possible' Infective Endocarditis: |
| Q35 | varchar |  |  | SI | • 1 major criterion and 1 minor criterion, or |
| Q36 | varchar |  |  | SI | • 3 minor criterion |
| Q37 | varchar |  |  | SI | 'Rejected' Infective Endocarditis: |
| Q38 | varchar |  |  | SI | • Firm alternative diagnosis explaining evidence o... |
| Q39 | varchar |  |  | SI | • Resolution of IE symptoms with antibiotics for l... |
| Q40 | varchar |  |  | SI | • No pathological evidence of IE at surgery or aut... |
| Q41 | varchar |  |  | SI | • Does not meet criteria of 'possible', as above. |
| Q42 | varchar |  |  | SI | Score |
| Q43 | varchar |  |  | SI | Classification |
| Q44 | varchar |  |  | SI | ≥ 10 |
| Q45 | varchar |  |  | SI | Definite infective endocarditis |
| Q46 | varchar |  |  | SI | 6 - 9 |
| Q47 | varchar |  |  | SI | Possible infective endocarditis |
| Q48 | varchar |  |  | SI | ≤ 5 |
| Q49 | varchar |  |  | SI | Rejected for infective endocarditis |
| Q50 | varchar |  |  | SI | ≥ 10: Definite infective endocarditis |
| Q51 | varchar |  |  | SI | 6 - 9: Possible infective endocarditis |
| Q52 | varchar |  |  | SI | ≤ 5: Rejected for infective endocarditis |
| Q53 | varchar |  |  | SI | The Duke Criteria is a tool used to diagnose infec... |
| Q54 | varchar |  |  | SI | This criteria is sensitive for disease detection, ... |
| Q55 | varchar |  |  | SI | Rejected for infective endocarditis |
| Q56 | varchar |  |  | SI | Definite infective endocarditis |
| Q57 | varchar |  |  | SI | Possible infective endocarditis |
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