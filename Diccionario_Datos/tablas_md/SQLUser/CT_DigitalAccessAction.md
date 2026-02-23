# SQLUser.CT_DigitalAccessAction

**Schema:** SQLUser
**Columnas:** 288
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DIGAA_RowId | bigint | PK |  | NO | - |
| ChildQ143DR | - |  |  | SI | Child Reference: Family / Friend care arrangements |
| DIGAA_Code | varchar |  |  | NO | Code |
| DIGAA_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| DIGAA_CreatedDate | date |  |  | SI | Created Date |
| DIGAA_CreatedTime | time |  |  | SI | Created Time |
| DIGAA_CreatedUser_DR | bigint |  | FK | SI | Created User |
| DIGAA_DateFrom | date |  |  | SI | Date From |
| DIGAA_DateTo | date |  |  | SI | Date To |
| DIGAA_Desc | varchar |  |  | NO | Description |
| DIGAA_Owner | varchar |  |  | SI | Owner |
| DIGAA_UpdatedDate | date |  |  | SI | Updated Date |
| DIGAA_UpdatedTime | time |  |  | SI | Updated Time |
| DIGAA_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Type of admission |
| Q04 | - |  |  | SI | ID band updated |
| Q05 | - |  |  | SI | ID photograph |
| Q06 | - |  |  | SI | Has the patient been in any hospital in the past 1... |
| Q07 | - |  |  | SI | Readmission to hospital? |
| Q08 | - |  |  | SI | Is the child involved with the Department of Human... |
| Q09 | - |  |  | SI | Has DHS been notified of admission? |
| Q10 | - |  |  | SI | Date of notification |
| Q100 | - |  |  | SI | If the patient is aged 65 years or older or if Yes... |
| Q101 | - |  |  | SI | Is the patient confused? |
| Q102 | - |  |  | SI | Is the patient disorientated? |
| Q103 | - |  |  | SI | Does patient currently experience pain or discomfo... |
| Q104 | - |  |  | SI | Please complete pain assessment |
| Q105 | - |  |  | SI | Pain is |
| Q106 | - |  |  | SI | Provide full details when completing detailed pain... |
| Q107 | - |  |  | SI | On admission does the patient have any skin tears,... |
| Q108 | - |  |  | SI | Wound notes |
| Q109 | - |  |  | SI | Regardless of wound identified, Braden scale to be... |
| Q11 | - |  |  | SI | Provider |
| Q110 | - |  |  | SI | Has there been recent weight loss / decrease? |
| Q111 | - |  |  | SI | Any recent changes in sleep patterns, significant ... |
| Q112 | - |  |  | SI | Any recent mood or energy level changes? |
| Q113 | - |  |  | SI | Has the doctor been notified? |
| Q114 | - |  |  | SI | Referrals to Occupational Therapy or Physiotherapy... |
| Q115 | - |  |  | SI | Dentures |
| Q116 | - |  |  | SI | Any other new / pre-existing issues with communica... |
| Q117 | - |  |  | SI | Please specify |
| Q118 | - |  |  | SI | Does the patient have a hearing impairment? |
| Q118ObsDR | - |  |  | SI | Does the patient have a hearing impairment? DR |
| Q119 | - |  |  | SI | Does the patient have a visual impairment? |
| Q119ObsDR | - |  |  | SI | Does the patient have a visual impairment? DR |
| Q12 | - |  |  | SI | Services notified of admission |
| Q120 | - |  |  | SI | Infant protection device in situ? |
| Q121 | - |  |  | SI | Identification |
| Q122 | - |  |  | SI | Hospitalisation |
| Q123 | - |  |  | SI | Number of hospital admissions in last 12 months |
| Q124 | - |  |  | SI | Parents staying overnight |
| Q125 | - |  |  | SI | Has the parent signed general admission consent fo... |
| Q126 | - |  |  | SI | Hospitalisation notes |
| Q127 | - |  |  | SI | Immunisations |
| Q128 | - |  |  | SI | COVID vaccination status |
| Q129 | - |  |  | SI | Has vaccination certificate been sighted and scann... |
| Q13 | - |  |  | SI | Welcome information given and explained |
| Q130 | - |  |  | SI | Are all other immunisations up to date? |
| Q131 | - |  |  | SI | Immunisation notes |
| Q132 | - |  |  | SI | Culture and Language |
| Q133 | - |  |  | SI | Culture / Language notes |
| Q134 | - |  |  | SI | Referral considerations: |
| Q135 | - |  |  | SI | Indigenous liaison |
| Q136 | - |  |  | SI | Accommodation and Living Arrangements |
| Q137 | - |  |  | SI | Other accommodation type |
| Q138 | - |  |  | SI | Current parent / guardian living arrangements |
| Q139 | - |  |  | SI | Other arrangement |
| Q14 | - |  |  | SI | Patient rights and responsibilities booklet |
| Q140 | - |  |  | SI | Does the patient live alone? |
| Q141 | - |  |  | SI | Family / Friend care arrangements |
| Q142 | - |  |  | SI | Please use next section to document formal care se... |
| Q144 | - |  |  | SI | Accommodation / Living arrangement notes |
| Q145 | - |  |  | SI | Referral considerations: |
| Q146 | - |  |  | SI | Social worker |
| Q147 | - |  |  | SI | Behavioural |
| Q148 | - |  |  | SI | Please ensure alerts are updated as appropriate |
| Q149 | - |  |  | SI | Is the patient at risk of suicide, self harm or ha... |
| Q15 | - |  |  | SI | Orientate to unit - bathroom / visiting times |
| Q150 | - |  |  | SI | Consider history of self-harm or current self harm... |
| Q151 | - |  |  | SI | Is the patient verbally or physically aggressive? |
| Q152 | - |  |  | SI | Behavioural notes |
| Q153 | - |  |  | SI | Referral considerations: |
| Q154 | - |  |  | SI | Occupational therapist, Psych liaison |
| Q155 | - |  |  | SI | Mood, Stress and Sleep |
| Q156 | - |  |  | SI | Normal sleeping surface |
| Q157 | - |  |  | SI | Notifications: |
| Q158 | - |  |  | SI | Doctor to be notified if yes to above questions |
| Q159 | - |  |  | SI | Referral considerations: |
| Q16 | - |  |  | SI | Use of nurse call |
| Q160 | - |  |  | SI | Dummy text |
| Q163 | - |  |  | SI | Hospital case management liaison coordinator |
| Q164 | - |  |  | SI | Orientation notes |
| Q165 | - |  |  | SI | Is the patient on any APINCH meds? |
| Q166 | - |  |  | SI | Does the patient use a dosette / webster pack? |
| Q167 | - |  |  | SI | Did patient bring medications with them? |
| Q168 | - |  |  | SI | Pharmacy review if more than five medications, on ... |
| Q169 | - |  |  | SI | Pain |
| Q17 | - |  |  | SI | Telephone location and use |
| Q170 | - |  |  | SI | Does the patient have any pain or discomfort? |
| Q171 | - |  |  | SI | Skin Integrity |
| Q172 | - |  |  | SI | Wounds identified on admission |
| Q173 | - |  |  | SI | Commence wound chart for each wound identified |
| Q174 | - |  |  | SI | Cognitive |
| Q175 | - |  |  | SI | Does the patient have a history of dementia? |
| Q176 | - |  |  | SI | Cognition notes |
| Q177 | - |  |  | SI | Referral considerations: |
| Q178 | - |  |  | SI | Social worker |
| Q179 | - |  |  | SI | Is patient at risk of wandering? |
| Q18 | - |  |  | SI | TV location and use |
| Q180 | - |  |  | SI | Referral considerations: |
| Q181 | - |  |  | SI | Mood / Stress / Sleep notes |
| Q182 | - |  |  | SI | Referral considerations: |
| Q183 | - |  |  | SI | Weight and Appetite |
| Q184 | - |  |  | SI | Complete Malnutrition Screen Tool |
| Q185 | - |  |  | SI | Does the patient have a significantly high or low ... |
| Q186 | - |  |  | SI | Is the patient >150kg or mobility / size may pose ... |
| Q187 | - |  |  | SI | Weight and appetite notes |
| Q188 | - |  |  | SI | Notifications: |
| Q189 | - |  |  | SI | Doctor to be notified if yes to above questions |
| Q19 | - |  |  | SI | Introduction to other patients |
| Q190 | - |  |  | SI | Referral considerations: |
| Q191 | - |  |  | SI | Dietician, Bariatric management plan |
| Q192 | - |  |  | SI | Swallowing |
| Q193 | - |  |  | SI | Reports difficulty in chewing / swallowing? |
| Q194 | - |  |  | SI | Does the patient cough / choke when eating / drink... |
| Q195 | - |  |  | SI | Swallowing notes |
| Q196 | - |  |  | SI | Referral considerations: |
| Q197 | - |  |  | SI | Speech pathology |
| Q198 | - |  |  | SI | Bowel and Bladder |
| Q199 | - |  |  | SI | Is patient toilet trained |
| Q20 | - |  |  | SI | Discharge time explained (10am) |
| Q200 | - |  |  | SI | Any concerns regarding urination? |
| Q201 | - |  |  | SI | Any bowel concerns? |
| Q202 | - |  |  | SI | Referral considerations: |
| Q203 | - |  |  | SI | Continence, stomal therapist |
| Q204 | - |  |  | SI | Developmental and Milestone Anomalies / Concerns |
| Q205 | - |  |  | SI | Details |
| Q206 | - |  |  | SI | Referral considerations: |
| Q207 | - |  |  | SI | Dummy Text |
| Q208 | - |  |  | SI | Please ensure alerts are updated as appropriate |
| Q209 | - |  |  | SI | Communication impairments |
| Q21 | - |  |  | SI | Smoking policy |
| Q210 | - |  |  | SI | Other communication impairment |
| Q211 | - |  |  | SI | Are the communications issues new or pre-existing |
| Q212 | - |  |  | SI | Communication assessment notes |
| Q213 | - |  |  | SI | Referral considerations: |
| Q214 | - |  |  | SI | Dummy Text |
| Q215 | - |  |  | SI | Visual aid |
| Q216 | - |  |  | SI | Hearing aid |
| Q217 | - |  |  | SI | Mobility aids |
| Q218 | - |  |  | SI | Other walking aid |
| Q219 | - |  |  | SI | Does patient have all required aids with them? |
| Q22 | - |  |  | SI | Plan of care discussed |
| Q220 | - |  |  | SI | Person requested to bring items in |
| Q221 | - |  |  | SI | Accommodation issues anticipated post discharge |
| Q222 | - |  |  | SI | Complex discharge planning notes |
| Q223 | - |  |  | SI | Antimicrobials |
| Q224 | - |  |  | SI | Potassium and other electrolytes |
| Q225 | - |  |  | SI | Insulin |
| Q226 | - |  |  | SI | Narcotics and other sedatives |
| Q227 | - |  |  | SI | Chemotherapeutic Agents |
| Q228 | - |  |  | SI | Heparin and other anticoagulants |
| Q23 | - |  |  | SI | Mutual help meeting explained |
| Q24 | - |  |  | SI | Buddy band provided and explained |
| Q25 | - |  |  | SI | Patient safe explained |
| Q26 | - |  |  | SI | Laundry location |
| Q27 | - |  |  | SI | Carer welcome pack provided |
| Q28 | - |  |  | SI | Ward phone numbers provided to next of kin (NOK) |
| Q29 | - |  |  | SI | Provide patient and family with information about ... |
| Q30 | - |  |  | SI | If yes to any please consider commencing complex d... |
| Q31 | - |  |  | SI | Frequent presenter |
| Q32 | - |  |  | SI | Homeless |
| Q33 | - |  |  | SI | Bariatric |
| Q34 | - |  |  | SI | Geriatric evaluation management (GEM) on acute |
| Q35 | - |  |  | SI | Discharge date and destination unclear |
| Q36 | - |  |  | SI | Unable to return home |
| Q37 | - |  |  | SI | Residential care required |
| Q38 | - |  |  | SI | Disability services required |
| Q39 | - |  |  | SI | One or more community services |
| Q40 | - |  |  | SI | Toilet / Bathroom - child / parents / parent facil... |
| Q41 | - |  |  | SI | Growth chart < 2 years |
| Q42 | - |  |  | SI | Ward security / monitoring |
| Q43 | - |  |  | SI | Satisfaction survey |
| Q44 | - |  |  | SI | Paediatric rosters |
| Q45 | - |  |  | SI | Milestones, Special Needs and Concerns |
| Q46 | - |  |  | SI | Developmental |
| Q47 | - |  |  | SI | Please specify |
| Q48 | - |  |  | SI | Physical |
| Q49 | - |  |  | SI | Please specify |
| Q50 | - |  |  | SI | Psychological |
| Q51 | - |  |  | SI | Please specify |
| Q52 | - |  |  | SI | Social |
| Q53 | - |  |  | SI | Please specify |
| Q54 | - |  |  | SI | Do you attend a maternal and child health nurse |
| Q55 | - |  |  | SI | Contact name |
| Q56 | - |  |  | SI | Contact number |
| Q57 | - |  |  | SI | Does the patient have a hearing impairment? |
| Q57ObsDR | - |  |  | SI | Does the patient have a hearing impairment? DR |
| Q58 | - |  |  | SI | Please specify |
| Q59 | - |  |  | SI | Does the patient have a vision impairment? |
| Q59ObsDR | - |  |  | SI | Does the patient have a vision impairment? DR |
| Q60 | - |  |  | SI | Please specify |
| Q61 | - |  |  | SI | Does the patient have a speech impairment? |
| Q61ObsDR | - |  |  | SI | Does the patient have a speech impairment? DR |
| Q62 | - |  |  | SI | Please specify |
| Q63 | - |  |  | SI | Glasses |
| Q63ObsDR | - |  |  | SI | Glasses DR |
| Q64 | - |  |  | SI | Non-slip footwear |
| Q65 | - |  |  | SI | Mobility aids |
| Q65ObsDR | - |  |  | SI | Mobility aids DR |
| Q66 | - |  |  | SI | Hearing aids |
| Q66ObsDR | - |  |  | SI | Hearing aids DR |
| Q67 | - |  |  | SI | Dentures |
| Q67ObsDR | - |  |  | SI | Dentures DR |
| Q68 | - |  |  | SI | If required, request family / friends to bring req... |
| Q69 | - |  |  | SI | Patient aid notes |
| Q70 | - |  |  | SI | Date requested |
| Q71 | - |  |  | SI | Indigenous status |
| Q72 | - |  |  | SI | Aboriginal liaison services referral required? |
| Q73 | - |  |  | SI | Is the patient identified as being culturally and ... |
| Q74 | - |  |  | SI | Preferred Language |
| Q75 | - |  |  | SI | Interpreter Required? |
| Q76 | - |  |  | SI | Does the patient have a case manager? |
| Q77 | - |  |  | SI | Case manager name |
| Q78 | - |  |  | SI | Case manager phone |
| Q79 | - |  |  | SI | Notify case management liaison coordinator of admi... |
| Q80 | - |  |  | SI | Does the patient have a support person / carer? |
| Q81 | - |  |  | SI | Notify carer of admission? |
| Q82 | - |  |  | SI | Does the patient live alone? |
| Q83 | - |  |  | SI | Name of person |
| Q84 | - |  |  | SI | Is patient a carer |
| Q85 | - |  |  | SI | Have arrangements been made? |
| Q86 | - |  |  | SI | Notify social worker (if concerned) |
| Q87 | - |  |  | SI | Post Acute Care (PAC)? |
| Q88 | - |  |  | SI | Transition Care Program (TCP)? |
| Q89 | - |  |  | SI | Current accommodation type |
| Q90 | - |  |  | SI | Is patient taking more than five (5) medications? |
| Q91 | - |  |  | SI | Have all medications been charted? |
| Q92 | - |  |  | SI | Does patient use a dosette or webster pack? |
| Q93 | - |  |  | SI | For pharmacy review |
| Q94 | - |  |  | SI | Name of local pharmacy |
| Q95 | - |  |  | SI | Does patient / carer understand current medication... |
| Q96 | - |  |  | SI | Does the patient have a history of dementia? |
| Q97 | - |  |  | SI | Social worker referral required? |
| Q98 | - |  |  | SI | Is patient at risk of wandering? |
| Q99 | - |  |  | SI | Occupational therapist referral required? |
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