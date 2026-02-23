# SQLUser.PAC_AdmissionPoint

**Schema:** SQLUser
**Columnas:** 294
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ADMPOINT_RowId | bigint | PK |  | NO | - |
| ADMPOINT_Code | varchar |  |  | NO | Code |
| ADMPOINT_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| ADMPOINT_CreatedDate | date |  |  | SI | Created Date |
| ADMPOINT_CreatedTime | time |  |  | SI | Created Time |
| ADMPOINT_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ADMPOINT_DateFrom | date |  |  | SI | Date From |
| ADMPOINT_DateTo | date |  |  | SI | Date To |
| ADMPOINT_Desc | varchar |  |  | NO | Description |
| ADMPOINT_Owner | varchar |  |  | SI | Owner |
| ADMPOINT_UpdatedDate | date |  |  | SI | Updated Date |
| ADMPOINT_UpdatedTime | time |  |  | SI | Updated Time |
| ADMPOINT_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | (Refer to the Guidelines below)	 |
| Q02 | - |  |  | SI | Pharmaceutical therapies |
| Q03 | - |  |  | SI | Comment/Justification	 |
| Q04 | - |  |  | SI | Nutrition |
| Q05 | - |  |  | SI | Comment/Justification	 |
| Q06 | - |  |  | SI | Functional status |
| Q07 | - |  |  | SI | Comment/Justification	 |
| Q08 | - |  |  | SI | Incontinence and renal insufficiency |
| Q09 | - |  |  | SI | Comment/Justification	 |
| Q10 | - |  |  | SI | Skin integrity |
| Q100 | - |  |  | SI | 2 - Continence care is problematic and requires ti... |
| Q101 | - |  |  | SI | OR |
| Q102 | - |  |  | SI | Catheter care and bowel management (i.e. manual ev... |
| Q103 | - |  |  | SI | OR |
| Q104 | - |  |  | SI | Complicated Ostomy care. |
| Q105 | - |  |  | SI | OR |
| Q106 | - |  |  | SI | Intermittent catheterisation. |
| Q107 | - |  |  | SI | OR |
| Q108 | - |  |  | SI | Patient on bladder rehabilitation program. |
| Q109 | - |  |  | SI | OR |
| Q11 | - |  |  | SI | Comment/Justification	 |
| Q110 | - |  |  | SI | Presence of renal insufficiency that requires regu... |
| Q111 | - |  |  | SI | 10 - Peritoneal Dialysis |
| Q112 | - |  |  | SI | OR |
| Q113 | - |  |  | SI | Home Haemodialysis |
| Q114 | - |  |  | SI | Skin integrity |
| Q115 | - |  |  | SI | 0 - Risk of skin breakdown which requires preventa... |
| Q116 | - |  |  | SI | 1 - High risk of skin breakdown (as per documented... |
| Q117 | - |  |  | SI | OR |
| Q118 | - |  |  | SI | Pressure ulcer(s) (Grade 1/4) either with ‘discolo... |
| Q119 | - |  |  | SI | OR |
| Q12 | - |  |  | SI | Breathing |
| Q120 | - |  |  | SI | Patient with open wound(s), pressure ulcer(s) (Gra... |
| Q121 | - |  |  | SI | 2 - High-risk of skin breakdown (as per documented... |
| Q122 | - |  |  | SI | OR |
| Q123 | - |  |  | SI | Pressure damage or open wound(s), pressure ulcer(s... |
| Q124 | - |  |  | SI | OR |
| Q125 | - |  |  | SI | Open wound(s), pressure ulcer(s) (Grade 3/4) which... |
| Q126 | - |  |  | SI | 10 - Open wound(s), pressure ulcer(s) (Grade 3/4) ... |
| Q127 | - |  |  | SI | OR |
| Q128 | - |  |  | SI | Large open wound(s), pressure ulcer(s) (Grade 4/4)... |
| Q129 | - |  |  | SI | under the supervision of professional and skilled ... |
| Q13 | - |  |  | SI | Comment/Justification |
| Q130 | - |  |  | SI | (e.g. large draining wounds, lower extremity non-h... |
| Q131 | - |  |  | SI | Breathing |
| Q132 | - |  |  | SI | 0 - Shortness of breath, which has no impact on da... |
| Q133 | - |  |  | SI | i. inhalers or a nebuliser |
| Q134 | - |  |  | SI | ii. oxygen therapy on need. |
| Q135 | - |  |  | SI | 1 - Episodes of shortness of breath which has an i... |
| Q136 | - |  |  | SI | i.e. Normal doses of inhalation/nebulisation |
| Q137 | - |  |  | SI | AND |
| Q138 | - |  |  | SI | i. On daily low level oxygen therapy (24%) |
| Q139 | - |  |  | SI | ii. Other therapeutic appliances to maintain airfl... |
| Q14 | - |  |  | SI | Cognition |
| Q140 | - |  |  | SI | 2 - Shortness of breath, which limits daily living... |
| Q141 | - |  |  | SI | i. Continuous monitoring |
| Q142 | - |  |  | SI | ii. The use of high doses of nebulisation |
| Q143 | - |  |  | SI | iii. Room air ventilators via a facial or nasal ma... |
| Q144 | - |  |  | SI | iv. Frequent suctioning |
| Q145 | - |  |  | SI | v. Simple Chest Physiotherapy |
| Q146 | - |  |  | SI | vi. The use of CPAP or BiPAP. |
| Q147 | - |  |  | SI | 10 - Mechanical Ventilation care (CPAP or BiPAP no... |
| Q148 | - |  |  | SI | Cognition	 |
| Q149 | - |  |  | SI | 0 - Patient diagnosed with simple cognitive impair... |
| Q15 | - |  |  | SI | Comment/Justification	 |
| Q150 | - |  |  | SI | 1 - Patient diagnosed with intermediate-extensive ... |
| Q151 | - |  |  | SI | prompting and assistance with ADL |
| Q152 | - |  |  | SI | 2 - Patient diagnosed with severe cognition impair... |
| Q153 | - |  |  | SI | Communication |
| Q154 | - |  |  | SI | 0 - Needs assistance to communicate their needs. |
| Q155 | - |  |  | SI | AND |
| Q156 | - |  |  | SI | Special effort may be needed to ensure accurate in... |
| Q157 | - |  |  | SI | 1 - Communication about needs is difficult to unde... |
| Q158 | - |  |  | SI | 2 - Unable to reliably communicate their needs at ... |
| Q159 | - |  |  | SI | AND |
| Q16 | - |  |  | SI | Communication |
| Q160 | - |  |  | SI | Must have at least assessment/re-assessment and cu... |
| Q161 | - |  |  | SI | Altered Status of Consciousness (ASC) |
| Q162 | - |  |  | SI | 0 - Occasional episodes of ASC that require the su... |
| Q163 | - |  |  | SI | 1 - Frequent episodes of ASC that require RN super... |
| Q164 | - |  |  | SI | Co-Morbidity score is calculated based on the Pati... |
| Q165 | - |  |  | SI | Patient's age: |
| Q166 | - |  |  | SI | ≤ 40 years: 0 points |
| Q167 | - |  |  | SI | 41 - 50 years: 1 point |
| Q168 | - |  |  | SI | 51 - 60 years: 2 points |
| Q169 | - |  |  | SI | 61 - 70 years: 3 points |
| Q17 | - |  |  | SI | Comment/Justification	 |
| Q170 | - |  |  | SI | ≥ 71 years: 4 points |
| Q171 | - |  |  | SI | Co-morbidities - 1 point: |
| Q172 | - |  |  | SI | Myocardial infarction |
| Q173 | - |  |  | SI | Congestive heart failure |
| Q174 | - |  |  | SI | Peripheral vascular disease |
| Q175 | - |  |  | SI | Cerebrovascular disease |
| Q176 | - |  |  | SI | Dementia |
| Q177 | - |  |  | SI | Chronic Obstructive Pulmonary Disease (COPD) |
| Q178 | - |  |  | SI | Connective tissue disease |
| Q179 | - |  |  | SI | Peptic ulcer disease |
| Q18 | - |  |  | SI | Altered Status of Consciousness (ASC) |
| Q180 | - |  |  | SI | Diabetes - uncomplicated |
| Q181 | - |  |  | SI | Liver disease - mild |
| Q182 | - |  |  | SI | Co-morbidities - 2 points: |
| Q183 | - |  |  | SI | Chronic kidney disease |
| Q184 | - |  |  | SI | Hemiplegia or paraplegia |
| Q185 | - |  |  | SI | Leukaemia |
| Q186 | - |  |  | SI | Malignant lymphoma |
| Q187 | - |  |  | SI | Diabetes - end-organ damage |
| Q188 | - |  |  | SI | Solid tumor |
| Q189 | - |  |  | SI | Co-morbidities - 3 points: |
| Q19 | - |  |  | SI | Comment/Justification	 |
| Q190 | - |  |  | SI | Liver disease - moderate-severe |
| Q191 | - |  |  | SI | Co-morbidities - 6 points: |
| Q192 | - |  |  | SI | Solid tumor - metastatic |
| Q193 | - |  |  | SI | AIDS |
| Q194 | - |  |  | SI | Level of Care |
| Q195 | - |  |  | SI | Score |
| Q196 | - |  |  | SI | Classification |
| Q197 | - |  |  | SI | 0 - 2 |
| Q198 | - |  |  | SI | Simple |
| Q199 | - |  |  | SI | 3 - 5 |
| Q20 | - |  |  | SI | Level of Care score	 |
| Q200 | - |  |  | SI | Intermediate |
| Q201 | - |  |  | SI | 6 - 9 |
| Q202 | - |  |  | SI | Intensive |
| Q203 | - |  |  | SI | > 9 |
| Q204 | - |  |  | SI | Complex |
| Q205 | - |  |  | SI | Co-Morbidity Index |
| Q206 | - |  |  | SI | 0 - 8 |
| Q207 | - |  |  | SI | Simple |
| Q208 | - |  |  | SI | 9 - 12 |
| Q209 | - |  |  | SI | Intermediate |
| Q21 | - |  |  | SI | 0 - 2: Simple |
| Q210 | - |  |  | SI | 13 - 15 |
| Q211 | - |  |  | SI | Intensive |
| Q212 | - |  |  | SI | > 15 |
| Q213 | - |  |  | SI | Complex |
| Q214 | - |  |  | SI | Nursing Duration |
| Q215 | - |  |  | SI | 1 |
| Q216 | - |  |  | SI | Simple |
| Q217 | - |  |  | SI | 2 |
| Q218 | - |  |  | SI | Intermediate |
| Q219 | - |  |  | SI | 3 |
| Q22 | - |  |  | SI | 3 - 5: Intermediate |
| Q220 | - |  |  | SI | Intensive |
| Q221 | - |  |  | SI | 5 |
| Q222 | - |  |  | SI | Complex |
| Q223 | - |  |  | SI | Supportive/Specialised |
| Q224 | - |  |  | SI | 1 |
| Q225 | - |  |  | SI | Simple |
| Q226 | - |  |  | SI | 2 |
| Q227 | - |  |  | SI | Intermediate |
| Q228 | - |  |  | SI | 3 |
| Q229 | - |  |  | SI | Intensive |
| Q23 | - |  |  | SI | 6 - 9: Intensive |
| Q230 | - |  |  | SI | 6 |
| Q231 | - |  |  | SI | Complex |
| Q232 | - |  |  | SI | The Home Health Authorization Scoring Assessment i... |
| Q233 | - |  |  | SI | Pattern of Care Total Score |
| Q234 | - |  |  | SI | 1 - 4 |
| Q235 | - |  |  | SI | Simple |
| Q236 | - |  |  | SI | 5 - 8 |
| Q237 | - |  |  | SI | Intermediate |
| Q238 | - |  |  | SI | 9 - 12 |
| Q239 | - |  |  | SI | Intensive |
| Q24 | - |  |  | SI | > 9: Complex |
| Q240 | - |  |  | SI | >12 |
| Q241 | - |  |  | SI | Complex |
| Q25 | - |  |  | SI | Age |
| Q26 | - |  |  | SI | Age score |
| Q27 | - |  |  | SI | 41 - 50 years - 1 point |
| Q28 | - |  |  | SI | 51 - 60 years - 2 points |
| Q29 | - |  |  | SI | 61 - 70 years - 3 points |
| Q30 | - |  |  | SI | 71+ years - 4 points |
| Q31 | - |  |  | SI | Co-Morbidities |
| Q32 | - |  |  | SI | Co-Morbidity index comment |
| Q33 | - |  |  | SI | Co-Morbidity index score |
| Q34 | - |  |  | SI | 0 - 8: Simple |
| Q35 | - |  |  | SI | 9 - 12: Intermediate	 |
| Q36 | - |  |  | SI | 13 - 15: Intensive |
| Q37 | - |  |  | SI | > 15: Complex |
| Q38 | - |  |  | SI | Nursing duration |
| Q39 | - |  |  | SI | Nursing duration comment |
| Q40 | - |  |  | SI | Nursing duration score |
| Q41 | - |  |  | SI | 1: Simple	 |
| Q42 | - |  |  | SI | 2: Intermediate |
| Q43 | - |  |  | SI | 3: Intensive |
| Q44 | - |  |  | SI | 5: Complex |
| Q45 | - |  |  | SI | Supportive/Specialised services |
| Q46 | - |  |  | SI | Supportive/Specialised services comment	 |
| Q47 | - |  |  | SI | Supportive/Specialised score	 |
| Q48 | - |  |  | SI | 1: Simple	 |
| Q49 | - |  |  | SI | 2: Intermediate |
| Q50 | - |  |  | SI | 3: Intensive |
| Q51 | - |  |  | SI | 6: Complex |
| Q52 | - |  |  | SI | Total score |
| Q53 | - |  |  | SI | Pharmaceutical therapies |
| Q54 | - |  |  | SI | 0 - Requires supervision/administration of and/or ... |
| Q55 | - |  |  | SI | 1 - Has oral, enteral, topical or inhalation pharm... |
| Q56 | - |  |  | SI | OR |
| Q57 | - |  |  | SI | Administration of statutory dose of parenteral pha... |
| Q58 | - |  |  | SI | 2 - Has a drug regime prescribed by licensed physi... |
| Q59 | - |  |  | SI | 3 - Has a drug regime that requires administration... |
| Q60 | - |  |  | SI | or risks regarding the severity of side-effects. |
| Q61 | - |  |  | SI | OR |
| Q62 | - |  |  | SI | IV infusion therapy > 1 hour per day. |
| Q63 | - |  |  | SI | Nutrition |
| Q64 | - |  |  | SI | 0 - Needs supervision, prompting with meals, or ma... |
| Q65 | - |  |  | SI | OR |
| Q66 | - |  |  | SI | Able to take food and drink by mouth but requires ... |
| Q67 | - |  |  | SI | OR |
| Q68 | - |  |  | SI | Patient on feeding device (such as NG or PEG) and ... |
| Q69 | - |  |  | SI | 1 - Needs supervision prompting with meals, requir... |
| Q70 | - |  |  | SI | OR |
| Q71 | - |  |  | SI | Dependent on feeding devices and needs supervision... |
| Q72 | - |  |  | SI | 2 - Dysphagia: needs oral feeding to ensure adequa... |
| Q73 | - |  |  | SI | OR |
| Q74 | - |  |  | SI | On Special Feeding Program (i.e. children with chr... |
| Q75 | - |  |  | SI | OR |
| Q76 | - |  |  | SI | Problematic PEG/NG feeding that needs daily skille... |
| Q77 | - |  |  | SI | OR |
| Q78 | - |  |  | SI | Nutritional status ‘at risk’ and requiring intrave... |
| Q79 | - |  |  | SI | 10 - Completely dependent on Total Parenteral Nutr... |
| Q80 | - |  |  | SI | Functional status |
| Q81 | - |  |  | SI | 0 - Able to weight bear but needs some assistance ... |
| Q82 | - |  |  | SI | 1 - Patient < 2 years of age and requires skilled ... |
| Q83 | - |  |  | SI | OR |
| Q84 | - |  |  | SI | Partially dependent in ADL performance. |
| Q85 | - |  |  | SI | OR |
| Q86 | - |  |  | SI | At moderate risk of falls (as evidenced in a falls... |
| Q87 | - |  |  | SI | 2 - Functional disability due to accident or disea... |
| Q88 | - |  |  | SI | daily passive exercises to prevent immobility comp... |
| Q89 | - |  |  | SI | 3 - Completely immobile, cannot perform ADL and re... |
| Q90 | - |  |  | SI | AND |
| Q91 | - |  |  | SI | Passive movement, positioning or transfer carries: |
| Q92 | - |  |  | SI | 1. High risk of serious physical harm, including i... |
| Q93 | - |  |  | SI | OR |
| Q94 | - |  |  | SI | 2. Overwhelming pain on movement needs careful pos... |
| Q95 | - |  |  | SI | Incontinence and renal insufficiency |
| Q96 | - |  |  | SI | 0 - Continence care is routine on a day-to-day bas... |
| Q97 | - |  |  | SI | OR |
| Q98 | - |  |  | SI | Incontinence of urine managed through, for example... |
| Q99 | - |  |  | SI | 1 - Continence care is routine but requires monito... |
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