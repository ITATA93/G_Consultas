# questionnaire.QTCISTA

> Infection Screening Tool Adult

**Schema:** questionnaire
**Columnas:** 168
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Infection Screening Tool Adult

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
| Q100 | varchar |  |  | SI | Consciousness: CVP or U	 |
| Q101 | varchar |  |  | SI | Please indicate if patient is not alert.	 |
| Q102 | varchar |  |  | SI | Lactate >= 2 mmol/L	 |
| Q103 | varchar |  |  | SI | Please indicate if patient's lactate is more than ... |
| Q104 | varchar |  |  | SI | Acute Kidney Injury	 |
| Q105 | varchar |  |  | SI | Please indicate if patient has Acute Kidney Injury... |
| Q106 | varchar |  |  | SI | Other evidence of organ dysfunction	 |
| Q107 | varchar |  |  | SI | Please indicate if patient has any other organ dys... |
| Q108 | varchar |  |  | SI | Details |
| Q109 | varchar |  |  | SI | Please specify detail of organ dysfunction	 |
| Q11 | varchar |  |  | SI | - Over 65 years old |
| Q110 | varchar |  |  | SI | Answered Yes to one or more of the above	 |
| Q111 | varchar |  |  | SI | Have you answered Yes to one or more of the above ... |
| Q112 | varchar |  |  | SI | The patient is now on the sepsis pathway. Please b... |
| Q113 | varchar |  |  | SI | Please indicate if you wish to remove patient from... |
| Q114 | varchar |  |  | SI | Reasoning |
| Q115 | varchar |  |  | SI | Please specify the reason patient is being removed... |
| Q116 | varchar |  |  | SI | Have you answered Yes to one or more of the above	 |
| Q117 | varchar |  |  | SI | Capillary refill time >= 3 seconds	 |
| Q118 | varchar |  |  | SI | Remove patient from pathway |
| Q119 | varchar |  |  | SI | Specific Information |
| Q12 | varchar |  |  | SI | - Chronic lung disease |
| Q120 | date |  |  | SI | Date |
| Q121 | time |  |  | SI | Time |
| Q13 | varchar |  |  | SI | Click on the link below for more details	 |
| Q14 | bigint |  |  | SI | - Pneumonia risk factors |
| Q14TxtOnly | bigint |  |  | SI | - Pneumonia risk factors Plain Text Only |
| Q15 | varchar |  |  | SI | Clinical suspicion of Pneumonia |
| Q16 | varchar |  |  | SI | Please carry out: |
| Q17 | varchar |  |  | SI | - Order immediate CXR |
| Q18 | varchar |  |  | SI | - Assess oxygen sats |
| Q19 | varchar |  |  | SI | - Order oxygen Therapy	 |
| Q20 | varchar |  |  | SI | Suspected source of infection: |
| Q21 | varchar |  |  | SI | Details: |
| Q22 | varchar |  |  | SI | Patient age range |
| Q23 | varchar |  |  | SI | Does Patient look sick? |
| Q24 | varchar |  |  | SI | Last EWS: |
| Q24ObsDR | varchar |  | FK | SI | Last EWS: DR |
| Q25 | varchar |  |  | SI | EWS >= 5 |
| Q26 | varchar |  |  | SI | Impaired immune system |
| Q27 | varchar |  |  | SI | Last RR: |
| Q27ObsDR | varchar |  | FK | SI | Last RR: DR |
| Q28 | varchar |  |  | SI | >90 or <=15 |
| Q29 | varchar |  |  | SI | >80 or <=15 |
| Q30 | varchar |  |  | SI | >70 or <=12 |
| Q31 | varchar |  |  | SI | >50 or <=10 |
| Q32 | varchar |  |  | SI | >=30 or <=9 |
| Q33 | varchar |  |  | SI | Respiratory Rate:	 |
| Q34 | varchar |  |  | SI | Severe increased respiratory effort / any apnoea	 |
| Q35 | varchar |  |  | SI | Oxygen therapy >= 4L/min or >50%	 |
| Q36 | varchar |  |  | SI | Last HR:	 |
| Q36ObsDR | varchar |  | FK | SI | Last HR:	 DR |
| Q37 | varchar |  |  | SI | >=190 or <=80 |
| Q38 | varchar |  |  | SI | >=180 or <=70	 |
| Q39 | varchar |  |  | SI | >=170 or <=60	 |
| Q40 | varchar |  |  | SI | >=150 or <=50	 |
| Q41 | varchar |  |  | SI | >=140 or <=40 |
| Q42 | varchar |  |  | SI | Heart rate:	 |
| Q43 | varchar |  |  | SI | Last SYS BP: |
| Q43ObsDR | varchar |  | FK | SI | Last SYS BP: DR |
| Q44 | varchar |  |  | SI | >=130 or <=45	 |
| Q45 | varchar |  |  | SI | >=150 or <=60	 |
| Q46 | varchar |  |  | SI | >= 160 or <=65	 |
| Q47 | varchar |  |  | SI | >= 170 or <=70	 |
| Q48 | varchar |  |  | SI | >=190 or <=75	 |
| Q49 | varchar |  |  | SI | Systolic BP:	 |
| Q50 | varchar |  |  | SI | Capillary refill time >= 3 seconds	 |
| Q51 | varchar |  |  | SI | Age 12+ and not passed uring in last 18 hours or u... |
| Q52 | varchar |  |  | SI | Last Consciousness:	 |
| Q52ObsDR | varchar |  | FK | SI | Last Consciousness:	 DR |
| Q53 | varchar |  |  | SI | Consciousness: CVP or U	 |
| Q54 | varchar |  |  | SI | Lactate >= 2 mmol/L	 |
| Q55 | varchar |  |  | SI | Acute Kidney Injury |
| Q56 | varchar |  |  | SI | Other evidence of organ dysfunction	 |
| Q57 | varchar |  |  | SI | Details |
| Q58 | varchar |  |  | SI | Answered Yes to one or more of the above	 |
| Q59 | varchar |  |  | SI | The patient is now on the sepsis pathway. Please b... |
| Q60 | varchar |  |  | SI | Reasoning:	 |
| Q61 | varchar |  |  | SI | Carry out routine bloods including lactate. A Seni... |
| Q62 | varchar |  |  | SI | region / site specific text 1 |
| Q63 | varchar |  |  | SI | region / site specific text 2 |
| Q64 | varchar |  |  | SI | region / site specific text 3 |
| Q65 | varchar |  |  | SI | region / site specific text 4 |
| Q66 | varchar |  |  | SI | region / site specific text 5 |
| Q67 | varchar |  |  | SI | region / site specific text 6 |
| Q68 | varchar |  |  | SI | Increased shortness of breath |
| Q69 | varchar |  |  | SI | Does patient currently have a shortness of breath |
| Q70 | varchar |  |  | SI | Fever |
| Q71 | varchar |  |  | SI | Does patient currently have a fever	 |
| Q72 | varchar |  |  | SI | Productive cough	 |
| Q73 | varchar |  |  | SI | Is patient currently coughing up sputum 	 |
| Q74 | varchar |  |  | SI | Answered Yes to one or more of the above	 |
| Q75 | varchar |  |  | SI | Clinical suspicion of Pneumonia	 |
| Q76 | varchar |  |  | SI | Is there a clinical suspicion that patient has pne... |
| Q77 | varchar |  |  | SI | Suspected source of infection:	 |
| Q78 | varchar |  |  | SI | Please select a source of infection	 |
| Q79 | varchar |  |  | SI | Details:	 |
| Q80 | varchar |  |  | SI | Please specify other source	 |
| Q81 | varchar |  |  | SI | Patient age range	 |
| Q82 | varchar |  |  | SI | Please select the patients age range	 |
| Q83 | varchar |  |  | SI | Does Patient look sick?	 |
| Q84 | varchar |  |  | SI | Please indicate if patient looks sick	 |
| Q85 | varchar |  |  | SI | EWS >= 5	 |
| Q86 | varchar |  |  | SI | Please indicate if the early warning score is five... |
| Q87 | varchar |  |  | SI | Impaired immune system	 |
| Q88 | varchar |  |  | SI | Plesse indicate if patient has an impaired immune ... |
| Q89 | varchar |  |  | SI | Respiratory Rate:	 |
| Q90 | varchar |  |  | SI | Please indicate if patient's respiratory rate is o... |
| Q91 | varchar |  |  | SI | Severe increased respiratory effort / any apnoea	 |
| Q92 | varchar |  |  | SI | Please indicate if patient has severe increased ef... |
| Q93 | varchar |  |  | SI | Oxygen therapy >= 4L/min or >50%	 |
| Q94 | varchar |  |  | SI | Please indicate if patient is on oxygen therapy of... |
| Q95 | varchar |  |  | SI | Systolic BP:	 |
| Q96 | varchar |  |  | SI | Please indicate if patient's systolic blood pressu... |
| Q97 | varchar |  |  | SI | Please indicate if patient's capillary refill time... |
| Q98 | varchar |  |  | SI | Age 12+ and not passed urine in last 18 hours or u... |
| Q99 | varchar |  |  | SI | Please indicate if patient is 12 years old or over... |
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