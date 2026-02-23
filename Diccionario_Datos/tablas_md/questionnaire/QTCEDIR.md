# questionnaire.QTCEDIR

> Intubation Record

**Schema:** questionnaire
**Columnas:** 137
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Intubation Record

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | time |  |  | SI | Time |
| Q02 | date |  |  | SI | Date |
| Q03 | varchar |  |  | SI | Indication |
| Q04 | varchar |  |  | SI | Specify |
| Q05 | varchar |  |  | SI | Intubation Checklist |
| Q06 | varchar |  |  | SI | Preparation |
| Q07 | varchar |  |  | SI | Pre-oxygenation |
| Q08 | varchar |  |  | SI | Patient position |
| Q09 | varchar |  |  | SI | Nasal cannula at 15 l/min |
| Q10 | varchar |  |  | SI | Assess if this is predicted to be a difficult airw... |
| Q11 | varchar |  |  | SI | Adopt vortex approach - articulate the airway plan... |
| Q12 | varchar |  |  | SI | Post intubation ventilation, PEEP & Sedation |
| Q13 | varchar |  |  | SI | Equipment |
| Q14 | varchar |  |  | SI | Drugs |
| Q15 | varchar |  |  | SI | Monitoring |
| Q16 | varchar |  |  | SI | Is there significant cardiovascular instability? |
| Q17 | varchar |  |  | SI |  - Consider - Starting inotropes before induction |
| Q18 | varchar |  |  | SI |  - Consider - Reducing induction dose eg. Propofol... |
| Q19 | varchar |  |  | SI | - Consider - Upper limit of muscle relaxant dose |
| Q20 | varchar |  |  | SI | Difficult Airway Predictors |
| Q21 | varchar |  |  | SI | - Look – Does it look difficult |
| Q22 | varchar |  |  | SI | - Inadequate 3-3-2 |
| Q23 | varchar |  |  | SI | - 3 Fingers between teeth |
| Q24 | varchar |  |  | SI | - 3 fingers under chin |
| Q25 | varchar |  |  | SI |  - 2 above thyroid |
| Q26 | varchar |  |  | SI | - Mallampati 3 or 4 |
| Q27 | varchar |  |  | SI | - Obstruction? – Foreign body, stridor etc. |
| Q28 | varchar |  |  | SI | - Poor neck mobility |
| Q29 | time |  |  | SI | Decision to intubate time |
| Q30 | varchar |  |  | SI | ETT size |
| Q30ObsDR | varchar |  | FK | SI | ETT size DR |
| Q31 | varchar |  |  | SI | ETT lip length |
| Q31ObsDR | varchar |  | FK | SI | ETT lip length DR |
| Q32 | varchar |  |  | SI | Cuff pressure (cm H2O) |
| Q32ObsDR | varchar |  | FK | SI | Cuff pressure (cm H2O) DR |
| Q33 | varchar |  |  | SI | ETT placement confirmation |
| Q34 | varchar |  |  | SI | Airway manoeuvres required |
| Q35 | varchar |  |  | SI | Pre-oxygenation |
| Q36 | varchar |  |  | SI | Apnoeic oxygenation |
| Q37 | varchar |  |  | SI | Patient position |
| Q38 | varchar |  |  | SI | Was the intubation checklist used ? |
| Q40 | varchar |  |  | SI | Was laryngoscopy predicted to be difficult? |
| Q41 | varchar |  |  | SI | If yes, why? |
| Q42 | varchar |  |  | SI | Was a formal assessment made? |
| Q43 | varchar |  |  | SI | Intubation complications |
| Q44 | varchar |  |  | SI | NGT or OGT placed |
| Q45 | varchar |  |  | SI | Urinary catheter inserted? |
| Q46 | numeric |  |  | SI | Catheter size (Fr) |
| Q47 | varchar |  |  | SI | Post intubation chest x-ray required? |
| Q48 | varchar |  |  | SI | Notes |
| Q49 | varchar |  |  | SI | Post intubation sedation and analgesia ordered? |
| Q50 | varchar |  |  | SI | Notes |
| Q51 | varchar |  |  | SI | Is there significant cardiovascular instability? |
| Q52 | varchar |  |  | SI |  - Consider - Starting inotropes before induction |
| Q53 | varchar |  |  | SI |  - Consider - Reducing induction dose eg. Propofol... |
| Q54 | varchar |  |  | SI | - Consider - Upper limit of muscle relaxant dose |
| Q55 | varchar |  |  | SI | Difficult Airway Predictors  |
| Q56 | varchar |  |  | SI | - Look – Does it look difficult |
| Q57 | varchar |  |  | SI | - Inadequate 3-3-2 |
| Q58 | varchar |  |  | SI | - 3 Fingers between teeth |
| Q59 | varchar |  |  | SI | - 3 fingers under chin |
| Q60 | varchar |  |  | SI |  - 2 above thyroid |
| Q61 | varchar |  |  | SI | - Mallampati 3 or 4 |
| Q62 | varchar |  |  | SI | - Obstruction? – Foreign body, stridor etc. |
| Q63 | varchar |  |  | SI | - Poor neck mobility |
| Q64 | varchar |  |  | SI | Nasogastric tube (NGT) |
| Q65 | varchar |  |  | SI | Orogastric tube (OGT) |
| Q66 | varchar |  |  | SI | Endotracheal tube (ETT) |
| Q67 | varchar |  |  | SI | Laryngeal mask (LMA) |
| Q68 | varchar |  |  | SI | Non-invasive blood pressure (NIBP) |
| Q69 | varchar |  |  | SI | Sa02 (Oxygen Saturation) |
| Q70 | varchar |  |  | SI | Electrocardiogram (ECG) |
| Q71 | varchar |  |  | SI | End-tidal carbon dioxide (ETCO2) |
| Q72 | varchar |  |  | SI | Team leader |
| Q73 | varchar |  |  | SI | Estimated patient weight |
| Q73ObsDR | varchar |  | FK | SI | Estimated patient weight DR |
| Q74 | numeric |  |  | SI | NGT/OGT size (Fr) |
| Q76 | date |  |  | SI | Decision to intubate date |
| Q77 | date |  |  | SI | Intubation date |
| Q78 | time |  |  | SI | Intubation time |
| Q79 | varchar |  |  | SI | ETT cuffed |
| Q80 | varchar |  |  | SI | Cormack and Lehane grade |
| Q81 | varchar |  |  | SI | Grade I: Most of the glottis is visible) |
| Q82 | varchar |  |  | SI | Grade II: Only the posterior extremity of the glot... |
| Q83 | varchar |  |  | SI | Grade III: No part of the glottis can be seen, onl... |
| Q84 | varchar |  |  | SI | Grade IV: No part of the epiglottis can be seen |
| Q85 | varchar |  |  | SI | Cormack, R.S.; Lehane, J. (1984). ''Difficult trac... |
| Q86 | varchar |  |  | SI | Grade I |
| Q87 | varchar |  |  | SI | Grade II |
| Q88 | varchar |  |  | SI | Grade III |
| Q89 | varchar |  |  | SI | Grade IV |
| Q90 | varchar |  |  | SI | Abbreviation Key |
| Q91 | varchar |  |  | SI | ETT measurement (cm) |
| Q91ObsDR | varchar |  | FK | SI | ETT measurement (cm) DR |
| Q92 | varchar |  |  | SI | Positive end-expiratory pressure (PEEP) |
| Q94 | varchar |  |  | SI | Positive end-expiratory pressure (PEEP) |
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