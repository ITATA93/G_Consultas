# SQLUser.ORC_Partograms

**Schema:** SQLUser
**Columnas:** 150
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Órdenes**. Parámetros de órdenes médicas.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PARTO_RowId | bigint | PK |  | NO | - |
| ChildQ39DR | - |  |  | SI | Child Reference: Intubation |
| PARTO_Code | varchar |  |  | NO | Code |
| PARTO_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| PARTO_CreatedDate | date |  |  | SI | Created Date |
| PARTO_CreatedTime | time |  |  | SI | Created Time |
| PARTO_CreatedUser_DR | bigint |  | FK | SI | Created User |
| PARTO_DateFrom | date |  |  | SI | Date From |
| PARTO_DateTo | date |  |  | SI | Date To |
| PARTO_Desc | varchar |  |  | NO | Description |
| PARTO_Owner | varchar |  |  | SI | Owner |
| PARTO_UpdatedDate | date |  |  | SI | Updated Date |
| PARTO_UpdatedTime | time |  |  | SI | Updated Time |
| PARTO_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Time |
| Q02 | - |  |  | SI | Date |
| Q03 | - |  |  | SI | Indication |
| Q04 | - |  |  | SI | Specify |
| Q05 | - |  |  | SI | Intubation Checklist |
| Q06 | - |  |  | SI | Preparation |
| Q07 | - |  |  | SI | Pre-oxygenation |
| Q08 | - |  |  | SI | Patient position |
| Q09 | - |  |  | SI | Nasal cannula at 15 l/min |
| Q10 | - |  |  | SI | Assess if this is predicted to be a difficult airw... |
| Q11 | - |  |  | SI | Adopt vortex approach - articulate the airway plan... |
| Q12 | - |  |  | SI | Post intubation ventilation, PEEP & Sedation |
| Q13 | - |  |  | SI | Equipment |
| Q14 | - |  |  | SI | Drugs |
| Q15 | - |  |  | SI | Monitoring |
| Q16 | - |  |  | SI | Is there significant cardiovascular instability? |
| Q17 | - |  |  | SI | - Consider - Starting inotropes before induction |
| Q18 | - |  |  | SI | - Consider - Reducing induction dose eg. Propofol ... |
| Q19 | - |  |  | SI | - Consider - Upper limit of muscle relaxant dose |
| Q20 | - |  |  | SI | Difficult Airway Predictors |
| Q21 | - |  |  | SI | - Look – Does it look difficult |
| Q22 | - |  |  | SI | - Inadequate 3-3-2 |
| Q23 | - |  |  | SI | - 3 Fingers between teeth |
| Q24 | - |  |  | SI | - 3 fingers under chin |
| Q25 | - |  |  | SI | - 2 above thyroid |
| Q26 | - |  |  | SI | - Mallampati 3 or 4 |
| Q27 | - |  |  | SI | - Obstruction? – Foreign body, stridor etc. |
| Q28 | - |  |  | SI | - Poor neck mobility |
| Q29 | - |  |  | SI | Decision to intubate time |
| Q30 | - |  |  | SI | ETT size |
| Q30ObsDR | - |  |  | SI | ETT size DR |
| Q31 | - |  |  | SI | ETT lip length |
| Q31ObsDR | - |  |  | SI | ETT lip length DR |
| Q32 | - |  |  | SI | Cuff pressure (cm H2O) |
| Q32ObsDR | - |  |  | SI | Cuff pressure (cm H2O) DR |
| Q33 | - |  |  | SI | ETT placement confirmation |
| Q34 | - |  |  | SI | Airway manoeuvres required |
| Q35 | - |  |  | SI | Pre-oxygenation |
| Q36 | - |  |  | SI | Apnoeic oxygenation |
| Q37 | - |  |  | SI | Patient position |
| Q38 | - |  |  | SI | Was the intubation checklist used ? |
| Q40 | - |  |  | SI | Was laryngoscopy predicted to be difficult? |
| Q41 | - |  |  | SI | If yes, why? |
| Q42 | - |  |  | SI | Was a formal assessment made? |
| Q43 | - |  |  | SI | Intubation complications |
| Q44 | - |  |  | SI | NGT or OGT placed |
| Q45 | - |  |  | SI | Urinary catheter inserted? |
| Q46 | - |  |  | SI | Catheter size (Fr) |
| Q47 | - |  |  | SI | Post intubation chest x-ray required? |
| Q48 | - |  |  | SI | Notes |
| Q49 | - |  |  | SI | Post intubation sedation and analgesia ordered? |
| Q50 | - |  |  | SI | Notes |
| Q51 | - |  |  | SI | Is there significant cardiovascular instability? |
| Q52 | - |  |  | SI | - Consider - Starting inotropes before induction |
| Q53 | - |  |  | SI | - Consider - Reducing induction dose eg. Propofol ... |
| Q54 | - |  |  | SI | - Consider - Upper limit of muscle relaxant dose |
| Q55 | - |  |  | SI | Difficult Airway Predictors |
| Q56 | - |  |  | SI | - Look – Does it look difficult |
| Q57 | - |  |  | SI | - Inadequate 3-3-2 |
| Q58 | - |  |  | SI | - 3 Fingers between teeth |
| Q59 | - |  |  | SI | - 3 fingers under chin |
| Q60 | - |  |  | SI | - 2 above thyroid |
| Q61 | - |  |  | SI | - Mallampati 3 or 4 |
| Q62 | - |  |  | SI | - Obstruction? – Foreign body, stridor etc. |
| Q63 | - |  |  | SI | - Poor neck mobility |
| Q64 | - |  |  | SI | Nasogastric tube (NGT) |
| Q65 | - |  |  | SI | Orogastric tube (OGT) |
| Q66 | - |  |  | SI | Endotracheal tube (ETT) |
| Q67 | - |  |  | SI | Laryngeal mask (LMA) |
| Q68 | - |  |  | SI | Non-invasive blood pressure (NIBP) |
| Q69 | - |  |  | SI | Sa02 (Oxygen Saturation) |
| Q70 | - |  |  | SI | Electrocardiogram (ECG) |
| Q71 | - |  |  | SI | End-tidal carbon dioxide (ETCO2) |
| Q72 | - |  |  | SI | Team leader |
| Q73 | - |  |  | SI | Estimated patient weight |
| Q73ObsDR | - |  |  | SI | Estimated patient weight DR |
| Q74 | - |  |  | SI | NGT/OGT size (Fr) |
| Q76 | - |  |  | SI | Decision to intubate date |
| Q77 | - |  |  | SI | Intubation date |
| Q78 | - |  |  | SI | Intubation time |
| Q79 | - |  |  | SI | ETT cuffed |
| Q80 | - |  |  | SI | Cormack and Lehane grade |
| Q81 | - |  |  | SI | Grade I: Most of the glottis is visible) |
| Q82 | - |  |  | SI | Grade II: Only the posterior extremity of the glot... |
| Q83 | - |  |  | SI | Grade III: No part of the glottis can be seen, onl... |
| Q84 | - |  |  | SI | Grade IV: No part of the epiglottis can be seen |
| Q85 | - |  |  | SI | Cormack, R.S. |
| Q86 | - |  |  | SI | Grade I |
| Q87 | - |  |  | SI | Grade II |
| Q88 | - |  |  | SI | Grade III |
| Q89 | - |  |  | SI | Grade IV |
| Q90 | - |  |  | SI | Abbreviation Key |
| Q91 | - |  |  | SI | ETT measurement (cm) |
| Q91ObsDR | - |  |  | SI | ETT measurement (cm) DR |
| Q92 | - |  |  | SI | Positive end-expiratory pressure (PEEP) |
| Q94 | - |  |  | SI | Positive end-expiratory pressure (PEEP) |
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