# SQLUser.PAC_Allergy

**Schema:** SQLUser
**Columnas:** 238
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ALG_RowId | bigint | PK |  | NO | - |
| ALG_AllergyCategoryDR | bigint |  | FK | SI | Allergy Category Des Ref |
| ALG_Code | varchar |  |  | NO | Code |
| ALG_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| ALG_CodeTranslated | varchar |  |  | SI | - |
| ALG_CreatedDate | date |  |  | SI | Created Date |
| ALG_CreatedTime | time |  |  | SI | Created Time |
| ALG_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ALG_DateFrom | date |  |  | SI | Date From |
| ALG_DateTo | date |  |  | SI | Date To |
| ALG_Desc | varchar |  |  | NO | Description |
| ALG_DescTranslated | varchar |  |  | SI | - |
| ALG_Owner | varchar |  |  | SI | Owner |
| ALG_SnomedConcept_DR | bigint |  | FK | SI | Des Ref PACSnomedConcept |
| ALG_SnomedTerms_DR | bigint |  | FK | SI | Des Ref PACSnomedTerms |
| ALG_Type_DR | bigint |  | FK | SI | Des Ref to ALGType |
| ALG_UpdatedDate | date |  |  | SI | Updated Date |
| ALG_UpdatedTime | time |  |  | SI | Updated Time |
| ALG_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Date of accident	 |
| Q02 | - |  |  | SI | Affected side |
| Q03 | - |  |  | SI | Walk |
| Q04 | - |  |  | SI | Walk backwards |
| Q05 | - |  |  | SI | Walk on toes |
| Q06 | - |  |  | SI | Walk over obstacle |
| Q07 | - |  |  | SI | Run |
| Q08 | - |  |  | SI | Skip |
| Q09 | - |  |  | SI | Hop forward (more-affected leg) |
| Q10 | - |  |  | SI | Bound (more-affected leg) |
| Q100 | - |  |  | SI | • As for walking. |
| Q101 | - |  |  | SI | • Any heel contact during the middle 10cm is recor... |
| Q102 | - |  |  | SI | Walk over obstacle |
| Q103 | - |  |  | SI | • As for walking. |
| Q104 | - |  |  | SI | • A house brick is placed across the walkway at th... |
| Q105 | - |  |  | SI | • Patients must step over the brick without contac... |
| Q106 | - |  |  | SI | • A fail is recorded if patients step around the b... |
| Q107 | - |  |  | SI | Run |
| Q108 | - |  |  | SI | • The middle 10m of a 20m trial is timed. |
| Q109 | - |  |  | SI | • A fail is recorded if patients fail to have a co... |
| Q11 | - |  |  | SI | Bound (less-affected leg) |
| Q110 | - |  |  | SI | Skipping |
| Q111 | - |  |  | SI | • The middle 10m of a 20m trial is timed. |
| Q112 | - |  |  | SI | • A fail is recorded if patients fail to have a co... |
| Q113 | - |  |  | SI | Hop forward |
| Q114 | - |  |  | SI | • Patients stand on their more affected leg and ho... |
| Q115 | - |  |  | SI | Bound (affected) |
| Q116 | - |  |  | SI | • A bound is a jump from one leg to the other with... |
| Q117 | - |  |  | SI | • Patients stand behind a line on their less affec... |
| Q118 | - |  |  | SI | • Each bound is measured from the line to the heel... |
| Q119 | - |  |  | SI | • The average of three trials is recorded. |
| Q12 | - |  |  | SI | Up stairs dependent (rail OR not reciprocal) |
| Q120 | - |  |  | SI | Bound (less affected) |
| Q121 | - |  |  | SI | • Patients stand behind a line on their more affec... |
| Q122 | - |  |  | SI | • The average of three trials is recorded. |
| Q123 | - |  |  | SI | Up stairs |
| Q124 | - |  |  | SI | • Patients are asked to walk up a flight of 14 sta... |
| Q125 | - |  |  | SI | • The trial is recorded from when the patient star... |
| Q126 | - |  |  | SI | • Patients who use a rail or a non-reciprocal patt... |
| Q127 | - |  |  | SI | • Patients who ascend the stairs reciprocally with... |
| Q128 | - |  |  | SI | Down stairs |
| Q129 | - |  |  | SI | • As for Up stairs. |
| Q13 | - |  |  | SI | Up stairs independent (no rail AND reciprocal) |
| Q130 | - |  |  | SI | Performance |
| Q131 | - |  |  | SI | Performance |
| Q132 | - |  |  | SI | Score |
| Q133 | - |  |  | SI | Score |
| Q134 | - |  |  | SI | Performance |
| Q135 | - |  |  | SI | Performance |
| Q136 | - |  |  | SI | Performance |
| Q137 | - |  |  | SI | Performance |
| Q138 | - |  |  | SI | Performance |
| Q139 | - |  |  | SI | Performance |
| Q14 | - |  |  | SI | Down stairs dependent (rail OR not reciprocal) |
| Q140 | - |  |  | SI | Performance |
| Q141 | - |  |  | SI | Performance |
| Q142 | - |  |  | SI | Performance |
| Q143 | - |  |  | SI | Performance |
| Q144 | - |  |  | SI | Performance |
| Q145 | - |  |  | SI | Score |
| Q146 | - |  |  | SI | Score |
| Q147 | - |  |  | SI | Score |
| Q148 | - |  |  | SI | Score |
| Q149 | - |  |  | SI | Score |
| Q15 | - |  |  | SI | Down stairs independent (no rail AND reciprocal) |
| Q150 | - |  |  | SI | Score |
| Q151 | - |  |  | SI | Score |
| Q152 | - |  |  | SI | Score |
| Q153 | - |  |  | SI | Score |
| Q154 | - |  |  | SI | Score |
| Q155 | - |  |  | SI | Score |
| Q156 | - |  |  | SI | Walk |
| Q157 | - |  |  | SI | Walk backwards |
| Q158 | - |  |  | SI | Walk on toes |
| Q159 | - |  |  | SI | Walk over obstacle |
| Q16 | - |  |  | SI | Score |
| Q160 | - |  |  | SI | Run |
| Q161 | - |  |  | SI | Skip |
| Q162 | - |  |  | SI | Hop forward (more-affected leg) |
| Q163 | - |  |  | SI | Bound (more-affected leg) |
| Q164 | - |  |  | SI | Bound (less-affected leg) |
| Q165 | - |  |  | SI | Up stairs dependent (rail OR not reciprocal) |
| Q166 | - |  |  | SI | Up stairs independent (no rail AND reciprocal) |
| Q167 | - |  |  | SI | Down stairs dependent (rail OR not reciprocal) |
| Q168 | - |  |  | SI | Down stairs independent (no rail AND reciprocal) |
| Q169 | - |  |  | SI | Walk |
| Q17 | - |  |  | SI | Classification |
| Q170 | - |  |  | SI | Walk backwards |
| Q171 | - |  |  | SI | Walk on toes |
| Q172 | - |  |  | SI | Walk over obstacle |
| Q173 | - |  |  | SI | Run |
| Q174 | - |  |  | SI | Skip |
| Q175 | - |  |  | SI | Hop forward (more-affected leg) |
| Q176 | - |  |  | SI | Up stairs dependent (rail OR not reciprocal) |
| Q177 | - |  |  | SI | Up stairs independent (no rail AND reciprocal) |
| Q178 | - |  |  | SI | Down stairs dependent (rail OR not reciprocal) |
| Q179 | - |  |  | SI | Down stairs independent (no rail AND reciprocal) |
| Q18 | - |  |  | SI | 0 - 54 |
| Q19 | - |  |  | SI | Higher scores indicate better mobility performance |
| Q20 | - |  |  | SI | The High Level Mobility and Assessment tool (HiMAT... |
| Q21 | - |  |  | SI | 0 - 54: Higher scores indicate better mobility per... |
| Q22 | - |  |  | SI | Equipment Required |
| Q23 | - |  |  | SI | • at least 20m even surface walkway |
| Q24 | - |  |  | SI | • 1 house brick |
| Q25 | - |  |  | SI | • access to a flight of 14 stairs |
| Q26 | - |  |  | SI | • stopwatch |
| Q27 | - |  |  | SI | • tape measure |
| Q28 | - |  |  | SI | • pen and a copy of the HiMAT tool |
| Q29 | - |  |  | SI | Preparation of Environment |
| Q30 | - |  |  | SI | • Measure and mark a 20m walkway to count the midd... |
| Q31 | - |  |  | SI | Instructions |
| Q32 | - |  |  | SI | • Patients are permitted 1 practice trial per item |
| Q33 | - |  |  | SI | • Patients are to perform each task at the maximum... |
| Q34 | - |  |  | SI | • All items (except stairs) are timed or counted i... |
| Q35 | - |  |  | SI | Date |
| Q36 | - |  |  | SI | Time |
| Q37 | - |  |  | SI | Score |
| Q38 | - |  |  | SI | Performance |
| Q39 | - |  |  | SI | Walk |
| Q40 | - |  |  | SI | seconds |
| Q41 | - |  |  | SI | Walk performance (seconds) |
| Q42 | - |  |  | SI | Walk backwards |
| Q43 | - |  |  | SI | seconds |
| Q44 | - |  |  | SI | Walk backwards performance (seconds) |
| Q45 | - |  |  | SI | Walk on toes |
| Q46 | - |  |  | SI | seconds |
| Q47 | - |  |  | SI | Walk on toes performance (seconds) |
| Q48 | - |  |  | SI | Walk over obstacle |
| Q49 | - |  |  | SI | seconds |
| Q50 | - |  |  | SI | Walk over obstacle performance (seconds) |
| Q51 | - |  |  | SI | Run |
| Q52 | - |  |  | SI | seconds |
| Q53 | - |  |  | SI | Run performance (seconds) |
| Q54 | - |  |  | SI | Skip |
| Q55 | - |  |  | SI | seconds |
| Q56 | - |  |  | SI | Skip performance (seconds) |
| Q57 | - |  |  | SI | Hop forward (more-affected leg) |
| Q58 | - |  |  | SI | seconds |
| Q59 | - |  |  | SI | Hop forward (more-affected leg) performance (secon... |
| Q60 | - |  |  | SI | Bound (more-affected leg) |
| Q61 | - |  |  | SI | cm - Attempt one |
| Q62 | - |  |  | SI | cm - Attempt two |
| Q63 | - |  |  | SI | cm - Attempt three |
| Q64 | - |  |  | SI | cm - Average of attempts |
| Q65 | - |  |  | SI | Bound (more-affected leg) performance (cm) - attem... |
| Q66 | - |  |  | SI | Bound (more-affected leg) performance (cm) - attem... |
| Q67 | - |  |  | SI | Bound (more-affected leg) performance (cm) - attem... |
| Q68 | - |  |  | SI | Bound (more-affected leg) performance (cm) - Avera... |
| Q69 | - |  |  | SI | Bound (less-affected leg) |
| Q70 | - |  |  | SI | cm - Attempt one |
| Q71 | - |  |  | SI | cm - Attempt two |
| Q72 | - |  |  | SI | cm - Attempt three |
| Q73 | - |  |  | SI | cm - Average of attempts |
| Q74 | - |  |  | SI | Bound (less-affected leg) performance (cm) - attem... |
| Q75 | - |  |  | SI | Bound (less-affected leg) performance (cm) - attem... |
| Q76 | - |  |  | SI | Bound (less-affected leg) performance (cm) - attem... |
| Q77 | - |  |  | SI | Bound (less-affected leg) performance (cm) - Avera... |
| Q78 | - |  |  | SI | Up stairs dependent (rail OR not reciprocal) |
| Q79 | - |  |  | SI | seconds |
| Q80 | - |  |  | SI | Up stairs dependent performance (seconds) |
| Q81 | - |  |  | SI | Up stairs independent (no rail AND reciprocal) |
| Q82 | - |  |  | SI | seconds |
| Q83 | - |  |  | SI | Up stairs independent performance (seconds) |
| Q84 | - |  |  | SI | Down stairs - Dependent (rail OR not reciprocal) |
| Q85 | - |  |  | SI | seconds |
| Q86 | - |  |  | SI | Down stairs dependent performance (seconds) |
| Q87 | - |  |  | SI | Down stairs independent (no rail AND reciprocal) |
| Q88 | - |  |  | SI | seconds |
| Q89 | - |  |  | SI | Down stairs independent performance (seconds) |
| Q90 | - |  |  | SI | Notes |
| Q91 | - |  |  | SI | Subject suitability |
| Q92 | - |  |  | SI | • The HiMAT is appropriate for assessing people wi... |
| Q93 | - |  |  | SI | • The minimal mobility requirement for testing is ... |
| Q94 | - |  |  | SI | • Orthoses are permitted. |
| Q95 | - |  |  | SI | Walking |
| Q96 | - |  |  | SI | • The middle 10m of a 20m trial is timed. |
| Q97 | - |  |  | SI | Walk backward |
| Q98 | - |  |  | SI | • As for walking. |
| Q99 | - |  |  | SI | Walk on toes |
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