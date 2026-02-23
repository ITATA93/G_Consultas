# SQLUser.OR_An_Oper_BiopsiesGastric

**Schema:** SQLUser
**Columnas:** 128
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Pabellón Quirúrgico**. Gestión de cirugías.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| OPBG_ParRef | varchar | PK |  | NO | OR_Anaest_Operation Parent Reference |
| OPBG_Childsub | double |  |  | NO | Childsub |
| OPBG_RowId | varchar |  |  | NO | - |
| OPBG_Type_DR | bigint |  | FK | SI | Des Ref StatePPP |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Constitutional |
| Q04 | - |  |  | SI | Lymphadenopathy |
| Q05 | - |  |  | SI | Glandular |
| Q06 | - |  |  | SI | Articular |
| Q07 | - |  |  | SI | Cutaneous |
| Q08 | - |  |  | SI | Pulmonary |
| Q09 | - |  |  | SI | Renal |
| Q10 | - |  |  | SI | Muscular |
| Q11 | - |  |  | SI | Peripheral nervous system |
| Q12 | - |  |  | SI | Central nervous system |
| Q13 | - |  |  | SI | Haematological |
| Q14 | - |  |  | SI | Biological |
| Q15 | - |  |  | SI | Score |
| Q16 | - |  |  | SI | Constitutional - Exclusion of fever of infectious ... |
| Q17 | - |  |  | SI | No: Absence of the following symptoms |
| Q18 | - |  |  | SI | Low: Mild or intermittent fever (37.5o-38.5oC) / n... |
| Q19 | - |  |  | SI | Moderate: Severe fever (>38.5oC) / night sweats an... |
| Q20 | - |  |  | SI | Lymphadenopathy - Exclusion of infection |
| Q21 | - |  |  | SI | No: Absence of the following features |
| Q22 | - |  |  | SI | Low: Lymphadenopathy ≥ 1 cm in any nodal region or... |
| Q23 | - |  |  | SI | Moderate: Lymphadenopathy ≥ 2 cm in any nodal regi... |
| Q24 | - |  |  | SI | High: Current malignant B-cell proliferative disor... |
| Q25 | - |  |  | SI | Glandular - Exclusion of stone or infection |
| Q26 | - |  |  | SI | No: Absence of glandular swelling |
| Q27 | - |  |  | SI | Low: Small glandular swelling with enlarged paroti... |
| Q28 | - |  |  | SI | Moderate: Major glandular swelling with enlarged p... |
| Q29 | - |  |  | SI | Articular - Exclusion of osteoarthritis |
| Q30 | - |  |  | SI | No: Absence of current active articular involvemen... |
| Q31 | - |  |  | SI | Low: Arthralgias in hands, wrists, ankles and feet... |
| Q32 | - |  |  | SI | Moderate: 1 to 5 (of 28 total count) synovitis |
| Q33 | - |  |  | SI | High: ≥6 (of 28 total count) synovitis |
| Q34 | - |  |  | SI | Cutaneous - Rate as ''No Activity'' stable long-la... |
| Q35 | - |  |  | SI | No: Absence of currently active cutaneous involvem... |
| Q36 | - |  |  | SI | Low: Erythema multiforma |
| Q37 | - |  |  | SI | Moderate: Limited cutaneous vasculitis, including ... |
| Q38 | - |  |  | SI | High: Diffuse cutaneous vasculitis, including urti... |
| Q39 | - |  |  | SI | Pulmonary - Rate as ''No activity'' stable long-la... |
| Q40 | - |  |  | SI | No: Absence of currently active pulmonary involvem... |
| Q41 | - |  |  | SI | Low: Persistent cough or bronchial involvement wit... |
| Q42 | - |  |  | SI | No breathlessness and normal lung function test |
| Q43 | - |  |  | SI | Moderate: Moderately active pulmonary involvement,... |
| Q44 | - |  |  | SI | (New York heart association classification (NHYA) ... |
| Q45 | - |  |  | SI | High: Highly active pulmonary involvement, such as... |
| Q46 | - |  |  | SI | Renal - Rate as ''No activity'' stable long-lastin... |
| Q47 | - |  |  | SI | No: Absence of currently active renal involvement ... |
| Q48 | - |  |  | SI | Low: Evidence of mild active renal involvement, li... |
| Q49 | - |  |  | SI | Moderate: Moderately active renal involvement, suc... |
| Q50 | - |  |  | SI | renal failure (GFR ≥60 ml/min) or histological evi... |
| Q51 | - |  |  | SI | High: Highly active renal involvement, such as glo... |
| Q52 | - |  |  | SI | histological evidence of proliferative glomerulone... |
| Q53 | - |  |  | SI | Muscular - Exclusion of weakness due to corticoste... |
| Q54 | - |  |  | SI | No: Absence of currently active muscular involveme... |
| Q55 | - |  |  | SI | Low: Mild active myositis shown by abnormal electr... |
| Q56 | - |  |  | SI | Moderate: Moderately active myositis proven by abn... |
| Q57 | - |  |  | SI | High: Highly active myositis shown by abnormal EMG... |
| Q58 | - |  |  | SI | Peripheral Nervous System (PNS) - Rate as No activ... |
| Q59 | - |  |  | SI | No: Absence of currently active PNS involvement |
| Q60 | - |  |  | SI | Low: Mild active PNS involvement, such as pure sen... |
| Q61 | - |  |  | SI | Moderate: Moderately active PNS involvement shown ... |
| Q62 | - |  |  | SI | ganglionopathy with symptoms restricted to mild / ... |
| Q63 | - |  |  | SI | or cranial nerve involvement of peripheral origin ... |
| Q64 | - |  |  | SI | High: Highly active PNS involvement shown by NCS, ... |
| Q65 | - |  |  | SI | severe ataxia due to ganglionopathy, inflammatory ... |
| Q66 | - |  |  | SI | Central Nervous System (CNS) - Rate as “No activit... |
| Q67 | - |  |  | SI | No: Absence of currently active CNS involvement |
| Q68 | - |  |  | SI | Low: Moderately active CNS features, such as crani... |
| Q69 | - |  |  | SI | optic neuritis or multiple sclerosis-like syndrome... |
| Q70 | - |  |  | SI | Moderate: Highly active CNS features, such as cere... |
| Q71 | - |  |  | SI | transverse myelitis, lymphocytic meningitis, multi... |
| Q72 | - |  |  | SI | Haematological - For anaemia, neutropenia, and thr... |
| Q73 | - |  |  | SI | No: Absence of auto-immune cytopenia |
| Q74 | - |  |  | SI | Low: Cytopenia of auto-immune origin with neutrope... |
| Q75 | - |  |  | SI | and/or anemia (10 < hemoglobin < 12 g/dl), and/or ... |
| Q76 | - |  |  | SI | Moderate: Cytopenia of auto-immune origin with neu... |
| Q77 | - |  |  | SI | and/or anemia (8 ≤ hemoglobin ≤ 10 g/dl), and/or t... |
| Q78 | - |  |  | SI | High: Cytopenia of auto-immune origin with neutrop... |
| Q79 | - |  |  | SI | Biological |
| Q80 | - |  |  | SI | No: Absence of any of the following biological fea... |
| Q81 | - |  |  | SI | Low: Clonal component and/or hypocomplementemia (l... |
| Q82 | - |  |  | SI | Moderate: Presence of cryoglobulinemia and/or hype... |
| Q83 | - |  |  | SI | The EULAR Sjogren's syndrome (SS) disease activity... |
| Q84 | - |  |  | SI | renal failure (glomerular filtration rate (GFR) ≥6... |
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