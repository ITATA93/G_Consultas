# questionnaire.QGXXXPOPC

> Pre-OP Check List

**Schema:** questionnaire
**Columnas:** 394
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Pre-OP Check List

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| CQ110 | varchar |  |  | SI | - |
| CQ235 | varchar |  |  | SI | - |
| Q01 | varchar |  |  | SI | ID band correct and in place |
| Q01b | varchar |  |  | SI | ID band correct and in place OT |
| Q02 | varchar |  |  | SI | Valid consent signed |
| Q02b | varchar |  |  | SI | Valid consent signed OT |
| Q02c | varchar |  |  | SI | Consent incomplete action taken |
| Q02d | varchar |  |  | SI | Consent incomplete action taken OT |
| Q02n | varchar |  |  | SI | Note |
| Q02not | varchar |  |  | SI | Note OT |
| Q03 | varchar |  |  | SI | Premed given and recorded |
| Q03b | varchar |  |  | SI | Premed given and recorded OT |
| Q03c | time |  |  | SI | Time premed given |
| Q03d | time |  |  | SI | Time premed given OT |
| Q03e | date |  |  | SI | Date premed given |
| Q03f | date |  |  | SI | Date premed given OT |
| Q04 | varchar |  |  | SI | Patient's medical imaging available |
| Q04b | varchar |  |  | SI | Patient's medical imaging available OT |
| Q05 | varchar |  |  | SI | Procedural area prepared / marked |
| Q05b | varchar |  |  | SI | Procedural area prepared / marked OT |
| Q06 | varchar |  |  | SI | Prosthesis / Hearing aid |
| Q06b | varchar |  |  | SI | Prosthesis / Hearing aid OT |
| Q06c | varchar |  |  | SI | Type / Location |
| Q06e | varchar |  |  | SI | Type / Location OT |
| Q06f | varchar |  |  | SI | Prosthesis specify	 |
| Q06g | varchar |  |  | SI | Prosthesis OT |
| Q07 | time |  |  | SI | Last food time |
| Q07b | time |  |  | SI | Last food time OT |
| Q07c | date |  |  | SI | Last food date |
| Q07d | date |  |  | SI | Last food at date OT |
| Q08 | varchar |  |  | SI | Dentures |
| Q08b | varchar |  |  | SI | Dentures OT |
| Q08c | varchar |  |  | SI | Dentures removed / in situ |
| Q08d | varchar |  |  | SI | Dentures removed / in situ OT |
| Q08e | varchar |  |  | SI | Dentition comments |
| Q08f | varchar |  |  | SI | Dentition comments OT |
| Q100 | varchar |  |  | SI | Hearing aid removed OT |
| Q101 | varchar |  |  | SI | Proposed operation |
| Q102 | varchar |  |  | SI | Proposed operation |
| Q103 | varchar |  |  | SI | Surgeon |
| Q104 | varchar |  |  | SI | Bowel prep result |
| Q105 | varchar |  |  | SI | History of infectious diseases OT |
| Q106 | varchar |  |  | SI | History of infectious diseases |
| Q107 | varchar |  |  | SI | Skin condition |
| Q108 | varchar |  |  | SI | Discharge planning |
| Q109 | varchar |  |  | SI | Please specify list / name of anticoagulants |
| Q11 | time |  |  | SI | Last voided time |
| Q110 | varchar |  |  | SI | Ward status |
| Q111 | varchar |  |  | SI | Entering user |
| Q112 | varchar |  |  | SI | Hovermatt in situ OT |
| Q113 | varchar |  |  | SI | Pads in situ |
| Q114 | varchar |  |  | SI | Continent |
| Q115 | varchar |  |  | SI | Completed by ward nurse |
| Q116 | date |  |  | SI | Ward completed date |
| Q117 | time |  |  | SI | Ward completed time |
| Q118 | varchar |  |  | SI | Inform: surgeon |
| Q119 | varchar |  |  | SI | Inform: surgeon OT |
| Q11b | time |  |  | SI | Last voided time OT |
| Q11c | date |  |  | SI | Last voided date |
| Q11d | date |  |  | SI | Last voided date OT |
| Q12 | varchar |  |  | SI | Hair clips /  make up /  nail varnish removed |
| Q120 | varchar |  |  | SI | Inform: assistant surgeon  |
| Q121 | varchar |  |  | SI | Inform: anesthesiologist  |
| Q122 | varchar |  |  | SI | Inform: anesthesiologist OT |
| Q123 | varchar |  |  | SI | Inform: assistant surgeon OT |
| Q124 | varchar |  |  | SI | Assessment: assessment and history contrast media |
| Q125 | varchar |  |  | SI | Assessment: assessment and history contrast media ... |
| Q126 | varchar |  |  | SI | Assessment: history / physical examination OT |
| Q127 | varchar |  |  | SI | Assessment: pre and post conscious sedation  |
| Q128 | varchar |  |  | SI | Assessment: pre and post conscious sedation OT |
| Q129 | varchar |  |  | SI | Assessment: history / physical examination  |
| Q12b | varchar |  |  | SI | Hair clips /  make up /  nail varnish removed OT |
| Q12c | varchar |  |  | SI | Jewellery removed / taped |
| Q12d | varchar |  |  | SI | Jewellery removed / taped OT |
| Q130 | varchar |  |  | SI | Assessment: preoperative medical assessment as pol... |
| Q131 | varchar |  |  | SI | Assessment: preoperative medical assessment as pol... |
| Q132 | varchar |  |  | SI | Skin / Eye preparation |
| Q133 | varchar |  |  | SI | Skin / Eye preparation OT |
| Q134 | varchar |  |  | SI | SSE / Fleet enema / NSE  |
| Q135 | varchar |  |  | SI | SSE / Fleet enema / NSE OT |
| Q136 | varchar |  |  | SI | Medication brought to procedure unit  |
| Q137 | varchar |  |  | SI | Medication brought to procedure unit OT |
| Q138 | varchar |  |  | SI | Equipment brought to procedure unit  |
| Q139 | varchar |  |  | SI | Equipment brought to procedure unit OT |
| Q140 | varchar |  |  | SI | Pedal pulse marked both sides |
| Q141 | varchar |  |  | SI | Pedal pulse marked both sides OT |
| Q142 | varchar |  |  | SI | Film |
| Q143 | varchar |  |  | SI | Film OT |
| Q144 | date |  |  | SI | Bowels last opened date |
| Q145 | date |  |  | SI | Bowels last opened date OT |
| Q146 | varchar |  |  | SI | Patient's medical imaging available |
| Q147 | time |  |  | SI | Bowels last opened time |
| Q148 | time |  |  | SI | Bowels last opened time OT |
| Q150 | varchar |  |  | SI | Antibiotic prescribed |
| Q150b | varchar |  |  | SI | Antibiotic prescribed OT |
| Q151 | varchar |  |  | SI | Antibiotic given |
| Q151b | varchar |  |  | SI | Antibiotic given OT |
| Q152 | varchar |  |  | SI | Antithrombotic prescribed |
| Q152b | varchar |  |  | SI | Antithrombotic prescribed OT |
| Q153 | varchar |  |  | SI | Antithrombotic given |
| Q153b | varchar |  |  | SI | Antithrombotic given OT |
| Q154 | varchar |  |  | SI | Has a pregnancy test been performed? |
| Q154b | varchar |  |  | SI | Has a pregnancy test been performed? OT |
| Q155 | varchar |  |  | SI | Is the patient pregnant? |
| Q155b | varchar |  |  | SI | Is the patient pregnant? OT |
| Q155c | date |  |  | SI | Last menstrual period |
| Q155d | date |  |  | SI | Last menstrual period OT |
| Q156 | varchar |  |  | SI | Pacemaker |
| Q156b | varchar |  |  | SI | Pacemaker OT |
| Q157 | varchar |  |  | SI | Defibrillator |
| Q157b | varchar |  |  | SI | Defibrillator OT |
| Q158 | varchar |  |  | SI | Suitable clothing |
| Q158b | varchar |  |  | SI | Suitable clothing OT |
| Q159 | varchar |  |  | SI | Amount of blood available |
| Q159b | varchar |  |  | SI | Amount of blood available OT |
| Q169 | varchar |  |  | SI | Care provider name |
| Q170 | varchar |  |  | SI | Care provider role |
| Q171 | longvarbinary |  |  | SI | Care provider signature |
| Q171UDt | date |  |  | SI | Care provider signature Last Updated Date |
| Q171UTm | time |  |  | SI | Care provider signature Last Updated Time |
| Q172 | varchar |  |  | SI | OT nurse name |
| Q173 | varchar |  |  | SI | OT nurse role |
| Q174 | longvarbinary |  |  | SI | OT nurse signature |
| Q174UDt | date |  |  | SI | OT nurse signature Last Updated Date |
| Q174UTm | time |  |  | SI | OT nurse signature Last Updated Time |
| Q175 | varchar |  |  | SI | Ward nurse |
| Q176 | varchar |  |  | SI | OT nurse |
| Q208a | varchar |  |  | SI | Routine medications taken |
| Q208b | varchar |  |  | SI | Routine medications taken OT |
| Q209a | varchar |  |  | SI | Gowned, underwear removed	 |
| Q209b | varchar |  |  | SI | Gowned, underwear removed OT |
| Q210a | varchar |  |  | SI | Pacemaker / ICD checked 	 |
| Q211 | varchar |  |  | SI | Dentures |
| Q211a | date |  |  | SI | Pacemaker date	 |
| Q211b | date |  |  | SI | Pacemaker date OT |
| Q212 | varchar |  |  | SI | Dentures OT |
| Q212a | varchar |  |  | SI | Anti-embolism stockings on patient and correctly f... |
| Q212b | varchar |  |  | SI | Anti-embolism stockings on patient and correctly f... |
| Q213a | varchar |  |  | SI | Are there any pressure areas or areas of frail ski... |
| Q213b | varchar |  |  | SI | Are there any pressure areas or areas of frail ski... |
| Q214a | date |  |  | SI | Skin / Pressure areas date last checked |
| Q214b | date |  |  | SI | Skin / Pressure areas date last checked OT |
| Q215a | time |  |  | SI | Skin / Pressure areas time last checked |
| Q215b | time |  |  | SI | Skin / Pressure areas time last checked OT |
| Q216 | varchar |  |  | SI | Nursing / Care Assessment |
| Q217 | varchar |  |  | SI | Additional information (anxiety, dementia, mobilit... |
| Q218 | varchar |  |  | SI | Nursing / Care assessment notes |
| Q219 | varchar |  |  | SI | Ward staff name	 |
| Q220 | varchar |  |  | SI | Theatre staff name	 |
| Q221 | varchar |  |  | SI | Catheter or drain present |
| Q222 | varchar |  |  | SI | Catheter or drain present OT |
| Q223 | varchar |  |  | SI | Intravenous access |
| Q224 | varchar |  |  | SI | Intravenous access	OT |
| Q225 | varchar |  |  | SI | Side rails up |
| Q226 | varchar |  |  | SI | Side rails up OT |
| Q227 | varchar |  |  | SI | Language barrier |
| Q228 | varchar |  |  | SI | Language barrier OT |
| Q229 | varchar |  |  | SI | Pre-operative instruction given |
| Q230 | varchar |  |  | SI | Pre-operative instruction given OT |
| Q231 | varchar |  |  | SI | Special precautions |
| Q232 | varchar |  |  | SI | All notes and comments reviewed |
| Q233 | date |  |  | SI | Date |
| Q234 | time |  |  | SI | Time |
| Q235 | varchar |  |  | SI | Modes of transportation |
| Q236 | varchar |  |  | SI | Other |
| Q237 | varchar |  |  | SI | Known motor / articular difficulties |
| Q238 | varchar |  |  | SI | Patient fasting |
| Q239 | varchar |  |  | SI | Bowel preparation taken |
| Q240 | varchar |  |  | SI | Antiplatelet and antithrombotic therapy suspended |
| Q241 | varchar |  |  | SI | Has the procedure for taking charge of personal ef... |
| Q242 | varchar |  |  | SI | Marking of the surgical site |
| Q243 | date |  |  | SI | Date |
| Q244 | time |  |  | SI | Time |
| Q245 | varchar |  |  | SI | Proposed operation comments |
| Q246 | varchar |  |  | SI | Jewellery removed |
| Q247 | varchar |  |  | SI | Jewellery removed OT |
| Q248 | varchar |  |  | SI | Jewellery taped |
| Q249 | varchar |  |  | SI | Jewellery taped OT |
| Q250 | varchar |  |  | SI | Hair clips removed |
| Q251 | varchar |  |  | SI | Hair clips removed OT |
| Q252 | varchar |  |  | SI | Hair clips added |
| Q253 | varchar |  |  | SI | Hair clips added OT |
| Q254 | varchar |  |  | SI | Make up / Nail varnish removed |
| Q255 | varchar |  |  | SI | Make up / Nail varnish removed OT |
| Q256 | time |  |  | SI | COVID-19 screening time last performed OT |
| Q257 | varchar |  |  | SI | Has the COVID-19 screening being performed? |
| Q258 | varchar |  |  | SI | COVID-19 test type |
| Q259 | date |  |  | SI | COVID-19 screening date last performed |
| Q260 | time |  |  | SI | COVID-19 screening time last performed |
| Q261 | varchar |  |  | SI | COVID-19 screening results |
| Q262 | varchar |  |  | SI | Has the COVID-19 screening being performed? OT |
| Q263 | varchar |  |  | SI | COVID-19 test type OT |
| Q264 | date |  |  | SI | COVID-19 screening date last performed OT |
| Q265 | varchar |  |  | SI | COVID-19 screening results OT |
| Q266c | varchar |  |  | SI | Jewellery removed / taped |
| Q267 | varchar |  |  | SI | Medical imaging comments |
| Q267b | varchar |  |  | SI | Medical imaging comments OT |
| Q268 | varchar |  |  | SI | Chlorhexidine bath |
| Q268b | varchar |  |  | SI | Chlorhexidine bath OT |
| Q269 | varchar |  |  | SI | Bowel preparation notes |
| Q270 | varchar |  |  | SI | Medical / Carers certificate required |
| Q271 | varchar |  |  | SI | Medical / Carers certificate required OT |
| Q272 | varchar |  |  | SI | Plan for tissue not required for pathology testing |
| Q273 | varchar |  |  | SI | Plan for tissue not required for pathology testing... |
| Q274 | time |  |  | SI | Time antibiotic administered |
| Q275 | time |  |  | SI | Time antibiotic administered OT |
| Q276 | time |  |  | SI | Time antithrombotic administered |
| Q277 | time |  |  | SI | Time antithrombotic administered OT |
| Q278 | varchar |  |  | SI | Routine medication details |
| Q279 | varchar |  |  | SI | Routine medication details OT |
| Q280 | varchar |  |  | SI | Medication patches on |
| Q281 | varchar |  |  | SI | Medication patches on OT |
| Q282 | varchar |  |  | SI | ID band correct and in place OT |
| Q283 | varchar |  |  | SI | Side rails up OT |
| Q284 | varchar |  |  | SI | Last food date OT |
| Q285 | varchar |  |  | SI | Last fluid date OT |
| Q286 | varchar |  |  | SI | Last voided date OT |
| Q287 | varchar |  |  | SI | Bowels last opened OT |
| Q288 | varchar |  |  | SI | Valid consent signed OT |
| Q289 | varchar |  |  | SI | Language barrier OT |
| Q290 | varchar |  |  | SI | Pre-operative instruction given OT |
| Q291 | varchar |  |  | SI | Consent incomplete action taken OT |
| Q292 | varchar |  |  | SI | Note OT |
| Q293 | varchar |  |  | SI | Medical / Carers certificate required OT |
| Q294 | varchar |  |  | SI | Allergies recorded OT |
| Q295 | varchar |  |  | SI | Plan for tissue not required for pathology testing... |
| Q296 | varchar |  |  | SI | Procedural area prepared / marked OT |
| Q297 | varchar |  |  | SI | Premed given and recorded OT |
| Q298 | varchar |  |  | SI | Date premed given OT |
| Q299 | varchar |  |  | SI | Blood results available OT |
| Q300 | varchar |  |  | SI | Enema |
| Q301 | varchar |  |  | SI | Is clotting normal OT |
| Q302 | varchar |  |  | SI | Anti-coagulant checked OT |
| Q303 | varchar |  |  | SI | Platelets checked OT |
| Q304 | varchar |  |  | SI | Group and save requested OT |
| Q305 | varchar |  |  | SI | Cross match specimen sent OT |
| Q306 | varchar |  |  | SI | Cross-matched blood available OT |
| Q307 | varchar |  |  | SI | Amount of blood available OT |
| Q308 | varchar |  |  | SI | Valid blood consent signed OT |
| Q309 | varchar |  |  | SI | ECG attended OT |
| Q310 | varchar |  |  | SI | Patient's medical imaging available OT |
| Q311 | varchar |  |  | SI | Medical imaging comments OT |
| Q312 | varchar |  |  | SI | Pacemaker OT |
| Q313 | varchar |  |  | SI | Pacemaker date OT |
| Q314 | varchar |  |  | SI | Defibrillator OT |
| Q315 | varchar |  |  | SI | Dentures removed / in situ OT |
| Q316 | varchar |  |  | SI | Dentition comments OT |
| Q317 | varchar |  |  | SI | Contact lenses / glasses removed OT |
| Q318 | varchar |  |  | SI | Prosthesis / Hearing aid OT |
| Q319 | varchar |  |  | SI | Prosthesis specify OT |
| Q320 | varchar |  |  | SI | Type / Location OT |
| Q321 | varchar |  |  | SI | Hair clips added OT |
| Q322 | varchar |  |  | SI | Shaved / Hair clipped OT |
| Q323 | varchar |  |  | SI | Chlorhexidine bath OT |
| Q324 | varchar |  |  | SI | Suitable clothing OT |
| Q325 | varchar |  |  | SI | Multi resistant organism OT |
| Q326 | varchar |  |  | SI | CJD assessment OT |
| Q327 | varchar |  |  | SI | Catheter or drain present OT |
| Q328 | varchar |  |  | SI | Intravenous access OT |
| Q329 | varchar |  |  | SI | TEDS / Calf compressors OT |
| Q330 | varchar |  |  | SI | Anti-embolism stockings on patient and correctly f... |
| Q331 | varchar |  |  | SI | Antibiotic prescribed OT |
| Q332 | varchar |  |  | SI | Antibiotic given OT |
| Q333 | varchar |  |  | SI | Time antibiotic administered OT |
| Q334 | varchar |  |  | SI | Antithrombotic prescribed OT |
| Q335 | varchar |  |  | SI | Antithrombotic given OT |
| Q336 | varchar |  |  | SI | Time antithrombotic administered OT |
| Q337 | varchar |  |  | SI | Has a pregnancy test been performed? OT |
| Q338 | varchar |  |  | SI | Is the patient pregnant? OT |
| Q339 | varchar |  |  | SI | LMP OT |
| Q340 | varchar |  |  | SI | Has the COVID-19 screening being performed? OT |
| Q341 | varchar |  |  | SI | COVID-19 test type OT |
| Q342 | varchar |  |  | SI | COVID-19 screening date last performed OT |
| Q343 | varchar |  |  | SI | COVID-19 screening results OT |
| Q344 | varchar |  |  | SI | Routine medications taken OT |
| Q345 | varchar |  |  | SI | Routine medication details OT |
| Q346 | varchar |  |  | SI | Medication patches on OT |
| Q347 | varchar |  |  | SI | Gowned, underwear removed OT |
| Q348 | varchar |  |  | SI | Are there any pressure areas or areas of frail ski... |
| Q349 | varchar |  |  | SI | Skin / Pressure areas date last checked OT |
| Q350 | varchar |  |  | SI | Dentures OT |
| Q351 | varchar |  |  | SI | Jewellery removed / taped OT |
| Q352 | varchar |  |  | SI | Hair clips / make up / nail varnish removed OT |
| Q43 | varchar |  |  | SI | Contact lenses / glasses removed |
| Q43b | varchar |  |  | SI | Contact lenses / glasses removed OT |
| Q45 | date |  |  | SI | Last fluid date |
| Q45b | date |  |  | SI | Last fluid date OT |
| Q45c | time |  |  | SI | Last fluid time |
| Q45d | time |  |  | SI | Last fluid time OT |
| Q49 | varchar |  |  | SI | TEDS / Calf compressors |
| Q49b | varchar |  |  | SI | TEDS / Calf compressors OT |
| Q51 | varchar |  |  | SI | Multi resisant organism |
| Q51b | varchar |  |  | SI | Multi resisant organism OT |
| Q53 | varchar |  |  | SI | Creutzfeldt-Jakob Disease |
| Q53b | varchar |  |  | SI | Creutzfeldt-Jakob Disease OT |
| Q55 | varchar |  |  | SI | ECG attended |
| Q55b | varchar |  |  | SI | ECG attended OT |
| Q57 | varchar |  |  | SI | Blood results available |
| Q57b | varchar |  |  | SI | Blood results available OT |
| Q59 | varchar |  |  | SI | Cross-matched blood available |
| Q59b | varchar |  |  | SI | Cross-matched blood available OT |
| Q5a | varchar |  |  | SI | Procedural area prepared / marked |
| Q60 | varchar |  |  | SI | Is clotting normal |
| Q60b | varchar |  |  | SI | Is clotting normal OT |
| Q60c | varchar |  |  | SI | Anti-coagulant checked |
| Q60d | varchar |  |  | SI | Anti-coagulant checked OT |
| Q60e | varchar |  |  | SI | Platelets checked |
| Q60f | varchar |  |  | SI | Platelets checked OT |
| Q60g | varchar |  |  | SI | Group and save requested |
| Q60h | varchar |  |  | SI | Group and save requested OT |
| Q60i | varchar |  |  | SI | Cross match specimen sent |
| Q60j | varchar |  |  | SI | Cross match specimen sent OT |
| Q61 | varchar |  |  | SI | Note |
| Q62 | varchar |  |  | SI | Valid blood consent signed |
| Q62b | varchar |  |  | SI | Valid blood consent signed OT |
| Q64 | varchar |  |  | SI | Allergies recorded |
| Q64b | varchar |  |  | SI | Allergies recorded OT |
| Q66 | varchar |  |  | SI | Proposed operation |
| Q66a | varchar |  |  | SI | Proposed procedure |
| Q67 | varchar |  |  | SI | Weight |
| Q67ObsDR | varchar |  | FK | SI | Weight DR |
| Q68 | varchar |  |  | SI | Height |
| Q68ObsDR | varchar |  | FK | SI | Height DR |
| Q70 | varchar |  |  | SI | Ward check |
| Q71 | varchar |  |  | SI | OT check |
| Q73 | varchar |  |  | SI | Procedure room notified |
| Q74 | varchar |  |  | SI | On anticoagulants |
| Q75 | varchar |  |  | SI | Bowel prep |
| Q76 | varchar |  |  | SI | Shaved / Hair clipped |
| Q76b | varchar |  |  | SI | Shaved / Hair clipped OT |
| Q77 | varchar |  |  | SI | History of infectious diseases |
| Q78 | varchar |  |  | SI | Comment (history of infectious diseases) |
| Q79 | varchar |  |  | SI | Indwelling catheter in situ |
| Q80 | varchar |  |  | SI | Indwelling catheter in situ OT |
| Q81 | varchar |  |  | SI | Smoker |
| Q82 | varchar |  |  | SI | Ex smoker |
| Q83 | varchar |  |  | SI | Ex smoker comment |
| Q84 | varchar |  |  | SI | Diabetic |
| Q85 | varchar |  |  | SI | BSL on admission |
| Q86 | varchar |  |  | SI | Asthmatic |
| Q87 | varchar |  |  | SI | Sleep apnoea |
| Q88 | varchar |  |  | SI | Is CPAP present |
| Q89 | date |  |  | SI | Last dose date (anticoagulants) |
| Q90 | varchar |  |  | SI | Patient ready for theatre |
| Q91 | varchar |  |  | SI | CJD risk |
| Q92 | varchar |  |  | SI | CJD risk note |
| Q93 | varchar |  |  | SI | Clinical handover |
| Q94 | varchar |  |  | SI | Previous anaesthetic |
| Q95 | varchar |  |  | SI | Previous anaesthetic notes |
| Q96 | varchar |  |  | SI | Hearing aid removed |
| Q97 | date |  |  | SI | Patient ready for theatre - date |
| Q98 | time |  |  | SI | Patient ready for theatre - time |
| Q99 | varchar |  |  | SI | Hovermatt in situ |
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