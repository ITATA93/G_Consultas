# questionnaire.QTCHHCSA

> Home Health Care Scoring Assessment

**Schema:** questionnaire
**Columnas:** 282
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Home Health Care Scoring Assessment

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | (Refer to the Guidelines below)	 |
| Q02 | varchar |  |  | SI | Pharmaceutical therapies |
| Q03 | varchar |  |  | SI | Comment/Justification	 |
| Q04 | varchar |  |  | SI | Nutrition |
| Q05 | varchar |  |  | SI | Comment/Justification	 |
| Q06 | varchar |  |  | SI | Functional status |
| Q07 | varchar |  |  | SI | Comment/Justification	 |
| Q08 | varchar |  |  | SI | Incontinence and renal insufficiency |
| Q09 | varchar |  |  | SI | Comment/Justification	 |
| Q10 | varchar |  |  | SI | Skin integrity |
| Q100 | varchar |  |  | SI | 2 - Continence care is problematic and requires ti... |
| Q101 | varchar |  |  | SI | OR |
| Q102 | varchar |  |  | SI | Catheter care and bowel management (i.e. manual ev... |
| Q103 | varchar |  |  | SI | OR |
| Q104 | varchar |  |  | SI | Complicated Ostomy care. |
| Q105 | varchar |  |  | SI | OR |
| Q106 | varchar |  |  | SI | Intermittent catheterisation. |
| Q107 | varchar |  |  | SI | OR |
| Q108 | varchar |  |  | SI | Patient on bladder rehabilitation program. |
| Q109 | varchar |  |  | SI | OR |
| Q11 | varchar |  |  | SI | Comment/Justification	 |
| Q110 | varchar |  |  | SI | Presence of renal insufficiency that requires regu... |
| Q111 | varchar |  |  | SI | 10 - Peritoneal Dialysis |
| Q112 | varchar |  |  | SI | OR |
| Q113 | varchar |  |  | SI | Home Haemodialysis |
| Q114 | varchar |  |  | SI | Skin integrity |
| Q115 | varchar |  |  | SI | 0 - Risk of skin breakdown which requires preventa... |
| Q116 | varchar |  |  | SI | 1 - High risk of skin breakdown (as per documented... |
| Q117 | varchar |  |  | SI | OR |
| Q118 | varchar |  |  | SI | Pressure ulcer(s) (Grade 1/4) either with ‘discolo... |
| Q119 | varchar |  |  | SI | OR |
| Q12 | varchar |  |  | SI | Breathing |
| Q120 | varchar |  |  | SI | Patient with open wound(s), pressure ulcer(s) (Gra... |
| Q121 | varchar |  |  | SI | 2 - High-risk of skin breakdown (as per documented... |
| Q122 | varchar |  |  | SI | OR |
| Q123 | varchar |  |  | SI | Pressure damage or open wound(s), pressure ulcer(s... |
| Q124 | varchar |  |  | SI | OR |
| Q125 | varchar |  |  | SI | Open wound(s), pressure ulcer(s) (Grade 3/4) which... |
| Q126 | varchar |  |  | SI | 10 - Open wound(s), pressure ulcer(s) (Grade 3/4) ... |
| Q127 | varchar |  |  | SI | OR |
| Q128 | varchar |  |  | SI | Large open wound(s), pressure ulcer(s) (Grade 4/4)... |
| Q129 | varchar |  |  | SI | under the supervision of professional and skilled ... |
| Q13 | varchar |  |  | SI | Comment/Justification |
| Q130 | varchar |  |  | SI | (e.g. large draining wounds, lower extremity non-h... |
| Q131 | varchar |  |  | SI | Breathing |
| Q132 | varchar |  |  | SI | 0 - Shortness of breath, which has no impact on da... |
| Q133 | varchar |  |  | SI | i. inhalers or a nebuliser; or |
| Q134 | varchar |  |  | SI | ii. oxygen therapy on need. |
| Q135 | varchar |  |  | SI | 1 - Episodes of shortness of breath which has an i... |
| Q136 | varchar |  |  | SI | i.e. Normal doses of inhalation/nebulisation |
| Q137 | varchar |  |  | SI | AND |
| Q138 | varchar |  |  | SI | i. On daily low level oxygen therapy (24%); or |
| Q139 | varchar |  |  | SI | ii. Other therapeutic appliances to maintain airfl... |
| Q14 | varchar |  |  | SI | Cognition |
| Q140 | varchar |  |  | SI | 2 - Shortness of breath, which limits daily living... |
| Q141 | varchar |  |  | SI | i. Continuous monitoring; or |
| Q142 | varchar |  |  | SI | ii. The use of high doses of nebulisation; or |
| Q143 | varchar |  |  | SI | iii. Room air ventilators via a facial or nasal ma... |
| Q144 | varchar |  |  | SI | iv. Frequent suctioning; or |
| Q145 | varchar |  |  | SI | v. Simple Chest Physiotherapy; or |
| Q146 | varchar |  |  | SI | vi. The use of CPAP or BiPAP. |
| Q147 | varchar |  |  | SI | 10 - Mechanical Ventilation care (CPAP or BiPAP no... |
| Q148 | varchar |  |  | SI | Cognition	 |
| Q149 | varchar |  |  | SI | 0 - Patient diagnosed with simple cognitive impair... |
| Q15 | varchar |  |  | SI | Comment/Justification	 |
| Q150 | varchar |  |  | SI | 1 - Patient diagnosed with intermediate-extensive ... |
| Q151 | varchar |  |  | SI | prompting and assistance with ADL |
| Q152 | varchar |  |  | SI | 2 - Patient diagnosed with severe cognition impair... |
| Q153 | varchar |  |  | SI | Communication |
| Q154 | varchar |  |  | SI | 0 - Needs assistance to communicate their needs. |
| Q155 | varchar |  |  | SI | AND |
| Q156 | varchar |  |  | SI | Special effort may be needed to ensure accurate in... |
| Q157 | varchar |  |  | SI | 1 - Communication about needs is difficult to unde... |
| Q158 | varchar |  |  | SI | 2 - Unable to reliably communicate their needs at ... |
| Q159 | varchar |  |  | SI | AND |
| Q16 | varchar |  |  | SI | Communication |
| Q160 | varchar |  |  | SI | Must have at least assessment/re-assessment and cu... |
| Q161 | varchar |  |  | SI | Altered Status of Consciousness (ASC) |
| Q162 | varchar |  |  | SI | 0 - Occasional episodes of ASC that require the su... |
| Q163 | varchar |  |  | SI | 1 - Frequent episodes of ASC that require RN super... |
| Q164 | varchar |  |  | SI | Co-Morbidity score is calculated based on the Pati... |
| Q165 | varchar |  |  | SI | Patient's age: |
| Q166 | varchar |  |  | SI | ≤ 40 years: 0 points |
| Q167 | varchar |  |  | SI | 41 - 50 years: 1 point |
| Q168 | varchar |  |  | SI | 51 - 60 years: 2 points |
| Q169 | varchar |  |  | SI | 61 - 70 years: 3 points |
| Q17 | varchar |  |  | SI | Comment/Justification	 |
| Q170 | varchar |  |  | SI | ≥ 71 years: 4 points |
| Q171 | varchar |  |  | SI | Co-morbidities - 1 point: |
| Q172 | varchar |  |  | SI | Myocardial infarction |
| Q173 | varchar |  |  | SI | Congestive heart failure |
| Q174 | varchar |  |  | SI | Peripheral vascular disease |
| Q175 | varchar |  |  | SI | Cerebrovascular disease |
| Q176 | varchar |  |  | SI | Dementia |
| Q177 | varchar |  |  | SI | Chronic Obstructive Pulmonary Disease (COPD) |
| Q178 | varchar |  |  | SI | Connective tissue disease |
| Q179 | varchar |  |  | SI | Peptic ulcer disease |
| Q18 | varchar |  |  | SI | Altered Status of Consciousness (ASC) |
| Q180 | varchar |  |  | SI | Diabetes - uncomplicated |
| Q181 | varchar |  |  | SI | Liver disease - mild |
| Q182 | varchar |  |  | SI | Co-morbidities - 2 points: |
| Q183 | varchar |  |  | SI | Chronic kidney disease |
| Q184 | varchar |  |  | SI | Hemiplegia or paraplegia |
| Q185 | varchar |  |  | SI | Leukaemia |
| Q186 | varchar |  |  | SI | Malignant lymphoma |
| Q187 | varchar |  |  | SI | Diabetes - end-organ damage |
| Q188 | varchar |  |  | SI | Solid tumor |
| Q189 | varchar |  |  | SI | Co-morbidities - 3 points: |
| Q19 | varchar |  |  | SI | Comment/Justification	 |
| Q190 | varchar |  |  | SI | Liver disease - moderate-severe |
| Q191 | varchar |  |  | SI | Co-morbidities - 6 points: |
| Q192 | varchar |  |  | SI | Solid tumor - metastatic |
| Q193 | varchar |  |  | SI | AIDS |
| Q194 | varchar |  |  | SI | Level of Care |
| Q195 | varchar |  |  | SI | Score |
| Q196 | varchar |  |  | SI | Classification |
| Q197 | varchar |  |  | SI | 0 - 2 |
| Q198 | varchar |  |  | SI | Simple |
| Q199 | varchar |  |  | SI | 3 - 5 |
| Q20 | varchar |  |  | SI | Level of Care score	 |
| Q200 | varchar |  |  | SI | Intermediate |
| Q201 | varchar |  |  | SI | 6 - 9 |
| Q202 | varchar |  |  | SI | Intensive |
| Q203 | varchar |  |  | SI | > 9 |
| Q204 | varchar |  |  | SI | Complex |
| Q205 | varchar |  |  | SI | Co-Morbidity Index |
| Q206 | varchar |  |  | SI | 0 - 8 |
| Q207 | varchar |  |  | SI | Simple |
| Q208 | varchar |  |  | SI | 9 - 12 |
| Q209 | varchar |  |  | SI | Intermediate |
| Q21 | varchar |  |  | SI | 0 - 2: Simple |
| Q210 | varchar |  |  | SI | 13 - 15 |
| Q211 | varchar |  |  | SI | Intensive |
| Q212 | varchar |  |  | SI | > 15 |
| Q213 | varchar |  |  | SI | Complex |
| Q214 | varchar |  |  | SI | Nursing Duration |
| Q215 | varchar |  |  | SI | 1 |
| Q216 | varchar |  |  | SI | Simple |
| Q217 | varchar |  |  | SI | 2 |
| Q218 | varchar |  |  | SI | Intermediate |
| Q219 | varchar |  |  | SI | 3 |
| Q22 | varchar |  |  | SI | 3 - 5: Intermediate |
| Q220 | varchar |  |  | SI | Intensive |
| Q221 | varchar |  |  | SI | 5 |
| Q222 | varchar |  |  | SI | Complex |
| Q223 | varchar |  |  | SI | Supportive/Specialised  |
| Q224 | varchar |  |  | SI | 1 |
| Q225 | varchar |  |  | SI | Simple |
| Q226 | varchar |  |  | SI | 2 |
| Q227 | varchar |  |  | SI | Intermediate |
| Q228 | varchar |  |  | SI | 3 |
| Q229 | varchar |  |  | SI | Intensive |
| Q23 | varchar |  |  | SI | 6 - 9: Intensive |
| Q230 | varchar |  |  | SI | 6 |
| Q231 | varchar |  |  | SI | Complex |
| Q232 | varchar |  |  | SI | The Home Health Authorization Scoring Assessment i... |
| Q233 | varchar |  |  | SI | Pattern of Care Total Score |
| Q234 | varchar |  |  | SI | 1 - 4 |
| Q235 | varchar |  |  | SI | Simple |
| Q236 | varchar |  |  | SI | 5 - 8 |
| Q237 | varchar |  |  | SI | Intermediate |
| Q238 | varchar |  |  | SI | 9 - 12 |
| Q239 | varchar |  |  | SI | Intensive |
| Q24 | varchar |  |  | SI | > 9: Complex |
| Q240 | varchar |  |  | SI | >12 |
| Q241 | varchar |  |  | SI | Complex |
| Q25 | varchar |  |  | SI | Age |
| Q26 | numeric |  |  | SI | Age score |
| Q27 | varchar |  |  | SI | 41 - 50 years - 1 point |
| Q28 | varchar |  |  | SI | 51 - 60 years - 2 points |
| Q29 | varchar |  |  | SI | 61 - 70 years - 3 points |
| Q30 | varchar |  |  | SI | 71+ years - 4 points |
| Q31 | varchar |  |  | SI | Co-Morbidities |
| Q32 | varchar |  |  | SI | Co-Morbidity index comment |
| Q33 | varchar |  |  | SI | Co-Morbidity index score |
| Q34 | varchar |  |  | SI | 0 - 8: Simple |
| Q35 | varchar |  |  | SI | 9 - 12: Intermediate	 |
| Q36 | varchar |  |  | SI | 13 - 15: Intensive |
| Q37 | varchar |  |  | SI | > 15: Complex |
| Q38 | varchar |  |  | SI | Nursing duration |
| Q39 | varchar |  |  | SI | Nursing duration comment |
| Q40 | varchar |  |  | SI | Nursing duration score |
| Q41 | varchar |  |  | SI | 1: Simple	 |
| Q42 | varchar |  |  | SI | 2: Intermediate |
| Q43 | varchar |  |  | SI | 3: Intensive |
| Q44 | varchar |  |  | SI | 5: Complex |
| Q45 | varchar |  |  | SI | Supportive/Specialised services |
| Q46 | varchar |  |  | SI | Supportive/Specialised services comment	 |
| Q47 | varchar |  |  | SI | Supportive/Specialised score	 |
| Q48 | varchar |  |  | SI | 1: Simple	 |
| Q49 | varchar |  |  | SI | 2: Intermediate |
| Q50 | varchar |  |  | SI | 3: Intensive |
| Q51 | varchar |  |  | SI | 6: Complex |
| Q52 | varchar |  |  | SI | Total score |
| Q53 | varchar |  |  | SI | Pharmaceutical therapies |
| Q54 | varchar |  |  | SI | 0 - Requires supervision/administration of and/or ... |
| Q55 | varchar |  |  | SI | 1 - Has oral, enteral, topical or inhalation pharm... |
| Q56 | varchar |  |  | SI | OR |
| Q57 | varchar |  |  | SI | Administration of statutory dose of parenteral pha... |
| Q58 | varchar |  |  | SI | 2 - Has a drug regime prescribed by licensed physi... |
| Q59 | varchar |  |  | SI | 3 - Has a drug regime that requires administration... |
| Q60 | varchar |  |  | SI | or risks regarding the severity of side-effects. |
| Q61 | varchar |  |  | SI | OR |
| Q62 | varchar |  |  | SI | IV infusion therapy > 1 hour per day. |
| Q63 | varchar |  |  | SI | Nutrition |
| Q64 | varchar |  |  | SI | 0 - Needs supervision, prompting with meals, or ma... |
| Q65 | varchar |  |  | SI | OR |
| Q66 | varchar |  |  | SI | Able to take food and drink by mouth but requires ... |
| Q67 | varchar |  |  | SI | OR |
| Q68 | varchar |  |  | SI | Patient on feeding device (such as NG or PEG) and ... |
| Q69 | varchar |  |  | SI | 1 - Needs supervision prompting with meals, requir... |
| Q70 | varchar |  |  | SI | OR |
| Q71 | varchar |  |  | SI | Dependent on feeding devices and needs supervision... |
| Q72 | varchar |  |  | SI | 2 - Dysphagia: needs oral feeding to ensure adequa... |
| Q73 | varchar |  |  | SI | OR |
| Q74 | varchar |  |  | SI | On Special Feeding Program (i.e. children with chr... |
| Q75 | varchar |  |  | SI | OR |
| Q76 | varchar |  |  | SI | Problematic PEG/NG feeding that needs daily skille... |
| Q77 | varchar |  |  | SI | OR |
| Q78 | varchar |  |  | SI | Nutritional status ‘at risk’ and requiring intrave... |
| Q79 | varchar |  |  | SI | 10 - Completely dependent on Total Parenteral Nutr... |
| Q80 | varchar |  |  | SI | Functional status |
| Q81 | varchar |  |  | SI | 0 - Able to weight bear but needs some assistance ... |
| Q82 | varchar |  |  | SI | 1 - Patient < 2 years of age and requires skilled ... |
| Q83 | varchar |  |  | SI | OR |
| Q84 | varchar |  |  | SI | Partially dependent in ADL performance. |
| Q85 | varchar |  |  | SI | OR |
| Q86 | varchar |  |  | SI | At moderate risk of falls (as evidenced in a falls... |
| Q87 | varchar |  |  | SI | 2 - Functional disability due to accident or disea... |
| Q88 | varchar |  |  | SI | daily passive exercises to prevent immobility comp... |
| Q89 | varchar |  |  | SI | 3 - Completely immobile, cannot perform ADL and re... |
| Q90 | varchar |  |  | SI | AND |
| Q91 | varchar |  |  | SI | Passive movement, positioning or transfer carries: |
| Q92 | varchar |  |  | SI | 1. High risk of serious physical harm, including i... |
| Q93 | varchar |  |  | SI | OR |
| Q94 | varchar |  |  | SI | 2. Overwhelming pain on movement needs careful pos... |
| Q95 | varchar |  |  | SI | Incontinence and renal insufficiency |
| Q96 | varchar |  |  | SI | 0 - Continence care is routine on a day-to-day bas... |
| Q97 | varchar |  |  | SI | OR |
| Q98 | varchar |  |  | SI | Incontinence of urine managed through, for example... |
| Q99 | varchar |  |  | SI | 1 - Continence care is routine but requires monito... |
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