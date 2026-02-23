# questionnaire.QGXXXMAN

> Antenatal Booking

**Schema:** questionnaire
**Columnas:** 386
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Antenatal Booking

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Height |
| Q01ObsDR | varchar |  | FK | SI | Height DR |
| Q02 | varchar |  |  | SI | Weight |
| Q02ObsDR | varchar |  | FK | SI | Weight DR |
| Q03 | varchar |  |  | SI | BMI |
| Q04 | varchar |  |  | SI | Have you taken folic acid |
| Q04ObsDR | varchar |  | FK | SI | Have you taken folic acid DR |
| Q05 | varchar |  |  | SI | Folic acid dose |
| Q05ObsDR | varchar |  | FK | SI | Folic acid dose DR |
| Q06 | varchar |  |  | SI | Have you ever injected street drugs |
| Q06ObsDR | varchar |  | FK | SI | Have you ever injected street drugs DR |
| Q07 | varchar |  |  | SI | Prescribed / over the counter drugs |
| Q08 | varchar |  |  | SI | Oral drug misuse (inc Dispensing) |
| Q09 | varchar |  |  | SI | Other intravenous drug use |
| Q100 | varchar |  |  | SI | Consent for follow-up |
| Q100ObsDR | varchar |  | FK | SI | Consent for follow-up DR |
| Q101 | date |  |  | SI | Next smear due |
| Q102 | varchar |  |  | SI | Over the counter preperations or medications not p... |
| Q103 | varchar |  |  | SI | Thrombosis risk |
| Q103ObsDR | varchar |  | FK | SI | Thrombosis risk DR |
| Q104 | varchar |  |  | SI | Have you ever had a cervical smear |
| Q104ObsDR | varchar |  | FK | SI | Have you ever had a cervical smear DR |
| Q105 | date |  |  | SI | Date of smear |
| Q106 | varchar |  |  | SI | Special dietary needs |
| Q107 | varchar |  |  | SI | Mental health team |
| Q108 | varchar |  |  | SI | Heath and Safety risks at work |
| Q109 | varchar |  |  | SI | Religious and cultural comments |
| Q110 | varchar |  |  | SI | female circumcision comments |
| Q111 | varchar |  |  | SI | Blood transfusion acceptable comments |
| Q112 | varchar |  |  | SI | Other information booklets given |
| Q113 | varchar |  |  | SI | Outcome of referrals |
| Q114 | varchar |  |  | SI | Other involved workers |
| Q115 | bit |  |  | SI | Previous history |
| Q116 | bit |  |  | SI | BMI >30 |
| Q117 | bit |  |  | SI | Age >30 |
| Q118 | bit |  |  | SI | Parity >4 |
| Q119 | varchar |  |  | SI | Other |
| Q12 | varchar |  |  | SI | Units of alcohol per week |
| Q120 | varchar |  |  | SI | TB comments |
| Q121 | varchar |  |  | SI | Prescribed Medications - current or recently stopp... |
| Q122 | varchar |  |  | SI | Comments including Colposcopy referral / treatment |
| Q123 | varchar |  |  | SI | Maximum units per day before pregnancy |
| Q123ObsDR | varchar |  | FK | SI | Maximum units per day before pregnancy DR |
| Q124 | varchar |  |  | SI | Maximum units per week before pregnancy confirmed |
| Q124ObsDR | varchar |  | FK | SI | Maximum units per week before pregnancy confirmed ... |
| Q125 | varchar |  |  | SI | Alcohol risks discussed |
| Q125ObsDR | varchar |  | FK | SI | Alcohol risks discussed DR |
| Q126 | varchar |  |  | SI | Has difficulty understanding English |
| Q126ObsDR | varchar |  | FK | SI | Has difficulty understanding English DR |
| Q127 | varchar |  |  | SI | Needs help completing forms |
| Q127ObsDR | varchar |  | FK | SI | Needs help completing forms DR |
| Q128 | varchar |  |  | SI | Employment status |
| Q129 | numeric |  |  | SI | Years in education |
| Q12ObsDR | varchar |  | FK | SI | Units of alcohol per week DR |
| Q13 | varchar |  |  | SI | Smoking |
| Q130 | varchar |  |  | SI | Assistance required |
| Q130ObsDR | varchar |  | FK | SI | Assistance required DR |
| Q131 | varchar |  |  | SI | Do you speak English |
| Q131ObsDR | varchar |  | FK | SI | Do you speak English DR |
| Q132 | varchar |  |  | SI | Your preferred language |
| Q133 | varchar |  |  | SI | Interpreter |
| Q135P | varchar |  |  | SI | First name |
| Q136 | varchar |  |  | SI | Address (if different) |
| Q137 | varchar |  |  | SI | Surname |
| Q138 | varchar |  |  | SI | Postcode |
| Q13ObsDR | varchar |  | FK | SI | Smoking DR |
| Q14 | varchar |  |  | SI | Is blood transfusion acceptable to you |
| Q140 | date |  |  | SI | Date of birth |
| Q141 | numeric |  |  | SI | Telephone  |
| Q142 | varchar |  |  | SI | Employed |
| Q143 | varchar |  |  | SI | Admission to ITU/HDU |
| Q143ObsDR | varchar |  | FK | SI | Admission to ITU/HDU DR |
| Q143P | varchar |  |  | SI | Occupation |
| Q144 | varchar |  |  | SI | Admission to ED |
| Q144ObsDR | varchar |  | FK | SI | Admission to ED DR |
| Q145 | varchar |  |  | SI | Anaesthetic problems |
| Q145ObsDR | varchar |  | FK | SI | Anaesthetic problems DR |
| Q146 | varchar |  |  | SI | Allergies |
| Q146ObsDR | varchar |  | FK | SI | Allergies DR |
| Q147 | varchar |  |  | SI | Autoimmune disease |
| Q147ObsDR | varchar |  | FK | SI | Autoimmune disease DR |
| Q148 | varchar |  |  | SI | Back problems |
| Q148ObsDR | varchar |  | FK | SI | Back problems DR |
| Q149 | varchar |  |  | SI | Blood / clotting disorder |
| Q149ObsDR | varchar |  | FK | SI | Blood / clotting disorder DR |
| Q14ObsDR | varchar |  | FK | SI | Is blood transfusion acceptable to you DR |
| Q15 | varchar |  |  | SI | Attended infertility clinic |
| Q150 | varchar |  |  | SI | Blood transfusions |
| Q150ObsDR | varchar |  | FK | SI | Blood transfusions DR |
| Q151 | varchar |  |  | SI | Cancer |
| Q151ObsDR | varchar |  | FK | SI | Cancer DR |
| Q152 | varchar |  |  | SI | Cardiac problems |
| Q152ObsDR | varchar |  | FK | SI | Cardiac problems DR |
| Q153 | varchar |  |  | SI | Cervical smear |
| Q153ObsDR | varchar |  | FK | SI | Cervical smear DR |
| Q154 | varchar |  |  | SI | Diabetes |
| Q154ObsDR | varchar |  | FK | SI | Diabetes DR |
| Q155 | varchar |  |  | SI | Epilepsy / neurological problems |
| Q155ObsDR | varchar |  | FK | SI | Epilepsy / neurological problems DR |
| Q156 | varchar |  |  | SI | Exposure to toxic substances |
| Q156ObsDR | varchar |  | FK | SI | Exposure to toxic substances DR |
| Q157 | varchar |  |  | SI | Fertility problems (this pregnancy) |
| Q157ObsDR | varchar |  | FK | SI | Fertility problems (this pregnancy) DR |
| Q158 | varchar |  |  | SI | Female circumcision |
| Q158ObsDR | varchar |  | FK | SI | Female circumcision DR |
| Q159 | varchar |  |  | SI | Gastro-intestinal problems |
| Q159ObsDR | varchar |  | FK | SI | Gastro-intestinal problems DR |
| Q15ObsDR | varchar |  | FK | SI | Attended infertility clinic DR |
| Q16 | varchar |  |  | SI | Current smoker |
| Q160 | varchar |  |  | SI | Genetic / inherited problems |
| Q160ObsDR | varchar |  | FK | SI | Genetic / inherited problems DR |
| Q162 | varchar |  |  | SI | Genital infections |
| Q162ObsDR | varchar |  | FK | SI | Genital infections DR |
| Q163 | varchar |  |  | SI | Gynae histoty / operations (excluding caesarean) |
| Q163ObsDR | varchar |  | FK | SI | Gynae histoty / operations (excluding caesarean) D... |
| Q164 | varchar |  |  | SI | High blood pressure |
| Q164ObsDR | varchar |  | FK | SI | High blood pressure DR |
| Q165 | varchar |  |  | SI | Incontinence |
| Q165ObsDR | varchar |  | FK | SI | Incontinence DR |
| Q166 | varchar |  |  | SI | Infections |
| Q166ObsDR | varchar |  | FK | SI | Infections DR |
| Q167 | varchar |  |  | SI | Liver disease including hepatitis |
| Q167ObsDR | varchar |  | FK | SI | Liver disease including hepatitis DR |
| Q168 | varchar |  |  | SI | Migraine or severe headache |
| Q168ObsDR | varchar |  | FK | SI | Migraine or severe headache DR |
| Q169 | varchar |  |  | SI | Musculo-skeletal problems |
| Q169ObsDR | varchar |  | FK | SI | Musculo-skeletal problems DR |
| Q16ObsDR | varchar |  | FK | SI | Current smoker DR |
| Q17 | varchar |  |  | SI | Number per day |
| Q170 | varchar |  |  | SI | Operations |
| Q170ObsDR | varchar |  | FK | SI | Operations DR |
| Q171 | varchar |  |  | SI | Pelvic injury |
| Q171ObsDR | varchar |  | FK | SI | Pelvic injury DR |
| Q172 | varchar |  |  | SI | Renal disease |
| Q172ObsDR | varchar |  | FK | SI | Renal disease DR |
| Q173 | varchar |  |  | SI | Respiratory diease |
| Q173ObsDR | varchar |  | FK | SI | Respiratory diease DR |
| Q174 | varchar |  |  | SI | TB exposure |
| Q174ObsDR | varchar |  | FK | SI | TB exposure DR |
| Q175 | varchar |  |  | SI | Thrombosis |
| Q175ObsDR | varchar |  | FK | SI | Thrombosis DR |
| Q176 | varchar |  |  | SI | Thyroid / endocrine problems |
| Q176ObsDR | varchar |  | FK | SI | Thyroid / endocrine problems DR |
| Q177 | varchar |  |  | SI | Medication in last 6 months |
| Q177ObsDR | varchar |  | FK | SI | Medication in last 6 months DR |
| Q178 | varchar |  |  | SI | Vaginal bleeding in this pregnancy |
| Q178ObsDR | varchar |  | FK | SI | Vaginal bleeding in this pregnancy DR |
| Q179 | varchar |  |  | SI | Other (provide details) |
| Q179ObsDR | varchar |  | FK | SI | Other (provide details) DR |
| Q17ObsDR | varchar |  | FK | SI | Number per day DR |
| Q18 | varchar |  |  | SI | Risks explained |
| Q180 | varchar |  |  | SI | Diabetes |
| Q180ObsDR | varchar |  | FK | SI | Diabetes DR |
| Q181 | varchar |  |  | SI | Type |
| Q181ObsDR | varchar |  | FK | SI | Type DR |
| Q182 | varchar |  |  | SI | Thrombisis |
| Q182ObsDR | varchar |  | FK | SI | Thrombisis DR |
| Q183 | varchar |  |  | SI | High blood pressure / eclampsia |
| Q183ObsDR | varchar |  | FK | SI | High blood pressure / eclampsia DR |
| Q184 | varchar |  |  | SI | Hip problems at birth |
| Q184ObsDR | varchar |  | FK | SI | Hip problems at birth DR |
| Q185 | varchar |  |  | SI | Is your partner the baby's father |
| Q185ObsDR | varchar |  | FK | SI | Is your partner the baby's father DR |
| Q186 | varchar |  |  | SI | Is the baby's father a blood relation |
| Q186D | varchar |  |  | SI | Details |
| Q186ObsDR | varchar |  | FK | SI | Is the baby's father a blood relation DR |
| Q187 | varchar |  |  | SI | Previous treatment / in-patient care |
| Q187ObsDR | varchar |  | FK | SI | Previous treatment / in-patient care DR |
| Q188 | varchar |  |  | SI | Family history |
| Q188ObsDR | varchar |  | FK | SI | Family history DR |
| Q189 | varchar |  |  | SI | Does your partner have any history |
| Q189ObsDR | varchar |  | FK | SI | Does your partner have any history DR |
| Q18ObsDR | varchar |  | FK | SI | Risks explained DR |
| Q19 | varchar |  |  | SI | Advice on how to stop |
| Q190 | varchar |  |  | SI | Feeling down, depressed or hopeless |
| Q190ObsDR | varchar |  | FK | SI | Feeling down, depressed or hopeless DR |
| Q191 | varchar |  |  | SI | Having little interest or pleasure in doing things |
| Q191ObsDR | varchar |  | FK | SI | Having little interest or pleasure in doing things... |
| Q192 | varchar |  |  | SI | Worrying or feeling anxious |
| Q192ObsDR | varchar |  | FK | SI | Worrying or feeling anxious DR |
| Q193 | varchar |  |  | SI | Do you feel you need or want help |
| Q193ObsDR | varchar |  | FK | SI | Do you feel you need or want help DR |
| Q194 | varchar |  |  | SI | Referral required |
| Q194ObsDR | varchar |  | FK | SI | Referral required DR |
| Q195 | varchar |  |  | SI | A disease that runs in your family |
| Q195ObsDR | varchar |  | FK | SI | A disease that runs in your family DR |
| Q196 | varchar |  |  | SI | A disease that runs in your baby's fathers family |
| Q196ObsDR | varchar |  | FK | SI | A disease that runs in your baby's fathers family ... |
| Q197 | varchar |  |  | SI | Need for genetic counselling in your family |
| Q197ObsDR | varchar |  | FK | SI | Need for genetic counselling in your family DR |
| Q198 | varchar |  |  | SI | Need for genetic counselling in your baby's  |
| Q198ObsDR | varchar |  | FK | SI | Need for genetic counselling in your baby's  DR |
| Q199 | varchar |  |  | SI | Stillbirths or multiple miscarriages in your famil... |
| Q199ObsDR | varchar |  | FK | SI | Stillbirths or multiple miscarriages in your famil... |
| Q19ObsDR | varchar |  | FK | SI | Advice on how to stop DR |
| Q20 | varchar |  |  | SI | Referral to smoking cessation |
| Q200 | varchar |  |  | SI | Stillbirths or multiple miscarriages in baby's fat... |
| Q200ObsDR | varchar |  | FK | SI | Stillbirths or multiple miscarriages in baby's fat... |
| Q201 | varchar |  |  | SI | Sudden infant death in your family |
| Q201ObsDR | varchar |  | FK | SI | Sudden infant death in your family DR |
| Q202 | varchar |  |  | SI | Sudden infant death in baby's fathers family |
| Q202ObsDR | varchar |  | FK | SI | Sudden infant death in baby's fathers family DR |
| Q203 | varchar |  |  | SI | Leaning difficulties in your family |
| Q203ObsDR | varchar |  | FK | SI | Leaning difficulties in your family DR |
| Q204 | varchar |  |  | SI | Learning difficulties in baby's fathers family |
| Q204ObsDR | varchar |  | FK | SI | Learning difficulties in baby's fathers family DR |
| Q205 | varchar |  |  | SI | Hearing loss from childhood in your family |
| Q205ObsDR | varchar |  | FK | SI | Hearing loss from childhood in your family DR |
| Q206 | varchar |  |  | SI | Hearing loss from childhood in baby's fathers fami... |
| Q206MH | varchar |  |  | SI | Details |
| Q206ObsDR | varchar |  | FK | SI | Hearing loss from childhood in baby's fathers fami... |
| Q207 | varchar |  |  | SI | Details |
| Q207FH | varchar |  |  | SI | Details |
| Q208 | varchar |  |  | SI | Past or present mental illness |
| Q208ObsDR | varchar |  | FK | SI | Past or present mental illness DR |
| Q20ObsDR | varchar |  | FK | SI | Referral to smoking cessation DR |
| Q21 | varchar |  |  | SI | Exposed to cigarette smoke at home |
| Q211 | varchar |  |  | SI | Housing |
| Q211ObsDR | varchar |  | FK | SI | Housing DR |
| Q21ObsDR | varchar |  | FK | SI | Exposed to cigarette smoke at home DR |
| Q22 | date |  |  | SI | Date stopped smoking |
| Q23 | varchar |  |  | SI | Physical disabilities |
| Q23ObsDR | varchar |  | FK | SI | Physical disabilities DR |
| Q24 | varchar |  |  | SI | Any support needs |
| Q24ObsDR | varchar |  | FK | SI | Any support needs DR |
| Q25 | varchar |  |  | SI | Any learning disabilities |
| Q25ObsDR | varchar |  | FK | SI | Any learning disabilities DR |
| Q26 | varchar |  |  | SI | Are you still at school |
| Q26ObsDR | varchar |  | FK | SI | Are you still at school DR |
| Q27 | varchar |  |  | SI | Living in looked after care services |
| Q27ObsDR | varchar |  | FK | SI | Living in looked after care services DR |
| Q28 | varchar |  |  | SI | Do you have support through this pregnancy |
| Q28ObsDR | varchar |  | FK | SI | Do you have support through this pregnancy DR |
| Q29 | varchar |  |  | SI | Are you in temporary housing |
| Q29ObsDR | varchar |  | FK | SI | Are you in temporary housing DR |
| Q30 | varchar |  |  | SI | Need advice on financial or housing issues |
| Q30ObsDR | varchar |  | FK | SI | Need advice on financial or housing issues DR |
| Q31 | varchar |  |  | SI | Do your other children live with you |
| Q31ObsDR | varchar |  | FK | SI | Do your other children live with you DR |
| Q32 | varchar |  |  | SI | Who looks after them |
| Q33 | varchar |  |  | SI | Ever needed social work assistance |
| Q33ObsDR | varchar |  | FK | SI | Ever needed social work assistance DR |
| Q34 | varchar |  |  | SI | Any difficulty reading / writing English |
| Q34ObsDR | varchar |  | FK | SI | Any difficulty reading / writing English DR |
| Q35 | varchar |  |  | SI | Needs help understanding pregnancy notes |
| Q35ObsDR | varchar |  | FK | SI | Needs help understanding pregnancy notes DR |
| Q36 | varchar |  |  | SI | Social work contact details |
| Q37 | varchar |  |  | SI | Infant feeding checklist |
| Q38 | varchar |  |  | SI | Do you visit the dentist regularly |
| Q38ObsDR | varchar |  | FK | SI | Do you visit the dentist regularly DR |
| Q39 | varchar |  |  | SI | Smear normal |
| Q39ObsDR | varchar |  | FK | SI | Smear normal DR |
| Q40 | varchar |  |  | SI | Refugee or asylum seeker |
| Q40ObsDR | varchar |  | FK | SI | Refugee or asylum seeker DR |
| Q41 | varchar |  |  | SI | Smear abnormal |
| Q42 | varchar |  |  | SI | TB risk |
| Q42ObsDR | varchar |  | FK | SI | TB risk DR |
| Q43 | varchar |  |  | SI | Parent or Grandparent born in high prevalence area |
| Q43ObsDR | varchar |  | FK | SI | Parent or Grandparent born in high prevalence area... |
| Q44 | varchar |  |  | SI | Family member with TB in last 5 yrs |
| Q44ObsDR | varchar |  | FK | SI | Family member with TB in last 5 yrs DR |
| Q45 | varchar |  |  | SI | Is family member likely to live for >1month in a h... |
| Q45ObsDR | varchar |  | FK | SI | Is family member likely to live for >1month in a h... |
| Q46 | varchar |  |  | SI | Has either parent moved from a high prevalence are... |
| Q46ObsDR | varchar |  | FK | SI | Has either parent moved from a high prevalence are... |
| Q47 | varchar |  |  | SI | Baby requires BCG |
| Q47ObsDR | varchar |  | FK | SI | Baby requires BCG DR |
| Q48 | varchar |  |  | SI | Previous difficult intubation |
| Q48ObsDR | varchar |  | FK | SI | Previous difficult intubation DR |
| Q49 | varchar |  |  | SI | Have you ever had general anaesthetic |
| Q49ObsDR | varchar |  | FK | SI | Have you ever had general anaesthetic DR |
| Q50 | varchar |  |  | SI | Sensitivity to anaesthetic drugs |
| Q50ObsDR | varchar |  | FK | SI | Sensitivity to anaesthetic drugs DR |
| Q51 | varchar |  |  | SI | Family / personal history of Suxamethonium apnoea ... |
| Q51ObsDR | varchar |  | FK | SI | Family / personal history of Suxamethonium apnoea ... |
| Q52 | varchar |  |  | SI | Abnormal spinal, neck or facial anatomy |
| Q52ObsDR | varchar |  | FK | SI | Abnormal spinal, neck or facial anatomy DR |
| Q53 | varchar |  |  | SI | Weight >120kg |
| Q53ObsDR | varchar |  | FK | SI | Weight >120kg DR |
| Q54 | varchar |  |  | SI | Leaflets given |
| Q54ObsDR | varchar |  | FK | SI | Leaflets given DR |
| Q55 | bit |  |  | SI | Your baby your choice |
| Q56 | bit |  |  | SI | Breast feeding discussed / charter |
| Q57 | bit |  |  | SI | Smoking - what happens when smoking during pregnan... |
| Q58 | bit |  |  | SI | FW8 maternity excemption form |
| Q59 | bit |  |  | SI | Mat B1 |
| Q60 | bit |  |  | SI | Guide to maternity benefits |
| Q61 | bit |  |  | SI | Pregnancy and work |
| Q62 | bit |  |  | SI | Information on wearing a car seat belt |
| Q63 | bit |  |  | SI | Routine blood tests including HIV |
| Q64 | bit |  |  | SI | Spina bifida and Downs screening |
| Q65 | bit |  |  | SI | Other screening |
| Q66 | bit |  |  | SI | Reduce the risk of cot death |
| Q67 | bit |  |  | SI | Off to a good start, all you need to know about BF |
| Q68 | bit |  |  | SI | BF and returning to work |
| Q69 | bit |  |  | SI | Parents guide to newborn blood spot testing |
| Q70 | bit |  |  | SI | Your baby's hering screen |
| Q71 | bit |  |  | SI | Hospital information |
| Q72 | bit |  |  | SI | BCG and your baby |
| Q73 | bit |  |  | SI | Talking about Postnatal depression |
| Q74 | bit |  |  | SI | HEBS leaflet |
| Q75 | bit |  |  | SI | Vitimin K information |
| Q76 | bit |  |  | SI | Folic acid supplements |
| Q77 | varchar |  |  | SI | Are you affected by domestic abuse |
| Q77ObsDR | varchar |  | FK | SI | Are you affected by domestic abuse DR |
| Q78 | varchar |  |  | SI | Referred to Alcohol Problem service |
| Q78ObsDR | varchar |  | FK | SI | Referred to Alcohol Problem service DR |
| Q79 | varchar |  |  | SI | Referral for advice on reducing drinking |
| Q79ObsDR | varchar |  | FK | SI | Referral for advice on reducing drinking DR |
| Q80 | varchar |  |  | SI | How many units of alcohol a week are you drinking ... |
| Q80ObsDR | varchar |  | FK | SI | How many units of alcohol a week are you drinking ... |
| Q81 | varchar |  |  | SI | Pattern of alcohol use |
| Q81ObsDR | varchar |  | FK | SI | Pattern of alcohol use DR |
| Q82 | varchar |  |  | SI | Blood Group +Rh |
| Q82ObsDR | varchar |  | FK | SI | Blood Group +Rh DR |
| Q83 | varchar |  |  | SI | Female circumcision |
| Q83ObsDR | varchar |  | FK | SI | Female circumcision DR |
| Q84 | varchar |  |  | SI | Comments |
| Q85 | varchar |  |  | SI | Interested in parent education classes |
| Q85ObsDR | varchar |  | FK | SI | Interested in parent education classes DR |
| Q86 | varchar |  |  | SI | Ever injected illicit drugs |
| Q86ObsDR | varchar |  | FK | SI | Ever injected illicit drugs DR |
| Q87 | bit |  |  | SI | Ready steady baby |
| Q88 | varchar |  |  | SI | Most often used street drug |
| Q88ObsDR | varchar |  | FK | SI | Most often used street drug DR |
| Q89 | varchar |  |  | SI | Have you used oral street drugs |
| Q89ObsDR | varchar |  | FK | SI | Have you used oral street drugs DR |
| Q90 | varchar |  |  | SI | Have you ever use street drugs |
| Q90ObsDR | varchar |  | FK | SI | Have you ever use street drugs DR |
| Q91 | varchar |  |  | SI | Midwife countersigning |
| Q92 | varchar |  |  | SI | Occupation |
| Q93 | varchar |  |  | SI | Health and Safety discussed |
| Q93ObsDR | varchar |  | FK | SI | Health and Safety discussed DR |
| Q94 | varchar |  |  | SI | Diet discussed |
| Q94ObsDR | varchar |  | FK | SI | Diet discussed DR |
| Q95 | varchar |  |  | SI | Units of alcohol per week before pregnancy |
| Q95ObsDR | varchar |  | FK | SI | Units of alcohol per week before pregnancy DR |
| Q96 | varchar |  |  | SI | Maximum daily units - currently |
| Q96ObsDR | varchar |  | FK | SI | Maximum daily units - currently DR |
| Q97 | varchar |  |  | SI | Alcohol risks discussed |
| Q97ObsDR | varchar |  | FK | SI | Alcohol risks discussed DR |
| Q98 | varchar |  |  | SI | Offer patient a brief intervention if pregnant and... |
| Q98ObsDR | varchar |  | FK | SI | Offer patient a brief intervention if pregnant and... |
| Q99 | varchar |  |  | SI | Brief intervention offered |
| Q99ObsDR | varchar |  | FK | SI | Brief intervention offered DR |
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