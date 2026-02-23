# questionnaire.QTCSCCP

> Stroke Critical Care Pathway

**Schema:** questionnaire
**Columnas:** 133
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Stroke Critical Care Pathway

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | Stroke pathway day |
| Q04 | varchar |  |  | SI | Central Nervous System |
| Q05 | varchar |  |  | SI | Patient has attended all required investigative pr... |
| Q06 | varchar |  |  | SI | Variance |
| Q07 | varchar |  |  | SI | Patient remained neurologically stable with no fur... |
| Q08 | varchar |  |  | SI | Variance |
| Q09 | varchar |  |  | SI | Patient remained seizure free |
| Q10 | varchar |  |  | SI | Variance |
| Q11 | varchar |  |  | SI | Patient had no further deterioration in language, ... |
| Q12 | varchar |  |  | SI | Variance |
| Q13 | varchar |  |  | SI | Patient able to communication basic needs |
| Q14 | varchar |  |  | SI | Variance |
| Q15 | varchar |  |  | SI | All neurological deficits documented and reported ... |
| Q16 | varchar |  |  | SI | Variance |
| Q17 | varchar |  |  | SI | Cardiovascular System |
| Q18 | varchar |  |  | SI | Patient remained hemodynamically stable and observ... |
| Q19 | varchar |  |  | SI | Variance |
| Q20 | varchar |  |  | SI | Cardiac rhythm monitoring in place and all arrhyth... |
| Q21 | varchar |  |  | SI | Variance |
| Q22 | varchar |  |  | SI | Cardiac rhythm monitoring ceased as per medical in... |
| Q23 | varchar |  |  | SI | Variance |
| Q24 | varchar |  |  | SI | 12 lead electrocardiogram conducted and reviewed b... |
| Q25 | varchar |  |  | SI | Variance |
| Q26 | varchar |  |  | SI | All ordered blood tests taken and results reviewed... |
| Q27 | varchar |  |  | SI | Variance |
| Q28 | varchar |  |  | SI | Medications reviewed and considered for best pract... |
| Q29 | varchar |  |  | SI | Variance |
| Q30 | varchar |  |  | SI | Appropriate venous thrombosis therapy prophylaxis ... |
| Q31 | varchar |  |  | SI | Variance |
| Q32 | varchar |  |  | SI | Respiratory System |
| Q33 | varchar |  |  | SI | Respiratory rate less than 20 bpm |
| Q34 | varchar |  |  | SI | Variance |
| Q35 | varchar |  |  | SI | Oxygen saturations ≥ 95% or 88 - 92% for CO2 retai... |
| Q36 | varchar |  |  | SI | Variance |
| Q37 | varchar |  |  | SI | Airway remained patent and all secretions managed ... |
| Q38 | varchar |  |  | SI | Variance |
| Q39 | varchar |  |  | SI | Lung fields clear and air entry equal |
| Q40 | varchar |  |  | SI | Variance |
| Q41 | varchar |  |  | SI | Patient nursed in 30° upright position or as clini... |
| Q42 | varchar |  |  | SI | Variance |
| Q43 | varchar |  |  | SI | Metabolic |
| Q44 | varchar |  |  | SI | Patient remained normothermic |
| Q45 | varchar |  |  | SI | Variance |
| Q46 | varchar |  |  | SI | Blood glucose level maintained between 4 - 8 mmol/... |
| Q47 | varchar |  |  | SI | Variance |
| Q48 | varchar |  |  | SI | Elimination / Fluid Balance |
| Q49 | varchar |  |  | SI | Urine output > 30 mLs per hour |
| Q50 | varchar |  |  | SI | Variance |
| Q51 | varchar |  |  | SI | Strict fluid balance chart maintained |
| Q52 | varchar |  |  | SI | Variance |
| Q53 | varchar |  |  | SI | Patient assessed for dysphagia |
| Q54 | varchar |  |  | SI | Variance |
| Q55 | varchar |  |  | SI | Patient is receiving adequate nutrition |
| Q56 | varchar |  |  | SI | Variance |
| Q57 | varchar |  |  | SI | All bowel motions document. If bowels not open for... |
| Q58 | varchar |  |  | SI | Variance |
| Q59 | varchar |  |  | SI | Patient remained continent of both urine and faece... |
| Q60 | varchar |  |  | SI | Variance |
| Q61 | varchar |  |  | SI | Skin Care and Hygiene |
| Q62 | varchar |  |  | SI | Skin remains intact and free from pressure injurie... |
| Q63 | varchar |  |  | SI | Variance |
| Q64 | varchar |  |  | SI | Patient has received regular pressure area care |
| Q65 | varchar |  |  | SI | Variance |
| Q66 | varchar |  |  | SI | Pressure relieving devices in situ as needed |
| Q67 | varchar |  |  | SI | Variance |
| Q68 | varchar |  |  | SI | Personal hygiene attended |
| Q69 | varchar |  |  | SI | Variance |
| Q70 | varchar |  |  | SI | Patient received mouth and eye care as clinically ... |
| Q71 | varchar |  |  | SI | Variance |
| Q72 | varchar |  |  | SI | Mobilisation / Physiotherapy |
| Q73 | varchar |  |  | SI | Mobility has been assessed and documented |
| Q74 | varchar |  |  | SI | Variance |
| Q75 | varchar |  |  | SI | Patient mobilising as tolerated |
| Q76 | varchar |  |  | SI | Variance |
| Q77 | varchar |  |  | SI | Stroke Education |
| Q78 | varchar |  |  | SI | Patient commenced on stroke education |
| Q79 | varchar |  |  | SI | Variance |
| Q80 | varchar |  |  | SI | Patient continuing with stroke education |
| Q81 | varchar |  |  | SI | Variance |
| Q82 | varchar |  |  | SI | Social |
| Q83 | varchar |  |  | SI | Problems, barriers to discharge assessed |
| Q84 | varchar |  |  | SI | Variance |
| Q85 | varchar |  |  | SI | Estimated date of discharge recorded |
| Q86 | varchar |  |  | SI | Variance |
| Q87 | varchar |  |  | SI | Estimated date of discharge reviewed and updated i... |
| Q88 | varchar |  |  | SI | Variance |
| Q89 | varchar |  |  | SI | Referred to allied health services as clinically i... |
| Q90 | varchar |  |  | SI | Variance |
| Q91 | varchar |  |  | SI | Referred to appropriate rehabilitation services as... |
| Q92 | varchar |  |  | SI | Variance |
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