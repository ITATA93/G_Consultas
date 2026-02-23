# SQLUser.OEC_NeedleGauge

**Schema:** SQLUser
**Columnas:** 237
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Entry Orders**. Tipos y estados de órdenes.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| NEDG_RowId | bigint | PK |  | NO | - |
| NEDG_Code | varchar |  |  | NO | Code |
| NEDG_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| NEDG_CreatedDate | date |  |  | SI | Created Date |
| NEDG_CreatedTime | time |  |  | SI | Created Time |
| NEDG_CreatedUser_DR | bigint |  | FK | SI | Created User |
| NEDG_DateFrom | date |  |  | SI | Date From |
| NEDG_DateTo | date |  |  | SI | Date To |
| NEDG_Desc | varchar |  |  | NO | Description |
| NEDG_Epidural | varchar |  |  | SI | Checkbox for Epidural Restriction |
| NEDG_Owner | varchar |  |  | SI | Owner |
| NEDG_Spinal | varchar |  |  | SI | Checkbox for Spinal Restriction |
| NEDG_UpdatedDate | date |  |  | SI | Updated Date |
| NEDG_UpdatedTime | time |  |  | SI | Updated Time |
| NEDG_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Visual Acuity - Uncorrected |
| Q02 | - |  |  | SI | Right eye |
| Q03 | - |  |  | SI | Left eye |
| Q04 | - |  |  | SI | Both eyes |
| Q05 | - |  |  | SI | VA-Dt |
| Q06 | - |  |  | SI | Va-dt2 |
| Q07 | - |  |  | SI | Va-dt3 |
| Q08 | - |  |  | SI | VA-PH |
| Q09 | - |  |  | SI | VA-ph2 |
| Q10 | - |  |  | SI | vA-Ph3 |
| Q100 | - |  |  | SI | add2 |
| Q101 | - |  |  | SI | VA-Dt |
| Q102 | - |  |  | SI | VA-dt2 |
| Q103 | - |  |  | SI | VA-dt3 |
| Q104 | - |  |  | SI | VA-Nr |
| Q105 | - |  |  | SI | va-nr2 |
| Q106 | - |  |  | SI | va-nr3 |
| Q107 | - |  |  | SI | Notes |
| Q108 | - |  |  | SI | Prescription (Final) Refraction |
| Q109 | - |  |  | SI | Date |
| Q11 | - |  |  | SI | VA-Nr |
| Q110 | - |  |  | SI | IPD |
| Q111 | - |  |  | SI | mm |
| Q112 | - |  |  | SI | Material |
| Q113 | - |  |  | SI | Right eye |
| Q114 | - |  |  | SI | Left eye |
| Q115 | - |  |  | SI | Both eyes |
| Q116 | - |  |  | SI | Sph |
| Q117 | - |  |  | SI | sph2 |
| Q118 | - |  |  | SI | Cyl |
| Q119 | - |  |  | SI | Axis |
| Q12 | - |  |  | SI | va-nr2 |
| Q120 | - |  |  | SI | axis2 |
| Q121 | - |  |  | SI | Add |
| Q122 | - |  |  | SI | add2 |
| Q123 | - |  |  | SI | VA-Dt |
| Q124 | - |  |  | SI | VA-Dt2 |
| Q125 | - |  |  | SI | va-dt3 |
| Q126 | - |  |  | SI | VA-Nr |
| Q127 | - |  |  | SI | VA-nr2 |
| Q128 | - |  |  | SI | va-nr3 |
| Q129 | - |  |  | SI | Notes |
| Q13 | - |  |  | SI | va-nr3 |
| Q130 | - |  |  | SI | Add 2 |
| Q131 | - |  |  | SI | Cyl 2 |
| Q132 | - |  |  | SI | Cyl2 |
| Q133 | - |  |  | SI | Date |
| Q134 | - |  |  | SI | Time |
| Q135 | - |  |  | SI | Prism |
| Q136 | - |  |  | SI | Prism |
| Q137 | - |  |  | SI | Prism |
| Q138 | - |  |  | SI | Prism |
| Q139 | - |  |  | SI | Prism |
| Q14 | - |  |  | SI | Notes |
| Q140 | - |  |  | SI | Prism |
| Q141 | - |  |  | SI | Prism |
| Q142 | - |  |  | SI | Prism |
| Q143 | - |  |  | SI | Prism |
| Q144 | - |  |  | SI | Prism |
| Q145 | - |  |  | SI | Prism |
| Q146 | - |  |  | SI | Prism |
| Q147 | - |  |  | SI | Prism |
| Q148 | - |  |  | SI | Prism |
| Q149 | - |  |  | SI | Prism |
| Q15 | - |  |  | SI | Visual Acuity - Corrected |
| Q150 | - |  |  | SI | Prism |
| Q151 | - |  |  | SI | Base |
| Q152 | - |  |  | SI | Base |
| Q153 | - |  |  | SI | Base |
| Q154 | - |  |  | SI | Base |
| Q155 | - |  |  | SI | Base |
| Q156 | - |  |  | SI | Base |
| Q157 | - |  |  | SI | Base |
| Q158 | - |  |  | SI | Base |
| Q159 | - |  |  | SI | Base |
| Q16 | - |  |  | SI | Right eye |
| Q160 | - |  |  | SI | Base |
| Q161 | - |  |  | SI | Base |
| Q162 | - |  |  | SI | Base |
| Q163 | - |  |  | SI | Base |
| Q164 | - |  |  | SI | Base |
| Q165 | - |  |  | SI | Base |
| Q166 | - |  |  | SI | Base |
| Q167 | - |  |  | SI | Prism |
| Q168 | - |  |  | SI | Prism |
| Q169 | - |  |  | SI | Base |
| Q17 | - |  |  | SI | Left eye |
| Q170 | - |  |  | SI | Base |
| Q171 | - |  |  | SI | Prism |
| Q172 | - |  |  | SI | Prism |
| Q173 | - |  |  | SI | Prism |
| Q174 | - |  |  | SI | Base |
| Q175 | - |  |  | SI | Base |
| Q176 | - |  |  | SI | Base |
| Q177 | - |  |  | SI | Prism |
| Q178 | - |  |  | SI | Prism |
| Q179 | - |  |  | SI | Prism |
| Q18 | - |  |  | SI | Sph |
| Q180 | - |  |  | SI | Base |
| Q181 | - |  |  | SI | Base |
| Q182 | - |  |  | SI | Base |
| Q19 | - |  |  | SI | sph2 |
| Q20 | - |  |  | SI | Cyl |
| Q21 | - |  |  | SI | Cyl2 |
| Q22 | - |  |  | SI | Axis |
| Q23 | - |  |  | SI | axis2 |
| Q24 | - |  |  | SI | Add |
| Q25 | - |  |  | SI | VA-Dt |
| Q26 | - |  |  | SI | VA-dt2 |
| Q27 | - |  |  | SI | Va-dt3 |
| Q28 | - |  |  | SI | Both eyes |
| Q29 | - |  |  | SI | VA-Nr |
| Q30 | - |  |  | SI | VA-Nr2 |
| Q31 | - |  |  | SI | VA-Nr3 |
| Q32 | - |  |  | SI | Notes |
| Q33 | - |  |  | SI | Refraction Type |
| Q34 | - |  |  | SI | Right eye |
| Q35 | - |  |  | SI | Left eye |
| Q36 | - |  |  | SI | Both eyes |
| Q37 | - |  |  | SI | Sph |
| Q38 | - |  |  | SI | sph2 |
| Q39 | - |  |  | SI | Cyl |
| Q40 | - |  |  | SI | Axis |
| Q41 | - |  |  | SI | Axis2 |
| Q42 | - |  |  | SI | Add |
| Q43 | - |  |  | SI | Add2 |
| Q44 | - |  |  | SI | VA-Dt |
| Q45 | - |  |  | SI | va-dt2 |
| Q46 | - |  |  | SI | va-dt3 |
| Q47 | - |  |  | SI | VA-Nr |
| Q48 | - |  |  | SI | VA-Nr2 |
| Q49 | - |  |  | SI | VA-nr3 |
| Q50 | - |  |  | SI | Notes |
| Q51 | - |  |  | SI | Refraction Type |
| Q52 | - |  |  | SI | Right eye |
| Q53 | - |  |  | SI | Left eye |
| Q54 | - |  |  | SI | Both eyes |
| Q55 | - |  |  | SI | Sph |
| Q56 | - |  |  | SI | sph2 |
| Q57 | - |  |  | SI | Cyl |
| Q58 | - |  |  | SI | Cyl2 |
| Q59 | - |  |  | SI | Axis |
| Q60 | - |  |  | SI | Axis2 |
| Q61 | - |  |  | SI | Add |
| Q62 | - |  |  | SI | Add2 |
| Q63 | - |  |  | SI | VA-Dt |
| Q64 | - |  |  | SI | va-dt2 |
| Q65 | - |  |  | SI | va-dt3 |
| Q66 | - |  |  | SI | VA-Nr |
| Q67 | - |  |  | SI | va-nr2 |
| Q68 | - |  |  | SI | va-nr3 |
| Q69 | - |  |  | SI | Notes |
| Q70 | - |  |  | SI | Subjective Refraction - Dry |
| Q71 | - |  |  | SI | Right eye |
| Q72 | - |  |  | SI | Left eye |
| Q73 | - |  |  | SI | Both eyes |
| Q74 | - |  |  | SI | Sph |
| Q75 | - |  |  | SI | sph2 |
| Q76 | - |  |  | SI | Cyl |
| Q77 | - |  |  | SI | Cyl2 |
| Q78 | - |  |  | SI | Axis |
| Q79 | - |  |  | SI | axis2 |
| Q80 | - |  |  | SI | Add |
| Q81 | - |  |  | SI | add2 |
| Q82 | - |  |  | SI | VA-Dt |
| Q83 | - |  |  | SI | VA-Dt2 |
| Q84 | - |  |  | SI | va-dt3 |
| Q85 | - |  |  | SI | VA-Nr |
| Q86 | - |  |  | SI | VA-nt2 |
| Q87 | - |  |  | SI | va-nt3 |
| Q88 | - |  |  | SI | Notes |
| Q89 | - |  |  | SI | Subjective Refraction - Wet |
| Q90 | - |  |  | SI | Right eye |
| Q91 | - |  |  | SI | Left eye |
| Q92 | - |  |  | SI | Both eyes |
| Q93 | - |  |  | SI | Sph |
| Q94 | - |  |  | SI | sph2 |
| Q95 | - |  |  | SI | Cyl |
| Q96 | - |  |  | SI | Cyl2 |
| Q97 | - |  |  | SI | Axis |
| Q98 | - |  |  | SI | Axis2 |
| Q99 | - |  |  | SI | Add |
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