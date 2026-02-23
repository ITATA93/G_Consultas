# questionnaire.QTCISTP

> Infection Screening Tool Paediatric

**Schema:** questionnaire
**Columnas:** 111
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Infection Screening Tool Paediatric

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | The following assessment has been shown because th... |
| Q02 | varchar |  |  | SI | Increased shortness of breath |
| Q03 | varchar |  |  | SI | Fever |
| Q04 | varchar |  |  | SI | Productive cough |
| Q05 | varchar |  |  | SI | Answered Yes to one or more of the above |
| Q06 | varchar |  |  | SI | Pneumonia Risk Factors: |
| Q07 | varchar |  |  | SI | - A past diagnosis of CAP |
| Q08 | varchar |  |  | SI | - Patient is a smoker |
| Q09 | varchar |  |  | SI | - HIV + |
| Q10 | varchar |  |  | SI | - On inhaled or oral steroids |
| Q11 | varchar |  |  | SI | - Over 65 years old |
| Q12 | varchar |  |  | SI | - Chronic lung disease |
| Q13 | varchar |  |  | SI | Click on the link below for more details: |
| Q14 | varchar |  |  | SI | - Pneumonia risk factors |
| Q15 | varchar |  |  | SI | Clinical suspicion of Pneumonia |
| Q16 | varchar |  |  | SI | Please carry out: |
| Q17 | varchar |  |  | SI | - Order immediate CXR |
| Q18 | varchar |  |  | SI | - Assess oxygen sats |
| Q19 | varchar |  |  | SI | - Order oxygen Therapy |
| Q20 | varchar |  |  | SI | Suspected source of infection: |
| Q21 | varchar |  |  | SI | Details: |
| Q22 | varchar |  |  | SI | Does patient look sick? |
| Q23 | varchar |  |  | SI | Last EWS: |
| Q23ObsDR | varchar |  | FK | SI | Last EWS: DR |
| Q24 | varchar |  |  | SI | EWS > 5 |
| Q25 | varchar |  |  | SI | Recent chemotherapy |
| Q26 | varchar |  |  | SI | Last RR: |
| Q26ObsDR | varchar |  | FK | SI | Last RR: DR |
| Q27 | varchar |  |  | SI | Tachypnoea RR >= 25 |
| Q28 | varchar |  |  | SI | Last HR: |
| Q28ObsDR | varchar |  | FK | SI | Last HR: DR |
| Q29 | varchar |  |  | SI | Heart rate >= 130  |
| Q30 | varchar |  |  | SI | Last SYS BP: |
| Q30ObsDR | varchar |  | FK | SI | Last SYS BP: DR |
| Q31 | varchar |  |  | SI | Systolic BP <= 90 |
| Q32 | varchar |  |  | SI | Needs oxygen to keep SaO2 >= 92% or more than 88% ... |
| Q33 | varchar |  |  | SI | Last Patient has oliguria: |
| Q33ObsDR | varchar |  | FK | SI | Last Patient has oliguria: DR |
| Q34 | varchar |  |  | SI | Last Patient has anuria: |
| Q34ObsDR | varchar |  | FK | SI | Last Patient has anuria: DR |
| Q35 | varchar |  |  | SI | Not passed urine in the last 18 hours or urine out... |
| Q36 | varchar |  |  | SI | Lactate >= 2 mmol/L |
| Q37 | varchar |  |  | SI | Acute Kidney Injury |
| Q38 | varchar |  |  | SI | Other evidence of organ dysfunction |
| Q39 | varchar |  |  | SI | Details: |
| Q40 | varchar |  |  | SI | Answered Yes to one or more of the above |
| Q41 | varchar |  |  | SI | The patient is now on the sepsis pathway. Please b... |
| Q42 | varchar |  |  | SI | Reasoning:	 |
| Q43 | varchar |  |  | SI | Carry out routine bloods including lactate. A Seni... |
| Q44 | varchar |  |  | SI | region / site specific text 1 |
| Q45 | varchar |  |  | SI | region / site specific text 2 |
| Q46 | varchar |  |  | SI | region / site specific text 3 |
| Q47 | varchar |  |  | SI | region / site specific text 4 |
| Q48 | varchar |  |  | SI | region / site specific text 5 |
| Q49 | varchar |  |  | SI | region / site specific text 6 |
| Q50 | varchar |  |  | SI | Increased shortness of breath: Does patient curren... |
| Q51 | varchar |  |  | SI | Fever: Does patient currently have a fever |
| Q52 | varchar |  |  | SI | Productive cough: Is patient currently coughing up... |
| Q53 | varchar |  |  | SI | EWS > 5: Please indicate if the early warning scor... |
| Q54 | varchar |  |  | SI | Recent chemotherapy: Plesse indicate if patient ha... |
| Q55 | varchar |  |  | SI | Tachypnoea RR >= 25: Please indicate if patient's ... |
| Q56 | varchar |  |  | SI | Heart rate >= 130: Please indicate if patient's he... |
| Q57 | varchar |  |  | SI | Systolic BP <= 90: Please indicate if patient's sy... |
| Q58 | varchar |  |  | SI | Needs oxygen to keep SaO2 >= 92% or more than 88% ... |
| Q59 | varchar |  |  | SI | Not passed urine in the last 18 hours or urine out... |
| Q60 | varchar |  |  | SI | Lactate >= 2 mmol/L: Please indicate if patient's ... |
| Q61 | varchar |  |  | SI | Acute Kidney Injury: Please indicate if patient ha... |
| Q62 | varchar |  |  | SI | Other evidence of organ dysfunction: Please indica... |
| Q63 | date |  |  | SI | Date |
| Q64 | time |  |  | SI | Time |
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