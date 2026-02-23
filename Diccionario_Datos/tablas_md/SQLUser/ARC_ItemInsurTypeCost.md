# SQLUser.ARC_ItemInsurTypeCost

**Schema:** SQLUser
**Columnas:** 230
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Arquetipo de configuración**. Definición base del sistema. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| COST_ParRef | varchar | PK |  | NO | ARC_ItmMast Parent Reference |
| COST_Amt | double |  |  | NO | Cost |
| COST_Childsub | double |  |  | NO | Childsub |
| COST_CreatedDate | date |  |  | SI | Created Date |
| COST_CreatedTime | time |  |  | SI | Created Time |
| COST_CreatedUser_DR | bigint |  | FK | SI | Created User |
| COST_EffDateFrom | date |  |  | SI | Eff Date From |
| COST_EffDateTo | date |  |  | SI | Eff Date To |
| COST_InsCover_DR | bigint |  | FK | SI | Des Ref to InsCover |
| COST_InsType_DR | bigint |  | FK | NO | Des Ref to InsType |
| COST_RowId | varchar |  |  | NO | - |
| COST_UpdatedDate | date |  |  | SI | Updated Date |
| COST_UpdatedTime | time |  |  | SI | Updated Time |
| COST_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Version |
| Q02 | - |  |  | SI | Date of Injury |
| Q03 | - |  |  | SI | Time of Injury |
| Q04 | - |  |  | SI | Reporter |
| Q05 | - |  |  | SI | Injury description |
| Q06 | - |  |  | SI | Evidence of forcible blow to the head (direct or i... |
| Q07 | - |  |  | SI | Evidence of intracranial injury or skull fracture? |
| Q08 | - |  |  | SI | Location of impact |
| Q09 | - |  |  | SI | Cause |
| Q10 | - |  |  | SI | If Sport (specify) |
| Q100 | - |  |  | SI | 6. Early signs. If present, ask the individuals wh... |
| Q101 | - |  |  | SI | injury. |
| Q102 | - |  |  | SI | 7. Inquire whether seizures were observed or not. |
| Q103 | - |  |  | SI | B. Symptom Checklist: |
| Q104 | - |  |  | SI | 1. Ask patient (and/or parent, if child) to report... |
| Q105 | - |  |  | SI | One or all symptoms may be present depending upon ... |
| Q106 | - |  |  | SI | 2. For all symptoms, indicate presence of symptoms... |
| Q107 | - |  |  | SI | change from their usual presentation. |
| Q108 | - |  |  | SI | 3. Scoring: Sum total number of symptoms present p... |
| Q109 | - |  |  | SI | Drowsiness may be present on the day of injury.) I... |
| Q11 | - |  |  | SI | Other cause |
| Q110 | - |  |  | SI | 4. Exertion: Inquire whether any symptoms worsen w... |
| Q111 | - |  |  | SI | concentration) exertion. Clinicians should be awar... |
| Q112 | - |  |  | SI | 5. Overall Rating: Determine how different the per... |
| Q113 | - |  |  | SI | C. Risk Factors for Protracted Recovery: Assess th... |
| Q114 | - |  |  | SI | 1. Concussion history: Assess the number and date(... |
| Q115 | - |  |  | SI | and symptom effects of concussion may be cumulativ... |
| Q116 | - |  |  | SI | from initial trauma). |
| Q117 | - |  |  | SI | 2. Headache history: Assess personal and/or family... |
| Q118 | - |  |  | SI | 3. Developmental history: Assess history of learni... |
| Q119 | - |  |  | SI | recovery with these conditions. |
| Q12 | - |  |  | SI | Amnesia |
| Q120 | - |  |  | SI | 4. Psychiatric history: Assess for history of depr... |
| Q121 | - |  |  | SI | D. Red Flags: The patient should be carefully obse... |
| Q122 | - |  |  | SI | Any positive report should prompt strong considera... |
| Q123 | - |  |  | SI | E. Diagnosis: The following ICD diagnostic codes m... |
| Q124 | - |  |  | SI | S06.0 (Concussive injury) |
| Q125 | - |  |  | SI | S06.00 (Concussion) |
| Q126 | - |  |  | SI | Diagnostic category of S06 should be considered. |
| Q127 | - |  |  | SI | F. Follow-Up Action Plan: Develop a follow-up plan... |
| Q128 | - |  |  | SI | Serial evaluation of the concussion is critical as... |
| Q129 | - |  |  | SI | Referral to a specialist can be particularly valua... |
| Q13 | - |  |  | SI | Amnesia Before (Retrograde) - Are there any events... |
| Q130 | - |  |  | SI | 1. Physician / Clinician serial monitoring – Parti... |
| Q131 | - |  |  | SI | referral to a specialist is warranted. |
| Q132 | - |  |  | SI | 2. Referral to a specialist – Appropriate if sympt... |
| Q133 | - |  |  | SI | • Neuropsychological Testing can provide valuable ... |
| Q134 | - |  |  | SI | • Physician Evaluation is particularly relevant fo... |
| Q135 | - |  |  | SI | It may be useful for medication management (e.g., ... |
| Q136 | - |  |  | SI | ACE ED Instructions |
| Q137 | - |  |  | SI | A. Injury Characteristics |
| Q138 | - |  |  | SI | 1. Injury Description: Ask for description of even... |
| Q139 | - |  |  | SI | 2. Cause: Indicate the cause of injury or write in... |
| Q14 | - |  |  | SI | Duration |
| Q140 | - |  |  | SI | 3. Amnesia: Determine whether child was not regist... |
| Q141 | - |  |  | SI | 4. Estimate length of time for each (Retrograde am... |
| Q142 | - |  |  | SI | 5. Loss of consciousness (LOC) - If occurs, determ... |
| Q143 | - |  |  | SI | 6. Early signs observed by others. Ask the individ... |
| Q144 | - |  |  | SI | Signs are typically observed early after the injur... |
| Q145 | - |  |  | SI | 7. Seizures: Inquire whether seizures were observe... |
| Q146 | - |  |  | SI | B. Symptom Check List: |
| Q147 | - |  |  | SI | • Ask patient (and/ or parent, if child) to report... |
| Q148 | - |  |  | SI | One or all symptoms may be present depending upon ... |
| Q149 | - |  |  | SI | • Note: Most sleep symptoms are only applicable af... |
| Q15 | - |  |  | SI | Amnesia After (Anterograde) - Are there any events... |
| Q150 | - |  |  | SI | • Since symptoms can be present premorbidly/ at ba... |
| Q151 | - |  |  | SI | if Patient/ Parent indicates “I/ He usually has th... |
| Q152 | - |  |  | SI | Scoring: Sum total number of symptoms present per ... |
| Q153 | - |  |  | SI | Drowsiness may be present on the day of injury.) I... |
| Q154 | - |  |  | SI | • General Impression: Ask how different the person... |
| Q155 | - |  |  | SI | • Patient Participation: Indicate the extent to wh... |
| Q156 | - |  |  | SI | C. Concussion history: Assess the number and date(... |
| Q157 | - |  |  | SI | decision-making regarding Return to Play, and gene... |
| Q158 | - |  |  | SI | Headache history: Assess personal history of diagn... |
| Q159 | - |  |  | SI | D. Diagnosis: The following ICD diagnostic codes m... |
| Q16 | - |  |  | SI | Duration |
| Q160 | - |  |  | SI | S06.0 (Concussive injury) |
| Q161 | - |  |  | SI | S06.00 (Concussion) |
| Q162 | - |  |  | SI | Diagnostic category of S06 should be considered. |
| Q163 | - |  |  | SI | E. Follow-Up Action: Determine a plan of action fo... |
| Q164 | - |  |  | SI | (e.g., cognitive/ physical exertion, comorbidities... |
| Q165 | - |  |  | SI | (a) Patient monitoring in the primary care physici... |
| Q166 | - |  |  | SI | (b) Referral to a specialist: particularly valuabl... |
| Q167 | - |  |  | SI | • Neuropsychological Testing is particularly relev... |
| Q168 | - |  |  | SI | Testing is also recommended when a patient may be ... |
| Q169 | - |  |  | SI | • Physician Evaluation is particularly relevant fo... |
| Q17 | - |  |  | SI | Loss of Consciousness |
| Q170 | - |  |  | SI | May be useful for medication management (e.g., hea... |
| Q171 | - |  |  | SI | Score |
| Q172 | - |  |  | SI | Classification |
| Q173 | - |  |  | SI | The Acute Concussion Evaluation (ACE) is intended ... |
| Q174 | - |  |  | SI | Higher the score, higher the risk of concussion |
| Q175 | - |  |  | SI | 0 - 22 |
| Q176 | - |  |  | SI | 0 - 22: Higher the score, higher the risk of concu... |
| Q177 | - |  |  | SI | Mild Traumatic Brain Injury (MTBI) |
| Q18 | - |  |  | SI | Duration |
| Q19 | - |  |  | SI | Early Signs |
| Q20 | - |  |  | SI | Were seizures observed? |
| Q21 | - |  |  | SI | Seizure Details |
| Q22 | - |  |  | SI | Physical |
| Q23 | - |  |  | SI | Since your injury, have you experienced any of the... |
| Q24 | - |  |  | SI | Headache |
| Q25 | - |  |  | SI | Nausea |
| Q26 | - |  |  | SI | Vomiting |
| Q27 | - |  |  | SI | Balance problems |
| Q28 | - |  |  | SI | Dizziness |
| Q29 | - |  |  | SI | Visual problems |
| Q30 | - |  |  | SI | Fatigue |
| Q31 | - |  |  | SI | Sensitivity to light |
| Q32 | - |  |  | SI | Sensitivity to noise |
| Q33 | - |  |  | SI | Numbness / Tingling |
| Q34 | - |  |  | SI | Physical Total |
| Q35 | - |  |  | SI | Cognitive |
| Q36 | - |  |  | SI | Since your injury, have you experienced any of the... |
| Q37 | - |  |  | SI | Feeling mentally foggy |
| Q38 | - |  |  | SI | Feeling slowed down |
| Q39 | - |  |  | SI | Difficulty concentrating |
| Q40 | - |  |  | SI | Difficulty remembering |
| Q41 | - |  |  | SI | Cognitive Total |
| Q42 | - |  |  | SI | Emotional |
| Q43 | - |  |  | SI | Since your injury, have you experienced any of the... |
| Q44 | - |  |  | SI | Irritability |
| Q45 | - |  |  | SI | Sadness |
| Q46 | - |  |  | SI | More emotional |
| Q47 | - |  |  | SI | Nervousness |
| Q48 | - |  |  | SI | Emotional Total |
| Q49 | - |  |  | SI | Sleep |
| Q50 | - |  |  | SI | Since your injury, have you experienced any of the... |
| Q51 | - |  |  | SI | Drowsiness |
| Q52 | - |  |  | SI | Sleeping less than usual |
| Q53 | - |  |  | SI | Sleeping more than usual |
| Q54 | - |  |  | SI | Trouble falling asleep |
| Q55 | - |  |  | SI | Sleep Total |
| Q56 | - |  |  | SI | Total Symptom Score |
| Q57 | - |  |  | SI | Other Observations |
| Q58 | - |  |  | SI | Patient Participation |
| Q59 | - |  |  | SI | Reason for Partial / None |
| Q60 | - |  |  | SI | Other Reasons |
| Q61 | - |  |  | SI | Exertion |
| Q62 | - |  |  | SI | Do these symptoms worsen with Physical activity? |
| Q63 | - |  |  | SI | Do these symptoms worsen with Cognitive activity? |
| Q64 | - |  |  | SI | Overall rating |
| Q65 | - |  |  | SI | How differently are you acting compared to your no... |
| Q67 | - |  |  | SI | History of Concussion |
| Q68 | - |  |  | SI | Number of previous concussions |
| Q69 | - |  |  | SI | Longest concussion symptom duration |
| Q70 | - |  |  | SI | Days |
| Q71 | - |  |  | SI | Weeks |
| Q72 | - |  |  | SI | Months |
| Q73 | - |  |  | SI | Years |
| Q74 | - |  |  | SI | If multiple concussions, less force caused re-inju... |
| Q75 | - |  |  | SI | History of Headache |
| Q76 | - |  |  | SI | Prior treatment for headache |
| Q77 | - |  |  | SI | History of Personal migraine headache |
| Q78 | - |  |  | SI | History of Family migraine headache |
| Q79 | - |  |  | SI | Developmental History |
| Q80 | - |  |  | SI | Other developmental disorder |
| Q81 | - |  |  | SI | Psychiatric History |
| Q82 | - |  |  | SI | Other psychiatric disorder |
| Q83 | - |  |  | SI | Risk Factor comments |
| Q84 | - |  |  | SI | List other co-morbid medical disorders or medicati... |
| Q85 | - |  |  | SI | Refer to Emergency Department (ED) with sudden ons... |
| Q86 | - |  |  | SI | Diagnosis (ICD) |
| Q87 | - |  |  | SI | Complete ACE Care Plan and provide copy to patient... |
| Q88 | - |  |  | SI | Follow-Up Action Plan |
| Q89 | - |  |  | SI | Date of Next Followup |
| Q90 | - |  |  | SI | Referrals (Please place the appropriate referral o... |
| Q91 | - |  |  | SI | ACE Instructions |
| Q92 | - |  |  | SI | A. Injury Characteristics: |
| Q93 | - |  |  | SI | 1. Obtain description of the injury – how injury o... |
| Q94 | - |  |  | SI | (e.g., occipital blow may result in visual changes... |
| Q95 | - |  |  | SI | 2. Indicate the cause of injury. Greater forces as... |
| Q96 | - |  |  | SI | 3/4. Amnesia: Amnesia is defined as the failure to... |
| Q97 | - |  |  | SI | injury. Even seconds to minutes of memory loss can... |
| Q98 | - |  |  | SI | is LOC (less than 1 minute). |
| Q99 | - |  |  | SI | 5. Loss of consciousness (LOC) – If occurs, determ... |
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