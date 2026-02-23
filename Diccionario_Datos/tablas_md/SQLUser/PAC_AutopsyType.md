# SQLUser.PAC_AutopsyType

**Schema:** SQLUser
**Columnas:** 348
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| AUTOP_RowId | bigint | PK |  | NO | - |
| AUTOP_Code | varchar |  |  | NO | Code |
| AUTOP_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| AUTOP_CreatedDate | date |  |  | SI | Created Date |
| AUTOP_CreatedTime | time |  |  | SI | Created Time |
| AUTOP_CreatedUser_DR | bigint |  | FK | SI | Created User |
| AUTOP_DateFrom | date |  |  | SI | Date From |
| AUTOP_DateTo | date |  |  | SI | Date To |
| AUTOP_Desc | varchar |  |  | NO | Description |
| AUTOP_Owner | varchar |  |  | SI | Owner |
| AUTOP_UpdatedDate | date |  |  | SI | Updated Date |
| AUTOP_UpdatedTime | time |  |  | SI | Updated Time |
| AUTOP_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Short List of Body Functions |
| Q04 | - |  |  | SI | Qualifier ''Extent of Impairments |
| Q05 | - |  |  | SI | b1. |
| Q06 | - |  |  | SI | Mental functions |
| Q07 | - |  |  | SI | b110 Consciousness |
| Q08 | - |  |  | SI | b114 Orientation (time, place, person) |
| Q09 | - |  |  | SI | b117 Intellectual (incl. Retardation, dementia) |
| Q10 | - |  |  | SI | b130 Energy and drive functions |
| Q100 | - |  |  | SI | Any other body structures |
| Q101 | - |  |  | SI | Short list of A&P domains |
| Q102 | - |  |  | SI | Performance qualifier ''Extent of participation re... |
| Q103 | - |  |  | SI | Capacity qualifier ''Extent of activity limitation... |
| Q104 | - |  |  | SI | d1. |
| Q105 | - |  |  | SI | Learning and applying knowledge |
| Q106 | - |  |  | SI | d110 Watching |
| Q107 | - |  |  | SI | d110 Sq-Watching |
| Q108 | - |  |  | SI | d115 Listening |
| Q109 | - |  |  | SI | d115 Sq-Listening |
| Q11 | - |  |  | SI | b134 Sleep |
| Q110 | - |  |  | SI | d140 Learning to read |
| Q111 | - |  |  | SI | d140 Sq-Learning to read |
| Q112 | - |  |  | SI | d145 Learning to write |
| Q113 | - |  |  | SI | d145 Sq-Learning to write |
| Q114 | - |  |  | SI | d150 Learning to calculate (arithmetic) |
| Q115 | - |  |  | SI | d150 Sq-Learning to calculate (arithmetic) |
| Q116 | - |  |  | SI | d175 Solving problems |
| Q117 | - |  |  | SI | d175 Sq-Solving problems |
| Q118 | - |  |  | SI | d2. |
| Q119 | - |  |  | SI | d210 Undertaking a single task |
| Q12 | - |  |  | SI | b140 Attention |
| Q120 | - |  |  | SI | d210 Sq-Undertaking a single task |
| Q121 | - |  |  | SI | d220 Undertaking multiple tasks |
| Q122 | - |  |  | SI | d220 Sq-Undertaking multiple tasks |
| Q123 | - |  |  | SI | d3. |
| Q124 | - |  |  | SI | Communication |
| Q125 | - |  |  | SI | d310 Communicating with -- receiving -- spoken mes... |
| Q126 | - |  |  | SI | d310 Communicating |
| Q127 | - |  |  | SI | d315 Communicating with -- receiving -- non-verbal... |
| Q128 | - |  |  | SI | d315 Sq-Communicating with -- receiving -- non-ver... |
| Q129 | - |  |  | SI | d330 Speaking |
| Q13 | - |  |  | SI | b144 Memory |
| Q130 | - |  |  | SI | d330 Sq-Speaking |
| Q131 | - |  |  | SI | d335 Producing non-verbal messages |
| Q132 | - |  |  | SI | d335 Sq-Producing non-verbal messages |
| Q133 | - |  |  | SI | d350 Conversation |
| Q134 | - |  |  | SI | d350 Sq-Conversation |
| Q135 | - |  |  | SI | d4. |
| Q136 | - |  |  | SI | Mobility |
| Q137 | - |  |  | SI | d430 Lifting and carrying objects |
| Q138 | - |  |  | SI | d430 Sq-Lifting and carrying objects |
| Q139 | - |  |  | SI | d440 Fine hand use (picking up, grasping) |
| Q14 | - |  |  | SI | b152 Emotional functions |
| Q140 | - |  |  | SI | d440 Sq-Fine hand use (picking up, grasping) |
| Q141 | - |  |  | SI | d450 Walking |
| Q142 | - |  |  | SI | d450 Sq-Walking |
| Q143 | - |  |  | SI | d465 Moving around using equipment (wheelchair, sk... |
| Q144 | - |  |  | SI | d465 Sq-Moving around using equipment (wheelchair,... |
| Q145 | - |  |  | SI | d470 Using transportation (car, bus, train, plane,... |
| Q146 | - |  |  | SI | d470 Sq-Using transportation (car, bus, train, pla... |
| Q147 | - |  |  | SI | d475 Driving (riding bicycle and motorbike, drivin... |
| Q148 | - |  |  | SI | d475 Sq-Driving (riding bicycle and motorbike, dri... |
| Q149 | - |  |  | SI | d5. |
| Q15 | - |  |  | SI | b156 Perceptual functions |
| Q150 | - |  |  | SI | Self care |
| Q151 | - |  |  | SI | d510 Washing oneself (bathing, drying, washing han... |
| Q152 | - |  |  | SI | d510 Sq-Washing oneself (bathing, drying, washing ... |
| Q153 | - |  |  | SI | d520 Caring for body parts (brushing teeth, shavin... |
| Q154 | - |  |  | SI | d520 Sq-Caring for body parts (brushing teeth, sha... |
| Q155 | - |  |  | SI | d530 Toileting |
| Q156 | - |  |  | SI | d530 Sq-Toileting |
| Q157 | - |  |  | SI | d540 Dressing |
| Q158 | - |  |  | SI | d540 Sq-Dressing |
| Q159 | - |  |  | SI | d550 Eating |
| Q16 | - |  |  | SI | b164 Higher level cognitive functions |
| Q160 | - |  |  | SI | d550 Sq-Eating |
| Q161 | - |  |  | SI | d560 Drinking |
| Q162 | - |  |  | SI | d560 Sq-Drinking |
| Q163 | - |  |  | SI | d570 Looking after one's health |
| Q164 | - |  |  | SI | d570 Sq-Looking after one's health |
| Q165 | - |  |  | SI | d6. |
| Q166 | - |  |  | SI | Domestic life |
| Q167 | - |  |  | SI | d620 Acquisition of goods and services (shopping, ... |
| Q168 | - |  |  | SI | d620 Sq-Acquisition of goods and services (shoppin... |
| Q169 | - |  |  | SI | d630 Preparation of meals (cooking etc.) |
| Q17 | - |  |  | SI | b167 Language |
| Q170 | - |  |  | SI | d630 Sq-Preparation of meals (cooking etc.) |
| Q171 | - |  |  | SI | d640 Doing Housework (Cleaning house, washing dish... |
| Q172 | - |  |  | SI | d640 Sq-Doing Housework (Cleaning house, washing d... |
| Q173 | - |  |  | SI | d660 Assisting others |
| Q174 | - |  |  | SI | d660 Sq-Assisting others |
| Q175 | - |  |  | SI | Interpersonal interactions and relationships |
| Q176 | - |  |  | SI | d7. |
| Q177 | - |  |  | SI | Interpersonal interactions and relationships |
| Q178 | - |  |  | SI | d710 Basic interpersonal interactions |
| Q179 | - |  |  | SI | d710 Sq-Basic interpersonal interactions |
| Q18 | - |  |  | SI | b2. |
| Q180 | - |  |  | SI | d720 Complex interpersonal interactions |
| Q181 | - |  |  | SI | d720 Sq-Complex interpersonal interactions |
| Q182 | - |  |  | SI | d730 Relating with strangers |
| Q183 | - |  |  | SI | d730 Sq-Relating with strangers |
| Q184 | - |  |  | SI | d740 Formal relationships |
| Q185 | - |  |  | SI | d740 Sq-Formal relationships |
| Q186 | - |  |  | SI | d750 Informal social relationships |
| Q187 | - |  |  | SI | d750 Sq-Informal social relationships |
| Q188 | - |  |  | SI | d760 Family relationships |
| Q189 | - |  |  | SI | d760 Sq-Family relationships |
| Q19 | - |  |  | SI | Sensory functions and pain |
| Q190 | - |  |  | SI | d770 Intimate relationships |
| Q191 | - |  |  | SI | d770 Sq-Intimate relationships |
| Q192 | - |  |  | SI | d8. |
| Q193 | - |  |  | SI | Major life areas |
| Q194 | - |  |  | SI | d810 Informal education |
| Q195 | - |  |  | SI | d810 Sq-Informal education |
| Q196 | - |  |  | SI | d820 School education |
| Q197 | - |  |  | SI | d820 Sq-School education |
| Q198 | - |  |  | SI | d830 Higher education |
| Q199 | - |  |  | SI | d830 Sq-Higher education |
| Q20 | - |  |  | SI | b210 Seeing |
| Q200 | - |  |  | SI | d850 Remunerative employment |
| Q201 | - |  |  | SI | d850 Sq-Remunerative employment |
| Q202 | - |  |  | SI | d860 Basic economic transactions |
| Q203 | - |  |  | SI | d860 Sq-Basic economic transactions |
| Q204 | - |  |  | SI | d870 Economic self-sufficiency |
| Q205 | - |  |  | SI | d870 Sq-Economic self-sufficiency |
| Q206 | - |  |  | SI | d9. |
| Q207 | - |  |  | SI | Community, social and civic life |
| Q208 | - |  |  | SI | d910 Community life |
| Q209 | - |  |  | SI | d910 Sq-Community life |
| Q21 | - |  |  | SI | b230 Hearing |
| Q210 | - |  |  | SI | d920 Recreation and leisure |
| Q211 | - |  |  | SI | d920 Sq-Recreation and leisure |
| Q212 | - |  |  | SI | d930 Religion and spirituality |
| Q213 | - |  |  | SI | d930 Sq-Religion And Spirituality |
| Q214 | - |  |  | SI | d940 Human rights |
| Q215 | - |  |  | SI | d940 Sq-Human rights |
| Q216 | - |  |  | SI | d950 Political life and citizenship |
| Q217 | - |  |  | SI | d950 Sq-Political life and citizenship |
| Q218 | - |  |  | SI | Any other activity and participation |
| Q219 | - |  |  | SI | Short list of environment |
| Q22 | - |  |  | SI | b235 Vestibular (incl. Balance functions) |
| Q220 | - |  |  | SI | Qualifier |
| Q221 | - |  |  | SI | e1. |
| Q222 | - |  |  | SI | Products and technology |
| Q223 | - |  |  | SI | e110 For personal consumption (food, medicines) |
| Q224 | - |  |  | SI | e115 For personal use in daily living |
| Q225 | - |  |  | SI | e120 For personal indoor and outdoor mobility and ... |
| Q226 | - |  |  | SI | e125 Products for communication |
| Q227 | - |  |  | SI | e150 Design, construction and building products an... |
| Q228 | - |  |  | SI | e155 Design, construction and building products an... |
| Q229 | - |  |  | SI | e2. |
| Q23 | - |  |  | SI | b280 Pain |
| Q230 | - |  |  | SI | Natural environment and human made changes to envi... |
| Q231 | - |  |  | SI | e225 Climate |
| Q232 | - |  |  | SI | e240 Light |
| Q233 | - |  |  | SI | e250 Sound |
| Q234 | - |  |  | SI | e3. |
| Q235 | - |  |  | SI | Support and relationships |
| Q236 | - |  |  | SI | e310 Immediate family |
| Q237 | - |  |  | SI | e320 Friends |
| Q238 | - |  |  | SI | e325 Acquaintances, peers, colleagues, neighbors a... |
| Q239 | - |  |  | SI | e330 People in position of authority |
| Q24 | - |  |  | SI | b3. |
| Q240 | - |  |  | SI | e340 Personal care providers and personal assistan... |
| Q241 | - |  |  | SI | e355 Health professionals |
| Q242 | - |  |  | SI | e360 Health related professionals |
| Q243 | - |  |  | SI | e4. |
| Q244 | - |  |  | SI | Attitudes |
| Q245 | - |  |  | SI | e410 Individual attitudes of immediate family memb... |
| Q246 | - |  |  | SI | e420 Individual attitudes of friends |
| Q247 | - |  |  | SI | e440 Individual attitudes of personal care provide... |
| Q248 | - |  |  | SI | e450 Individual attitudes of health professionals |
| Q249 | - |  |  | SI | e455 Individual attitudes of health related profes... |
| Q25 | - |  |  | SI | Voice and speech functions |
| Q250 | - |  |  | SI | e460 Societal Attitudes |
| Q251 | - |  |  | SI | e465 Social norms, practices and ideologies |
| Q252 | - |  |  | SI | e5. |
| Q253 | - |  |  | SI | Services, systems and policies |
| Q254 | - |  |  | SI | e525 Housing services, systems and policies |
| Q255 | - |  |  | SI | e535 Communication services, systems and policies |
| Q256 | - |  |  | SI | e540 Transportation services, systems and policies |
| Q257 | - |  |  | SI | e550 Legal services, systems and policies |
| Q258 | - |  |  | SI | e570 Social security, services, systems and polici... |
| Q259 | - |  |  | SI | e575 General social support services, systems and ... |
| Q26 | - |  |  | SI | b310 Voice |
| Q260 | - |  |  | SI | e580 Health services, systems and policies |
| Q261 | - |  |  | SI | e585 Education and training services, systems and ... |
| Q262 | - |  |  | SI | e590 Labour and employment services, systems and p... |
| Q263 | - |  |  | SI | Any other environmental factors |
| Q264 | - |  |  | SI | Qualifier in environment: |
| Q265 | - |  |  | SI | No barriers |
| Q266 | - |  |  | SI | Mild barriers |
| Q267 | - |  |  | SI | Severe barriers |
| Q268 | - |  |  | SI | Complete barriers |
| Q269 | - |  |  | SI | No facilitator |
| Q27 | - |  |  | SI | b4. |
| Q270 | - |  |  | SI | Mild facilitator |
| Q271 | - |  |  | SI | Moderate facilitator |
| Q272 | - |  |  | SI | Substantial facilitator |
| Q273 | - |  |  | SI | Complete facilitator |
| Q274 | - |  |  | SI | Part 1: Impairments of body functions and structur... |
| Q275 | - |  |  | SI | First qualifier: Extent of impairments |
| Q276 | - |  |  | SI | No impairment means the person has no problem. |
| Q277 | - |  |  | SI | Mild impairment means a problem that is present le... |
| Q278 | - |  |  | SI | Moderate impairment means that a problem that is p... |
| Q279 | - |  |  | SI | Severe impairment means that a problem that is pre... |
| Q28 | - |  |  | SI | Functions of the cardiovascular, haematological, i... |
| Q280 | - |  |  | SI | Complete impairment means that a problem that is p... |
| Q281 | - |  |  | SI | Not specified means there is insufficient informat... |
| Q282 | - |  |  | SI | Not applicable means it is inappropriate to apply ... |
| Q283 | - |  |  | SI | Part 2: Activity limitations & participation restr... |
| Q284 | - |  |  | SI | 0 No difficulty means the person has no problem |
| Q285 | - |  |  | SI | 1 Mild difficulty means a problem that is present ... |
| Q286 | - |  |  | SI | 2 Moderate difficulty means that a problem that is... |
| Q287 | - |  |  | SI | 3 Severe difficulty means that a problem that is p... |
| Q288 | - |  |  | SI | 4 Complete difficulty means that a problem that is... |
| Q289 | - |  |  | SI | 8 Not specified means there is insufficient inform... |
| Q29 | - |  |  | SI | b410 Heart |
| Q290 | - |  |  | SI | 9 Not applicable means it is inappropriate to appl... |
| Q291 | - |  |  | SI | Extent of  impairment |
| Q292 | - |  |  | SI | Nature of the change |
| Q293 | - |  |  | SI | General tasks and demands |
| Q294 | - |  |  | SI | barrier or facilitator |
| Q295 | - |  |  | SI | Moderate barriers |
| Q30 | - |  |  | SI | b420 Blood pressure |
| Q31 | - |  |  | SI | b430 Haematological (blood) |
| Q32 | - |  |  | SI | b435 Immunological (allergies, hypersensitivity) |
| Q33 | - |  |  | SI | b440 Respiration (breathing) |
| Q34 | - |  |  | SI | b5. |
| Q35 | - |  |  | SI | Functions of the digestive, metabolic and endocrin... |
| Q36 | - |  |  | SI | b515 Digestive |
| Q37 | - |  |  | SI | b525 Defecation |
| Q38 | - |  |  | SI | b530 Weight maintenance |
| Q39 | - |  |  | SI | b555 Endocrine glands (hormonal changes) |
| Q40 | - |  |  | SI | b6. |
| Q41 | - |  |  | SI | Genitourinary and reproductive functions |
| Q42 | - |  |  | SI | b620 Urination functions |
| Q43 | - |  |  | SI | b640 Sexual functions |
| Q44 | - |  |  | SI | b7. |
| Q45 | - |  |  | SI | Neuro-musculoskeletal and movement related functio... |
| Q46 | - |  |  | SI | b710 Mobility of joint |
| Q47 | - |  |  | SI | b730 Muscle Power |
| Q48 | - |  |  | SI | b735 Muscle Tone |
| Q49 | - |  |  | SI | b765 Involuntary movements |
| Q50 | - |  |  | SI | b8. |
| Q51 | - |  |  | SI | Functions of the skin and related structures |
| Q52 | - |  |  | SI | Any other body functions |
| Q53 | - |  |  | SI | Short list of body structures |
| Q54 | - |  |  | SI | First Qualifier: |
| Q55 | - |  |  | SI | Second Qualifier: |
| Q56 | - |  |  | SI | s1. |
| Q57 | - |  |  | SI | Structure of the nervous system |
| Q58 | - |  |  | SI | s110 Brain |
| Q59 | - |  |  | SI | s110 Sq-Brain |
| Q60 | - |  |  | SI | s120 Spinal cord and peripheral nerves |
| Q61 | - |  |  | SI | s120 Sq-Spinal cord and peripheral nerves |
| Q62 | - |  |  | SI | s2. |
| Q63 | - |  |  | SI | The eye, ear and related structures |
| Q64 | - |  |  | SI | s2 Sq-The eye, ear and related structures |
| Q65 | - |  |  | SI | s3. |
| Q66 | - |  |  | SI | Structures involved in voice and speech |
| Q67 | - |  |  | SI | s3 Sq-Structures involved in voice and speech |
| Q68 | - |  |  | SI | s4. |
| Q69 | - |  |  | SI | Structure of the cardiovascular, immunological and... |
| Q70 | - |  |  | SI | s410 Cardiovascular system |
| Q71 | - |  |  | SI | s410 Sq-Cardiovascular system |
| Q72 | - |  |  | SI | s430 Respiratory system |
| Q73 | - |  |  | SI | s430 Sq-Respiratory system |
| Q74 | - |  |  | SI | s5. |
| Q75 | - |  |  | SI | Structures related to the digestive, metabolism an... |
| Q76 | - |  |  | SI | s5 Sq-Structures related to the digestive, metabol... |
| Q77 | - |  |  | SI | s6. |
| Q78 | - |  |  | SI | Structure related to genitourinary and reproductiv... |
| Q79 | - |  |  | SI | s610 Urinary system |
| Q80 | - |  |  | SI | s610 Sq-Urinary system |
| Q81 | - |  |  | SI | s630 Reproductive System |
| Q82 | - |  |  | SI | s630 Sq-Reproductive system |
| Q83 | - |  |  | SI | s7. |
| Q84 | - |  |  | SI | Structure related to movement |
| Q85 | - |  |  | SI | s710 Head and neck region |
| Q86 | - |  |  | SI | s710 Sq-Head and neck region |
| Q87 | - |  |  | SI | s720 Shoulder region |
| Q88 | - |  |  | SI | s720 Sq-Shoulder region |
| Q89 | - |  |  | SI | s730 Upper extremity (arm, hand) |
| Q90 | - |  |  | SI | s730 Sq-Upper extremity (arm, hand) |
| Q91 | - |  |  | SI | s740 Pelvis |
| Q92 | - |  |  | SI | s740 Sq-Pelvis |
| Q93 | - |  |  | SI | s750 Lower extremity (leg, foot) |
| Q94 | - |  |  | SI | s750 Sq-Lower extremity (leg, foot) |
| Q95 | - |  |  | SI | s760 Trunk |
| Q96 | - |  |  | SI | s760 Sq-Trunk |
| Q97 | - |  |  | SI | s8. |
| Q98 | - |  |  | SI | Skin and related structures |
| Q99 | - |  |  | SI | s8 Sq-Skin and related structures |
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