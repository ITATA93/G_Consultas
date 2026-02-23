# questionnaire.QTCICF

> International classification of functioning, disability and health (ICF) checklist

**Schema:** questionnaire
**Columnas:** 336
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* International classification of functioning, disability and health (ICF) checklist

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | Short List of Body Functions |
| Q04 | varchar |  |  | SI | Qualifier ''Extent of Impairments'' |
| Q05 | varchar |  |  | SI | b1. |
| Q06 | varchar |  |  | SI | Mental functions |
| Q07 | varchar |  |  | SI | b110 Consciousness |
| Q08 | varchar |  |  | SI | b114 Orientation (time, place, person) |
| Q09 | varchar |  |  | SI | b117 Intellectual (incl. Retardation, dementia) |
| Q10 | varchar |  |  | SI | b130 Energy and drive functions |
| Q100 | varchar |  |  | SI | Any other body structures |
| Q101 | varchar |  |  | SI | Short list of A&P domains |
| Q102 | varchar |  |  | SI | Performance qualifier ''Extent of participation re... |
| Q103 | varchar |  |  | SI | Capacity qualifier ''Extent of activity limitation... |
| Q104 | varchar |  |  | SI | d1. |
| Q105 | varchar |  |  | SI | Learning and applying knowledge |
| Q106 | varchar |  |  | SI | d110 Watching |
| Q107 | varchar |  |  | SI | d110 Sq-Watching |
| Q108 | varchar |  |  | SI | d115 Listening |
| Q109 | varchar |  |  | SI | d115 Sq-Listening |
| Q11 | varchar |  |  | SI | b134 Sleep |
| Q110 | varchar |  |  | SI | d140 Learning to read |
| Q111 | varchar |  |  | SI | d140 Sq-Learning to read |
| Q112 | varchar |  |  | SI | d145 Learning to write |
| Q113 | varchar |  |  | SI | d145 Sq-Learning to write |
| Q114 | varchar |  |  | SI | d150 Learning to calculate (arithmetic) |
| Q115 | varchar |  |  | SI | d150 Sq-Learning to calculate (arithmetic) |
| Q116 | varchar |  |  | SI | d175 Solving problems |
| Q117 | varchar |  |  | SI | d175 Sq-Solving problems |
| Q118 | varchar |  |  | SI | d2. |
| Q119 | varchar |  |  | SI | d210 Undertaking a single task |
| Q12 | varchar |  |  | SI | b140 Attention |
| Q120 | varchar |  |  | SI | d210 Sq-Undertaking a single task |
| Q121 | varchar |  |  | SI | d220 Undertaking multiple tasks |
| Q122 | varchar |  |  | SI | d220 Sq-Undertaking multiple tasks |
| Q123 | varchar |  |  | SI | d3. |
| Q124 | varchar |  |  | SI | Communication |
| Q125 | varchar |  |  | SI | d310 Communicating with -- receiving -- spoken mes... |
| Q126 | varchar |  |  | SI | d310 Communicating |
| Q127 | varchar |  |  | SI | d315 Communicating with -- receiving -- non-verbal... |
| Q128 | varchar |  |  | SI | d315 Sq-Communicating with -- receiving -- non-ver... |
| Q129 | varchar |  |  | SI | d330 Speaking |
| Q13 | varchar |  |  | SI | b144 Memory |
| Q130 | varchar |  |  | SI | d330 Sq-Speaking |
| Q131 | varchar |  |  | SI | d335 Producing non-verbal messages |
| Q132 | varchar |  |  | SI | d335 Sq-Producing non-verbal messages |
| Q133 | varchar |  |  | SI | d350 Conversation |
| Q134 | varchar |  |  | SI | d350 Sq-Conversation |
| Q135 | varchar |  |  | SI | d4. |
| Q136 | varchar |  |  | SI | Mobility |
| Q137 | varchar |  |  | SI | d430 Lifting and carrying objects |
| Q138 | varchar |  |  | SI | d430 Sq-Lifting and carrying objects |
| Q139 | varchar |  |  | SI | d440 Fine hand use (picking up, grasping) |
| Q14 | varchar |  |  | SI | b152 Emotional functions |
| Q140 | varchar |  |  | SI | d440 Sq-Fine hand use (picking up, grasping) |
| Q141 | varchar |  |  | SI | d450 Walking |
| Q142 | varchar |  |  | SI | d450 Sq-Walking |
| Q143 | varchar |  |  | SI | d465 Moving around using equipment (wheelchair, sk... |
| Q144 | varchar |  |  | SI | d465 Sq-Moving around using equipment (wheelchair,... |
| Q145 | varchar |  |  | SI | d470 Using transportation (car, bus, train, plane,... |
| Q146 | varchar |  |  | SI | d470 Sq-Using transportation (car, bus, train, pla... |
| Q147 | varchar |  |  | SI | d475 Driving (riding bicycle and motorbike, drivin... |
| Q148 | varchar |  |  | SI | d475 Sq-Driving (riding bicycle and motorbike, dri... |
| Q149 | varchar |  |  | SI | d5. |
| Q15 | varchar |  |  | SI | b156 Perceptual functions |
| Q150 | varchar |  |  | SI | Self care |
| Q151 | varchar |  |  | SI | d510 Washing oneself (bathing, drying, washing han... |
| Q152 | varchar |  |  | SI | d510 Sq-Washing oneself (bathing, drying, washing ... |
| Q153 | varchar |  |  | SI | d520 Caring for body parts (brushing teeth, shavin... |
| Q154 | varchar |  |  | SI | d520 Sq-Caring for body parts (brushing teeth, sha... |
| Q155 | varchar |  |  | SI | d530 Toileting |
| Q156 | varchar |  |  | SI | d530 Sq-Toileting |
| Q157 | varchar |  |  | SI | d540 Dressing |
| Q158 | varchar |  |  | SI | d540 Sq-Dressing |
| Q159 | varchar |  |  | SI | d550 Eating |
| Q16 | varchar |  |  | SI | b164 Higher level cognitive functions |
| Q160 | varchar |  |  | SI | d550 Sq-Eating |
| Q161 | varchar |  |  | SI | d560 Drinking |
| Q162 | varchar |  |  | SI | d560 Sq-Drinking |
| Q163 | varchar |  |  | SI | d570 Looking after one's health |
| Q164 | varchar |  |  | SI | d570 Sq-Looking after one's health |
| Q165 | varchar |  |  | SI | d6. |
| Q166 | varchar |  |  | SI | Domestic life |
| Q167 | varchar |  |  | SI | d620 Acquisition of goods and services (shopping, ... |
| Q168 | varchar |  |  | SI | d620 Sq-Acquisition of goods and services (shoppin... |
| Q169 | varchar |  |  | SI | d630 Preparation of meals (cooking etc.) |
| Q17 | varchar |  |  | SI | b167 Language |
| Q170 | varchar |  |  | SI | d630 Sq-Preparation of meals (cooking etc.) |
| Q171 | varchar |  |  | SI | d640 Doing Housework (Cleaning house, washing dish... |
| Q172 | varchar |  |  | SI | d640 Sq-Doing Housework (Cleaning house, washing d... |
| Q173 | varchar |  |  | SI | d660 Assisting others |
| Q174 | varchar |  |  | SI | d660 Sq-Assisting others |
| Q175 | varchar |  |  | SI | Interpersonal interactions and relationships |
| Q176 | varchar |  |  | SI | d7. |
| Q177 | varchar |  |  | SI | Interpersonal interactions and relationships |
| Q178 | varchar |  |  | SI | d710 Basic interpersonal interactions |
| Q179 | varchar |  |  | SI | d710 Sq-Basic interpersonal interactions |
| Q18 | varchar |  |  | SI | b2. |
| Q180 | varchar |  |  | SI | d720 Complex interpersonal interactions |
| Q181 | varchar |  |  | SI | d720 Sq-Complex interpersonal interactions |
| Q182 | varchar |  |  | SI | d730 Relating with strangers |
| Q183 | varchar |  |  | SI | d730 Sq-Relating with strangers |
| Q184 | varchar |  |  | SI | d740 Formal relationships |
| Q185 | varchar |  |  | SI | d740 Sq-Formal relationships |
| Q186 | varchar |  |  | SI | d750 Informal social relationships |
| Q187 | varchar |  |  | SI | d750 Sq-Informal social relationships |
| Q188 | varchar |  |  | SI | d760 Family relationships |
| Q189 | varchar |  |  | SI | d760 Sq-Family relationships |
| Q19 | varchar |  |  | SI | Sensory functions and pain |
| Q190 | varchar |  |  | SI | d770 Intimate relationships |
| Q191 | varchar |  |  | SI | d770 Sq-Intimate relationships |
| Q192 | varchar |  |  | SI | d8. |
| Q193 | varchar |  |  | SI | Major life areas |
| Q194 | varchar |  |  | SI | d810 Informal education |
| Q195 | varchar |  |  | SI | d810 Sq-Informal education |
| Q196 | varchar |  |  | SI | d820 School education |
| Q197 | varchar |  |  | SI | d820 Sq-School education |
| Q198 | varchar |  |  | SI | d830 Higher education |
| Q199 | varchar |  |  | SI | d830 Sq-Higher education |
| Q20 | varchar |  |  | SI | b210 Seeing |
| Q200 | varchar |  |  | SI | d850 Remunerative employment |
| Q201 | varchar |  |  | SI | d850 Sq-Remunerative employment |
| Q202 | varchar |  |  | SI | d860 Basic economic transactions |
| Q203 | varchar |  |  | SI | d860 Sq-Basic economic transactions |
| Q204 | varchar |  |  | SI | d870 Economic self-sufficiency |
| Q205 | varchar |  |  | SI | d870 Sq-Economic self-sufficiency |
| Q206 | varchar |  |  | SI | d9. |
| Q207 | varchar |  |  | SI | Community, social and civic life |
| Q208 | varchar |  |  | SI | d910 Community life |
| Q209 | varchar |  |  | SI | d910 Sq-Community life |
| Q21 | varchar |  |  | SI | b230 Hearing |
| Q210 | varchar |  |  | SI | d920 Recreation and leisure |
| Q211 | varchar |  |  | SI | d920 Sq-Recreation and leisure |
| Q212 | varchar |  |  | SI | d930 Religion and spirituality |
| Q213 | varchar |  |  | SI | d930 Sq-Religion And Spirituality |
| Q214 | varchar |  |  | SI | d940 Human rights |
| Q215 | varchar |  |  | SI | d940 Sq-Human rights |
| Q216 | varchar |  |  | SI | d950 Political life and citizenship |
| Q217 | varchar |  |  | SI | d950 Sq-Political life and citizenship |
| Q218 | varchar |  |  | SI | Any other activity and participation |
| Q219 | varchar |  |  | SI | Short list of environment |
| Q22 | varchar |  |  | SI | b235 Vestibular (incl. Balance functions) |
| Q220 | varchar |  |  | SI | Qualifier |
| Q221 | varchar |  |  | SI | e1. |
| Q222 | varchar |  |  | SI | Products and technology |
| Q223 | varchar |  |  | SI | e110 For personal consumption (food, medicines) |
| Q224 | varchar |  |  | SI | e115 For personal use in daily living |
| Q225 | varchar |  |  | SI | e120 For personal indoor and outdoor mobility and ... |
| Q226 | varchar |  |  | SI | e125 Products for communication |
| Q227 | varchar |  |  | SI | e150 Design, construction and building products an... |
| Q228 | varchar |  |  | SI | e155 Design, construction and building products an... |
| Q229 | varchar |  |  | SI | e2. |
| Q23 | varchar |  |  | SI | b280 Pain |
| Q230 | varchar |  |  | SI | Natural environment and human made changes to envi... |
| Q231 | varchar |  |  | SI | e225 Climate |
| Q232 | varchar |  |  | SI | e240 Light |
| Q233 | varchar |  |  | SI | e250 Sound |
| Q234 | varchar |  |  | SI | e3. |
| Q235 | varchar |  |  | SI | Support and relationships |
| Q236 | varchar |  |  | SI | e310 Immediate family |
| Q237 | varchar |  |  | SI | e320 Friends |
| Q238 | varchar |  |  | SI | e325 Acquaintances, peers, colleagues, neighbors a... |
| Q239 | varchar |  |  | SI | e330 People in position of authority |
| Q24 | varchar |  |  | SI | b3. |
| Q240 | varchar |  |  | SI | e340 Personal care providers and personal assistan... |
| Q241 | varchar |  |  | SI | e355 Health professionals |
| Q242 | varchar |  |  | SI | e360 Health related professionals |
| Q243 | varchar |  |  | SI | e4. |
| Q244 | varchar |  |  | SI | Attitudes |
| Q245 | varchar |  |  | SI | e410 Individual attitudes of immediate family memb... |
| Q246 | varchar |  |  | SI | e420 Individual attitudes of friends |
| Q247 | varchar |  |  | SI | e440 Individual attitudes of personal care provide... |
| Q248 | varchar |  |  | SI | e450 Individual attitudes of health professionals |
| Q249 | varchar |  |  | SI | e455 Individual attitudes of health related profes... |
| Q25 | varchar |  |  | SI | Voice and speech functions |
| Q250 | varchar |  |  | SI | e460 Societal Attitudes |
| Q251 | varchar |  |  | SI | e465 Social norms, practices and ideologies |
| Q252 | varchar |  |  | SI | e5. |
| Q253 | varchar |  |  | SI | Services, systems and policies |
| Q254 | varchar |  |  | SI | e525 Housing services, systems and policies |
| Q255 | varchar |  |  | SI | e535 Communication services, systems and policies |
| Q256 | varchar |  |  | SI | e540 Transportation services, systems and policies |
| Q257 | varchar |  |  | SI | e550 Legal services, systems and policies |
| Q258 | varchar |  |  | SI | e570 Social security, services, systems and polici... |
| Q259 | varchar |  |  | SI | e575 General social support services, systems and ... |
| Q26 | varchar |  |  | SI | b310 Voice |
| Q260 | varchar |  |  | SI | e580 Health services, systems and policies |
| Q261 | varchar |  |  | SI | e585 Education and training services, systems and ... |
| Q262 | varchar |  |  | SI | e590 Labour and employment services, systems and p... |
| Q263 | varchar |  |  | SI | Any other environmental factors |
| Q264 | varchar |  |  | SI | Qualifier in environment: |
| Q265 | varchar |  |  | SI | No barriers |
| Q266 | varchar |  |  | SI | Mild barriers |
| Q267 | varchar |  |  | SI | Severe barriers |
| Q268 | varchar |  |  | SI | Complete barriers |
| Q269 | varchar |  |  | SI | No facilitator |
| Q27 | varchar |  |  | SI | b4. |
| Q270 | varchar |  |  | SI | Mild facilitator |
| Q271 | varchar |  |  | SI | Moderate facilitator |
| Q272 | varchar |  |  | SI | Substantial facilitator |
| Q273 | varchar |  |  | SI | Complete facilitator |
| Q274 | varchar |  |  | SI | Part 1: Impairments of body functions and structur... |
| Q275 | varchar |  |  | SI | First qualifier: Extent of impairments |
| Q276 | varchar |  |  | SI | No impairment means the person has no problem. |
| Q277 | varchar |  |  | SI | Mild impairment means a problem that is present le... |
| Q278 | varchar |  |  | SI | Moderate impairment means that a problem that is p... |
| Q279 | varchar |  |  | SI | Severe impairment means that a problem that is pre... |
| Q28 | varchar |  |  | SI | Functions of the cardiovascular, haematological, i... |
| Q280 | varchar |  |  | SI | Complete impairment means that a problem that is p... |
| Q281 | varchar |  |  | SI | Not specified means there is insufficient informat... |
| Q282 | varchar |  |  | SI | Not applicable means it is inappropriate to apply ... |
| Q283 | varchar |  |  | SI | Part 2: Activity limitations & participation restr... |
| Q284 | varchar |  |  | SI | 0 No difficulty means the person has no problem |
| Q285 | varchar |  |  | SI | 1 Mild difficulty means a problem that is present ... |
| Q286 | varchar |  |  | SI | 2 Moderate difficulty means that a problem that is... |
| Q287 | varchar |  |  | SI | 3 Severe difficulty means that a problem that is p... |
| Q288 | varchar |  |  | SI | 4 Complete difficulty means that a problem that is... |
| Q289 | varchar |  |  | SI | 8 Not specified means there is insufficient inform... |
| Q29 | varchar |  |  | SI | b410 Heart |
| Q290 | varchar |  |  | SI | 9 Not applicable means it is inappropriate to appl... |
| Q291 | varchar |  |  | SI | Extent of  impairment |
| Q292 | varchar |  |  | SI | Nature of the change |
| Q293 | varchar |  |  | SI | General tasks and demands |
| Q294 | varchar |  |  | SI | barrier or facilitator |
| Q295 | varchar |  |  | SI | Moderate barriers |
| Q30 | varchar |  |  | SI | b420 Blood pressure |
| Q31 | varchar |  |  | SI | b430 Haematological (blood) |
| Q32 | varchar |  |  | SI | b435 Immunological (allergies, hypersensitivity) |
| Q33 | varchar |  |  | SI | b440 Respiration (breathing) |
| Q34 | varchar |  |  | SI | b5. |
| Q35 | varchar |  |  | SI | Functions of the digestive, metabolic and endocrin... |
| Q36 | varchar |  |  | SI | b515 Digestive |
| Q37 | varchar |  |  | SI | b525 Defecation |
| Q38 | varchar |  |  | SI | b530 Weight maintenance |
| Q39 | varchar |  |  | SI | b555 Endocrine glands (hormonal changes) |
| Q40 | varchar |  |  | SI | b6. |
| Q41 | varchar |  |  | SI | Genitourinary and reproductive functions |
| Q42 | varchar |  |  | SI | b620 Urination functions |
| Q43 | varchar |  |  | SI | b640 Sexual functions |
| Q44 | varchar |  |  | SI | b7. |
| Q45 | varchar |  |  | SI | Neuro-musculoskeletal and movement related functio... |
| Q46 | varchar |  |  | SI | b710 Mobility of joint |
| Q47 | varchar |  |  | SI | b730 Muscle Power |
| Q48 | varchar |  |  | SI | b735 Muscle Tone |
| Q49 | varchar |  |  | SI | b765 Involuntary movements |
| Q50 | varchar |  |  | SI | b8. |
| Q51 | varchar |  |  | SI | Functions of the skin and related structures |
| Q52 | varchar |  |  | SI | Any other body functions |
| Q53 | varchar |  |  | SI | Short list of body structures |
| Q54 | varchar |  |  | SI | First Qualifier: |
| Q55 | varchar |  |  | SI | Second Qualifier: |
| Q56 | varchar |  |  | SI | s1. |
| Q57 | varchar |  |  | SI | Structure of the nervous system |
| Q58 | varchar |  |  | SI | s110 Brain |
| Q59 | varchar |  |  | SI | s110 Sq-Brain |
| Q60 | varchar |  |  | SI | s120 Spinal cord and peripheral nerves |
| Q61 | varchar |  |  | SI | s120 Sq-Spinal cord and peripheral nerves |
| Q62 | varchar |  |  | SI | s2. |
| Q63 | varchar |  |  | SI | The eye, ear and related structures |
| Q64 | varchar |  |  | SI | s2 Sq-The eye, ear and related structures |
| Q65 | varchar |  |  | SI | s3. |
| Q66 | varchar |  |  | SI | Structures involved in voice and speech |
| Q67 | varchar |  |  | SI | s3 Sq-Structures involved in voice and speech |
| Q68 | varchar |  |  | SI | s4. |
| Q69 | varchar |  |  | SI | Structure of the cardiovascular, immunological and... |
| Q70 | varchar |  |  | SI | s410 Cardiovascular system |
| Q71 | varchar |  |  | SI | s410 Sq-Cardiovascular system |
| Q72 | varchar |  |  | SI | s430 Respiratory system |
| Q73 | varchar |  |  | SI | s430 Sq-Respiratory system |
| Q74 | varchar |  |  | SI | s5. |
| Q75 | varchar |  |  | SI | Structures related to the digestive, metabolism an... |
| Q76 | varchar |  |  | SI | s5 Sq-Structures related to the digestive, metabol... |
| Q77 | varchar |  |  | SI | s6. |
| Q78 | varchar |  |  | SI | Structure related to genitourinary and reproductiv... |
| Q79 | varchar |  |  | SI | s610 Urinary system |
| Q80 | varchar |  |  | SI | s610 Sq-Urinary system |
| Q81 | varchar |  |  | SI | s630 Reproductive System |
| Q82 | varchar |  |  | SI | s630 Sq-Reproductive system |
| Q83 | varchar |  |  | SI | s7. |
| Q84 | varchar |  |  | SI | Structure related to movement |
| Q85 | varchar |  |  | SI | s710 Head and neck region |
| Q86 | varchar |  |  | SI | s710 Sq-Head and neck region |
| Q87 | varchar |  |  | SI | s720 Shoulder region |
| Q88 | varchar |  |  | SI | s720 Sq-Shoulder region |
| Q89 | varchar |  |  | SI | s730 Upper extremity (arm, hand) |
| Q90 | varchar |  |  | SI | s730 Sq-Upper extremity (arm, hand) |
| Q91 | varchar |  |  | SI | s740 Pelvis |
| Q92 | varchar |  |  | SI | s740 Sq-Pelvis |
| Q93 | varchar |  |  | SI | s750 Lower extremity (leg, foot) |
| Q94 | varchar |  |  | SI | s750 Sq-Lower extremity (leg, foot) |
| Q95 | varchar |  |  | SI | s760 Trunk |
| Q96 | varchar |  |  | SI | s760 Sq-Trunk |
| Q97 | varchar |  |  | SI | s8. |
| Q98 | varchar |  |  | SI | Skin and related structures |
| Q99 | varchar |  |  | SI | s8 Sq-Skin and related structures |
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