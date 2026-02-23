# SQLUser.LBC_BloodProductGroupBGExceptCriteria

**Schema:** SQLUser
**Columnas:** 175
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Laboratorio**. Parámetros del módulo de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCBPGBGEC_ParRef | bigint | PK |  | NO | Parent Blood Product Group |
| LBCBPGBGEC_AgeFrom | numeric |  |  | SI | Age Range From (format [yy].mmdd , ddd is 0-1231).... |
| LBCBPGBGEC_AgeTo | numeric |  |  | SI | Age Range To (format [yy].mmdd , ddd is 0-1231). O... |
| LBCBPGBGEC_ClinicalCondition_DR | bigint |  | FK | SI | Clinical Condition DR. Optional
Compared with LBE... |
| LBCBPGBGEC_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LBCBPGBGEC_DateFrom | date |  |  | NO | Effective date for the record |
| LBCBPGBGEC_DateTo | date |  |  | SI | DateTo
Last day the record is active |
| LBCBPGBGEC_Desc | varchar |  |  | NO | Description |
| LBCBPGBGEC_NeonatalMode | varchar |  |  | SI | Flag to indicate that this configuration applies o... |
| LBCBPGBGEC_RowID | varchar |  |  | NO | - |
| LBCBPGBGEC_Sequence | numeric |  |  | SI | Priority  Sequence |
| LBCBPGBGEC_Species_DR | bigint |  | FK | SI | Species
Optional, Compared with PAPERSpeciesDR |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Post-operative care day |
| Q04 | - |  |  | SI | Alert and oriented - Glasgow coma scale 15 |
| Q05 | - |  |  | SI | Variance |
| Q06 | - |  |  | SI | Observations are within acceptable limits and stab... |
| Q07 | - |  |  | SI | Variance |
| Q08 | - |  |  | SI | Administer O2 via nasal prongs at 2L/min until SpO... |
| Q09 | - |  |  | SI | Variance |
| Q10 | - |  |  | SI | All ordered blood tests taken and the results revi... |
| Q100 | - |  |  | SI | Other education, please specify in variance |
| Q101 | - |  |  | SI | Variance |
| Q102 | - |  |  | SI | Discharge Planning |
| Q103 | - |  |  | SI | Problems, barriers to discharge assessed |
| Q104 | - |  |  | SI | Variance |
| Q105 | - |  |  | SI | Estimated date of discharge recorded |
| Q106 | - |  |  | SI | Variance |
| Q107 | - |  |  | SI | Discuss discharge plans, problems and barriers to ... |
| Q108 | - |  |  | SI | Variance |
| Q109 | - |  |  | SI | Patient assessed to ensure able to return home |
| Q11 | - |  |  | SI | Variance |
| Q110 | - |  |  | SI | Variance |
| Q111 | - |  |  | SI | Discharge Planners engaged to assist with home sup... |
| Q112 | - |  |  | SI | Variance |
| Q113 | - |  |  | SI | Patient reviewed and assessed for potential rehabi... |
| Q114 | - |  |  | SI | Variance |
| Q115 | - |  |  | SI | Pain management |
| Q116 | - |  |  | SI | Variance |
| Q117 | - |  |  | SI | Wound management |
| Q118 | - |  |  | SI | Variance |
| Q119 | - |  |  | SI | Patient provided with sick certificate |
| Q12 | - |  |  | SI | Patient has attended all required investigative pr... |
| Q120 | - |  |  | SI | Variance |
| Q121 | - |  |  | SI | Adequate care in community if to a remote area |
| Q122 | - |  |  | SI | Variance |
| Q13 | - |  |  | SI | Variance |
| Q14 | - |  |  | SI | Pain / Medication Management |
| Q15 | - |  |  | SI | Patient received prescribed analgesia and reports ... |
| Q16 | - |  |  | SI | Variance |
| Q17 | - |  |  | SI | All medication and IV fluid administered as ordere... |
| Q18 | - |  |  | SI | Variance |
| Q19 | - |  |  | SI | All medication administered as ordered |
| Q20 | - |  |  | SI | Variance |
| Q21 | - |  |  | SI | Skin, Wounds and Drains |
| Q22 | - |  |  | SI | If ordered by medical officer, drain removed witho... |
| Q23 | - |  |  | SI | Variance |
| Q24 | - |  |  | SI | Drain remained patent and all drainage documented.... |
| Q25 | - |  |  | SI | Variance |
| Q26 | - |  |  | SI | Dressing left intact |
| Q27 | - |  |  | SI | Variance |
| Q28 | - |  |  | SI | Wound site remains free from a haematoma and  sign... |
| Q29 | - |  |  | SI | Variance |
| Q30 | - |  |  | SI | Wound dressing attended. Wound site remains free f... |
| Q31 | - |  |  | SI | Variance |
| Q32 | - |  |  | SI | Patient skin remains intact and free from pressure... |
| Q33 | - |  |  | SI | Variance |
| Q34 | - |  |  | SI | Elimination / Fluid Balance |
| Q35 | - |  |  | SI | Patients fluid intake and output recorded on the f... |
| Q36 | - |  |  | SI | Variance |
| Q37 | - |  |  | SI | Patient has voided post operatively and urine outp... |
| Q38 | - |  |  | SI | Variance |
| Q39 | - |  |  | SI | Indwelling catheter removed at the direction of th... |
| Q40 | - |  |  | SI | Variance |
| Q41 | - |  |  | SI | Bowels open post op and documented |
| Q42 | - |  |  | SI | Variance |
| Q43 | - |  |  | SI | All bowel motions documented |
| Q44 | - |  |  | SI | Variance |
| Q45 | - |  |  | SI | Patient tolerating normal diet and IV therapy ceas... |
| Q46 | - |  |  | SI | Variance |
| Q47 | - |  |  | SI | Urine output remained within satisfactory levels |
| Q48 | - |  |  | SI | Variance |
| Q49 | - |  |  | SI | Diet and Fluids |
| Q50 | - |  |  | SI | Patient tolerating normal diet and oral fluids |
| Q51 | - |  |  | SI | Variance |
| Q52 | - |  |  | SI | Hygiene |
| Q53 | - |  |  | SI | Post-op wash attended |
| Q54 | - |  |  | SI | Variance |
| Q55 | - |  |  | SI | Patient tolerated shower with assistance |
| Q56 | - |  |  | SI | Variance |
| Q57 | - |  |  | SI | Mobilisation / Physiotherapy |
| Q58 | - |  |  | SI | Patient preformed deep breathing and coughing exer... |
| Q59 | - |  |  | SI | Variance |
| Q60 | - |  |  | SI | Patient mobilised at the direction of the Medical ... |
| Q61 | - |  |  | SI | Variance |
| Q62 | - |  |  | SI | Patient mobilised in/out of bed while maintaining ... |
| Q63 | - |  |  | SI | Variance |
| Q64 | - |  |  | SI | Mobilised with assistance of the  physiotherapist |
| Q65 | - |  |  | SI | Variance |
| Q66 | - |  |  | SI | Patient positioned and mobilised as per post op or... |
| Q67 | - |  |  | SI | Variance |
| Q68 | - |  |  | SI | Patient tolerating sitting out of bed |
| Q69 | - |  |  | SI | Variance |
| Q70 | - |  |  | SI | Compression stockings insitu |
| Q71 | - |  |  | SI | Variance |
| Q72 | - |  |  | SI | Consults / Referrals |
| Q73 | - |  |  | SI | Referrals arranged as necessary |
| Q74 | - |  |  | SI | Variance |
| Q75 | - |  |  | SI | Patient referred to allied health team as necessar... |
| Q76 | - |  |  | SI | Variance |
| Q77 | - |  |  | SI | OT Assessment completed |
| Q78 | - |  |  | SI | Variance |
| Q79 | - |  |  | SI | Patient referred to allied health team as necessar... |
| Q80 | - |  |  | SI | Variance |
| Q81 | - |  |  | SI | Education |
| Q82 | - |  |  | SI | Patient provided education on using Patient Contro... |
| Q83 | - |  |  | SI | Variance |
| Q84 | - |  |  | SI | Education around safe mobilisation provided to pat... |
| Q85 | - |  |  | SI | Variance |
| Q86 | - |  |  | SI | Mobilisation education provided to patient and und... |
| Q87 | - |  |  | SI | Variance |
| Q88 | - |  |  | SI | Education provided to patient regarding removing s... |
| Q89 | - |  |  | SI | Variance |
| Q90 | - |  |  | SI | Education provided to patient regarding discharge ... |
| Q91 | - |  |  | SI | Variance |
| Q92 | - |  |  | SI | Education provided to patient regarding gentle mob... |
| Q93 | - |  |  | SI | Variance |
| Q94 | - |  |  | SI | Education provided to patient regarding first outp... |
| Q95 | - |  |  | SI | Variance |
| Q96 | - |  |  | SI | Education provided to patient regarding second out... |
| Q97 | - |  |  | SI | Variance |
| Q98 | - |  |  | SI | Education provided to patient regarding no driving... |
| Q99 | - |  |  | SI | Variance |
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
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*