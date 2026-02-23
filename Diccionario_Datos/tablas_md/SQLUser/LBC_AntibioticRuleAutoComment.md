# SQLUser.LBC_AntibioticRuleAutoComment

**Schema:** SQLUser
**Columnas:** 103
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Laboratorio**. Parámetros del módulo de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCAAC_ParRef | bigint | PK |  | NO | LBCAntibiotic Rules Setup Parent Reference |
| LBCAAC_AutoComment_DR | bigint |  | FK | SI | AutoComment DR |
| LBCAAC_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LBCAAC_RowID | varchar |  |  | NO | - |
| Q01 | - |  |  | SI | Vascular Access |
| Q02 | - |  |  | SI | If Others, please specify	 |
| Q03 | - |  |  | SI | CRRT mode |
| Q04 | - |  |  | SI | Circuit priming |
| Q05 | - |  |  | SI | Heparin (units)	 |
| Q06 | - |  |  | SI | Haemofilter |
| Q07 | - |  |  | SI | If Others, please specify	 |
| Q08 | - |  |  | SI | Blood flow rate (ml/min) |
| Q09 | - |  |  | SI | *AV (atrioventricular) |
| Q10 | - |  |  | SI | Refer to: |
| Q11 | - |  |  | SI | AV 400 (20-200) |
| Q12 | - |  |  | SI | AV 600 (100-350) |
| Q13 | - |  |  | SI | M 100 (75-400) |
| Q14 | - |  |  | SI | M 150 (100-450) |
| Q15 | - |  |  | SI | AV 1000 (200-500)	 |
| Q16 | - |  |  | SI | Type of substitute |
| Q17 | - |  |  | SI | Substitute fluid |
| Q18 | - |  |  | SI | Post dilution	 |
| Q19 | - |  |  | SI | Substitute	 |
| Q20 | - |  |  | SI | At rate (ml/hr)	 |
| Q21 | - |  |  | SI | Fluid temperature (35-39 degree C)	 |
| Q22 | - |  |  | SI | Type of dialysate fluid and rate |
| Q23 | - |  |  | SI | Net fluid removal (ml/hr) |
| Q24 | - |  |  | SI | Fluid removal rate set on machine = (hourly IV (in... |
| Q25 | - |  |  | SI | Goal: central venous pressure (mmHg) for machine	 |
| Q26 | - |  |  | SI | Anti coagulation |
| Q27 | - |  |  | SI | Heparin bolus: units (10-50 u/kg BW)	 |
| Q28 | - |  |  | SI | Continuous hourly heparin: units (5- 20 u/kg BW)	 |
| Q29 | - |  |  | SI | Anti coagulation monitoring |
| Q30 | - |  |  | SI | Check post filter Partial Thromboplastin Time (PTT... |
| Q31 | - |  |  | SI | Anti coagulation monitoring |
| Q32 | - |  |  | SI | Note |
| Q33 | - |  |  | SI | Ordered by |
| Q34 | - |  |  | SI | Physician name	 |
| Q35 | - |  |  | SI | Physician ID No.	 |
| Q36 | - |  |  | SI | Physician signature	 |
| Q36UDt | - |  |  | SI | Physician signature	 Last Updated Date |
| Q36UTm | - |  |  | SI | Physician signature	 Last Updated Time |
| Q37 | - |  |  | SI | Date |
| Q38 | - |  |  | SI | Time	 |
| Q39 | - |  |  | SI | Carried out by |
| Q40 | - |  |  | SI | Nurse name	 |
| Q41 | - |  |  | SI | Nurse ID No.	 |
| Q42 | - |  |  | SI | Nurse signature	 |
| Q42UDt | - |  |  | SI | Nurse signature	 Last Updated Date |
| Q42UTm | - |  |  | SI | Nurse signature	 Last Updated Time |
| Q43 | - |  |  | SI | Date |
| Q44 | - |  |  | SI | Time	 |
| Q45 | - |  |  | SI | Post dilution rate |
| Q46 | - |  |  | SI | Dialysate |
| Q47 | - |  |  | SI | At rate (ml/hr) |
| Q48 | - |  |  | SI | Fluid temperature (35-39 degree C) |
| Q49 | - |  |  | SI | Blood flow rate comment |
| Q50 | - |  |  | SI | Net fluid removal (ml/hr) |
| Q51 | - |  |  | SI | At rate (ml/hr) |
| Q52 | - |  |  | SI | Fluid temperature (35-39 degree C) |
| Q53 | - |  |  | SI | At rate (ml/hr) |
| Q54 | - |  |  | SI | Fluid temperature (35-39 degree C) |
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