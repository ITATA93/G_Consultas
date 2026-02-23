# SQLUser.PAC_ContClientPresStat

**Schema:** SQLUser
**Columnas:** 180
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CONTCLNPRST_RowId | bigint | PK |  | NO | - |
| CONTCLNPRST_Code | varchar |  |  | NO | Code |
| CONTCLNPRST_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| CONTCLNPRST_CreatedDate | date |  |  | SI | Created Date |
| CONTCLNPRST_CreatedTime | time |  |  | SI | Created Time |
| CONTCLNPRST_CreatedUser_DR | bigint |  | FK | SI | Created User |
| CONTCLNPRST_DateFrom | date |  |  | SI | Date From |
| CONTCLNPRST_DateTo | date |  |  | SI | Date To |
| CONTCLNPRST_Desc | varchar |  |  | NO | Description |
| CONTCLNPRST_Owner | varchar |  |  | SI | Owner |
| CONTCLNPRST_UpdatedDate | date |  |  | SI | Updated Date |
| CONTCLNPRST_UpdatedTime | time |  |  | SI | Updated Time |
| CONTCLNPRST_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
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
| Q100 | - |  |  | SI | Consciousness: CVP or U	 |
| Q101 | - |  |  | SI | Please indicate if patient is not alert.	 |
| Q102 | - |  |  | SI | Lactate >= 2 mmol/L	 |
| Q103 | - |  |  | SI | Please indicate if patient's lactate is more than ... |
| Q104 | - |  |  | SI | Acute Kidney Injury	 |
| Q105 | - |  |  | SI | Please indicate if patient has Acute Kidney Injury... |
| Q106 | - |  |  | SI | Other evidence of organ dysfunction	 |
| Q107 | - |  |  | SI | Please indicate if patient has any other organ dys... |
| Q108 | - |  |  | SI | Details |
| Q109 | - |  |  | SI | Please specify detail of organ dysfunction	 |
| Q11 | - |  |  | SI | - Over 65 years old |
| Q110 | - |  |  | SI | Answered Yes to one or more of the above	 |
| Q111 | - |  |  | SI | Have you answered Yes to one or more of the above ... |
| Q112 | - |  |  | SI | The patient is now on the sepsis pathway. Please b... |
| Q113 | - |  |  | SI | Please indicate if you wish to remove patient from... |
| Q114 | - |  |  | SI | Reasoning |
| Q115 | - |  |  | SI | Please specify the reason patient is being removed... |
| Q116 | - |  |  | SI | Have you answered Yes to one or more of the above	 |
| Q117 | - |  |  | SI | Capillary refill time >= 3 seconds	 |
| Q118 | - |  |  | SI | Remove patient from pathway |
| Q119 | - |  |  | SI | Specific Information |
| Q12 | - |  |  | SI | - Chronic lung disease |
| Q120 | - |  |  | SI | Date |
| Q121 | - |  |  | SI | Time |
| Q13 | - |  |  | SI | Click on the link below for more details	 |
| Q14 | - |  |  | SI | - Pneumonia risk factors |
| Q14TxtOnly | - |  |  | SI | - Pneumonia risk factors Plain Text Only |
| Q15 | - |  |  | SI | Clinical suspicion of Pneumonia |
| Q16 | - |  |  | SI | Please carry out: |
| Q17 | - |  |  | SI | - Order immediate CXR |
| Q18 | - |  |  | SI | - Assess oxygen sats |
| Q19 | - |  |  | SI | - Order oxygen Therapy	 |
| Q20 | - |  |  | SI | Suspected source of infection: |
| Q21 | - |  |  | SI | Details: |
| Q22 | - |  |  | SI | Patient age range |
| Q23 | - |  |  | SI | Does Patient look sick? |
| Q24 | - |  |  | SI | Last EWS: |
| Q24ObsDR | - |  |  | SI | Last EWS: DR |
| Q25 | - |  |  | SI | EWS >= 5 |
| Q26 | - |  |  | SI | Impaired immune system |
| Q27 | - |  |  | SI | Last RR: |
| Q27ObsDR | - |  |  | SI | Last RR: DR |
| Q28 | - |  |  | SI | >90 or <=15 |
| Q29 | - |  |  | SI | >80 or <=15 |
| Q30 | - |  |  | SI | >70 or <=12 |
| Q31 | - |  |  | SI | >50 or <=10 |
| Q32 | - |  |  | SI | >=30 or <=9 |
| Q33 | - |  |  | SI | Respiratory Rate:	 |
| Q34 | - |  |  | SI | Severe increased respiratory effort / any apnoea	 |
| Q35 | - |  |  | SI | Oxygen therapy >= 4L/min or >50%	 |
| Q36 | - |  |  | SI | Last HR:	 |
| Q36ObsDR | - |  |  | SI | Last HR:	 DR |
| Q37 | - |  |  | SI | >=190 or <=80 |
| Q38 | - |  |  | SI | >=180 or <=70	 |
| Q39 | - |  |  | SI | >=170 or <=60	 |
| Q40 | - |  |  | SI | >=150 or <=50	 |
| Q41 | - |  |  | SI | >=140 or <=40 |
| Q42 | - |  |  | SI | Heart rate:	 |
| Q43 | - |  |  | SI | Last SYS BP: |
| Q43ObsDR | - |  |  | SI | Last SYS BP: DR |
| Q44 | - |  |  | SI | >=130 or <=45	 |
| Q45 | - |  |  | SI | >=150 or <=60	 |
| Q46 | - |  |  | SI | >= 160 or <=65	 |
| Q47 | - |  |  | SI | >= 170 or <=70	 |
| Q48 | - |  |  | SI | >=190 or <=75	 |
| Q49 | - |  |  | SI | Systolic BP:	 |
| Q50 | - |  |  | SI | Capillary refill time >= 3 seconds	 |
| Q51 | - |  |  | SI | Age 12+ and not passed uring in last 18 hours or u... |
| Q52 | - |  |  | SI | Last Consciousness:	 |
| Q52ObsDR | - |  |  | SI | Last Consciousness:	 DR |
| Q53 | - |  |  | SI | Consciousness: CVP or U	 |
| Q54 | - |  |  | SI | Lactate >= 2 mmol/L	 |
| Q55 | - |  |  | SI | Acute Kidney Injury |
| Q56 | - |  |  | SI | Other evidence of organ dysfunction	 |
| Q57 | - |  |  | SI | Details |
| Q58 | - |  |  | SI | Answered Yes to one or more of the above	 |
| Q59 | - |  |  | SI | The patient is now on the sepsis pathway. Please b... |
| Q60 | - |  |  | SI | Reasoning:	 |
| Q61 | - |  |  | SI | Carry out routine bloods including lactate. A Seni... |
| Q62 | - |  |  | SI | region / site specific text 1 |
| Q63 | - |  |  | SI | region / site specific text 2 |
| Q64 | - |  |  | SI | region / site specific text 3 |
| Q65 | - |  |  | SI | region / site specific text 4 |
| Q66 | - |  |  | SI | region / site specific text 5 |
| Q67 | - |  |  | SI | region / site specific text 6 |
| Q68 | - |  |  | SI | Increased shortness of breath |
| Q69 | - |  |  | SI | Does patient currently have a shortness of breath |
| Q70 | - |  |  | SI | Fever |
| Q71 | - |  |  | SI | Does patient currently have a fever	 |
| Q72 | - |  |  | SI | Productive cough	 |
| Q73 | - |  |  | SI | Is patient currently coughing up sputum 	 |
| Q74 | - |  |  | SI | Answered Yes to one or more of the above	 |
| Q75 | - |  |  | SI | Clinical suspicion of Pneumonia	 |
| Q76 | - |  |  | SI | Is there a clinical suspicion that patient has pne... |
| Q77 | - |  |  | SI | Suspected source of infection:	 |
| Q78 | - |  |  | SI | Please select a source of infection	 |
| Q79 | - |  |  | SI | Details:	 |
| Q80 | - |  |  | SI | Please specify other source	 |
| Q81 | - |  |  | SI | Patient age range	 |
| Q82 | - |  |  | SI | Please select the patients age range	 |
| Q83 | - |  |  | SI | Does Patient look sick?	 |
| Q84 | - |  |  | SI | Please indicate if patient looks sick	 |
| Q85 | - |  |  | SI | EWS >= 5	 |
| Q86 | - |  |  | SI | Please indicate if the early warning score is five... |
| Q87 | - |  |  | SI | Impaired immune system	 |
| Q88 | - |  |  | SI | Plesse indicate if patient has an impaired immune ... |
| Q89 | - |  |  | SI | Respiratory Rate:	 |
| Q90 | - |  |  | SI | Please indicate if patient's respiratory rate is o... |
| Q91 | - |  |  | SI | Severe increased respiratory effort / any apnoea	 |
| Q92 | - |  |  | SI | Please indicate if patient has severe increased ef... |
| Q93 | - |  |  | SI | Oxygen therapy >= 4L/min or >50%	 |
| Q94 | - |  |  | SI | Please indicate if patient is on oxygen therapy of... |
| Q95 | - |  |  | SI | Systolic BP:	 |
| Q96 | - |  |  | SI | Please indicate if patient's systolic blood pressu... |
| Q97 | - |  |  | SI | Please indicate if patient's capillary refill time... |
| Q98 | - |  |  | SI | Age 12+ and not passed urine in last 18 hours or u... |
| Q99 | - |  |  | SI | Please indicate if patient is 12 years old or over... |
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