# questionnaire.QTCTCIS

> Thrombolytic Checklist for Ischaemic Stroke

**Schema:** questionnaire
**Columnas:** 268
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Thrombolytic Checklist for Ischaemic Stroke

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | Symptom onset <4.5 hours |
| Q04 | varchar |  |  | SI | Age ≥ 18 years` |
| Q05 | varchar |  |  | SI | Clinical diagnosis of ischaemic stroke causing neu... |
| Q06 | varchar |  |  | SI | Mandatory inclusion criteria dummy 1 |
| Q07 | varchar |  |  | SI | Mandatory inclusion criteria dummy 2 |
| Q08 | varchar |  |  | SI | Mandatory inclusion criteria dummy 3 |
| Q09 | varchar |  |  | SI | Ineligible items total |
| Q10 | varchar |  |  | SI | If answered NO for any of the above questions pati... |
| Q100 | varchar |  |  | SI | Total score |
| Q101 | varchar |  |  | SI | Inclusion criteria total |
| Q102 | varchar |  |  | SI | Contraindication total |
| Q103 | varchar |  |  | SI | Relative contraindication total |
| Q104 | varchar |  |  | SI | Additional warning total |
| Q105 | varchar |  |  | SI | Score |
| Q106 | varchar |  |  | SI | Classification |
| Q107 | varchar |  |  | SI | Total score |
| Q108 | varchar |  |  | SI | Inclusion criteria total |
| Q109 | varchar |  |  | SI | Contraindication total |
| Q11 | varchar |  |  | SI | Patient History |
| Q110 | varchar |  |  | SI | Relative contraindication total |
| Q111 | varchar |  |  | SI | Additional warning total |
| Q112 | varchar |  |  | SI | 0 |
| Q113 | varchar |  |  | SI | 0 |
| Q114 | varchar |  |  | SI | 0 |
| Q115 | varchar |  |  | SI | 0 |
| Q116 | varchar |  |  | SI | 0 |
| Q117 | varchar |  |  | SI | > 0 |
| Q118 | varchar |  |  | SI | > 0 |
| Q119 | varchar |  |  | SI | > 0 |
| Q12 | varchar |  |  | SI | Significant head trauma or prior stroke in the pre... |
| Q120 | varchar |  |  | SI | > 0 |
| Q121 | varchar |  |  | SI | > 0 |
| Q122 | varchar |  |  | SI | Patient eligible for thrombolysis / tPA |
| Q123 | varchar |  |  | SI | Patient may not be eligible for thrombolysis / tPA |
| Q124 | varchar |  |  | SI | Patient meets eligibility criteria |
| Q125 | varchar |  |  | SI | Patient does not meet eligibility criteria. Discus... |
| Q126 | varchar |  |  | SI | Patient has no absolute contraindications |
| Q127 | varchar |  |  | SI | Absolute contraindications present. Discuss with n... |
| Q128 | varchar |  |  | SI | Patient has no relative contraindications |
| Q129 | varchar |  |  | SI | Relative contraindications present. Discuss risk /... |
| Q13 | varchar |  |  | SI | Intracranial or intraspinal surgery within the pri... |
| Q130 | varchar |  |  | SI | Patient has no additional warnings |
| Q131 | varchar |  |  | SI | Additional warnings present. Discuss risk / benefi... |
| Q132 | varchar |  |  | SI | 0: Patient eligible for thrombolysis / tPA |
| Q133 | varchar |  |  | SI | > 0: Patient may not be eligible for thrombolysis ... |
| Q134 | varchar |  |  | SI | 0: Patient meets eligibility criteria |
| Q135 | varchar |  |  | SI | > 0: Patient does not meet eligibility criteria. D... |
| Q136 | varchar |  |  | SI | 0: Patient has no absolute contraindications |
| Q137 | varchar |  |  | SI | > 0: Absolute contraindications present. Discuss w... |
| Q138 | varchar |  |  | SI | 0: Patient has no relative contraindications |
| Q139 | varchar |  |  | SI | > 0: Relative contraindications present. Discuss r... |
| Q14 | varchar |  |  | SI | History of intracranial haemorrhage |
| Q140 | varchar |  |  | SI | 0: Patient has no additional warnings |
| Q141 | varchar |  |  | SI | > 0: Additional warnings present. Discuss risk / b... |
| Q142 | varchar |  |  | SI | Total score |
| Q143 | varchar |  |  | SI | Inclusion criteria total |
| Q144 | varchar |  |  | SI | Contraindication total |
| Q145 | varchar |  |  | SI | Relative contraindication total |
| Q146 | varchar |  |  | SI | Additional warning total |
| Q147 | varchar |  |  | SI | Provides inclusion / exclusion criteria to aid dec... |
| Q148 | varchar |  |  | SI | Symptom onset <4.5 hours |
| Q149 | varchar |  |  | SI | Age ≥ 18 years |
| Q15 | varchar |  |  | SI | Known intracranial arteriovenous malformation, neo... |
| Q150 | varchar |  |  | SI | Clinical diagnosis of ischaemic stroke causing neu... |
| Q151 | varchar |  |  | SI | Mandatory inclusion criteria dummy 1 |
| Q152 | varchar |  |  | SI | Mandatory inclusion criteria dummy 2 |
| Q153 | varchar |  |  | SI | Mandatory inclusion criteria dummy 3 |
| Q154 | varchar |  |  | SI | Have all indication criteria been met? |
| Q155 | varchar |  |  | SI | Based on previous answers, this section is not req... |
| Q156 | varchar |  |  | SI | Significant head trauma or prior stroke in the pre... |
| Q157 | varchar |  |  | SI | Intracranial or intraspinal surgery within the pri... |
| Q158 | varchar |  |  | SI | History of intracranial haemorrhage |
| Q159 | varchar |  |  | SI | Known intracranial arteriovenous malformation, neo... |
| Q16 | varchar |  |  | SI | Absolute contraindication dummy 1 |
| Q160 | varchar |  |  | SI | Absolute contraindication dummy 1 |
| Q161 | varchar |  |  | SI | Absolute contraindication dummy 2 |
| Q162 | varchar |  |  | SI | Clinical presentation suggests subarachnoid haemor... |
| Q163 | varchar |  |  | SI | Blood pressure persistently > 185 mmHg systolic or... |
| Q164 | varchar |  |  | SI | Active internal bleeding |
| Q165 | varchar |  |  | SI | Suspected / Confirmed endocarditis |
| Q166 | varchar |  |  | SI | Coma or severe obtundation with fixed eye deviatio... |
| Q167 | varchar |  |  | SI | Absolute contraindication dummy 3 |
| Q168 | varchar |  |  | SI | Absolute contraindication dummy 4 |
| Q169 | varchar |  |  | SI | Absolute contraindication dummy 5 |
| Q17 | varchar |  |  | SI | Absolute contraindication dummy 2 |
| Q170 | varchar |  |  | SI | Intracranial haemorrhage on computed tomography (C... |
| Q171 | varchar |  |  | SI | Extensive regions of obvious hypodensity consisten... |
| Q172 | varchar |  |  | SI | Blood glucose < 2.8 mmol/L |
| Q173 | varchar |  |  | SI | Known bleeding diathesis |
| Q174 | varchar |  |  | SI | Platelet count < 100,000/mm3 |
| Q175 | varchar |  |  | SI | Patient has received heparin within 48 hours and h... |
| Q176 | varchar |  |  | SI | Current use of oral anticoagulants and INR > 1.7 |
| Q177 | varchar |  |  | SI | Current use (last dose within last 48 hours) of di... |
| Q178 | varchar |  |  | SI | Summary |
| Q179 | varchar |  |  | SI | Have all absolute contraindications been ruled out... |
| Q18 | varchar |  |  | SI | Clinical |
| Q180 | varchar |  |  | SI | Relative Contraindications and Warnings |
| Q181 | varchar |  |  | SI | Based on previous answers, this section is not req... |
| Q182 | varchar |  |  | SI | Based on previous answers, this section is not req... |
| Q183 | varchar |  |  | SI | Relative contraindication dummy 1 |
| Q184 | varchar |  |  | SI | Significant head trauma or prior stroke in the pre... |
| Q185 | varchar |  |  | SI | Intracranial or intraspinal surgery within the pri... |
| Q186 | varchar |  |  | SI | Other major surgery or serious non-head trauma in ... |
| Q187 | varchar |  |  | SI | History of intracranial haemorrhage (relative cont... |
| Q188 | varchar |  |  | SI | Known intracranial arteriovenous malformation, neo... |
| Q189 | varchar |  |  | SI | History of gastrointestinal or urinary tract haemo... |
| Q19 | varchar |  |  | SI | Clinical presentation suggests subarachnoid haemor... |
| Q190 | varchar |  |  | SI | Arterial puncture at a non-compressible site withi... |
| Q191 | varchar |  |  | SI | Lumbar puncture within seven days |
| Q192 | varchar |  |  | SI | Known / Suspected myocardial infarction within 90 ... |
| Q193 | varchar |  |  | SI | Post myocardial infarction pericarditis |
| Q194 | varchar |  |  | SI | Biopsy or surgery involving a parenchymal organ wi... |
| Q195 | varchar |  |  | SI | Trauma with internal injuries or ulcerative wounds... |
| Q196 | varchar |  |  | SI | Only minor or rapidly improving stroke symptoms |
| Q197 | varchar |  |  | SI | Seizure at stroke onset |
| Q198 | varchar |  |  | SI | Pregnancy |
| Q199 | varchar |  |  | SI | Severe neurological impairment with NIH Stroke Sca... |
| Q20 | varchar |  |  | SI | Blood pressure persistently > 185 mmHg systolic or... |
| Q200 | varchar |  |  | SI | Concomitant serious, advanced or terminal illness |
| Q201 | varchar |  |  | SI | Relative contraindication dummy 1 |
| Q202 | varchar |  |  | SI | Relative contraindication dummy 2 |
| Q203 | varchar |  |  | SI | Relative contraindication dummy 4 |
| Q204 | varchar |  |  | SI | Relative contraindication dummy 3 |
| Q205 | varchar |  |  | SI | Blood glucose > 22.0mmol/L |
| Q206 | varchar |  |  | SI | Relative contraindication dummy 6 |
| Q207 | varchar |  |  | SI | Relative contraindication dummy 5 |
| Q208 | varchar |  |  | SI | Age >80 years |
| Q209 | varchar |  |  | SI | History of prior stroke and diabetes |
| Q21 | varchar |  |  | SI | Active internal bleeding |
| Q210 | varchar |  |  | SI | Oral anticoagulant use regardless of INR |
| Q211 | varchar |  |  | SI | National Institutes of Health Stroke Scale (NIHSS)... |
| Q212 | varchar |  |  | SI | CT shows multi - lobar infarction (hypodensity >1/... |
| Q213 | varchar |  |  | SI | Additional warning dummy 1 |
| Q214 | varchar |  |  | SI | Additional warning dummy 2 |
| Q215 | varchar |  |  | SI | Summary |
| Q216 | varchar |  |  | SI | Have all relative contraindications +/- additional... |
| Q217 | varchar |  |  | SI | Patient may not be eligible for thrombolysis / tPA... |
| Q218 | varchar |  |  | SI | Discuss with neurology / senior consultant. |
| Q219 | varchar |  |  | SI | Absolute contraindication dummy 6 |
| Q22 | varchar |  |  | SI | Suspected / Confirmed endocarditis |
| Q220 | varchar |  |  | SI | Patient may not be eligible for thrombolysis / tPA... |
| Q221 | varchar |  |  | SI | Summary |
| Q222 | varchar |  |  | SI | Score |
| Q223 | varchar |  |  | SI | 0: Patient eligible for thrombolysis / tPA |
| Q224 | varchar |  |  | SI | >0: Patient may not be eligible for thrombolysis /... |
| Q225 | varchar |  |  | SI | Symptom onset < 4.5 hours |
| Q226 | varchar |  |  | SI | Was the symptom onset within 3 - 4.5 hours? |
| Q227 | varchar |  |  | SI | Have all relative contraindications +/- additional... |
| Q23 | varchar |  |  | SI | Coma or severe obtundation with fixed eye deviatio... |
| Q24 | varchar |  |  | SI | Absolute contraindication dummy 3 |
| Q25 | varchar |  |  | SI | Absolute contraindication dummy 4 |
| Q26 | varchar |  |  | SI | Absolute contraindication dummy 5 |
| Q27 | varchar |  |  | SI | Medical Imaging |
| Q28 | varchar |  |  | SI | Intracranial haemorrhage on computed tomography (C... |
| Q29 | varchar |  |  | SI | Extensive regions of obvious hypodensity consisten... |
| Q30 | varchar |  |  | SI | Haematological |
| Q31 | varchar |  |  | SI | Blood glucose <2.8 mmol/L |
| Q32 | varchar |  |  | SI | Known bleeding diathesis |
| Q33 | varchar |  |  | SI | Bleeding diathesis (systemic coagulopathy) element... |
| Q34 | varchar |  |  | SI | Platelet count <100,000/mm3 |
| Q35 | varchar |  |  | SI | Patient has received heparin within 48 hours and h... |
| Q36 | varchar |  |  | SI | Current use of oral anticoagulants and INR >1.7 |
| Q37 | varchar |  |  | SI | Current use (last dose within last 48 hours) of di... |
| Q38 | varchar |  |  | SI | Absolute contraindication dummy 6 |
| Q39 | varchar |  |  | SI | Absolute contraindications total present |
| Q40 | varchar |  |  | SI | If YES to any of the above patient does NOT meet c... |
| Q41 | varchar |  |  | SI | Patient History |
| Q42 | varchar |  |  | SI | Relative contraindication dummy 1 |
| Q43 | varchar |  |  | SI | Significant head trauma or prior stroke in the pre... |
| Q44 | varchar |  |  | SI | Intracranial or intraspinal surgery within the pri... |
| Q45 | varchar |  |  | SI | Other major surgery or serious non-head trauma in ... |
| Q46 | varchar |  |  | SI | History of intracranial haemorrhage (relative cont... |
| Q47 | varchar |  |  | SI | Known intracranial arteriovenous malformation, neo... |
| Q48 | varchar |  |  | SI | History of gastrointestinal or urinary tract haemo... |
| Q49 | varchar |  |  | SI | Arterial puncture at a non-compressible site withi... |
| Q50 | varchar |  |  | SI | Lumbar puncture within seven days |
| Q51 | varchar |  |  | SI | Known / Suspected myocardial infarction within 90 ... |
| Q52 | varchar |  |  | SI | Post myocardial infarction pericarditis |
| Q53 | varchar |  |  | SI | Biopsy or surgery involving a parenchymal organ wi... |
| Q54 | varchar |  |  | SI | Trauma with internal injuries or ulcerative wounds... |
| Q55 | varchar |  |  | SI | Clinical |
| Q56 | varchar |  |  | SI | Only minor or rapidly improving stroke symptoms |
| Q57 | varchar |  |  | SI | Seizure at stroke onset |
| Q58 | varchar |  |  | SI | Pregnancy |
| Q59 | varchar |  |  | SI | Severe neurological impairment with NIH Stroke Sca... |
| Q60 | varchar |  |  | SI | Concomitant serious, advanced or terminal illness |
| Q61 | varchar |  |  | SI | Relative contraindication dummy 1 |
| Q62 | varchar |  |  | SI | Relative contraindication dummy 2 |
| Q63 | varchar |  |  | SI | Medical Imaging |
| Q64 | varchar |  |  | SI | Relative contraindication dummy 4 |
| Q65 | varchar |  |  | SI | Relative contraindication dummy 3 |
| Q66 | varchar |  |  | SI | Haematologic |
| Q67 | varchar |  |  | SI | Blood glucose > 22.0mmol/L |
| Q68 | varchar |  |  | SI | Relative contraindication dummy 4 |
| Q69 | varchar |  |  | SI | Relative contraindication dummy 5 |
| Q70 | varchar |  |  | SI | Relative contraindications total present |
| Q71 | varchar |  |  | SI | If YES to any of the above consider and discuss ri... |
| Q72 | varchar |  |  | SI | Additional Warnings Where Onset >3 Hours |
| Q73 | varchar |  |  | SI | Age >80 years |
| Q74 | varchar |  |  | SI | History of prior stroke and diabetes |
| Q75 | varchar |  |  | SI | Oral anticoagulant use regardless of INR |
| Q76 | varchar |  |  | SI | National Institutes of Health Stroke Scale (NIHSS)... |
| Q77 | varchar |  |  | SI | CT shows multi - lobar infarction (hypodensity >1/... |
| Q78 | varchar |  |  | SI | Additional warning dummy 1 |
| Q79 | varchar |  |  | SI | Additional warning dummy 2 |
| Q80 | varchar |  |  | SI | Additional warning total present |
| Q81 | varchar |  |  | SI | If YES to any of the above consider and discuss ri... |
| Q82 | varchar |  |  | SI | Dummy 1 |
| Q83 | varchar |  |  | SI | Dummy 2 |
| Q84 | varchar |  |  | SI | Dummy 3 |
| Q85 | varchar |  |  | SI | • Highlight areas of concern to neurology / senior... |
| Q86 | varchar |  |  | SI | • Determine the onset of stroke symptoms (or time ... |
| Q87 | varchar |  |  | SI | • Obtain a stat head CT to evaluate for haemorrhag... |
| Q88 | varchar |  |  | SI | • In appropriate circumstances and in consultation... |
| Q89 | varchar |  |  | SI | • The NIHSS should be performed as part of their e... |
| Q90 | varchar |  |  | SI | • While a high NIHSS score (>22) is not an absolut... |
| Q91 | varchar |  |  | SI | be aware that the rate of symptomatic or fatal int... |
| Q92 | varchar |  |  | SI | • If the patient has an elevated blood pressure as... |
| Q93 | varchar |  |  | SI | • If the blood pressure can be adequately controll... |
| Q94 | varchar |  |  | SI | • When considering giving tPA in the extended wind... |
| Q95 | varchar |  |  | SI | • Thrombolysis may be considered for patients who ... |
| Q96 | varchar |  |  | SI | • If symptoms have completely resolved, continue o... |
| Q97 | varchar |  |  | SI | Dummy 4 |
| Q98 | varchar |  |  | SI | Dummy 5 |
| Q99 | varchar |  |  | SI | Dummy 6 |
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