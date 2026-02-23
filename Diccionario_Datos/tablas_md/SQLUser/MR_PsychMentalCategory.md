# SQLUser.MR_PsychMentalCategory

**Schema:** SQLUser
**Columnas:** 160
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| MC_ParRef | varchar | PK |  | NO | MR_PsychDetails Parent Reference |
| MC_Childsub | double |  |  | NO | Childsub |
| MC_DateFrom | date |  |  | SI | DateFrom |
| MC_DateTo | date |  |  | SI | DateTo |
| MC_MentalCateg_DR | bigint |  | FK | SI | Des Ref MentalCateg |
| MC_RowId | varchar |  |  | NO | - |
| MC_TimeFrom | time |  |  | SI | TimeFrom |
| Q01 | - |  |  | SI | Surgical Positioning |
| Q02 | - |  |  | SI | Safety Straps Applied |
| Q03 | - |  |  | SI | Position |
| Q04 | - |  |  | SI | canceled |
| Q05 | - |  |  | SI | The Patient is free from apparent injury |
| Q06 | - |  |  | SI | Chemical Agents |
| Q07 | - |  |  | SI | Shave Preparation |
| Q08 | - |  |  | SI | Skin Preparation |
| Q09 | - |  |  | SI | Irrigation Solution |
| Q10 | - |  |  | SI | Antibiotics |
| Q100 | - |  |  | SI | Start Date |
| Q101 | - |  |  | SI | Patient Outcome: |
| Q102 | - |  |  | SI | Patient Outcome: |
| Q103 | - |  |  | SI | Patient Outcome: |
| Q104 | - |  |  | SI | Patient Outcome: |
| Q105 | - |  |  | SI | Patient Outcome: |
| Q106 | - |  |  | SI | Potential of injury related to: |
| Q107 | - |  |  | SI | Position |
| Q108 | - |  |  | SI | Laser |
| Q109 | - |  |  | SI | Other |
| Q11 | - |  |  | SI | Other |
| Q110 | - |  |  | SI | Additional Equipments |
| Q111 | - |  |  | SI | Equipment Notes |
| Q112 | - |  |  | SI | Implants / Devices |
| Q113 | - |  |  | SI | Implants / Devices Notes |
| Q12 | - |  |  | SI | Added to Irrigation |
| Q13 | - |  |  | SI | Physical Hazards |
| Q14 | - |  |  | SI | Bair Hugger |
| Q15 | - |  |  | SI | Full Body |
| Q16 | - |  |  | SI | Lower Body |
| Q17 | - |  |  | SI | Space Blanket |
| Q18 | - |  |  | SI | Sequential Compression Device (SCD) applied |
| Q19 | - |  |  | SI | Right leg only |
| Q20 | - |  |  | SI | Left leg only |
| Q21 | - |  |  | SI | Tourniquet Right |
| Q22 | - |  |  | SI | Applied |
| Q23 | - |  |  | SI | Down |
| Q24 | - |  |  | SI | Pressure |
| Q25 | - |  |  | SI | Tourniquet left |
| Q26 | - |  |  | SI | Applied |
| Q27 | - |  |  | SI | Down |
| Q28 | - |  |  | SI | Pressure |
| Q29 | - |  |  | SI | Imaging |
| Q30 | - |  |  | SI | Single Exposure |
| Q31 | - |  |  | SI | Intraoperative X-Ray |
| Q32 | - |  |  | SI | Patient Outcome |
| Q33 | - |  |  | SI | Skin Integrity Not Altered |
| Q34 | - |  |  | SI | Electrical Hazards |
| Q35 | - |  |  | SI | Diathermy |
| Q36 | - |  |  | SI | Unit Number |
| Q37 | - |  |  | SI | Monopolar |
| Q38 | - |  |  | SI | Bipolar |
| Q39 | - |  |  | SI | Settings 1: |
| Q40 | - |  |  | SI | Coagulation: |
| Q41 | - |  |  | SI | Cutting: |
| Q42 | - |  |  | SI | Blend: |
| Q43 | - |  |  | SI | Setting 2: |
| Q44 | - |  |  | SI | Coagulation: |
| Q45 | - |  |  | SI | Cutting: |
| Q46 | - |  |  | SI | Blend: |
| Q47 | - |  |  | SI | Plate Placement |
| Q48 | - |  |  | SI | Plate Placement |
| Q49 | - |  |  | SI | Electrical Hazards |
| Q50 | - |  |  | SI | Skin Integrity Not Altered |
| Q51 | - |  |  | SI | Potential For Infection Related To Surgical Interv... |
| Q52 | - |  |  | SI | Surgical Wound Classification |
| Q53 | - |  |  | SI | Dressing Applied Using Aseptic Technique |
| Q54 | - |  |  | SI | Skin Closure |
| Q55 | - |  |  | SI | Dressing Type |
| Q56 | - |  |  | SI | Skin Closure |
| Q57 | - |  |  | SI | Dressing Type |
| Q58 | - |  |  | SI | Skin Closure |
| Q59 | - |  |  | SI | Dressing Type |
| Q60 | - |  |  | SI | Catheter |
| Q61 | - |  |  | SI | Straight |
| Q62 | - |  |  | SI | Foley |
| Q63 | - |  |  | SI | 3 Way |
| Q64 | - |  |  | SI | Size |
| Q65 | - |  |  | SI | Bulb fill: |
| Q66 | - |  |  | SI | Inserted By |
| Q67 | - |  |  | SI | No Known Potential For Infection Related To Intra-... |
| Q68 | - |  |  | SI | Potential For Alteration in Fluid And Electrolyte |
| Q69 | - |  |  | SI | Chest Tube |
| Q70 | - |  |  | SI | Size: |
| Q71 | - |  |  | SI | Site: |
| Q72 | - |  |  | SI | Suture: |
| Q73 | - |  |  | SI | Chest tube |
| Q74 | - |  |  | SI | Size: |
| Q75 | - |  |  | SI | Site: |
| Q76 | - |  |  | SI | Suture: |
| Q77 | - |  |  | SI | Chest Tube |
| Q78 | - |  |  | SI | Size: |
| Q79 | - |  |  | SI | Site: |
| Q80 | - |  |  | SI | Suture: |
| Q81 | - |  |  | SI | Nasogastric |
| Q82 | - |  |  | SI | Betadine Plug |
| Q83 | - |  |  | SI | Plain Gauze Pack |
| Q84 | - |  |  | SI | Hemovac |
| Q85 | - |  |  | SI | Cell Saver |
| Q86 | - |  |  | SI | Blood Available in : |
| Q87 | - |  |  | SI | The Patient's Fluid and Electrolyte balance is mai... |
| Q88 | - |  |  | SI | No alteration to skin integrity |
| Q89 | - |  |  | SI | Start Time |
| Q90 | - |  |  | SI | End Time |
| Q91 | - |  |  | SI | Specify others |
| Q92 | - |  |  | SI | Positioning Aids |
| Q93 | - |  |  | SI | 2 Way |
| Q94 | - |  |  | SI | Silicon |
| Q95 | - |  |  | SI | Size: |
| Q96 | - |  |  | SI | Notes |
| Q97 | - |  |  | SI | Notes |
| Q98 | - |  |  | SI | size text |
| Q99 | - |  |  | SI | End Date |
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