# SQLUser.OR_An_Oper_Circul_Nurse

**Schema:** SQLUser
**Columnas:** 350
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Pabellón Quirúrgico**. Gestión de cirugías.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CIRN_ParRef | varchar | PK |  | NO | OR_Anaest_Operation Parent Reference |
| CIRN_CTCP_DR | varchar |  | FK | SI | Des Ref to CTCP |
| CIRN_Childsub | double |  |  | NO | Childsub |
| CIRN_RowId | varchar |  |  | NO | - |
| CQ02c | - |  |  | SI | (null) |
| CQ02d | - |  |  | SI | (null) |
| CQ110 | - |  |  | SI | (null) |
| CQ208a | - |  |  | SI | (null) |
| CQ208b | - |  |  | SI | (null) |
| CQ400 | - |  |  | SI | (null) |
| CQ401 | - |  |  | SI | (null) |
| CQ403 | - |  |  | SI | (null) |
| CQ404 | - |  |  | SI | (null) |
| CQ405 | - |  |  | SI | (null) |
| CQ406 | - |  |  | SI | (null) |
| Q01 | - |  |  | SI | ID band correct and in place |
| Q01b | - |  |  | SI | ID band correct and in place OT |
| Q02 | - |  |  | SI | Valid consent signed |
| Q02b | - |  |  | SI | Valid consent signed OT |
| Q02c | - |  |  | SI | Consent incomplete action taken |
| Q02d | - |  |  | SI | Consent incomplete action taken OT |
| Q02n | - |  |  | SI | Note |
| Q02not | - |  |  | SI | Note OT |
| Q03c | - |  |  | SI | Time premed given |
| Q03d | - |  |  | SI | Time premed given OT |
| Q06 | - |  |  | SI | Hearing aid |
| Q06b | - |  |  | SI | Hearing aid OT |
| Q06c | - |  |  | SI | Type / Location |
| Q06e | - |  |  | SI | Type / Location OT |
| Q06f | - |  |  | SI | Prosthesis specify	 |
| Q06g | - |  |  | SI | Prosthesis specify	 |
| Q07 | - |  |  | SI | Last food time |
| Q07b | - |  |  | SI | Last food time OT |
| Q07c | - |  |  | SI | Last food date |
| Q07d | - |  |  | SI | Last food at date OT |
| Q08c | - |  |  | SI | Dentures removed / insitu |
| Q08d | - |  |  | SI | Dentures removed / insitu OT |
| Q08e | - |  |  | SI | Dentition comments |
| Q08f | - |  |  | SI | Dentition comments OT |
| Q100 | - |  |  | SI | Hearing aid removed |
| Q101 | - |  |  | SI | Proposed operation |
| Q102 | - |  |  | SI | Proposed operation |
| Q103 | - |  |  | SI | Surgeon |
| Q104 | - |  |  | SI | Bowel prep result |
| Q105 | - |  |  | SI | History of infectious diseases |
| Q106 | - |  |  | SI | History of infectious diseases |
| Q107 | - |  |  | SI | Skin condition |
| Q108 | - |  |  | SI | Discharge planning |
| Q109 | - |  |  | SI | Please specify list / name of anticoagulants |
| Q11 | - |  |  | SI | Last voided time |
| Q110 | - |  |  | SI | Ward status |
| Q111 | - |  |  | SI | Entering user |
| Q112 | - |  |  | SI | Hovermatt insitu |
| Q113 | - |  |  | SI | Pads in situ |
| Q114 | - |  |  | SI | Continent |
| Q115 | - |  |  | SI | Completed by ward nurse |
| Q116 | - |  |  | SI | Ward completed date |
| Q117 | - |  |  | SI | Ward completed time |
| Q118 | - |  |  | SI | Inform: surgeon |
| Q119 | - |  |  | SI | Inform: surgeon OT |
| Q11b | - |  |  | SI | Last voided time OT |
| Q11c | - |  |  | SI | Last voided date |
| Q11d | - |  |  | SI | Last voided date OT |
| Q120 | - |  |  | SI | Inform: assistant surgeon |
| Q121 | - |  |  | SI | Inform: anesthesiologist |
| Q122 | - |  |  | SI | Inform: anesthesiologist OT |
| Q123 | - |  |  | SI | Inform: assistant surgeon OT |
| Q124 | - |  |  | SI | Assessment: assessment and history contrast media |
| Q125 | - |  |  | SI | Assessment: assessment and history contrast media ... |
| Q126 | - |  |  | SI | Assessment: history / physical examination OT |
| Q127 | - |  |  | SI | Assessment: pre and post conscious sedation |
| Q128 | - |  |  | SI | Assessment: pre and post conscious sedation OT |
| Q129 | - |  |  | SI | Assessment: history / physical examination |
| Q130 | - |  |  | SI | Assessment: preoperative medical assessment as pol... |
| Q131 | - |  |  | SI | Assessment: preoperative medical assessment as pol... |
| Q132 | - |  |  | SI | Skin / Eye preparation |
| Q133 | - |  |  | SI | Skin / Eye preparation OT |
| Q134 | - |  |  | SI | SSE / Fleet enema / NSE |
| Q135 | - |  |  | SI | SSE / Fleet enema / NSE OT |
| Q136 | - |  |  | SI | Medication brought to procedure unit |
| Q137 | - |  |  | SI | Medication brought to procedure unit OT |
| Q138 | - |  |  | SI | Equipment brought to procedure unit |
| Q139 | - |  |  | SI | Equipment brought to procedure unit OT |
| Q140 | - |  |  | SI | Pedal pulse marked both side |
| Q141 | - |  |  | SI | Pedal pulse marked both side OT |
| Q142 | - |  |  | SI | Film |
| Q143 | - |  |  | SI | Film OT |
| Q144 | - |  |  | SI | Bowels last opened |
| Q145 | - |  |  | SI | Bowels last opened OT |
| Q147 | - |  |  | SI | Bowels last opened time |
| Q148 | - |  |  | SI | Bowels last opened time OT |
| Q154 | - |  |  | SI | Has a pregnancy test been performed? |
| Q154b | - |  |  | SI | Has a pregnancy test been performed? OT |
| Q155 | - |  |  | SI | Is the patient pregnant? |
| Q155b | - |  |  | SI | Is the patient pregnant? OT |
| Q155c | - |  |  | SI | LMP |
| Q155d | - |  |  | SI | LMP OT |
| Q156 | - |  |  | SI | Pacemaker |
| Q156b | - |  |  | SI | Pacemaker OT |
| Q157 | - |  |  | SI | Defibrillator |
| Q157b | - |  |  | SI | Defibrillator OT |
| Q169 | - |  |  | SI | Care provider name |
| Q170 | - |  |  | SI | Care provider role |
| Q171 | - |  |  | SI | Care provider signature |
| Q171UDt | - |  |  | SI | Care provider signature Last Updated Date |
| Q171UTm | - |  |  | SI | Care provider signature Last Updated Time |
| Q172 | - |  |  | SI | OT nurse name |
| Q173 | - |  |  | SI | OT nurse role |
| Q174 | - |  |  | SI | OT nurse signature |
| Q174UDt | - |  |  | SI | OT nurse signature Last Updated Date |
| Q174UTm | - |  |  | SI | OT nurse signature Last Updated Time |
| Q175 | - |  |  | SI | Ward nurse |
| Q176 | - |  |  | SI | OT nurse |
| Q208a | - |  |  | SI | Routine medications taken |
| Q208b | - |  |  | SI | Routine medications taken OT |
| Q210a | - |  |  | SI | Pacemaker / ICD checked 	 |
| Q211 | - |  |  | SI | Dentures |
| Q211a | - |  |  | SI | Pacemaker date	 |
| Q211b | - |  |  | SI | Pacemaker date OT |
| Q212 | - |  |  | SI | Dentures OT |
| Q213a | - |  |  | SI | Are there any pressure areas or areas of frail ski... |
| Q213b | - |  |  | SI | Are there any pressure areas or areas of frail ski... |
| Q214a | - |  |  | SI | Skin / Pressure areas date last checked |
| Q214b | - |  |  | SI | Skin / Pressure areas date last checked OT |
| Q215a | - |  |  | SI | Skin / Pressure areas time last checked |
| Q215b | - |  |  | SI | Skin / Pressure areas time last checked OT |
| Q216 | - |  |  | SI | Nursing / Care assessment	 |
| Q217 | - |  |  | SI | Additional information (anxiety, dementia, mobilit... |
| Q218 | - |  |  | SI | Nursing / Care assessment notes |
| Q219 | - |  |  | SI | Ward staff name	 |
| Q220 | - |  |  | SI | Theatre staff name	 |
| Q221 | - |  |  | SI | Catheter or drain present |
| Q222 | - |  |  | SI | Catheter or drain present OT |
| Q223 | - |  |  | SI | Intravenous access |
| Q224 | - |  |  | SI | Intravenous access	OT |
| Q225 | - |  |  | SI | Side rails up |
| Q226 | - |  |  | SI | Side rails up OT |
| Q227 | - |  |  | SI | Language barrier |
| Q228 | - |  |  | SI | Language barrier OT |
| Q229 | - |  |  | SI | Pre-procedure instructions given |
| Q230 | - |  |  | SI | Pre-procedure instructions given OT |
| Q231 | - |  |  | SI | Special precautions |
| Q232 | - |  |  | SI | All notes and comments reviewed |
| Q233 | - |  |  | SI | Date |
| Q234 | - |  |  | SI | Time |
| Q236 | - |  |  | SI | Other |
| Q237 | - |  |  | SI | Known motor / articular difficulties |
| Q238 | - |  |  | SI | Patient fasting |
| Q239 | - |  |  | SI | Bowel preparation taken |
| Q241 | - |  |  | SI | Has the procedure for taking charge of personal ef... |
| Q244 | - |  |  | SI | Time |
| Q245 | - |  |  | SI | Proposed operation comments |
| Q246 | - |  |  | SI | Jewellery removed |
| Q247 | - |  |  | SI | Jewellery removed OT |
| Q248 | - |  |  | SI | Jewellery taped |
| Q249 | - |  |  | SI | Jewellery taped OT |
| Q250 | - |  |  | SI | Hair clips removed |
| Q251 | - |  |  | SI | Hair clips removed OT |
| Q252 | - |  |  | SI | Hair clips added |
| Q253 | - |  |  | SI | Hair clips added OT |
| Q254 | - |  |  | SI | Make up / Nail varnish removed |
| Q255 | - |  |  | SI | Make up / Nail varnish removed OT |
| Q256 | - |  |  | SI | Covid-19 screening time last performed OT |
| Q257 | - |  |  | SI | Has the Covid-19 screening being performed? |
| Q258 | - |  |  | SI | Covid test type |
| Q259 | - |  |  | SI | Covid-19 screening date last performed |
| Q260 | - |  |  | SI | Covid-19 screening time last performed |
| Q261 | - |  |  | SI | Covid-19 screening results |
| Q262 | - |  |  | SI | Has the Covid-19 screening being performed? OT |
| Q263 | - |  |  | SI | Covid test type OT |
| Q264 | - |  |  | SI | Covid-19 screening date last performed OT |
| Q265 | - |  |  | SI | Covid-19 screening results OT |
| Q266c | - |  |  | SI | Jewelery removed / Taped |
| Q267 | - |  |  | SI | Medical imaging comments |
| Q267b | - |  |  | SI | Medical imaging comments OT |
| Q268 | - |  |  | SI | Chlorhexidine bath |
| Q268b | - |  |  | SI | Chlorhexidine bath OT |
| Q269 | - |  |  | SI | Bowel preparation notes |
| Q270 | - |  |  | SI | Medical / Carers certificate required |
| Q271 | - |  |  | SI | Medical / Carers certificate required OT |
| Q272 | - |  |  | SI | Plan for tissue not required for pathology testing |
| Q273 | - |  |  | SI | Plan for tissue not required for pathology testing... |
| Q274 | - |  |  | SI | Time antibiotic administered |
| Q275 | - |  |  | SI | Time antibiotic administered OT |
| Q276 | - |  |  | SI | Time antithrombotic administered |
| Q277 | - |  |  | SI | Time antithrombotic administered OT |
| Q278 | - |  |  | SI | Routine medication details |
| Q279 | - |  |  | SI | Routine medication details OT |
| Q280 | - |  |  | SI | Medication patches on |
| Q281 | - |  |  | SI | Medication patches on OT |
| Q282 | - |  |  | SI | ID band correct and in place OT |
| Q283 | - |  |  | SI | Side rails up OT |
| Q284 | - |  |  | SI | Last food date OT |
| Q285 | - |  |  | SI | Last fluid date OT |
| Q286 | - |  |  | SI | Last voided date OT |
| Q287 | - |  |  | SI | Bowels last opened OT |
| Q288 | - |  |  | SI | Valid consent signed OT |
| Q289 | - |  |  | SI | Language barrier OT |
| Q290 | - |  |  | SI | Pre-procedure instructions given OT |
| Q291 | - |  |  | SI | Consent incomplete action taken OT |
| Q292 | - |  |  | SI | Note OT |
| Q293 | - |  |  | SI | Medical / Carers certificate required OT |
| Q294 | - |  |  | SI | Allergies recorded OT |
| Q295 | - |  |  | SI | Plan for tissue not required for pathology testing... |
| Q300 | - |  |  | SI | Enema |
| Q309 | - |  |  | SI | ECG attended OT |
| Q311 | - |  |  | SI | Medical imaging comments OT |
| Q312 | - |  |  | SI | Pacemaker OT |
| Q313 | - |  |  | SI | Pacemaker date OT |
| Q314 | - |  |  | SI | Defibrillator OT |
| Q315 | - |  |  | SI | Dentures removed / insitu OT |
| Q316 | - |  |  | SI | Dentition comments OT |
| Q317 | - |  |  | SI | Contact lenses / glasses removed OT |
| Q318 | - |  |  | SI | Hearing aid OT |
| Q319 | - |  |  | SI | Prosthesis specify OT |
| Q320 | - |  |  | SI | Type / Location OT |
| Q321 | - |  |  | SI | Hair clips added OT |
| Q323 | - |  |  | SI | Chlorhexidine bath OT |
| Q325 | - |  |  | SI | Multi resistant organism OT |
| Q326 | - |  |  | SI | CJD assessment OT |
| Q327 | - |  |  | SI | Catheter or drain present OT |
| Q328 | - |  |  | SI | Intravenous access OT |
| Q333 | - |  |  | SI | Time antibiotic administered OT |
| Q336 | - |  |  | SI | Time antithrombotic administered OT |
| Q337 | - |  |  | SI | Has a pregnancy test been performed? OT |
| Q338 | - |  |  | SI | Is the patient pregnant? OT |
| Q339 | - |  |  | SI | LMP OT |
| Q340 | - |  |  | SI | Has the Covid-19 screening being performed? OT |
| Q341 | - |  |  | SI | Covid test type OT |
| Q342 | - |  |  | SI | Covid-19 screening date last performed OT |
| Q343 | - |  |  | SI | Covid-19 screening results OT |
| Q344 | - |  |  | SI | Routine medications taken OT |
| Q345 | - |  |  | SI | Routine medication details OT |
| Q346 | - |  |  | SI | Medication patches on OT |
| Q348 | - |  |  | SI | Are there any pressure areas or areas of frail ski... |
| Q349 | - |  |  | SI | Skin / Pressure areas date last checked OT |
| Q350 | - |  |  | SI | Dentures OT |
| Q353 | - |  |  | SI | Contraindicated medication withheld |
| Q354 | - |  |  | SI | Contraindicated medications include benzodiazepine... |
| Q355 | - |  |  | SI | Contraindicated medication withheld OT |
| Q356 | - |  |  | SI | Cochlear implant present |
| Q357 | - |  |  | SI | Cochlear implant present OT |
| Q358 | - |  |  | SI | History of bariatric surgery |
| Q359 | - |  |  | SI | History of bariatric surgery OT |
| Q400 | - |  |  | SI | If this is an emergency ECT, has it been appropria... |
| Q401 | - |  |  | SI | If this is an emergency ECT, has it been appropria... |
| Q402 | - |  |  | SI | Emergency ECT notes |
| Q403 | - |  |  | SI | Permission for trainee / other to be present |
| Q404 | - |  |  | SI | Permission for trainee / other to be present OT |
| Q405 | - |  |  | SI | Electroencephalogram performed |
| Q406 | - |  |  | SI | Electroencephalogram performed OT |
| Q407 | - |  |  | SI | Contraindicated medication withheld OT |
| Q408 | - |  |  | SI | Cochlear implant present OT |
| Q409 | - |  |  | SI | History of bariatric surgery OT |
| Q410 | - |  |  | SI | If this is an emergency ECT, has it been appropria... |
| Q411 | - |  |  | SI | Permission for trainee / other to be present OT |
| Q412 | - |  |  | SI | Electroencephalogram performed OT |
| Q413 | - |  |  | SI | Prosthesis |
| Q414 | - |  |  | SI | Prosthesis OT |
| Q415 | - |  |  | SI | Prosthesis OT |
| Q416 | - |  |  | SI | Emergency ECT notes OT |
| Q417 | - |  |  | SI | Emergency ECT notes OT |
| Q43 | - |  |  | SI | Contact lenses / glasses removed |
| Q43b | - |  |  | SI | Contact lenses / glasses removed OT |
| Q45 | - |  |  | SI | Last fluid date |
| Q45b | - |  |  | SI | Last fluid date OT |
| Q45c | - |  |  | SI | Last fluid time |
| Q45d | - |  |  | SI | Last fluid time OT |
| Q51 | - |  |  | SI | Multi resistant organism |
| Q51b | - |  |  | SI | Multi resistant organism OT |
| Q53 | - |  |  | SI | CJD assessment |
| Q53b | - |  |  | SI | CJD assessment OT |
| Q55 | - |  |  | SI | ECG attended |
| Q55b | - |  |  | SI | ECG attended OT |
| Q61 | - |  |  | SI | Note |
| Q64 | - |  |  | SI | Allergies recorded |
| Q64b | - |  |  | SI | Allergies recorded OT |
| Q66 | - |  |  | SI | Proposed operation |
| Q66a | - |  |  | SI | Proposed procedure |
| Q67 | - |  |  | SI | Weight |
| Q67ObsDR | - |  |  | SI | Weight DR |
| Q68 | - |  |  | SI | Height |
| Q68ObsDR | - |  |  | SI | Height DR |
| Q70 | - |  |  | SI | Ward check |
| Q71 | - |  |  | SI | OT check |
| Q73 | - |  |  | SI | Procedure room notified |
| Q74 | - |  |  | SI | On anticoagulants |
| Q77 | - |  |  | SI | History of infectious diseases |
| Q78 | - |  |  | SI | Comment (history of infectious diseases) |
| Q79 | - |  |  | SI | IDC insitu |
| Q80 | - |  |  | SI | IDC insitu |
| Q81 | - |  |  | SI | Smoker |
| Q82 | - |  |  | SI | Ex smoker |
| Q83 | - |  |  | SI | Ex smoker comment |
| Q84 | - |  |  | SI | Diabetic |
| Q85 | - |  |  | SI | BSL on admission |
| Q86 | - |  |  | SI | Asthmatic |
| Q87 | - |  |  | SI | Sleep apnoea |
| Q88 | - |  |  | SI | Is CPAP present |
| Q89 | - |  |  | SI | Last dose date (anticoagulants) |
| Q90 | - |  |  | SI | Patient ready for theatre |
| Q91 | - |  |  | SI | CJD risk |
| Q92 | - |  |  | SI | CJD risk note |
| Q93 | - |  |  | SI | Clinical handover |
| Q94 | - |  |  | SI | Previous anaesthetic |
| Q95 | - |  |  | SI | Previous anaesthetic notes |
| Q96 | - |  |  | SI | Hearing aid removed |
| Q97 | - |  |  | SI | Patient ready for theatre - date |
| Q98 | - |  |  | SI | Patient ready for theatre - time |
| Q99 | - |  |  | SI | Hovermatt insitu |
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