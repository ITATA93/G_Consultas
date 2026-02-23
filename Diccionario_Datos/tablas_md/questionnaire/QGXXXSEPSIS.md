# questionnaire.QGXXXSEPSIS

> Severe Sepsis Screening Tool

**Schema:** questionnaire
**Columnas:** 94
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Severe Sepsis Screening Tool

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | The Severe Sepsis Screening Tool is an optional to... |
| Q02 | varchar |  |  | SI | 0-1 Point: No suspicion of infection is present |
| Q03 | varchar |  |  | SI | 2 Points: Suspicion of infection is present |
| Q04 | varchar |  |  | SI | 3 Points: Severe sepsis is present |
| Q05 | varchar |  |  | SI | Is the patient’s history suggestive of a new infec... |
| Q06 | bit |  |  | SI | Pneumonia, empyema |
| Q07 | bit |  |  | SI | Urinary tract infection |
| Q08 | bit |  |  | SI | Acute abdominal infection |
| Q09 | bit |  |  | SI | Meningitis |
| Q10 | bit |  |  | SI | Skin/soft tissue infection |
| Q11 | bit |  |  | SI | Bone / joint infection |
| Q12 | bit |  |  | SI | Wound infection |
| Q13 | bit |  |  | SI | Bloodstream catheter infection |
| Q14 | bit |  |  | SI | Endocarditis |
| Q15 | bit |  |  | SI | Implantable device infection |
| Q16 | bit |  |  | SI | Other |
| Q16a | varchar |  |  | SI | Other |
| Q18 | varchar |  |  | SI | Are any two of following signs &amp; symptoms of i... |
| Q19 | varchar |  |  | SI | Note: laboratory values may have been obtained for... |
| Q20 | bit |  |  | SI | Hyperthermia &gt;38.3 °C (101.0 °F) |
| Q21 | bit |  |  | SI | Hypothermia &lt;36 °C (96.8°F) |
| Q22 | bit |  |  | SI | Tachycardia &gt;90 bpm |
| Q23 | bit |  |  | SI | Tachypnea &gt;20 bpm |
| Q24 | bit |  |  | SI | Altered mental status |
| Q25 | bit |  |  | SI | Leukocytosis (WBC count &gt;&gt;12,000 per microli... |
| Q26 | bit |  |  | SI | Leukopenia (WBC count &lt;&lt;4,000 per microlitre... |
| Q27 | bit |  |  | SI | Hyperglycemia (plasma glucose &gt;140 mg/dL or 7.7... |
| Q28 | varchar |  |  | SI | Obtain: lactic acid, blood cultures, complete bloo... |
| Q30 | varchar |  |  | SI | Are any of the following organ dysfunction criteri... |
| Q31 | varchar |  |  | SI | Note: the remote site stipulation is waived in the... |
| Q32 | bit |  |  | SI | Systolic BP &lt;90 mm Hg or MAP &lt;65 mm Hg |
| Q33 | bit |  |  | SI | SBP decrease &gt;40 mm Hg from baseline |
| Q34 | bit |  |  | SI | Bilateral pulmonary infiltrates with a new (or inc... |
| Q35 | bit |  |  | SI | Bilateral pulmonary infiltrates with PaO2/FiO2 rat... |
| Q36 | bit |  |  | SI | Creatinine &gt;2.0 mg/dL (176.8 mmol/L) or urine o... |
| Q37 | bit |  |  | SI | Bilirubin &gt;2 mg/dL (34.2 mmol/L) |
| Q38 | bit |  |  | SI | Platelet count &lt;100,000 per microlitre |
| Q39 | bit |  |  | SI | Coagulopathy (INR &gt;1.5 or aPTT &gt;60 seconds) |
| Q40 | bit |  |  | SI | Lactate &gt;2 mmol/L (18.0 mg/dL) |
| Q41 | varchar |  |  | SI | If suspicion of infection is present AND organ dys... |
| Q42 | varchar |  |  | SI | If the answer is yes to both either question 1 and... |
| Q43 | varchar |  |  | SI | Yes / No |
| Q44 | varchar |  |  | SI | Yes / No |
| Q45 | varchar |  |  | SI | Yes / No |
| Q46 | date |  |  | SI | Date |
| Q47 | time |  |  | SI | Time |
| Q50 | varchar |  |  | SI | .... |
| Q51 | varchar |  |  | SI | .... |
| Q52 | varchar |  |  | SI | ................ |
| Q53 | varchar |  |  | SI | Schorr C, Odden A, Evans L,&nbsp;et al. Implementa... |
| Q54 | varchar |  |  | SI | Are any two of following signs &amp; symptoms of i... |
| Q55 | varchar |  |  | SI | Are any of the following organ dysfunction criteri... |
| Q56 | varchar |  |  | SI | Is the patient’s history suggestive of a new infec... |
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