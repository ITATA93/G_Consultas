# questionnaire.QTCAC

> Admission Checklist

**Schema:** questionnaire
**Columnas:** 275
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Admission Checklist

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | Type of admission |
| Q04 | varchar |  |  | SI | ID band updated |
| Q05 | varchar |  |  | SI | ID photograph |
| Q06 | varchar |  |  | SI | Has the patient been in any hospital in the past 1... |
| Q07 | varchar |  |  | SI | Readmission to hospital? |
| Q08 | varchar |  |  | SI | Is the child involved with the Department of Human... |
| Q09 | varchar |  |  | SI | Has DHS been notified of admission? |
| Q10 | date |  |  | SI | Date of notification |
| Q100 | varchar |  |  | SI | If the patient is aged 65 years or older or if Yes... |
| Q101 | varchar |  |  | SI | Is the patient confused? |
| Q102 | varchar |  |  | SI | Is the patient disorientated? |
| Q103 | varchar |  |  | SI | Does patient currently experience pain or discomfo... |
| Q104 | varchar |  |  | SI | Please complete pain assessment |
| Q105 | varchar |  |  | SI | Pain is |
| Q106 | varchar |  |  | SI | Provide full details when completing detailed pain... |
| Q107 | varchar |  |  | SI | On admission does the patient have any skin tears,... |
| Q108 | varchar |  |  | SI | Wound notes |
| Q109 | varchar |  |  | SI | Regardless of wound identified, Braden scale to be... |
| Q11 | varchar |  |  | SI | Provider |
| Q110 | varchar |  |  | SI | Has there been recent weight loss / decrease? |
| Q111 | varchar |  |  | SI | Any recent changes in sleep patterns, significant ... |
| Q112 | varchar |  |  | SI | Any recent mood or energy level changes? |
| Q113 | varchar |  |  | SI | Has the doctor been notified? |
| Q114 | varchar |  |  | SI | Referrals to Occupational Therapy or Physiotherapy... |
| Q115 | varchar |  |  | SI | Dentures |
| Q116 | varchar |  |  | SI | Any other new / pre-existing issues with communica... |
| Q117 | varchar |  |  | SI | Please specify |
| Q118 | varchar |  |  | SI | Does the patient have a hearing impairment? |
| Q118ObsDR | varchar |  | FK | SI | Does the patient have a hearing impairment? DR |
| Q119 | varchar |  |  | SI | Does the patient have a visual impairment? |
| Q119ObsDR | varchar |  | FK | SI | Does the patient have a visual impairment? DR |
| Q12 | varchar |  |  | SI | Services notified of admission |
| Q120 | varchar |  |  | SI | Infant protection device in situ? |
| Q121 | varchar |  |  | SI | Identification |
| Q122 | varchar |  |  | SI | Hospitalisation |
| Q123 | varchar |  |  | SI | Number of hospital admissions in last 12 months |
| Q124 | varchar |  |  | SI | Parents staying overnight |
| Q125 | varchar |  |  | SI | Has the parent signed general admission consent fo... |
| Q126 | varchar |  |  | SI | Hospitalisation notes |
| Q127 | varchar |  |  | SI | Immunisations |
| Q128 | varchar |  |  | SI | COVID vaccination status |
| Q129 | varchar |  |  | SI | Has vaccination certificate been sighted and scann... |
| Q13 | varchar |  |  | SI | Welcome information given and explained |
| Q130 | varchar |  |  | SI | Are all other immunisations up to date? |
| Q131 | varchar |  |  | SI | Immunisation notes |
| Q132 | varchar |  |  | SI | Culture and Language |
| Q133 | varchar |  |  | SI | Culture / Language notes |
| Q134 | varchar |  |  | SI | Referral considerations:  |
| Q135 | varchar |  |  | SI | Indigenous liaison  |
| Q136 | varchar |  |  | SI | Accommodation and Living Arrangements |
| Q137 | varchar |  |  | SI | Other accommodation type |
| Q138 | varchar |  |  | SI | Current parent / guardian living arrangements |
| Q139 | varchar |  |  | SI | Other arrangement |
| Q14 | varchar |  |  | SI | Patient rights and responsibilities booklet |
| Q140 | varchar |  |  | SI | Does the patient live alone? |
| Q141 | varchar |  |  | SI | Family / Friend care arrangements |
| Q142 | varchar |  |  | SI | Please use next section to document formal care se... |
| Q144 | varchar |  |  | SI | Accommodation / Living arrangement notes |
| Q145 | varchar |  |  | SI | Referral considerations: |
| Q146 | varchar |  |  | SI | Social worker  |
| Q147 | varchar |  |  | SI | Behavioural |
| Q148 | varchar |  |  | SI | Please ensure alerts are updated as appropriate |
| Q149 | varchar |  |  | SI | Is the patient at risk of suicide, self harm or ha... |
| Q15 | varchar |  |  | SI | Orientate to unit - bathroom / visiting times |
| Q150 | varchar |  |  | SI | Consider history of self-harm or current self harm... |
| Q151 | varchar |  |  | SI | Is the patient verbally or physically aggressive? |
| Q152 | varchar |  |  | SI | Behavioural notes |
| Q153 | varchar |  |  | SI | Referral considerations:  |
| Q154 | varchar |  |  | SI | Occupational therapist, Psych liaison |
| Q155 | varchar |  |  | SI | Mood, Stress and Sleep |
| Q156 | varchar |  |  | SI | Normal sleeping surface |
| Q157 | varchar |  |  | SI | Notifications: |
| Q158 | varchar |  |  | SI | Doctor to be notified if yes to above questions |
| Q159 | varchar |  |  | SI | Referral considerations:  |
| Q16 | varchar |  |  | SI | Use of nurse call |
| Q160 | varchar |  |  | SI | Dummy text |
| Q163 | varchar |  |  | SI | Hospital case management liaison coordinator |
| Q164 | varchar |  |  | SI | Orientation notes |
| Q165 | varchar |  |  | SI | Is the patient on any APINCH meds? |
| Q166 | varchar |  |  | SI | Does the patient use a dosette / webster pack? |
| Q167 | varchar |  |  | SI | Did patient bring medications with them? |
| Q168 | varchar |  |  | SI | Pharmacy review if more than five medications, on ... |
| Q169 | varchar |  |  | SI | Pain |
| Q17 | varchar |  |  | SI | Telephone location and use |
| Q170 | varchar |  |  | SI | Does the patient have any pain or discomfort? |
| Q171 | varchar |  |  | SI | Skin Integrity |
| Q172 | varchar |  |  | SI | Wounds identified on admission |
| Q173 | varchar |  |  | SI | Commence wound chart for each wound identified |
| Q174 | varchar |  |  | SI | Cognitive |
| Q175 | varchar |  |  | SI | Does the patient have a history of dementia? |
| Q176 | varchar |  |  | SI | Cognition notes |
| Q177 | varchar |  |  | SI | Referral considerations: |
| Q178 | varchar |  |  | SI | Social worker |
| Q179 | varchar |  |  | SI | Is patient at risk of wandering? |
| Q18 | varchar |  |  | SI | TV location and use |
| Q180 | varchar |  |  | SI | Referral considerations: |
| Q181 | varchar |  |  | SI | Mood / Stress / Sleep notes |
| Q182 | varchar |  |  | SI | Referral considerations: |
| Q183 | varchar |  |  | SI | Weight and Appetite |
| Q184 | varchar |  |  | SI | Complete Malnutrition Screen Tool |
| Q185 | varchar |  |  | SI | Does the patient have a significantly high or low ... |
| Q186 | varchar |  |  | SI | Is the patient >150kg or mobility / size may pose ... |
| Q187 | varchar |  |  | SI | Weight and appetite notes |
| Q188 | varchar |  |  | SI | Notifications: |
| Q189 | varchar |  |  | SI | Doctor to be notified if yes to above questions |
| Q19 | varchar |  |  | SI | Introduction to other patients |
| Q190 | varchar |  |  | SI | Referral considerations: |
| Q191 | varchar |  |  | SI | Dietician, Bariatric management plan |
| Q192 | varchar |  |  | SI | Swallowing |
| Q193 | varchar |  |  | SI | Reports difficulty in chewing / swallowing? |
| Q194 | varchar |  |  | SI | Does the patient cough / choke when eating / drink... |
| Q195 | varchar |  |  | SI | Swallowing notes |
| Q196 | varchar |  |  | SI | Referral considerations: |
| Q197 | varchar |  |  | SI | Speech pathology |
| Q198 | varchar |  |  | SI | Bowel and Bladder |
| Q199 | varchar |  |  | SI | Is patient toilet trained |
| Q20 | varchar |  |  | SI | Discharge time explained (10am) |
| Q200 | varchar |  |  | SI | Any concerns regarding urination? |
| Q201 | varchar |  |  | SI | Any bowel concerns? |
| Q202 | varchar |  |  | SI | Referral considerations: |
| Q203 | varchar |  |  | SI | Continence, stomal therapist |
| Q204 | varchar |  |  | SI | Developmental and Milestone Anomalies / Concerns |
| Q205 | varchar |  |  | SI | Details |
| Q206 | varchar |  |  | SI | Referral considerations: |
| Q207 | varchar |  |  | SI | Dummy Text |
| Q208 | varchar |  |  | SI | Please ensure alerts are updated as appropriate |
| Q209 | varchar |  |  | SI | Communication impairments |
| Q21 | varchar |  |  | SI | Smoking policy |
| Q210 | varchar |  |  | SI | Other communication impairment |
| Q211 | varchar |  |  | SI | Are the communications issues new or pre-existing |
| Q212 | varchar |  |  | SI | Communication assessment notes |
| Q213 | varchar |  |  | SI | Referral considerations: |
| Q214 | varchar |  |  | SI | Dummy Text |
| Q215 | varchar |  |  | SI | Visual aid |
| Q216 | varchar |  |  | SI | Hearing aid |
| Q217 | varchar |  |  | SI | Mobility aids |
| Q218 | varchar |  |  | SI | Other walking aid |
| Q219 | varchar |  |  | SI | Does patient have all required aids with them? |
| Q22 | varchar |  |  | SI | Plan of care discussed |
| Q220 | varchar |  |  | SI | Person requested to bring items in |
| Q221 | varchar |  |  | SI | Accommodation issues anticipated post discharge |
| Q222 | varchar |  |  | SI | Complex discharge planning notes |
| Q223 | varchar |  |  | SI | Antimicrobials |
| Q224 | varchar |  |  | SI | Potassium and other electrolytes |
| Q225 | varchar |  |  | SI | Insulin |
| Q226 | varchar |  |  | SI | Narcotics and other sedatives |
| Q227 | varchar |  |  | SI | Chemotherapeutic Agents |
| Q228 | varchar |  |  | SI | Heparin and other anticoagulants |
| Q23 | varchar |  |  | SI | Mutual help meeting explained |
| Q24 | varchar |  |  | SI | Buddy band provided and explained |
| Q25 | varchar |  |  | SI | Patient safe explained |
| Q26 | varchar |  |  | SI | Laundry location |
| Q27 | varchar |  |  | SI | Carer welcome pack provided |
| Q28 | varchar |  |  | SI | Ward phone numbers provided to next of kin (NOK) |
| Q29 | varchar |  |  | SI | Provide patient and family with information about ... |
| Q30 | varchar |  |  | SI | If yes to any please consider commencing complex d... |
| Q31 | varchar |  |  | SI | Frequent presenter |
| Q32 | varchar |  |  | SI | Homeless |
| Q33 | varchar |  |  | SI | Bariatric |
| Q34 | varchar |  |  | SI | Geriatric evaluation management (GEM) on acute |
| Q35 | varchar |  |  | SI | Discharge date and destination unclear |
| Q36 | varchar |  |  | SI | Unable to return home |
| Q37 | varchar |  |  | SI | Residential care required |
| Q38 | varchar |  |  | SI | Disability services required |
| Q39 | varchar |  |  | SI | One or more community services |
| Q40 | varchar |  |  | SI | Toilet / Bathroom - child / parents / parent facil... |
| Q41 | varchar |  |  | SI | Growth chart < 2 years |
| Q42 | varchar |  |  | SI | Ward security / monitoring |
| Q43 | varchar |  |  | SI | Satisfaction survey |
| Q44 | varchar |  |  | SI | Paediatric rosters |
| Q45 | varchar |  |  | SI | Milestones, Special Needs and Concerns |
| Q46 | varchar |  |  | SI | Developmental |
| Q47 | varchar |  |  | SI | Please specify |
| Q48 | varchar |  |  | SI | Physical |
| Q49 | varchar |  |  | SI | Please specify |
| Q50 | varchar |  |  | SI | Psychological |
| Q51 | varchar |  |  | SI | Please specify |
| Q52 | varchar |  |  | SI | Social |
| Q53 | varchar |  |  | SI | Please specify |
| Q54 | varchar |  |  | SI | Do you attend a maternal and child health nurse |
| Q55 | varchar |  |  | SI | Contact name |
| Q56 | numeric |  |  | SI | Contact number |
| Q57 | varchar |  |  | SI | Does the patient have a hearing impairment? |
| Q57ObsDR | varchar |  | FK | SI | Does the patient have a hearing impairment? DR |
| Q58 | varchar |  |  | SI | Please specify |
| Q59 | varchar |  |  | SI | Does the patient have a vision impairment? |
| Q59ObsDR | varchar |  | FK | SI | Does the patient have a vision impairment? DR |
| Q60 | varchar |  |  | SI | Please specify |
| Q61 | varchar |  |  | SI | Does the patient have a speech impairment? |
| Q61ObsDR | varchar |  | FK | SI | Does the patient have a speech impairment? DR |
| Q62 | varchar |  |  | SI | Please specify |
| Q63 | varchar |  |  | SI | Glasses |
| Q63ObsDR | varchar |  | FK | SI | Glasses DR |
| Q64 | varchar |  |  | SI | Non-slip footwear |
| Q65 | varchar |  |  | SI | Mobility aids |
| Q65ObsDR | varchar |  | FK | SI | Mobility aids DR |
| Q66 | varchar |  |  | SI | Hearing aids |
| Q66ObsDR | varchar |  | FK | SI | Hearing aids DR |
| Q67 | varchar |  |  | SI | Dentures |
| Q67ObsDR | varchar |  | FK | SI | Dentures DR |
| Q68 | varchar |  |  | SI | If required, request family / friends to bring req... |
| Q69 | varchar |  |  | SI | Patient aid notes |
| Q70 | date |  |  | SI | Date requested |
| Q71 | varchar |  |  | SI | Indigenous status |
| Q72 | varchar |  |  | SI | Aboriginal liaison services referral required? |
| Q73 | varchar |  |  | SI | Is the patient identified as being culturally and ... |
| Q74 | varchar |  |  | SI | Preferred Language |
| Q75 | varchar |  |  | SI | Interpreter Required? |
| Q76 | varchar |  |  | SI | Does the patient have a case manager? |
| Q77 | varchar |  |  | SI | Case manager name |
| Q78 | varchar |  |  | SI | Case manager phone |
| Q79 | varchar |  |  | SI | Notify case management liaison coordinator of admi... |
| Q80 | varchar |  |  | SI | Does the patient have a support person / carer? |
| Q81 | varchar |  |  | SI | Notify carer of admission? |
| Q82 | varchar |  |  | SI | Does the patient live alone? |
| Q83 | varchar |  |  | SI | Name of person |
| Q84 | varchar |  |  | SI | Is patient a carer |
| Q85 | varchar |  |  | SI | Have arrangements been made? |
| Q86 | varchar |  |  | SI | Notify social worker (if concerned) |
| Q87 | varchar |  |  | SI | Post Acute Care (PAC)? |
| Q88 | varchar |  |  | SI | Transition Care Program (TCP)? |
| Q89 | varchar |  |  | SI | Current accommodation type |
| Q90 | varchar |  |  | SI | Is patient taking more than five (5) medications? |
| Q91 | varchar |  |  | SI | Have all medications been charted? |
| Q92 | varchar |  |  | SI | Does patient use a dosette or webster pack? |
| Q93 | varchar |  |  | SI | For pharmacy review |
| Q94 | varchar |  |  | SI | Name of local pharmacy |
| Q95 | varchar |  |  | SI | Does patient / carer understand current medication... |
| Q96 | varchar |  |  | SI | Does the patient have a history of dementia? |
| Q97 | varchar |  |  | SI | Social worker referral required? |
| Q98 | varchar |  |  | SI | Is patient at risk of wandering? |
| Q99 | varchar |  |  | SI | Occupational therapist referral required? |
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