# SQLUser.PAC_ConsciousState

**Schema:** SQLUser
**Columnas:** 123
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CONST_RowId | bigint | PK |  | NO | - |
| CONST_Code | varchar |  |  | NO | Code |
| CONST_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| CONST_CreatedDate | date |  |  | SI | Created Date |
| CONST_CreatedTime | time |  |  | SI | Created Time |
| CONST_CreatedUser_DR | bigint |  | FK | SI | Created User |
| CONST_DateFrom | date |  |  | SI | Date From |
| CONST_DateTo | date |  |  | SI | Date To |
| CONST_Desc | varchar |  |  | NO | Description |
| CONST_Owner | varchar |  |  | SI | Owner |
| CONST_UpdatedDate | date |  |  | SI | Updated Date |
| CONST_UpdatedTime | time |  |  | SI | Updated Time |
| CONST_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | The following assessment has been shown because th... |
| Q02 | - |  |  | SI | Increased shortness of breath |
| Q03 | - |  |  | SI | Fever |
| Q04 | - |  |  | SI | Productive cough |
| Q05 | - |  |  | SI | Answered Yes to one or more of the above |
| Q06 | - |  |  | SI | Pneumonia Risk Factors: |
| Q07 | - |  |  | SI | - A past diagnosis of CAP |
| Q08 | - |  |  | SI | - Patient is a smoker |
| Q09 | - |  |  | SI | - HIV + |
| Q10 | - |  |  | SI | - On inhaled or oral steroids |
| Q11 | - |  |  | SI | - Over 65 years old |
| Q12 | - |  |  | SI | - Chronic lung disease |
| Q13 | - |  |  | SI | Click on the link below for more details: |
| Q14 | - |  |  | SI | - Pneumonia risk factors |
| Q15 | - |  |  | SI | Clinical suspicion of Pneumonia |
| Q16 | - |  |  | SI | Please carry out: |
| Q17 | - |  |  | SI | - Order immediate CXR |
| Q18 | - |  |  | SI | - Assess oxygen sats |
| Q19 | - |  |  | SI | - Order oxygen Therapy |
| Q20 | - |  |  | SI | Suspected source of infection: |
| Q21 | - |  |  | SI | Details: |
| Q22 | - |  |  | SI | Does patient look sick? |
| Q23 | - |  |  | SI | Last EWS: |
| Q23ObsDR | - |  |  | SI | Last EWS: DR |
| Q24 | - |  |  | SI | EWS > 5 |
| Q25 | - |  |  | SI | Recent chemotherapy |
| Q26 | - |  |  | SI | Last RR: |
| Q26ObsDR | - |  |  | SI | Last RR: DR |
| Q27 | - |  |  | SI | Tachypnoea RR >= 25 |
| Q28 | - |  |  | SI | Last HR: |
| Q28ObsDR | - |  |  | SI | Last HR: DR |
| Q29 | - |  |  | SI | Heart rate >= 130 |
| Q30 | - |  |  | SI | Last SYS BP: |
| Q30ObsDR | - |  |  | SI | Last SYS BP: DR |
| Q31 | - |  |  | SI | Systolic BP <= 90 |
| Q32 | - |  |  | SI | Needs oxygen to keep SaO2 >= 92% or more than 88% ... |
| Q33 | - |  |  | SI | Last Patient has oliguria: |
| Q33ObsDR | - |  |  | SI | Last Patient has oliguria: DR |
| Q34 | - |  |  | SI | Last Patient has anuria: |
| Q34ObsDR | - |  |  | SI | Last Patient has anuria: DR |
| Q35 | - |  |  | SI | Not passed urine in the last 18 hours or urine out... |
| Q36 | - |  |  | SI | Lactate >= 2 mmol/L |
| Q37 | - |  |  | SI | Acute Kidney Injury |
| Q38 | - |  |  | SI | Other evidence of organ dysfunction |
| Q39 | - |  |  | SI | Details: |
| Q40 | - |  |  | SI | Answered Yes to one or more of the above |
| Q41 | - |  |  | SI | The patient is now on the sepsis pathway. Please b... |
| Q42 | - |  |  | SI | Reasoning:	 |
| Q43 | - |  |  | SI | Carry out routine bloods including lactate. A Seni... |
| Q44 | - |  |  | SI | region / site specific text 1 |
| Q45 | - |  |  | SI | region / site specific text 2 |
| Q46 | - |  |  | SI | region / site specific text 3 |
| Q47 | - |  |  | SI | region / site specific text 4 |
| Q48 | - |  |  | SI | region / site specific text 5 |
| Q49 | - |  |  | SI | region / site specific text 6 |
| Q50 | - |  |  | SI | Increased shortness of breath: Does patient curren... |
| Q51 | - |  |  | SI | Fever: Does patient currently have a fever |
| Q52 | - |  |  | SI | Productive cough: Is patient currently coughing up... |
| Q53 | - |  |  | SI | EWS > 5: Please indicate if the early warning scor... |
| Q54 | - |  |  | SI | Recent chemotherapy: Plesse indicate if patient ha... |
| Q55 | - |  |  | SI | Tachypnoea RR >= 25: Please indicate if patient's ... |
| Q56 | - |  |  | SI | Heart rate >= 130: Please indicate if patient's he... |
| Q57 | - |  |  | SI | Systolic BP <= 90: Please indicate if patient's sy... |
| Q58 | - |  |  | SI | Needs oxygen to keep SaO2 >= 92% or more than 88% ... |
| Q59 | - |  |  | SI | Not passed urine in the last 18 hours or urine out... |
| Q60 | - |  |  | SI | Lactate >= 2 mmol/L: Please indicate if patient's ... |
| Q61 | - |  |  | SI | Acute Kidney Injury: Please indicate if patient ha... |
| Q62 | - |  |  | SI | Other evidence of organ dysfunction: Please indica... |
| Q63 | - |  |  | SI | Date |
| Q64 | - |  |  | SI | Time |
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