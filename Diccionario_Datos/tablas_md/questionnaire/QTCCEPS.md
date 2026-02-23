# questionnaire.QTCCEPS

> Cardiac Exercise Prescription Sheet

**Schema:** questionnaire
**Columnas:** 196
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Cardiac Exercise Prescription Sheet

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Mode |
| Q02 | varchar |  |  | SI | Treadmill |
| Q03 | varchar |  |  | SI | Bike |
| Q04 | varchar |  |  | SI | Other |
| Q05 | varchar |  |  | SI | Note |
| Q06 | varchar |  |  | SI | Session 1 - 4 |
| Q07 | varchar |  |  | SI | Duration |
| Q08 | varchar |  |  | SI | Intensity |
| Q09 | varchar |  |  | SI | Heart Rate |
| Q10 | varchar |  |  | SI | RPE |
| Q100 | numeric |  |  | SI | Seated knee raise (RPE session 5-8) |
| Q101 | varchar |  |  | SI | Other1 (sets/rep session 5-8) |
| Q102 | numeric |  |  | SI | Other1 (HR session 5-8) |
| Q103 | numeric |  |  | SI | Other1 (RPE session 5-8) |
| Q104 | varchar |  |  | SI | Other2 (sets/rep session 5-8) |
| Q105 | numeric |  |  | SI | Other2 (HR session 5-8) |
| Q106 | numeric |  |  | SI | Other2 (RPE session 5-8) |
| Q107 | varchar |  |  | SI | Session 9-12 |
| Q108 | varchar |  |  | SI | Set to stand (sets/rep session 9-12) |
| Q109 | numeric |  |  | SI | Set to stand (HR session 9-12) |
| Q11 | varchar |  |  | SI | Duration (Treadmill Session 1-4) |
| Q110 | numeric |  |  | SI | Set to stand (RPE session 9-12)	 |
| Q111 | varchar |  |  | SI | Wall push up (sets/rep session 9-12) |
| Q112 | numeric |  |  | SI | Wall push up (HR session 9-12) |
| Q113 | numeric |  |  | SI | Wall push up (RPE session 9-12) |
| Q114 | varchar |  |  | SI | Standing hip ext (sets/rep session 9-12) |
| Q115 | numeric |  |  | SI | Standing hip ext (HR session 9-12) |
| Q116 | numeric |  |  | SI | Standing hip ext (RPE session 9-12 |
| Q117 | varchar |  |  | SI | Calf raises (sets/rep session 9-12) |
| Q118 | numeric |  |  | SI | Calf raises (HR session 9-12) |
| Q119 | numeric |  |  | SI | Calf raises (RPE session 9-12) |
| Q12 | varchar |  |  | SI | Intensity (Treadmill Session 1-4) |
| Q120 | varchar |  |  | SI | Seated knee raise (sets/rep session 9-12) |
| Q121 | numeric |  |  | SI | Seated knee raise (HR session 9-12) |
| Q122 | numeric |  |  | SI | Seated knee raise (RPE session 9-12) |
| Q123 | varchar |  |  | SI | Other1 (sets/rep session 9-12) |
| Q124 | numeric |  |  | SI | Other1 (HR session 9-12) |
| Q125 | numeric |  |  | SI | Other1 (RPE session 9-12) |
| Q126 | varchar |  |  | SI | Other2 (sets/rep session 9-12) |
| Q127 | numeric |  |  | SI | Other2 (HR session 9-12) |
| Q128 | numeric |  |  | SI | Other2 (RPE session 9-12) |
| Q129 | varchar |  |  | SI | Treadmill |
| Q13 | numeric |  |  | SI | HR (Treadmill Session 1-4) |
| Q130 | varchar |  |  | SI | Treadmill |
| Q131 | varchar |  |  | SI | Bike |
| Q132 | varchar |  |  | SI | Bike |
| Q133 | varchar |  |  | SI | Other |
| Q134 | varchar |  |  | SI | Other |
| Q135 | varchar |  |  | SI | Set to stand |
| Q136 | varchar |  |  | SI | Set to stand |
| Q137 | varchar |  |  | SI | Wall push ups |
| Q138 | varchar |  |  | SI | Wall push ups |
| Q139 | varchar |  |  | SI | Standing hip extension / Abduction |
| Q14 | numeric |  |  | SI | RPE (Treadmill Session 1-4) |
| Q140 | varchar |  |  | SI | Standing hip extension / Abduction |
| Q141 | varchar |  |  | SI | Calf raises |
| Q142 | varchar |  |  | SI | Seated knee raise |
| Q143 | varchar |  |  | SI | Seated knee raise |
| Q144 | varchar |  |  | SI | Other |
| Q145 | varchar |  |  | SI | Other |
| Q146 | varchar |  |  | SI | Other |
| Q147 | varchar |  |  | SI | Other |
| Q148 | varchar |  |  | SI | Calf raise |
| Q149 | varchar |  |  | SI | Other |
| Q15 | varchar |  |  | SI | Duration (Bike Session 1-4)	 |
| Q150 | varchar |  |  | SI | Other |
| Q151 | varchar |  |  | SI | Other |
| Q152 | varchar |  |  | SI | Note |
| Q153 | varchar |  |  | SI | Note |
| Q154 | varchar |  |  | SI | Other |
| Q155 | varchar |  |  | SI | Other |
| Q16 | varchar |  |  | SI | Intensity (Bike Session 1-4) |
| Q17 | numeric |  |  | SI | HR (Bike Session 1-4) |
| Q18 | numeric |  |  | SI | RPE (Bike Session 1-4) |
| Q19 | varchar |  |  | SI | Duration (Other Session 1-4) |
| Q20 | varchar |  |  | SI | Intensity (Other Session 1-4) |
| Q21 | numeric |  |  | SI | HR (Other Session 1-4) |
| Q22 | numeric |  |  | SI | RPE (Other Session 1-4) |
| Q23 | varchar |  |  | SI | Note (session 1-4) |
| Q24 | varchar |  |  | SI | Session 5 - 8 |
| Q25 | varchar |  |  | SI | Duration (Treadmill Session 5 - 8) |
| Q26 | varchar |  |  | SI | Intensity (Treadmill session 5-6) |
| Q27 | numeric |  |  | SI | HR (Treadmill session 5-6) |
| Q28 | numeric |  |  | SI | RPE (Treadmill session 5-6) |
| Q29 | varchar |  |  | SI | Duration (bike session 5-6) |
| Q30 | varchar |  |  | SI | Intensity (bike session 5-6) |
| Q31 | numeric |  |  | SI | HR (bike session 5-6) |
| Q32 | numeric |  |  | SI | RPE (bike session 5-6) |
| Q33 | varchar |  |  | SI | Duration (other session 5-6) |
| Q34 | varchar |  |  | SI | Intensity (other session 5-6) |
| Q35 | numeric |  |  | SI | HR (other session 5-6) |
| Q36 | numeric |  |  | SI | RPE (other session 5-6) |
| Q37 | varchar |  |  | SI | Note (session 5-6)	 |
| Q38 | varchar |  |  | SI | Session 9-12 |
| Q39 | varchar |  |  | SI | Duration (Treadmill session 9-12) |
| Q40 | varchar |  |  | SI | Intensity (Treadmill session 9-12) |
| Q41 | numeric |  |  | SI | HR (Treadmill session 9-12) |
| Q42 | numeric |  |  | SI | RPE (Treadmill session 9-12) |
| Q43 | varchar |  |  | SI | Duration (Bike session 9-12) |
| Q44 | varchar |  |  | SI | Intensity (Bike session 9-12) |
| Q45 | numeric |  |  | SI | HR (Bike session 9-12) |
| Q46 | numeric |  |  | SI | RPE (Bike session 9-12) |
| Q47 | varchar |  |  | SI | Duration (other session 9-12) |
| Q48 | varchar |  |  | SI | Intensity (other session 9-12) |
| Q49 | numeric |  |  | SI | HR (other session 9-12) |
| Q50 | numeric |  |  | SI | RPE (other session 9-12) |
| Q51 | varchar |  |  | SI | Note (session 9-12) |
| Q52 | varchar |  |  | SI | Mode |
| Q53 | varchar |  |  | SI | Set to stand |
| Q54 | varchar |  |  | SI | Wall push up |
| Q55 | varchar |  |  | SI | Standing hip extension / Abduction |
| Q56 | varchar |  |  | SI | Calf raises |
| Q57 | varchar |  |  | SI | Seated knee raise |
| Q58 | varchar |  |  | SI | Other1 |
| Q59 | varchar |  |  | SI | Other2 |
| Q60 | varchar |  |  | SI | Sets / Repetitions |
| Q61 | varchar |  |  | SI | Heart Rate |
| Q62 | varchar |  |  | SI | RPE |
| Q63 | varchar |  |  | SI | Session 1-4 |
| Q64 | varchar |  |  | SI | Set to stand (sets/rep session 1-4) |
| Q65 | numeric |  |  | SI | Set to stand (HR session 1-4) |
| Q66 | numeric |  |  | SI | Set to stand (RPE session 1-4) |
| Q67 | varchar |  |  | SI | Wall push up (sets/rep session 1-4) |
| Q68 | numeric |  |  | SI | Wall push up (HR session 1-4) |
| Q69 | numeric |  |  | SI | Wall push up (RPE session 1-4) |
| Q70 | varchar |  |  | SI | Standing hip ext (sets/rep session 1-4) |
| Q71 | numeric |  |  | SI | Standing hip ext (HR session 1-4) |
| Q72 | numeric |  |  | SI | Standing hip ext (RPE session 1-4) |
| Q73 | varchar |  |  | SI | Calf raises (sets/rep session 1-4) |
| Q74 | numeric |  |  | SI | Calf raises (HR session 1-4) |
| Q75 | numeric |  |  | SI | Calf raises (RPE session 1-4) |
| Q76 | varchar |  |  | SI | Seated knee raises (sets/rep session 1-4) |
| Q77 | numeric |  |  | SI | Seated knee raises (HR session 1-4) |
| Q78 | numeric |  |  | SI | Seated knee raises (RPE session 1-4) |
| Q79 | varchar |  |  | SI | Other1 (sets/rep session 1-4 |
| Q80 | numeric |  |  | SI | Other1 (HR session 1-4) |
| Q81 | numeric |  |  | SI | Other1 (RPE session 1-4) |
| Q82 | varchar |  |  | SI | Other2 (sets/rep session 1-4) |
| Q83 | numeric |  |  | SI | Other2 (HR session 1-4) |
| Q84 | numeric |  |  | SI | Other2 (RPE session 1-4) |
| Q85 | varchar |  |  | SI | Session 5-8 |
| Q86 | varchar |  |  | SI | Set to stand (sets/rep session 5-8) |
| Q87 | numeric |  |  | SI | Set to stand (HR session 5-8) |
| Q88 | numeric |  |  | SI | Set to stand (RPE session 5-8) |
| Q89 | varchar |  |  | SI | Wall push up (sets/rep session 5-8) |
| Q90 | numeric |  |  | SI | Wall push up (HR session 5-8) |
| Q91 | numeric |  |  | SI | Wall push up (RPE session 5-8) |
| Q92 | varchar |  |  | SI | Standing hip ext (sets/rep session 5-8) |
| Q93 | numeric |  |  | SI | Standing hip ext (HR session 5-8) |
| Q94 | numeric |  |  | SI | Standing hip ext (RPE session 5-8) |
| Q95 | varchar |  |  | SI | Calf raises (sets/rep session 5-8) |
| Q96 | numeric |  |  | SI | Calf raises (HR session 5-8) |
| Q97 | numeric |  |  | SI | Calf raises (RPE session 5-8)	 |
| Q98 | varchar |  |  | SI | Seated knee raise (sets/rep session 5-8) |
| Q99 | numeric |  |  | SI | Seated knee raise (HR session 5-8) |
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