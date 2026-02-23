# SQLUser.OEOrd_PharmacyReviewStatus

**Schema:** SQLUser
**Columnas:** 135
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Estados posibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PHREVST_ParRef | varchar | PK |  | NO | - |
| PHREVST_Childsub | double |  |  | NO | OE_OrdItem Parent Reference
Childsub |
| PHREVST_Date | date |  |  | SI | Date |
| PHREVST_DateReviewed | date |  |  | SI | DateReviewed |
| PHREVST_RowId | varchar |  |  | NO | - |
| PHREVST_Status_DR | bigint |  | FK | SI | Des Ref ReviewStatus |
| PHREVST_Time | time |  |  | SI | Time |
| PHREVST_TimeReviewed | time |  |  | SI | TimeReviewed |
| PHREVST_User_DR | bigint |  | FK | SI | Des Ref User |
| Q01 | - |  |  | SI | Cardiac arrest and/or countershock within past 48h |
| Q02 | - |  |  | SI | Controlled ventilation with or without PEEP |
| Q03 | - |  |  | SI | Controlled ventilation with intermittent or contin... |
| Q04 | - |  |  | SI | Balloon tamponade of varices |
| Q05 | - |  |  | SI | Continuous arterial infusion |
| Q06 | - |  |  | SI | Pulmonary artery catheter |
| Q07 | - |  |  | SI | Atrial and/or ventricular pacing |
| Q08 | - |  |  | SI | Hemodialysis in unstable patient |
| Q09 | - |  |  | SI | Peritoneal dialysis |
| Q10 | - |  |  | SI | Induced hypothermia |
| Q11 | - |  |  | SI | Pressure-activated blood infusion |
| Q12 | - |  |  | SI | G-suit. |
| Q13 | - |  |  | SI | Intracranial pressure monitoring |
| Q14 | - |  |  | SI | Platelet transfusion |
| Q15 | - |  |  | SI | IABP (Intra Aortic Balloon Pressure) |
| Q16 | - |  |  | SI | Emergency operative procedures (within past 24 h) |
| Q17 | - |  |  | SI | Lavage of acute GI bleeding |
| Q18 | - |  |  | SI | Emergency endoscopy or bronchoscopy |
| Q19 | - |  |  | SI | Vasoactive drug infusion (> 1 drug) |
| Q20 | - |  |  | SI | Central IV hyperalimentation (includes renal, card... |
| Q21 | - |  |  | SI | Pacemaker on standby |
| Q22 | - |  |  | SI | Chest tubes |
| Q23 | - |  |  | SI | IMV or assisted ventilation |
| Q24 | - |  |  | SI | CPAP |
| Q25 | - |  |  | SI | Concentrated K+ infusion via central catheter |
| Q26 | - |  |  | SI | Nasotracheal or orotracheal intubation |
| Q27 | - |  |  | SI | Blind intratracheal suctioning |
| Q28 | - |  |  | SI | Complex metabolic balance (frequent intake and out... |
| Q29 | - |  |  | SI | Multiple ABG, bleeding, and/or STAT studies (> 4 s... |
| Q30 | - |  |  | SI | Frequent infusion of blood products (>5 units /24 ... |
| Q31 | - |  |  | SI | Bolus IV medication (nonscheduled) |
| Q32 | - |  |  | SI | Vasoactive drug infusion (1 drug) |
| Q33 | - |  |  | SI | Continuous antiarrythmia infusions |
| Q34 | - |  |  | SI | Cardioversion for arrythmia (not defibrillation) |
| Q35 | - |  |  | SI | Hypothermia blanket |
| Q36 | - |  |  | SI | Arterial line |
| Q37 | - |  |  | SI | Acute digitalisation - within 48h |
| Q38 | - |  |  | SI | Measurement of cardiac output by any method |
| Q39 | - |  |  | SI | Active diuresis for fluid overload or cerebral ede... |
| Q40 | - |  |  | SI | Active Rx for metabolic alkalosis |
| Q41 | - |  |  | SI | Active Rx for metabolic acidosis |
| Q42 | - |  |  | SI | Emergency thora-para and peri-cardiocenteses |
| Q43 | - |  |  | SI | Active anticoagulation (initial 48h) |
| Q44 | - |  |  | SI | Phlebotomy for volume overload |
| Q45 | - |  |  | SI | Coverage with more than 2 IV antibiotics |
| Q46 | - |  |  | SI | Rx of seizures or metabolic encephalopathy (within... |
| Q47 | - |  |  | SI | Complicated orthopedic traction |
| Q48 | - |  |  | SI | CVP ( central venous pressure) |
| Q49 | - |  |  | SI | 2 peripheral IV catheter |
| Q50 | - |  |  | SI | Hemodialysis stable patient |
| Q51 | - |  |  | SI | Fresh tracheostomy (less than 48h) |
| Q52 | - |  |  | SI | Spontaneous respiration via endotracheal tube or t... |
| Q53 | - |  |  | SI | GI feedings |
| Q54 | - |  |  | SI | Replacement of excess fluid loss |
| Q55 | - |  |  | SI | Parenteral chemotherapy |
| Q56 | - |  |  | SI | Hourly neuro vitals signs |
| Q57 | - |  |  | SI | Multiple dressing changes |
| Q58 | - |  |  | SI | Pitressin infusion IV |
| Q59 | - |  |  | SI | ECG monitoring |
| Q60 | - |  |  | SI | Hourly vitals signs |
| Q61 | - |  |  | SI | 1 peripheral IV catheter |
| Q62 | - |  |  | SI | Chronic anticoagulation |
| Q63 | - |  |  | SI | Standard intake and output (q 24h) |
| Q64 | - |  |  | SI | STAT blood tests |
| Q65 | - |  |  | SI | Intermittent scheduled IV medications |
| Q66 | - |  |  | SI | Routine dressing changes |
| Q67 | - |  |  | SI | Standard orthopedic traction |
| Q68 | - |  |  | SI | Tracheostomy care |
| Q69 | - |  |  | SI | Decubitus ulcer |
| Q70 | - |  |  | SI | Urinary catheter |
| Q71 | - |  |  | SI | Supplemental oxygen |
| Q72 | - |  |  | SI | Antibiotics IV (2 or less) |
| Q73 | - |  |  | SI | Chest physiotherapy |
| Q74 | - |  |  | SI | Extensive irrigations, packings or debridement of ... |
| Q75 | - |  |  | SI | GI decompression |
| Q76 | - |  |  | SI | Peripheral hyperalimentation / Intralipid therapy |
| Q77 | - |  |  | SI | Date |
| Q78 | - |  |  | SI | Class I : < 10 points |
| Q79 | - |  |  | SI | Class II : 10 -19 points |
| Q80 | - |  |  | SI | Class III : 20 - 39 points |
| Q81 | - |  |  | SI | Class IV : >= 40 points |
| Q82 | - |  |  | SI | Therapeutic Intervention Scoring System (TISS) is ... |
| Q83 | - |  |  | SI | 4 Points |
| Q84 | - |  |  | SI | 3 Points |
| Q85 | - |  |  | SI | 2 Points |
| Q86 | - |  |  | SI | 1 Point |
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