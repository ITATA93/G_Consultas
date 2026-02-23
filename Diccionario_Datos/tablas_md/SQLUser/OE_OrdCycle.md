# SQLUser.OE_OrdCycle

**Schema:** SQLUser
**Columnas:** 225
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Órdenes Médicas**. Solicitudes de exámenes, procedimientos, etc.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CYCLE_ParRef | varchar | PK |  | NO | OE_OrdItem Parent Reference |
| CYCLE_Childsub | double |  |  | NO | Childsub |
| CYCLE_DayNumber | varchar |  |  | SI | Day Number |
| CYCLE_DayOfTheWeek | varchar |  |  | SI | Day of the week |
| CYCLE_DoseQty | varchar |  |  | SI | - |
| CYCLE_Instruction | varchar |  |  | SI | Instruction  |
| CYCLE_IsConditional | varchar |  |  | SI | Dosing cycle is a Conditional Dose |
| CYCLE_MinDoseQty | varchar |  |  | SI | - |
| CYCLE_RowId | varchar |  |  | NO | - |
| CYCLE_Time | time |  |  | SI | Dispensing Time |
| Q09 | - |  |  | SI | Discussed Borg Scale |
| Q10 | - |  |  | SI | Exercise Test |
| Q100 | - |  |  | SI | Level 11_11 |
| Q101 | - |  |  | SI | Level 11_12 |
| Q102 | - |  |  | SI | Level 11_13 |
| Q103 | - |  |  | SI | Level 12 |
| Q104 | - |  |  | SI | Level 12_2 |
| Q105 | - |  |  | SI | Level 12_3 |
| Q106 | - |  |  | SI | Level 12_4 |
| Q107 | - |  |  | SI | Level 12_5 |
| Q108 | - |  |  | SI | Level 12_6 |
| Q109 | - |  |  | SI | Level 12_7 |
| Q11 | - |  |  | SI | Max Exercise HR (% of max) |
| Q110 | - |  |  | SI | Level 12_8 |
| Q111 | - |  |  | SI | Level 12_9 |
| Q112 | - |  |  | SI | Level 12_10 |
| Q113 | - |  |  | SI | Level 12_11 |
| Q114 | - |  |  | SI | Level 12_12 |
| Q115 | - |  |  | SI | Level 12_13 |
| Q116 | - |  |  | SI | Level 12_14 |
| Q118 | - |  |  | SI | Total number of shuttles completed |
| Q119 | - |  |  | SI | Total Distance |
| Q12 | - |  |  | SI | %) |
| Q120 | - |  |  | SI | Reason for stopping test |
| Q121 | - |  |  | SI | Comments |
| Q122 | - |  |  | SI | Immediately Post test |
| Q123 | - |  |  | SI | Systolic |
| Q123ObsDR | - |  |  | SI | Systolic DR |
| Q125 | - |  |  | SI | Diastolic |
| Q125ObsDR | - |  |  | SI | Diastolic DR |
| Q126 | - |  |  | SI | Pulse |
| Q126ObsDR | - |  |  | SI | Pulse DR |
| Q127 | - |  |  | SI | Oxygen Saturation |
| Q127ObsDR | - |  |  | SI | Oxygen Saturation DR |
| Q128 | - |  |  | SI | Respirations |
| Q128ObsDR | - |  |  | SI | Respirations DR |
| Q129 | - |  |  | SI | Rating of Perceived Exertion |
| Q129ObsDR | - |  |  | SI | Rating of Perceived Exertion DR |
| Q13 | - |  |  | SI | (Refer to initial HR range guidelines) |
| Q130 | - |  |  | SI | 2 minutes |
| Q131 | - |  |  | SI | Systolic |
| Q131ObsDR | - |  |  | SI | Systolic DR |
| Q132 | - |  |  | SI | Diastolic |
| Q132ObsDR | - |  |  | SI | Diastolic DR |
| Q133 | - |  |  | SI | Pulse |
| Q133ObsDR | - |  |  | SI | Pulse DR |
| Q134 | - |  |  | SI | Oxygen Saturation |
| Q134ObsDR | - |  |  | SI | Oxygen Saturation DR |
| Q135 | - |  |  | SI | Respirations |
| Q135ObsDR | - |  |  | SI | Respirations DR |
| Q136 | - |  |  | SI | Rating of Perceived Exertion |
| Q136ObsDR | - |  |  | SI | Rating of Perceived Exertion DR |
| Q137 | - |  |  | SI | 5 minutes |
| Q138 | - |  |  | SI | Systolic |
| Q138ObsDR | - |  |  | SI | Systolic DR |
| Q139 | - |  |  | SI | Diastolic |
| Q139ObsDR | - |  |  | SI | Diastolic DR |
| Q140 | - |  |  | SI | Pulse |
| Q140ObsDR | - |  |  | SI | Pulse DR |
| Q141 | - |  |  | SI | Oxygen Saturation |
| Q141ObsDR | - |  |  | SI | Oxygen Saturation DR |
| Q142 | - |  |  | SI | Respirations |
| Q142ObsDR | - |  |  | SI | Respirations DR |
| Q143 | - |  |  | SI | Rating of Perceived Exertion |
| Q143ObsDR | - |  |  | SI | Rating of Perceived Exertion DR |
| Q144 | - |  |  | SI | Baseline values |
| Q145 | - |  |  | SI | Systolic |
| Q145ObsDR | - |  |  | SI | Systolic DR |
| Q146 | - |  |  | SI | Diastolic |
| Q146ObsDR | - |  |  | SI | Diastolic DR |
| Q147 | - |  |  | SI | Pulse |
| Q147ObsDR | - |  |  | SI | Pulse DR |
| Q148 | - |  |  | SI | Oxygen Saturation |
| Q148ObsDR | - |  |  | SI | Oxygen Saturation DR |
| Q149 | - |  |  | SI | Respirations |
| Q149ObsDR | - |  |  | SI | Respirations DR |
| Q15 | - |  |  | SI | Level 1 |
| Q150 | - |  |  | SI | Rating of Perceived Exertion |
| Q150ObsDR | - |  |  | SI | Rating of Perceived Exertion DR |
| Q151 | - |  |  | SI | Test at |
| Q152 | - |  |  | SI | Date |
| Q153 | - |  |  | SI | Time |
| Q154 | - |  |  | SI | ( |
| Q155 | - |  |  | SI | Burdon's Modified Borg Scale |
| Q155ObsDR | - |  |  | SI | Burdon's Modified Borg Scale DR |
| Q156 | - |  |  | SI | Burdon's Modified Borg Scale |
| Q156ObsDR | - |  |  | SI | Burdon's Modified Borg Scale DR |
| Q157 | - |  |  | SI | Burdon's Modified Borg Scale |
| Q157ObsDR | - |  |  | SI | Burdon's Modified Borg Scale DR |
| Q158 | - |  |  | SI | Burdon's Modified Borg Scale |
| Q158ObsDR | - |  |  | SI | Burdon's Modified Borg Scale DR |
| Q16 | - |  |  | SI | Level 1_2 |
| Q17 | - |  |  | SI | Level 1_3 |
| Q18 | - |  |  | SI | Level 2 |
| Q19 | - |  |  | SI | Level 2_2 |
| Q20 | - |  |  | SI | Level 2_3 |
| Q21 | - |  |  | SI | Level 2_4 |
| Q22 | - |  |  | SI | Level 3 |
| Q23 | - |  |  | SI | Level 3_2 |
| Q24 | - |  |  | SI | Level 3_3 |
| Q25 | - |  |  | SI | Level 3_4 |
| Q26 | - |  |  | SI | Level 3_5 |
| Q27 | - |  |  | SI | Level 4 |
| Q28 | - |  |  | SI | Level 4_2 |
| Q29 | - |  |  | SI | Level 4_3 |
| Q30 | - |  |  | SI | Level 4_4 |
| Q31 | - |  |  | SI | Level 4_5 |
| Q32 | - |  |  | SI | Level 4_6 |
| Q33 | - |  |  | SI | Level 5 |
| Q34 | - |  |  | SI | Level 5_2 |
| Q35 | - |  |  | SI | Level 5_3 |
| Q36 | - |  |  | SI | Level 5_4 |
| Q37 | - |  |  | SI | Level 5_5 |
| Q38 | - |  |  | SI | Level 5_6 |
| Q39 | - |  |  | SI | Level 5_7 |
| Q40 | - |  |  | SI | Level 6 |
| Q41 | - |  |  | SI | Level 6_2 |
| Q42 | - |  |  | SI | Level 6_3 |
| Q43 | - |  |  | SI | Level 6_4 |
| Q44 | - |  |  | SI | Level 6_5 |
| Q45 | - |  |  | SI | Level 6_6 |
| Q46 | - |  |  | SI | Level 6_7 |
| Q47 | - |  |  | SI | Level 6_8 |
| Q48 | - |  |  | SI | Level 7 |
| Q49 | - |  |  | SI | Level 7_2 |
| Q50 | - |  |  | SI | Level 7_3 |
| Q51 | - |  |  | SI | Level 7_4 |
| Q52 | - |  |  | SI | Level 7_5 |
| Q53 | - |  |  | SI | Level 7_6 |
| Q54 | - |  |  | SI | Level 7_7 |
| Q55 | - |  |  | SI | Level 7_8 |
| Q56 | - |  |  | SI | Level 7_9 |
| Q57 | - |  |  | SI | Level 8 |
| Q58 | - |  |  | SI | Level 8_2 |
| Q59 | - |  |  | SI | Level 8_3 |
| Q60 | - |  |  | SI | Level 8_4 |
| Q61 | - |  |  | SI | Level 8_5 |
| Q62 | - |  |  | SI | Level 8_6 |
| Q63 | - |  |  | SI | Level 8_7 |
| Q64 | - |  |  | SI | Level 8_8 |
| Q65 | - |  |  | SI | Level 8_9 |
| Q66 | - |  |  | SI | Level 8_10 |
| Q67 | - |  |  | SI | Level 9 |
| Q68 | - |  |  | SI | Level 9_2 |
| Q69 | - |  |  | SI | Level 9_3 |
| Q70 | - |  |  | SI | Level 9_4 |
| Q71 | - |  |  | SI | Level 9_5 |
| Q72 | - |  |  | SI | Level 9_6 |
| Q73 | - |  |  | SI | Level 9_7 |
| Q74 | - |  |  | SI | Level 9_8 |
| Q75 | - |  |  | SI | Level 9_9 |
| Q76 | - |  |  | SI | Level 9_10 |
| Q77 | - |  |  | SI | Level 9_11 |
| Q78 | - |  |  | SI | Level 10 |
| Q79 | - |  |  | SI | Level 10_2 |
| Q80 | - |  |  | SI | Level 10_3 |
| Q81 | - |  |  | SI | Level 10_4 |
| Q82 | - |  |  | SI | Level 10_5 |
| Q83 | - |  |  | SI | Level 10_6 |
| Q84 | - |  |  | SI | Level 10_7 |
| Q85 | - |  |  | SI | Level 10_8 |
| Q86 | - |  |  | SI | Level 10_9 |
| Q87 | - |  |  | SI | Level 10_10 |
| Q88 | - |  |  | SI | Level 10_11 |
| Q89 | - |  |  | SI | Level 10_12 |
| Q90 | - |  |  | SI | Level 11 |
| Q91 | - |  |  | SI | Level 11_2 |
| Q92 | - |  |  | SI | Level 11_3 |
| Q93 | - |  |  | SI | Level 11_4 |
| Q94 | - |  |  | SI | Level 11_5 |
| Q95 | - |  |  | SI | Level 11_6 |
| Q96 | - |  |  | SI | Level 11_7 |
| Q97 | - |  |  | SI | Level 11_8 |
| Q98 | - |  |  | SI | Level 11_9 |
| Q99 | - |  |  | SI | Level 11_10 |
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