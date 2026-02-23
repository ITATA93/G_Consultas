# questionnaire.QTCCRRT

> Continuous Renal Replacement Therapy (CRRT) Physician Order

**Schema:** questionnaire
**Columnas:** 99
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Continuous Renal Replacement Therapy (CRRT) Physician Order

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Vascular Access |
| Q02 | varchar |  |  | SI | If Others, please specify	 |
| Q03 | varchar |  |  | SI | CRRT mode |
| Q04 | varchar |  |  | SI | Circuit priming |
| Q05 | numeric |  |  | SI | Heparin (units)	 |
| Q06 | varchar |  |  | SI | Haemofilter |
| Q07 | varchar |  |  | SI | If Others, please specify	 |
| Q08 | numeric |  |  | SI | Blood flow rate (ml/min) |
| Q09 | varchar |  |  | SI | *AV (atrioventricular) |
| Q10 | varchar |  |  | SI | Refer to: |
| Q11 | varchar |  |  | SI | AV 400 (20-200) |
| Q12 | varchar |  |  | SI | AV 600 (100-350) |
| Q13 | varchar |  |  | SI | M 100 (75-400) |
| Q14 | varchar |  |  | SI | M 150 (100-450) |
| Q15 | varchar |  |  | SI | AV 1000 (200-500)	 |
| Q16 | varchar |  |  | SI | Type of substitute |
| Q17 | varchar |  |  | SI | Substitute fluid |
| Q18 | varchar |  |  | SI | Post dilution	 |
| Q19 | varchar |  |  | SI | Substitute	 |
| Q20 | numeric |  |  | SI | At rate (ml/hr)	 |
| Q21 | numeric |  |  | SI | Fluid temperature (35-39 degree C)	 |
| Q22 | varchar |  |  | SI | Type of dialysate fluid and rate |
| Q23 | numeric |  |  | SI | Net fluid removal (ml/hr) |
| Q24 | varchar |  |  | SI | Fluid removal rate set on machine = (hourly IV (in... |
| Q25 | numeric |  |  | SI | Goal: central venous pressure (mmHg) for machine	 |
| Q26 | varchar |  |  | SI | Anti coagulation |
| Q27 | numeric |  |  | SI | Heparin bolus: units (10-50 u/kg BW)	 |
| Q28 | numeric |  |  | SI | Continuous hourly heparin: units (5- 20 u/kg BW)	 |
| Q29 | varchar |  |  | SI | Anti coagulation monitoring |
| Q30 | numeric |  |  | SI | Check post filter Partial Thromboplastin Time (PTT... |
| Q31 | varchar |  |  | SI | Anti coagulation monitoring |
| Q32 | varchar |  |  | SI | Note |
| Q33 | varchar |  |  | SI | Ordered by |
| Q34 | varchar |  |  | SI | Physician name	 |
| Q35 | numeric |  |  | SI | Physician ID No.	 |
| Q36 | longvarbinary |  |  | SI | Physician signature	 |
| Q36UDt | date |  |  | SI | Physician signature	 Last Updated Date |
| Q36UTm | time |  |  | SI | Physician signature	 Last Updated Time |
| Q37 | date |  |  | SI | Date |
| Q38 | time |  |  | SI | Time	 |
| Q39 | varchar |  |  | SI | Carried out by |
| Q40 | varchar |  |  | SI | Nurse name	 |
| Q41 | numeric |  |  | SI | Nurse ID No.	 |
| Q42 | longvarbinary |  |  | SI | Nurse signature	 |
| Q42UDt | date |  |  | SI | Nurse signature	 Last Updated Date |
| Q42UTm | time |  |  | SI | Nurse signature	 Last Updated Time |
| Q43 | date |  |  | SI | Date |
| Q44 | time |  |  | SI | Time	 |
| Q45 | varchar |  |  | SI | Post dilution rate |
| Q46 | varchar |  |  | SI | Dialysate |
| Q47 | numeric |  |  | SI | At rate (ml/hr) |
| Q48 | numeric |  |  | SI | Fluid temperature (35-39 degree C) |
| Q49 | varchar |  |  | SI | Blood flow rate comment |
| Q50 | varchar |  |  | SI | Net fluid removal (ml/hr) |
| Q51 | numeric |  |  | SI | At rate (ml/hr) |
| Q52 | numeric |  |  | SI | Fluid temperature (35-39 degree C) |
| Q53 | numeric |  |  | SI | At rate (ml/hr) |
| Q54 | numeric |  |  | SI | Fluid temperature (35-39 degree C) |
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