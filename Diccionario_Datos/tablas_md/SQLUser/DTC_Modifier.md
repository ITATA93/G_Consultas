# SQLUser.DTC_Modifier

**Schema:** SQLUser
**Columnas:** 208
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Dieta**. Parámetros de alimentación y nutrición.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| MODIF_RowId | bigint | PK |  | NO | - |
| MODIF_Code | varchar |  |  | NO | Code |
| MODIF_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| MODIF_CreatedDate | date |  |  | SI | Created Date |
| MODIF_CreatedTime | time |  |  | SI | Created Time |
| MODIF_CreatedUser_DR | bigint |  | FK | SI | Created User |
| MODIF_DateFrom | date |  |  | SI | DateFrom |
| MODIF_DateTo | date |  |  | SI | DateTo |
| MODIF_Desc | varchar |  |  | NO | Description |
| MODIF_Owner | varchar |  |  | SI | Owner |
| MODIF_UpdatedDate | date |  |  | SI | Updated Date |
| MODIF_UpdatedTime | time |  |  | SI | Updated Time |
| MODIF_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Mode |
| Q02 | - |  |  | SI | Treadmill |
| Q03 | - |  |  | SI | Bike |
| Q04 | - |  |  | SI | Other |
| Q05 | - |  |  | SI | Note |
| Q06 | - |  |  | SI | Session 1 - 4 |
| Q07 | - |  |  | SI | Duration |
| Q08 | - |  |  | SI | Intensity |
| Q09 | - |  |  | SI | Heart Rate |
| Q10 | - |  |  | SI | RPE |
| Q100 | - |  |  | SI | Seated knee raise (RPE session 5-8) |
| Q101 | - |  |  | SI | Other1 (sets/rep session 5-8) |
| Q102 | - |  |  | SI | Other1 (HR session 5-8) |
| Q103 | - |  |  | SI | Other1 (RPE session 5-8) |
| Q104 | - |  |  | SI | Other2 (sets/rep session 5-8) |
| Q105 | - |  |  | SI | Other2 (HR session 5-8) |
| Q106 | - |  |  | SI | Other2 (RPE session 5-8) |
| Q107 | - |  |  | SI | Session 9-12 |
| Q108 | - |  |  | SI | Set to stand (sets/rep session 9-12) |
| Q109 | - |  |  | SI | Set to stand (HR session 9-12) |
| Q11 | - |  |  | SI | Duration (Treadmill Session 1-4) |
| Q110 | - |  |  | SI | Set to stand (RPE session 9-12)	 |
| Q111 | - |  |  | SI | Wall push up (sets/rep session 9-12) |
| Q112 | - |  |  | SI | Wall push up (HR session 9-12) |
| Q113 | - |  |  | SI | Wall push up (RPE session 9-12) |
| Q114 | - |  |  | SI | Standing hip ext (sets/rep session 9-12) |
| Q115 | - |  |  | SI | Standing hip ext (HR session 9-12) |
| Q116 | - |  |  | SI | Standing hip ext (RPE session 9-12 |
| Q117 | - |  |  | SI | Calf raises (sets/rep session 9-12) |
| Q118 | - |  |  | SI | Calf raises (HR session 9-12) |
| Q119 | - |  |  | SI | Calf raises (RPE session 9-12) |
| Q12 | - |  |  | SI | Intensity (Treadmill Session 1-4) |
| Q120 | - |  |  | SI | Seated knee raise (sets/rep session 9-12) |
| Q121 | - |  |  | SI | Seated knee raise (HR session 9-12) |
| Q122 | - |  |  | SI | Seated knee raise (RPE session 9-12) |
| Q123 | - |  |  | SI | Other1 (sets/rep session 9-12) |
| Q124 | - |  |  | SI | Other1 (HR session 9-12) |
| Q125 | - |  |  | SI | Other1 (RPE session 9-12) |
| Q126 | - |  |  | SI | Other2 (sets/rep session 9-12) |
| Q127 | - |  |  | SI | Other2 (HR session 9-12) |
| Q128 | - |  |  | SI | Other2 (RPE session 9-12) |
| Q129 | - |  |  | SI | Treadmill |
| Q13 | - |  |  | SI | HR (Treadmill Session 1-4) |
| Q130 | - |  |  | SI | Treadmill |
| Q131 | - |  |  | SI | Bike |
| Q132 | - |  |  | SI | Bike |
| Q133 | - |  |  | SI | Other |
| Q134 | - |  |  | SI | Other |
| Q135 | - |  |  | SI | Set to stand |
| Q136 | - |  |  | SI | Set to stand |
| Q137 | - |  |  | SI | Wall push ups |
| Q138 | - |  |  | SI | Wall push ups |
| Q139 | - |  |  | SI | Standing hip extension / Abduction |
| Q14 | - |  |  | SI | RPE (Treadmill Session 1-4) |
| Q140 | - |  |  | SI | Standing hip extension / Abduction |
| Q141 | - |  |  | SI | Calf raises |
| Q142 | - |  |  | SI | Seated knee raise |
| Q143 | - |  |  | SI | Seated knee raise |
| Q144 | - |  |  | SI | Other |
| Q145 | - |  |  | SI | Other |
| Q146 | - |  |  | SI | Other |
| Q147 | - |  |  | SI | Other |
| Q148 | - |  |  | SI | Calf raise |
| Q149 | - |  |  | SI | Other |
| Q15 | - |  |  | SI | Duration (Bike Session 1-4)	 |
| Q150 | - |  |  | SI | Other |
| Q151 | - |  |  | SI | Other |
| Q152 | - |  |  | SI | Note |
| Q153 | - |  |  | SI | Note |
| Q154 | - |  |  | SI | Other |
| Q155 | - |  |  | SI | Other |
| Q16 | - |  |  | SI | Intensity (Bike Session 1-4) |
| Q17 | - |  |  | SI | HR (Bike Session 1-4) |
| Q18 | - |  |  | SI | RPE (Bike Session 1-4) |
| Q19 | - |  |  | SI | Duration (Other Session 1-4) |
| Q20 | - |  |  | SI | Intensity (Other Session 1-4) |
| Q21 | - |  |  | SI | HR (Other Session 1-4) |
| Q22 | - |  |  | SI | RPE (Other Session 1-4) |
| Q23 | - |  |  | SI | Note (session 1-4) |
| Q24 | - |  |  | SI | Session 5 - 8 |
| Q25 | - |  |  | SI | Duration (Treadmill Session 5 - 8) |
| Q26 | - |  |  | SI | Intensity (Treadmill session 5-6) |
| Q27 | - |  |  | SI | HR (Treadmill session 5-6) |
| Q28 | - |  |  | SI | RPE (Treadmill session 5-6) |
| Q29 | - |  |  | SI | Duration (bike session 5-6) |
| Q30 | - |  |  | SI | Intensity (bike session 5-6) |
| Q31 | - |  |  | SI | HR (bike session 5-6) |
| Q32 | - |  |  | SI | RPE (bike session 5-6) |
| Q33 | - |  |  | SI | Duration (other session 5-6) |
| Q34 | - |  |  | SI | Intensity (other session 5-6) |
| Q35 | - |  |  | SI | HR (other session 5-6) |
| Q36 | - |  |  | SI | RPE (other session 5-6) |
| Q37 | - |  |  | SI | Note (session 5-6)	 |
| Q38 | - |  |  | SI | Session 9-12 |
| Q39 | - |  |  | SI | Duration (Treadmill session 9-12) |
| Q40 | - |  |  | SI | Intensity (Treadmill session 9-12) |
| Q41 | - |  |  | SI | HR (Treadmill session 9-12) |
| Q42 | - |  |  | SI | RPE (Treadmill session 9-12) |
| Q43 | - |  |  | SI | Duration (Bike session 9-12) |
| Q44 | - |  |  | SI | Intensity (Bike session 9-12) |
| Q45 | - |  |  | SI | HR (Bike session 9-12) |
| Q46 | - |  |  | SI | RPE (Bike session 9-12) |
| Q47 | - |  |  | SI | Duration (other session 9-12) |
| Q48 | - |  |  | SI | Intensity (other session 9-12) |
| Q49 | - |  |  | SI | HR (other session 9-12) |
| Q50 | - |  |  | SI | RPE (other session 9-12) |
| Q51 | - |  |  | SI | Note (session 9-12) |
| Q52 | - |  |  | SI | Mode |
| Q53 | - |  |  | SI | Set to stand |
| Q54 | - |  |  | SI | Wall push up |
| Q55 | - |  |  | SI | Standing hip extension / Abduction |
| Q56 | - |  |  | SI | Calf raises |
| Q57 | - |  |  | SI | Seated knee raise |
| Q58 | - |  |  | SI | Other1 |
| Q59 | - |  |  | SI | Other2 |
| Q60 | - |  |  | SI | Sets / Repetitions |
| Q61 | - |  |  | SI | Heart Rate |
| Q62 | - |  |  | SI | RPE |
| Q63 | - |  |  | SI | Session 1-4 |
| Q64 | - |  |  | SI | Set to stand (sets/rep session 1-4) |
| Q65 | - |  |  | SI | Set to stand (HR session 1-4) |
| Q66 | - |  |  | SI | Set to stand (RPE session 1-4) |
| Q67 | - |  |  | SI | Wall push up (sets/rep session 1-4) |
| Q68 | - |  |  | SI | Wall push up (HR session 1-4) |
| Q69 | - |  |  | SI | Wall push up (RPE session 1-4) |
| Q70 | - |  |  | SI | Standing hip ext (sets/rep session 1-4) |
| Q71 | - |  |  | SI | Standing hip ext (HR session 1-4) |
| Q72 | - |  |  | SI | Standing hip ext (RPE session 1-4) |
| Q73 | - |  |  | SI | Calf raises (sets/rep session 1-4) |
| Q74 | - |  |  | SI | Calf raises (HR session 1-4) |
| Q75 | - |  |  | SI | Calf raises (RPE session 1-4) |
| Q76 | - |  |  | SI | Seated knee raises (sets/rep session 1-4) |
| Q77 | - |  |  | SI | Seated knee raises (HR session 1-4) |
| Q78 | - |  |  | SI | Seated knee raises (RPE session 1-4) |
| Q79 | - |  |  | SI | Other1 (sets/rep session 1-4 |
| Q80 | - |  |  | SI | Other1 (HR session 1-4) |
| Q81 | - |  |  | SI | Other1 (RPE session 1-4) |
| Q82 | - |  |  | SI | Other2 (sets/rep session 1-4) |
| Q83 | - |  |  | SI | Other2 (HR session 1-4) |
| Q84 | - |  |  | SI | Other2 (RPE session 1-4) |
| Q85 | - |  |  | SI | Session 5-8 |
| Q86 | - |  |  | SI | Set to stand (sets/rep session 5-8) |
| Q87 | - |  |  | SI | Set to stand (HR session 5-8) |
| Q88 | - |  |  | SI | Set to stand (RPE session 5-8) |
| Q89 | - |  |  | SI | Wall push up (sets/rep session 5-8) |
| Q90 | - |  |  | SI | Wall push up (HR session 5-8) |
| Q91 | - |  |  | SI | Wall push up (RPE session 5-8) |
| Q92 | - |  |  | SI | Standing hip ext (sets/rep session 5-8) |
| Q93 | - |  |  | SI | Standing hip ext (HR session 5-8) |
| Q94 | - |  |  | SI | Standing hip ext (RPE session 5-8) |
| Q95 | - |  |  | SI | Calf raises (sets/rep session 5-8) |
| Q96 | - |  |  | SI | Calf raises (HR session 5-8) |
| Q97 | - |  |  | SI | Calf raises (RPE session 5-8)	 |
| Q98 | - |  |  | SI | Seated knee raise (sets/rep session 5-8) |
| Q99 | - |  |  | SI | Seated knee raise (HR session 5-8) |
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