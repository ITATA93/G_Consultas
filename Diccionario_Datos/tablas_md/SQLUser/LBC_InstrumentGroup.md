# SQLUser.LBC_InstrumentGroup

**Schema:** SQLUser
**Columnas:** 138
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Laboratorio**. Parámetros del módulo de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCING_RowID | bigint | PK |  | NO | - |
| ChildQ59DR | - |  |  | SI | Child Reference: Reassessment Details |
| LBCING_CheckDemographics | varchar |  |  | SI | POCT Check Demographics
List of Demographics to c... |
| LBCING_Code | varchar |  |  | NO | Instrument Group Code |
| LBCING_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LBCING_CreatedDate | date |  |  | SI | Created Date |
| LBCING_CreatedTime | time |  |  | SI | Created Time |
| LBCING_CreatedUser_DR | bigint |  | FK | SI | Created User |
| LBCING_DateFrom | date |  |  | SI | Date From |
| LBCING_DateTo | date |  |  | SI | Date To |
| LBCING_Desc | varchar |  |  | NO | Instrument Group Description |
| LBCING_InstrumentGroupType | varchar |  |  | SI | Type of the instrument group
Standard type: LabIn... |
| LBCING_Owner | varchar |  |  | SI | Owner |
| LBCING_UpdatedDate | date |  |  | SI | Updated Date |
| LBCING_UpdatedTime | time |  |  | SI | Updated Time |
| LBCING_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Risk factors (1 Point) |
| Q02 | - |  |  | SI | Risk factors (2 Points) |
| Q03 | - |  |  | SI | Risk factors (3 Points) |
| Q04 | - |  |  | SI | Risk factors (5 Points) |
| Q05 | - |  |  | SI | Contraindications |
| Q06 | - |  |  | SI | Warning / Precautions |
| Q08 | - |  |  | SI | <=1 |
| Q09 | - |  |  | SI | 2 |
| Q10 | - |  |  | SI | 3 - 4 |
| Q11 | - |  |  | SI | >=5 |
| Q12 | - |  |  | SI | The Venous Thromboembolism Risk Assessment assesse... |
| Q13 | - |  |  | SI | Prophylaxis Regimen Guidelines |
| Q14 | - |  |  | SI | Low Risk (<=1) |
| Q15 | - |  |  | SI | Moderate Risk (=2) |
| Q16 | - |  |  | SI | High Risk (3-4) |
| Q17 | - |  |  | SI | Highest Risk (>=5) |
| Q18 | - |  |  | SI | Based on Total Risks Factor, Place an order of one... |
| Q19 | - |  |  | SI | Low Risk (<=1) |
| Q20 | - |  |  | SI | Early Ambulation |
| Q21 | - |  |  | SI | Moderate Risk (=2) |
| Q22 | - |  |  | SI | Heparin 5000 units subcutaneously every 12hours OR |
| Q23 | - |  |  | SI | Enoxaparin (Preferred) 40mg subcutaneously once da... |
| Q24 | - |  |  | SI | Enoxaparin (Preferred) 30mg subcutaneously once da... |
| Q25 | - |  |  | SI | Sequential Compression Device (SCD) |
| Q26 | - |  |  | SI | High Risk (3-4) |
| Q27 | - |  |  | SI | Early Ambulation and from the following |
| Q28 | - |  |  | SI | Heparin 5000 units subcutaneously every 8 hours OR |
| Q29 | - |  |  | SI | Enoxaparin 40mg subcutaneously once daily OR |
| Q30 | - |  |  | SI | Enoxaparin 30mg subcutaneously once daily (Creatin... |
| Q31 | - |  |  | SI | +/- Sequential Compression Device (SCD) |
| Q32 | - |  |  | SI | Highest Risk (>=5) |
| Q33 | - |  |  | SI | Heparin 5000 units subcutaneously every 8 hours OR |
| Q34 | - |  |  | SI | Enoxaparin (Preferred) 40mg subcutaneously once da... |
| Q35 | - |  |  | SI | Enoxaparin (Preferred) 30mg subcutaneously once da... |
| Q36 | - |  |  | SI | Plus: Sequential Compression Device (SCD) |
| Q37 | - |  |  | SI | Contraindications |
| Q38 | - |  |  | SI | Active bleeding |
| Q39 | - |  |  | SI | Hypersensitivity to low molecular weight heparin, ... |
| Q40 | - |  |  | SI | patient on therapeutic dose of Heparin / Enoxapari... |
| Q41 | - |  |  | SI | uncontrolled HTN(SBP>185 and/or DBP> 100 mmHg) |
| Q42 | - |  |  | SI | Epidural anesthesia (within last24hrs. or planned ... |
| Q43 | - |  |  | SI | Recent intraocular surgery or intracranial surgery |
| Q44 | - |  |  | SI | Clinically significant thromborytopenla (platelet ... |
| Q45 | - |  |  | SI | Warnings / Precautions |
| Q46 | - |  |  | SI | History of gastrointestinal bleed or Hemorrhagic s... |
| Q47 | - |  |  | SI | Renal failure w/CLa < 30mL/min. |
| Q48 | - |  |  | SI | Coagulopathy (high a PTT, PT/INR) |
| Q49 | - |  |  | SI | If the patient has any of the above, Order Sequent... |
| Q50 | - |  |  | SI | Contraindications for SCD: Gangrene, Recent Skin G... |
| Q51 | - |  |  | SI | Labs: Check baseline Complete Blood Count (CBC) an... |
| Q52 | - |  |  | SI | This is a general guideline and physician’s clnica... |
| Q53 | - |  |  | SI | Patient considerations for pharmacologic therapy: ... |
| Q54 | - |  |  | SI | Assessment type |
| Q55 | - |  |  | SI | If patient is at significant risk of bleeding or c... |
| Q56 | - |  |  | SI | No orders for prophylaxis reason |
| Q57 | - |  |  | SI | Spinal / Orthopedic surgey |
| Q58 | - |  |  | SI | As per spine / Orthopedic consultant orders (Refer... |
| Q60 | - |  |  | SI | Date |
| Q61 | - |  |  | SI | Time |
| Q62 | - |  |  | SI | Score |
| Q63 | - |  |  | SI | Classification |
| Q64 | - |  |  | SI | Low risk |
| Q65 | - |  |  | SI | Moderate risk |
| Q66 | - |  |  | SI | High risk |
| Q67 | - |  |  | SI | Highest risk |
| Q68 | - |  |  | SI | Early Ambulation |
| Q69 | - |  |  | SI | Heparin 5000 units subcutaneously every 12hours OR |
| Q70 | - |  |  | SI | Enoxaparin (Preferred) 40mg subcutaneously once da... |
| Q71 | - |  |  | SI | Enoxaparin (Preferred) 30mg subcutaneously once da... |
| Q72 | - |  |  | SI | Sequential Compression Device (SCD) |
| Q73 | - |  |  | SI | Heparin 5000 units subcutaneously every 8 hours OR |
| Q74 | - |  |  | SI | Enoxaparin 40mg subcutaneously once daily OR |
| Q75 | - |  |  | SI | Enoxaparin 30mg subcutaneously once daily (Creatin... |
| Q76 | - |  |  | SI | +/- Sequential Compression Device (SCD) |
| Q77 | - |  |  | SI | Heparin 5000 units subcutaneously every 8 hours OR |
| Q78 | - |  |  | SI | Enoxaparin (Preferred) 40mg subcutaneously once da... |
| Q79 | - |  |  | SI | Enoxaparin (Preferred) 30mg subcutaneously once da... |
| Q80 | - |  |  | SI | Plus: Sequential Compression Device (SCD) |
| Q81 | - |  |  | SI | Heparin 5000 units subcutaneously every 8 hours OR |
| Q82 | - |  |  | SI | Enoxaparin 40mg subcutaneously once daily OR |
| Q83 | - |  |  | SI | Enoxaparin 30mg subcutaneously once daily (Creatin... |
| Q84 | - |  |  | SI | +/- Sequential Compression Device (SCD) |
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