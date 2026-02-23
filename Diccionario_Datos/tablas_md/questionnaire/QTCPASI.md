# questionnaire.QTCPASI

> Psoriasis Assessment

**Schema:** questionnaire
**Columnas:** 117
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Psoriasis Assessment

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Psoriasis history |
| Q02 | numeric |  |  | SI | Age of onset |
| Q03 | varchar |  |  | SI | CVS history |
| Q04 | varchar |  |  | SI | Screen for depression |
| Q05 | varchar |  |  | SI | During the last month, have you often been bothere... |
| Q06 | varchar |  |  | SI | During the last month, have you often been bothere... |
| Q07 | varchar |  |  | SI | Refer to GP |
| Q08 | numeric |  |  | SI | Dermatology Life Quality Index (DLQI) score |
| Q09 | numeric |  |  | SI | Psoriasis Epidemiology Screening Tool score (PEST) |
| Q10 | varchar |  |  | SI | Patient's assessment of current disease severity |
| Q11 | varchar |  |  | SI | Height |
| Q11ObsDR | varchar |  | FK | SI | Height DR |
| Q12 | varchar |  |  | SI | Weight |
| Q12ObsDR | varchar |  | FK | SI | Weight DR |
| Q13 | varchar |  |  | SI | Systolic BP |
| Q13ObsDR | varchar |  | FK | SI | Systolic BP DR |
| Q14 | varchar |  |  | SI | Diastolic BP |
| Q14ObsDR | varchar |  | FK | SI | Diastolic BP DR |
| Q15 | varchar |  |  | SI | Type of psoriasis |
| Q16 | varchar |  |  | SI | Physician's global assessment |
| Q17 | varchar |  |  | SI | Body surface area affected |
| Q18 | varchar |  |  | SI | Any involvement of |
| Q19 | varchar |  |  | SI | Nail Psoriasis Severity Index (NAPSI)(optional) |
| Q20 | varchar |  |  | SI | Discussed risk factors for cardiovascular comorbid... |
| Q21 | varchar |  |  | SI | Discussed risk of VTE |
| Q22 | varchar |  |  | SI | Other management |
| Q23 | varchar |  |  | SI | PASI is a quantative rating score for measuring th... |
| Q24 | varchar |  |  | SI | Plaque Characteristics |
| Q25 | varchar |  |  | SI | 0 = None |
| Q26 | varchar |  |  | SI | 1 = Slight |
| Q27 | varchar |  |  | SI | 2 = Moderate |
| Q28 | varchar |  |  | SI | 3 = Severe |
| Q29 | varchar |  |  | SI | 4 = Very severe |
| Q30 | varchar |  |  | SI | Erythema head |
| Q31 | varchar |  |  | SI | Erythema upper limb |
| Q32 | varchar |  |  | SI | Erythema trunk |
| Q33 | varchar |  |  | SI | Erythema lower limb |
| Q34 | varchar |  |  | SI | Induration / Thickness head |
| Q35 | varchar |  |  | SI | Induration / Thickness upper limb |
| Q36 | varchar |  |  | SI | Induration / Thickness  trunk |
| Q37 | varchar |  |  | SI | Induration / Thickness lower limb |
| Q38 | varchar |  |  | SI | Scaling head |
| Q39 | varchar |  |  | SI | Scaling upper limb |
| Q40 | varchar |  |  | SI | Scaling trunk |
| Q41 | varchar |  |  | SI | Scaling lower limb |
| Q42 | varchar |  |  | SI | The scores for each body region will be given as 4... |
| Q43 | varchar |  |  | SI | Lesion Score Sum (A) |
| Q44 | varchar |  |  | SI | Head score |
| Q45 | varchar |  |  | SI | Upper Limb score |
| Q46 | varchar |  |  | SI | Trunk score |
| Q47 | varchar |  |  | SI | Lower Limbs score |
| Q48 | varchar |  |  | SI | Area Score (B) Degree of movement as a percentage ... |
| Q49 | varchar |  |  | SI | Percentage area affected: head |
| Q50 | varchar |  |  | SI | Percentage area affected: upper limb |
| Q51 | varchar |  |  | SI | Percentage area affected: trunk |
| Q52 | varchar |  |  | SI | Percentage area affected: lower limbs |
| Q53 | varchar |  |  | SI | Sub-Totals- Lesion Score Sum multiplied by Area Sc... |
| Q54 | varchar |  |  | SI | Head subtotal |
| Q55 | varchar |  |  | SI | Upper limb subtotal |
| Q56 | varchar |  |  | SI | Trunk subtotal |
| Q57 | varchar |  |  | SI | Lower limb subtotal |
| Q58 | varchar |  |  | SI | Total - Each of the Subtotals multiplied by the am... |
| Q59 | varchar |  |  | SI | Head total |
| Q60 | varchar |  |  | SI | Upper limb total |
| Q61 | varchar |  |  | SI | Trunk total |
| Q62 | varchar |  |  | SI | Lower limb total |
| Q63 | varchar |  |  | SI | PASI Score |
| Q64 | varchar |  |  | SI | The DLQI Score is used to measure the impact of sk... |
| Q65 | varchar |  |  | SI | 0 – 1 no effect at all on patient's life |
| Q66 | varchar |  |  | SI | 2 – 5 small effect on patient's life |
| Q67 | varchar |  |  | SI | 6 – 10 moderate effect on patient's life |
| Q68 | varchar |  |  | SI | 11 – 20 very large effect on patient's life |
| Q69 | varchar |  |  | SI | 21 – 30 extremely large effect on patient's life |
| Q70 | varchar |  |  | SI | PEST score |
| Q71 | varchar |  |  | SI | 0 - 5 |
| Q72 | varchar |  |  | SI | A score of 3 or more indicates referral to rheumat... |
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