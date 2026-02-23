# SQLUser.PA_AdmMother

**Schema:** SQLUser
**Columnas:** 310
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Admisión de Pacientes**. Registra episodios de atención hospitalaria.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| MOTH_RowId1 | double | PK |  | NO | - |
| MOTH_AbdState_DR | bigint |  | FK | SI | Des Ref PACAbdState |
| MOTH_ActualDelivPlace_DR | bigint |  | FK | SI | Des Ref Actual Delivery Place |
| MOTH_BookingChangeManagem_DR | bigint |  | FK | SI | Des Ref Booking Change Management |
| MOTH_BookingChangePlace_DR | bigint |  | FK | SI | Des Ref Booking Change Place |
| MOTH_BreastFeedingActual | varchar |  |  | SI | Breast Feeding Actual |
| MOTH_Breast_DR | bigint |  | FK | SI | Des Ref to Breast |
| MOTH_CervixDilation | double |  |  | SI | Cervix Dilation |
| MOTH_Char_DR | bigint |  | FK | SI | Des Ref to PACChar |
| MOTH_CircumAbdomen | double |  |  | SI | Circumference of Abdomen |
| MOTH_CondEpis | bigint |  |  | SI | Des Ref Condition Episiotomy |
| MOTH_DateOfBooking | date |  |  | SI | Date Of Booking |
| MOTH_DelivPlanManagement_DR | bigint |  | FK | SI | Des Ref Deliv Plan Management |
| MOTH_Diabetes_DR | bigint |  | FK | SI | Des Ref Diabetes |
| MOTH_Effacement | double |  |  | SI | Effacement |
| MOTH_FetHeartLoc | bigint |  |  | SI | Des Ref to PACFetHeartLoc |
| MOTH_FetHeartRate | double |  |  | SI | Fetal Heart Rate |
| MOTH_FetHeartSound | double |  |  | SI | Fetal Heart Sound |
| MOTH_FetusMoving | varchar |  |  | SI | Fetus Moving |
| MOTH_FirstAntenatalAssesDate | date |  |  | SI | First Antenatal Assesment Date |
| MOTH_GMPAntenatalCare_DR | bigint |  | FK | SI | Des Ref GMP responsible for Antenatal Care |
| MOTH_GoLabour | varchar |  |  | SI | Sign Go to Labour |
| MOTH_HeightFundus | double |  |  | SI | Height of Fundus |
| MOTH_IntendedDelivPlace_DR | bigint |  | FK | SI | Des Ref Intended Deliv Place |
| MOTH_LMP | date |  |  | SI | LMP |
| MOTH_MacStain_DR | bigint |  | FK | SI | Des Ref to PACMaconium Stain |
| MOTH_ManagementOfAbortion_DR | bigint |  | FK | SI | Des Ref Management Of Abortion |
| MOTH_MidwifeConsultTransf_DR | bigint |  | FK | SI | Des Ref Midwife to Consultant Transfer |
| MOTH_OriginalBooking_DR | bigint |  | FK | SI | Des Ref Original Booking |
| MOTH_PAADM_DR | bigint |  | FK | SI | Des Ref PAADM |
| MOTH_Perineum_DR | bigint |  | FK | SI | Des Ref Perineum |
| MOTH_Present_DR | bigint |  | FK | SI | Des Ref PACPresent |
| MOTH_PrevAdmToHosp | varchar |  |  | SI | Prev Admissions To Hosp |
| MOTH_PrevCaesareanSections | varchar |  |  | SI | not used |
| MOTH_PrevNeonatalBirths | varchar |  |  | SI | not used |
| MOTH_PrevStillBirths | varchar |  |  | SI | not used |
| MOTH_Puerper_DR | bigint |  | FK | SI | Des Ref PACPuerper |
| MOTH_Remarks | varchar |  |  | SI | Remarks |
| MOTH_RowId | double |  |  | NO | PA_AdmMother Row ID |
| MOTH_SmokerDuringPregn_DR | bigint |  | FK | SI | Des Ref Smoker During Pregnancy |
| MOTH_Station | bigint |  |  | SI | Station |
| MOTH_TypeOfAbortion_DR | bigint |  | FK | SI | Des Ref Type Of Abortion |
| MOTH_Uterus_DR | bigint |  | FK | SI | Des Ref Uterus |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Symptom onset <4.5 hours |
| Q04 | - |  |  | SI | Age ≥ 18 years` |
| Q05 | - |  |  | SI | Clinical diagnosis of ischaemic stroke causing neu... |
| Q06 | - |  |  | SI | Mandatory inclusion criteria dummy 1 |
| Q07 | - |  |  | SI | Mandatory inclusion criteria dummy 2 |
| Q08 | - |  |  | SI | Mandatory inclusion criteria dummy 3 |
| Q09 | - |  |  | SI | Ineligible items total |
| Q10 | - |  |  | SI | If answered NO for any of the above questions pati... |
| Q100 | - |  |  | SI | Total score |
| Q101 | - |  |  | SI | Inclusion criteria total |
| Q102 | - |  |  | SI | Contraindication total |
| Q103 | - |  |  | SI | Relative contraindication total |
| Q104 | - |  |  | SI | Additional warning total |
| Q105 | - |  |  | SI | Score |
| Q106 | - |  |  | SI | Classification |
| Q107 | - |  |  | SI | Total score |
| Q108 | - |  |  | SI | Inclusion criteria total |
| Q109 | - |  |  | SI | Contraindication total |
| Q11 | - |  |  | SI | Patient History |
| Q110 | - |  |  | SI | Relative contraindication total |
| Q111 | - |  |  | SI | Additional warning total |
| Q112 | - |  |  | SI | 0 |
| Q113 | - |  |  | SI | 0 |
| Q114 | - |  |  | SI | 0 |
| Q115 | - |  |  | SI | 0 |
| Q116 | - |  |  | SI | 0 |
| Q117 | - |  |  | SI | > 0 |
| Q118 | - |  |  | SI | > 0 |
| Q119 | - |  |  | SI | > 0 |
| Q12 | - |  |  | SI | Significant head trauma or prior stroke in the pre... |
| Q120 | - |  |  | SI | > 0 |
| Q121 | - |  |  | SI | > 0 |
| Q122 | - |  |  | SI | Patient eligible for thrombolysis / tPA |
| Q123 | - |  |  | SI | Patient may not be eligible for thrombolysis / tPA |
| Q124 | - |  |  | SI | Patient meets eligibility criteria |
| Q125 | - |  |  | SI | Patient does not meet eligibility criteria. Discus... |
| Q126 | - |  |  | SI | Patient has no absolute contraindications |
| Q127 | - |  |  | SI | Absolute contraindications present. Discuss with n... |
| Q128 | - |  |  | SI | Patient has no relative contraindications |
| Q129 | - |  |  | SI | Relative contraindications present. Discuss risk /... |
| Q13 | - |  |  | SI | Intracranial or intraspinal surgery within the pri... |
| Q130 | - |  |  | SI | Patient has no additional warnings |
| Q131 | - |  |  | SI | Additional warnings present. Discuss risk / benefi... |
| Q132 | - |  |  | SI | 0: Patient eligible for thrombolysis / tPA |
| Q133 | - |  |  | SI | > 0: Patient may not be eligible for thrombolysis ... |
| Q134 | - |  |  | SI | 0: Patient meets eligibility criteria |
| Q135 | - |  |  | SI | > 0: Patient does not meet eligibility criteria. D... |
| Q136 | - |  |  | SI | 0: Patient has no absolute contraindications |
| Q137 | - |  |  | SI | > 0: Absolute contraindications present. Discuss w... |
| Q138 | - |  |  | SI | 0: Patient has no relative contraindications |
| Q139 | - |  |  | SI | > 0: Relative contraindications present. Discuss r... |
| Q14 | - |  |  | SI | History of intracranial haemorrhage |
| Q140 | - |  |  | SI | 0: Patient has no additional warnings |
| Q141 | - |  |  | SI | > 0: Additional warnings present. Discuss risk / b... |
| Q142 | - |  |  | SI | Total score |
| Q143 | - |  |  | SI | Inclusion criteria total |
| Q144 | - |  |  | SI | Contraindication total |
| Q145 | - |  |  | SI | Relative contraindication total |
| Q146 | - |  |  | SI | Additional warning total |
| Q147 | - |  |  | SI | Provides inclusion / exclusion criteria to aid dec... |
| Q148 | - |  |  | SI | Symptom onset <4.5 hours |
| Q149 | - |  |  | SI | Age ≥ 18 years |
| Q15 | - |  |  | SI | Known intracranial arteriovenous malformation, neo... |
| Q150 | - |  |  | SI | Clinical diagnosis of ischaemic stroke causing neu... |
| Q151 | - |  |  | SI | Mandatory inclusion criteria dummy 1 |
| Q152 | - |  |  | SI | Mandatory inclusion criteria dummy 2 |
| Q153 | - |  |  | SI | Mandatory inclusion criteria dummy 3 |
| Q154 | - |  |  | SI | Have all indication criteria been met? |
| Q155 | - |  |  | SI | Based on previous answers, this section is not req... |
| Q156 | - |  |  | SI | Significant head trauma or prior stroke in the pre... |
| Q157 | - |  |  | SI | Intracranial or intraspinal surgery within the pri... |
| Q158 | - |  |  | SI | History of intracranial haemorrhage |
| Q159 | - |  |  | SI | Known intracranial arteriovenous malformation, neo... |
| Q16 | - |  |  | SI | Absolute contraindication dummy 1 |
| Q160 | - |  |  | SI | Absolute contraindication dummy 1 |
| Q161 | - |  |  | SI | Absolute contraindication dummy 2 |
| Q162 | - |  |  | SI | Clinical presentation suggests subarachnoid haemor... |
| Q163 | - |  |  | SI | Blood pressure persistently > 185 mmHg systolic or... |
| Q164 | - |  |  | SI | Active internal bleeding |
| Q165 | - |  |  | SI | Suspected / Confirmed endocarditis |
| Q166 | - |  |  | SI | Coma or severe obtundation with fixed eye deviatio... |
| Q167 | - |  |  | SI | Absolute contraindication dummy 3 |
| Q168 | - |  |  | SI | Absolute contraindication dummy 4 |
| Q169 | - |  |  | SI | Absolute contraindication dummy 5 |
| Q17 | - |  |  | SI | Absolute contraindication dummy 2 |
| Q170 | - |  |  | SI | Intracranial haemorrhage on computed tomography (C... |
| Q171 | - |  |  | SI | Extensive regions of obvious hypodensity consisten... |
| Q172 | - |  |  | SI | Blood glucose < 2.8 mmol/L |
| Q173 | - |  |  | SI | Known bleeding diathesis |
| Q174 | - |  |  | SI | Platelet count < 100,000/mm3 |
| Q175 | - |  |  | SI | Patient has received heparin within 48 hours and h... |
| Q176 | - |  |  | SI | Current use of oral anticoagulants and INR > 1.7 |
| Q177 | - |  |  | SI | Current use (last dose within last 48 hours) of di... |
| Q178 | - |  |  | SI | Summary |
| Q179 | - |  |  | SI | Have all absolute contraindications been ruled out... |
| Q18 | - |  |  | SI | Clinical |
| Q180 | - |  |  | SI | Relative Contraindications and Warnings |
| Q181 | - |  |  | SI | Based on previous answers, this section is not req... |
| Q182 | - |  |  | SI | Based on previous answers, this section is not req... |
| Q183 | - |  |  | SI | Relative contraindication dummy 1 |
| Q184 | - |  |  | SI | Significant head trauma or prior stroke in the pre... |
| Q185 | - |  |  | SI | Intracranial or intraspinal surgery within the pri... |
| Q186 | - |  |  | SI | Other major surgery or serious non-head trauma in ... |
| Q187 | - |  |  | SI | History of intracranial haemorrhage (relative cont... |
| Q188 | - |  |  | SI | Known intracranial arteriovenous malformation, neo... |
| Q189 | - |  |  | SI | History of gastrointestinal or urinary tract haemo... |
| Q19 | - |  |  | SI | Clinical presentation suggests subarachnoid haemor... |
| Q190 | - |  |  | SI | Arterial puncture at a non-compressible site withi... |
| Q191 | - |  |  | SI | Lumbar puncture within seven days |
| Q192 | - |  |  | SI | Known / Suspected myocardial infarction within 90 ... |
| Q193 | - |  |  | SI | Post myocardial infarction pericarditis |
| Q194 | - |  |  | SI | Biopsy or surgery involving a parenchymal organ wi... |
| Q195 | - |  |  | SI | Trauma with internal injuries or ulcerative wounds... |
| Q196 | - |  |  | SI | Only minor or rapidly improving stroke symptoms |
| Q197 | - |  |  | SI | Seizure at stroke onset |
| Q198 | - |  |  | SI | Pregnancy |
| Q199 | - |  |  | SI | Severe neurological impairment with NIH Stroke Sca... |
| Q20 | - |  |  | SI | Blood pressure persistently > 185 mmHg systolic or... |
| Q200 | - |  |  | SI | Concomitant serious, advanced or terminal illness |
| Q201 | - |  |  | SI | Relative contraindication dummy 1 |
| Q202 | - |  |  | SI | Relative contraindication dummy 2 |
| Q203 | - |  |  | SI | Relative contraindication dummy 4 |
| Q204 | - |  |  | SI | Relative contraindication dummy 3 |
| Q205 | - |  |  | SI | Blood glucose > 22.0mmol/L |
| Q206 | - |  |  | SI | Relative contraindication dummy 6 |
| Q207 | - |  |  | SI | Relative contraindication dummy 5 |
| Q208 | - |  |  | SI | Age >80 years |
| Q209 | - |  |  | SI | History of prior stroke and diabetes |
| Q21 | - |  |  | SI | Active internal bleeding |
| Q210 | - |  |  | SI | Oral anticoagulant use regardless of INR |
| Q211 | - |  |  | SI | National Institutes of Health Stroke Scale (NIHSS)... |
| Q212 | - |  |  | SI | CT shows multi - lobar infarction (hypodensity >1/... |
| Q213 | - |  |  | SI | Additional warning dummy 1 |
| Q214 | - |  |  | SI | Additional warning dummy 2 |
| Q215 | - |  |  | SI | Summary |
| Q216 | - |  |  | SI | Have all relative contraindications +/- additional... |
| Q217 | - |  |  | SI | Patient may not be eligible for thrombolysis / tPA... |
| Q218 | - |  |  | SI | Discuss with neurology / senior consultant. |
| Q219 | - |  |  | SI | Absolute contraindication dummy 6 |
| Q22 | - |  |  | SI | Suspected / Confirmed endocarditis |
| Q220 | - |  |  | SI | Patient may not be eligible for thrombolysis / tPA... |
| Q221 | - |  |  | SI | Summary |
| Q222 | - |  |  | SI | Score |
| Q223 | - |  |  | SI | 0: Patient eligible for thrombolysis / tPA |
| Q224 | - |  |  | SI | >0: Patient may not be eligible for thrombolysis /... |
| Q225 | - |  |  | SI | Symptom onset < 4.5 hours |
| Q226 | - |  |  | SI | Was the symptom onset within 3 - 4.5 hours? |
| Q227 | - |  |  | SI | Have all relative contraindications +/- additional... |
| Q23 | - |  |  | SI | Coma or severe obtundation with fixed eye deviatio... |
| Q24 | - |  |  | SI | Absolute contraindication dummy 3 |
| Q25 | - |  |  | SI | Absolute contraindication dummy 4 |
| Q26 | - |  |  | SI | Absolute contraindication dummy 5 |
| Q27 | - |  |  | SI | Medical Imaging |
| Q28 | - |  |  | SI | Intracranial haemorrhage on computed tomography (C... |
| Q29 | - |  |  | SI | Extensive regions of obvious hypodensity consisten... |
| Q30 | - |  |  | SI | Haematological |
| Q31 | - |  |  | SI | Blood glucose <2.8 mmol/L |
| Q32 | - |  |  | SI | Known bleeding diathesis |
| Q33 | - |  |  | SI | Bleeding diathesis (systemic coagulopathy) element... |
| Q34 | - |  |  | SI | Platelet count <100,000/mm3 |
| Q35 | - |  |  | SI | Patient has received heparin within 48 hours and h... |
| Q36 | - |  |  | SI | Current use of oral anticoagulants and INR >1.7 |
| Q37 | - |  |  | SI | Current use (last dose within last 48 hours) of di... |
| Q38 | - |  |  | SI | Absolute contraindication dummy 6 |
| Q39 | - |  |  | SI | Absolute contraindications total present |
| Q40 | - |  |  | SI | If YES to any of the above patient does NOT meet c... |
| Q41 | - |  |  | SI | Patient History |
| Q42 | - |  |  | SI | Relative contraindication dummy 1 |
| Q43 | - |  |  | SI | Significant head trauma or prior stroke in the pre... |
| Q44 | - |  |  | SI | Intracranial or intraspinal surgery within the pri... |
| Q45 | - |  |  | SI | Other major surgery or serious non-head trauma in ... |
| Q46 | - |  |  | SI | History of intracranial haemorrhage (relative cont... |
| Q47 | - |  |  | SI | Known intracranial arteriovenous malformation, neo... |
| Q48 | - |  |  | SI | History of gastrointestinal or urinary tract haemo... |
| Q49 | - |  |  | SI | Arterial puncture at a non-compressible site withi... |
| Q50 | - |  |  | SI | Lumbar puncture within seven days |
| Q51 | - |  |  | SI | Known / Suspected myocardial infarction within 90 ... |
| Q52 | - |  |  | SI | Post myocardial infarction pericarditis |
| Q53 | - |  |  | SI | Biopsy or surgery involving a parenchymal organ wi... |
| Q54 | - |  |  | SI | Trauma with internal injuries or ulcerative wounds... |
| Q55 | - |  |  | SI | Clinical |
| Q56 | - |  |  | SI | Only minor or rapidly improving stroke symptoms |
| Q57 | - |  |  | SI | Seizure at stroke onset |
| Q58 | - |  |  | SI | Pregnancy |
| Q59 | - |  |  | SI | Severe neurological impairment with NIH Stroke Sca... |
| Q60 | - |  |  | SI | Concomitant serious, advanced or terminal illness |
| Q61 | - |  |  | SI | Relative contraindication dummy 1 |
| Q62 | - |  |  | SI | Relative contraindication dummy 2 |
| Q63 | - |  |  | SI | Medical Imaging |
| Q64 | - |  |  | SI | Relative contraindication dummy 4 |
| Q65 | - |  |  | SI | Relative contraindication dummy 3 |
| Q66 | - |  |  | SI | Haematologic |
| Q67 | - |  |  | SI | Blood glucose > 22.0mmol/L |
| Q68 | - |  |  | SI | Relative contraindication dummy 4 |
| Q69 | - |  |  | SI | Relative contraindication dummy 5 |
| Q70 | - |  |  | SI | Relative contraindications total present |
| Q71 | - |  |  | SI | If YES to any of the above consider and discuss ri... |
| Q72 | - |  |  | SI | Additional Warnings Where Onset >3 Hours |
| Q73 | - |  |  | SI | Age >80 years |
| Q74 | - |  |  | SI | History of prior stroke and diabetes |
| Q75 | - |  |  | SI | Oral anticoagulant use regardless of INR |
| Q76 | - |  |  | SI | National Institutes of Health Stroke Scale (NIHSS)... |
| Q77 | - |  |  | SI | CT shows multi - lobar infarction (hypodensity >1/... |
| Q78 | - |  |  | SI | Additional warning dummy 1 |
| Q79 | - |  |  | SI | Additional warning dummy 2 |
| Q80 | - |  |  | SI | Additional warning total present |
| Q81 | - |  |  | SI | If YES to any of the above consider and discuss ri... |
| Q82 | - |  |  | SI | Dummy 1 |
| Q83 | - |  |  | SI | Dummy 2 |
| Q84 | - |  |  | SI | Dummy 3 |
| Q85 | - |  |  | SI | • Highlight areas of concern to neurology / senior... |
| Q86 | - |  |  | SI | • Determine the onset of stroke symptoms (or time ... |
| Q87 | - |  |  | SI | • Obtain a stat head CT to evaluate for haemorrhag... |
| Q88 | - |  |  | SI | • In appropriate circumstances and in consultation... |
| Q89 | - |  |  | SI | • The NIHSS should be performed as part of their e... |
| Q90 | - |  |  | SI | • While a high NIHSS score (>22) is not an absolut... |
| Q91 | - |  |  | SI | be aware that the rate of symptomatic or fatal int... |
| Q92 | - |  |  | SI | • If the patient has an elevated blood pressure as... |
| Q93 | - |  |  | SI | • If the blood pressure can be adequately controll... |
| Q94 | - |  |  | SI | • When considering giving tPA in the extended wind... |
| Q95 | - |  |  | SI | • Thrombolysis may be considered for patients who ... |
| Q96 | - |  |  | SI | • If symptoms have completely resolved, continue o... |
| Q97 | - |  |  | SI | Dummy 4 |
| Q98 | - |  |  | SI | Dummy 5 |
| Q99 | - |  |  | SI | Dummy 6 |
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