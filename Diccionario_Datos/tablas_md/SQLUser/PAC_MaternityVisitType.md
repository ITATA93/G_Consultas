# SQLUser.PAC_MaternityVisitType

**Schema:** SQLUser
**Columnas:** 455
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| MATVT_RowId | bigint | PK |  | NO | - |
| MATVT_Code | varchar |  |  | NO | Code |
| MATVT_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| MATVT_CreatedDate | date |  |  | SI | Created Date |
| MATVT_CreatedTime | time |  |  | SI | Created Time |
| MATVT_CreatedUser_DR | bigint |  | FK | SI | Created User |
| MATVT_DateFrom | date |  |  | SI | Date From |
| MATVT_DateTo | date |  |  | SI | Date To |
| MATVT_Desc | varchar |  |  | NO | Description |
| MATVT_Owner | varchar |  |  | SI | Owner |
| MATVT_UpdatedDate | date |  |  | SI | Updated Date |
| MATVT_UpdatedTime | time |  |  | SI | Updated Time |
| MATVT_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | NNS hearing test |
| Q02 | - |  |  | SI | Date |
| Q03 | - |  |  | SI | Note |
| Q04 | - |  |  | SI | Covered by |
| Q05 | - |  |  | SI | Parent present |
| Q06 | - |  |  | SI | Immunisation |
| Q07 | - |  |  | SI | Date |
| Q08 | - |  |  | SI | Note |
| Q09 | - |  |  | SI | Covered by |
| Q10 | - |  |  | SI | Parent present |
| Q100 | - |  |  | SI | Hand washing and limiting visitors to prevent infe... |
| Q101 | - |  |  | SI | Date |
| Q102 | - |  |  | SI | Note |
| Q103 | - |  |  | SI | Covered by |
| Q104 | - |  |  | SI | Parent present |
| Q105 | - |  |  | SI | Signs of unwellness (baby's temp, feeding, stoolin... |
| Q106 | - |  |  | SI | Date |
| Q107 | - |  |  | SI | Note |
| Q108 | - |  |  | SI | Covered by |
| Q109 | - |  |  | SI | Parent present |
| Q11 | - |  |  | SI | Circumcision |
| Q110 | - |  |  | SI | Managing choking or breathing difficulties |
| Q111 | - |  |  | SI | Date |
| Q112 | - |  |  | SI | Covered by |
| Q113 | - |  |  | SI | Parent present |
| Q114 | - |  |  | SI | Note |
| Q115 | - |  |  | SI | Administration of medication |
| Q116 | - |  |  | SI | Date |
| Q117 | - |  |  | SI | Note |
| Q118 | - |  |  | SI | Covered by |
| Q119 | - |  |  | SI | Parent present |
| Q12 | - |  |  | SI | Date |
| Q120 | - |  |  | SI | Emergency plan at home (nearest hospital, emergenc... |
| Q121 | - |  |  | SI | Date |
| Q122 | - |  |  | SI | Note |
| Q123 | - |  |  | SI | Covered by |
| Q124 | - |  |  | SI | Parent present |
| Q125 | - |  |  | SI | Cardiopulmonary resuscitation (CPR) demo |
| Q126 | - |  |  | SI | Date |
| Q127 | - |  |  | SI | Note |
| Q128 | - |  |  | SI | Covered by |
| Q129 | - |  |  | SI | Parent present |
| Q13 | - |  |  | SI | Note |
| Q130 | - |  |  | SI | Cardiopulmonary resuscitation (CPR) return demo |
| Q131 | - |  |  | SI | Date |
| Q132 | - |  |  | SI | Note |
| Q133 | - |  |  | SI | Covered by |
| Q134 | - |  |  | SI | Parent present |
| Q135 | - |  |  | SI | Car seat challenge |
| Q136 | - |  |  | SI | Parent / Guardian name |
| Q137 | - |  |  | SI | Parent / Guardian signature |
| Q137UDt | - |  |  | SI | Parent / Guardian signature Last Updated Date |
| Q137UTm | - |  |  | SI | Parent / Guardian signature Last Updated Time |
| Q138 | - |  |  | SI | Nurse name |
| Q139 | - |  |  | SI | Nurse signature |
| Q139UDt | - |  |  | SI | Nurse signature Last Updated Date |
| Q139UTm | - |  |  | SI | Nurse signature Last Updated Time |
| Q14 | - |  |  | SI | Covered by |
| Q140 | - |  |  | SI | Upon final completion and at time of discharge, re... |
| Q141 | - |  |  | SI | Date |
| Q142 | - |  |  | SI | Note |
| Q143 | - |  |  | SI | Covered by |
| Q144 | - |  |  | SI | Date |
| Q145 | - |  |  | SI | Time |
| Q146 | - |  |  | SI | Recognition of non-nutritive sucking |
| Q147 | - |  |  | SI | Date |
| Q148 | - |  |  | SI | Note |
| Q149 | - |  |  | SI | Covered by |
| Q15 | - |  |  | SI | Parent present |
| Q150 | - |  |  | SI | Hearing loss |
| Q151 | - |  |  | SI | Date |
| Q152 | - |  |  | SI | Note |
| Q153 | - |  |  | SI | Covered by |
| Q156 | - |  |  | SI | Sleeping position: supine or side lying position (... |
| Q157 | - |  |  | SI | Carer education complete |
| Q158 | - |  |  | SI | Date |
| Q159 | - |  |  | SI | Note |
| Q16 | - |  |  | SI | Eye test - Retinopathy of Prematurity (ROP) |
| Q160 | - |  |  | SI | Covered by |
| Q161 | - |  |  | SI | Immunisations correctly documented |
| Q162 | - |  |  | SI | Date |
| Q163 | - |  |  | SI | Note |
| Q164 | - |  |  | SI | Covered by |
| Q165 | - |  |  | SI | Immunisation booklet provided |
| Q166 | - |  |  | SI | Date |
| Q167 | - |  |  | SI | Note |
| Q168 | - |  |  | SI | Covered by |
| Q169 | - |  |  | SI | Discharge drugs prescription provided |
| Q17 | - |  |  | SI | Date |
| Q170 | - |  |  | SI | Date |
| Q171 | - |  |  | SI | Note |
| Q172 | - |  |  | SI | Covered by |
| Q173 | - |  |  | SI | Screening |
| Q174 | - |  |  | SI | Examination of newborn completed |
| Q175 | - |  |  | SI | Date |
| Q176 | - |  |  | SI | Note |
| Q177 | - |  |  | SI | Covered by |
| Q178 | - |  |  | SI | Hearing screen completed |
| Q179 | - |  |  | SI | Date |
| Q18 | - |  |  | SI | Note |
| Q180 | - |  |  | SI | Note |
| Q181 | - |  |  | SI | Covered by |
| Q182 | - |  |  | SI | Eye check completed (if <32 weeks) |
| Q183 | - |  |  | SI | Date |
| Q184 | - |  |  | SI | Note |
| Q185 | - |  |  | SI | Covered by |
| Q186 | - |  |  | SI | Newborn Screening Test (NST) completed |
| Q187 | - |  |  | SI | Date |
| Q188 | - |  |  | SI | Note |
| Q189 | - |  |  | SI | Covered by |
| Q19 | - |  |  | SI | Covered by |
| Q190 | - |  |  | SI | Express breast milk stores taken |
| Q191 | - |  |  | SI | Date |
| Q192 | - |  |  | SI | Note |
| Q193 | - |  |  | SI | Covered by |
| Q194 | - |  |  | SI | Bottle kit ready, if bottle feeding |
| Q195 | - |  |  | SI | Date |
| Q196 | - |  |  | SI | Note |
| Q197 | - |  |  | SI | Covered by |
| Q198 | - |  |  | SI | Breast pump returned |
| Q199 | - |  |  | SI | Date |
| Q20 | - |  |  | SI | Parent present |
| Q200 | - |  |  | SI | Note |
| Q201 | - |  |  | SI | Covered by |
| Q202 | - |  |  | SI | Discharge summary finalised and sent |
| Q203 | - |  |  | SI | Date |
| Q204 | - |  |  | SI | Note |
| Q205 | - |  |  | SI | Covered by |
| Q206 | - |  |  | SI | Admission and discharge book completed |
| Q207 | - |  |  | SI | Date |
| Q208 | - |  |  | SI | Note |
| Q209 | - |  |  | SI | Covered by |
| Q21 | - |  |  | SI | Date |
| Q210 | - |  |  | SI | Day of discharge |
| Q211 | - |  |  | SI | Reception / Administration informed of discharge |
| Q212 | - |  |  | SI | Date |
| Q213 | - |  |  | SI | Note |
| Q214 | - |  |  | SI | Covered by |
| Q215 | - |  |  | SI | Transport arranged and confirmed |
| Q216 | - |  |  | SI | Date |
| Q217 | - |  |  | SI | Note |
| Q218 | - |  |  | SI | Covered by |
| Q219 | - |  |  | SI | Name of person the patient is discharged with |
| Q22 | - |  |  | SI | Note |
| Q220 | - |  |  | SI | Relationship to patient |
| Q221 | - |  |  | SI | Cot card and/or keepsakes prepared |
| Q222 | - |  |  | SI | Date |
| Q223 | - |  |  | SI | Note |
| Q224 | - |  |  | SI | Covered by |
| Q225 | - |  |  | SI | Outpatient appointments required |
| Q226 | - |  |  | SI | Type |
| Q227 | - |  |  | SI | Other referral type |
| Q228 | - |  |  | SI | Relevant community or support service notified of ... |
| Q229 | - |  |  | SI | Date |
| Q23 | - |  |  | SI | Covered by |
| Q230 | - |  |  | SI | Note |
| Q231 | - |  |  | SI | Covered by |
| Q232 | - |  |  | SI | Immunisations and Medications |
| Q233 | - |  |  | SI | Day of Discharge |
| Q234 | - |  |  | SI | Transport |
| Q235 | - |  |  | SI | Follow up and Referral |
| Q236 | - |  |  | SI | Date |
| Q237 | - |  |  | SI | Date |
| Q238 | - |  |  | SI | Date |
| Q239 | - |  |  | SI | Date |
| Q24 | - |  |  | SI | Parent present |
| Q240 | - |  |  | SI | Date |
| Q241 | - |  |  | SI | Date |
| Q242 | - |  |  | SI | Date |
| Q243 | - |  |  | SI | Date |
| Q244 | - |  |  | SI | Date |
| Q245 | - |  |  | SI | Date |
| Q246 | - |  |  | SI | Date |
| Q247 | - |  |  | SI | Date |
| Q248 | - |  |  | SI | Date |
| Q249 | - |  |  | SI | Note |
| Q25 | - |  |  | SI | Follow up arrangements made |
| Q250 | - |  |  | SI | Note |
| Q251 | - |  |  | SI | Note |
| Q252 | - |  |  | SI | Note |
| Q253 | - |  |  | SI | Note |
| Q254 | - |  |  | SI | Note |
| Q255 | - |  |  | SI | Note |
| Q256 | - |  |  | SI | Note |
| Q257 | - |  |  | SI | Note |
| Q258 | - |  |  | SI | Note |
| Q259 | - |  |  | SI | Note |
| Q26 | - |  |  | SI | Date |
| Q260 | - |  |  | SI | Note |
| Q261 | - |  |  | SI | Note |
| Q262 | - |  |  | SI | Covered by |
| Q263 | - |  |  | SI | Covered by |
| Q264 | - |  |  | SI | Covered by |
| Q265 | - |  |  | SI | Covered by |
| Q266 | - |  |  | SI | Covered by |
| Q267 | - |  |  | SI | Covered by |
| Q268 | - |  |  | SI | Covered by |
| Q269 | - |  |  | SI | Covered by |
| Q27 | - |  |  | SI | Note |
| Q270 | - |  |  | SI | Covered by |
| Q271 | - |  |  | SI | Covered by |
| Q272 | - |  |  | SI | Covered by |
| Q273 | - |  |  | SI | Covered by |
| Q274 | - |  |  | SI | Covered by |
| Q275 | - |  |  | SI | Date |
| Q276 | - |  |  | SI | Date |
| Q277 | - |  |  | SI | Date |
| Q278 | - |  |  | SI | Date |
| Q279 | - |  |  | SI | Date |
| Q28 | - |  |  | SI | Covered by |
| Q280 | - |  |  | SI | Date |
| Q281 | - |  |  | SI | Note |
| Q282 | - |  |  | SI | Note |
| Q283 | - |  |  | SI | Note |
| Q284 | - |  |  | SI | Note |
| Q285 | - |  |  | SI | Note |
| Q286 | - |  |  | SI | Note |
| Q287 | - |  |  | SI | Covered by |
| Q288 | - |  |  | SI | Covered by |
| Q289 | - |  |  | SI | Covered by |
| Q29 | - |  |  | SI | Parent present |
| Q290 | - |  |  | SI | Covered by |
| Q291 | - |  |  | SI | Covered by |
| Q292 | - |  |  | SI | Covered by |
| Q293 | - |  |  | SI | Date |
| Q294 | - |  |  | SI | Note |
| Q295 | - |  |  | SI | Covered by |
| Q296 | - |  |  | SI | Date |
| Q297 | - |  |  | SI | Note |
| Q298 | - |  |  | SI | Covered by |
| Q299 | - |  |  | SI | Date |
| Q30 | - |  |  | SI | Breastfeeding - Mother is confident by herself |
| Q300 | - |  |  | SI | Date |
| Q301 | - |  |  | SI | Date |
| Q302 | - |  |  | SI | Date |
| Q303 | - |  |  | SI | Date |
| Q304 | - |  |  | SI | Date |
| Q305 | - |  |  | SI | Date |
| Q306 | - |  |  | SI | Note |
| Q307 | - |  |  | SI | Note |
| Q308 | - |  |  | SI | Note |
| Q309 | - |  |  | SI | Note |
| Q30A | - |  |  | SI | Breastfeeding - mother is confident by herself |
| Q31 | - |  |  | SI | Date |
| Q310 | - |  |  | SI | Note |
| Q311 | - |  |  | SI | Note |
| Q312 | - |  |  | SI | Note |
| Q313 | - |  |  | SI | Covered by |
| Q314 | - |  |  | SI | Covered by |
| Q315 | - |  |  | SI | Covered by |
| Q316 | - |  |  | SI | Covered by |
| Q317 | - |  |  | SI | Covered by |
| Q318 | - |  |  | SI | Covered by |
| Q319 | - |  |  | SI | Covered by |
| Q32 | - |  |  | SI | Note |
| Q320 | - |  |  | SI | Date |
| Q321 | - |  |  | SI | Date |
| Q322 | - |  |  | SI | Date |
| Q323 | - |  |  | SI | Date |
| Q324 | - |  |  | SI | Date |
| Q325 | - |  |  | SI | Date |
| Q326 | - |  |  | SI | Date |
| Q327 | - |  |  | SI | Date |
| Q328 | - |  |  | SI | Date |
| Q329 | - |  |  | SI | Date |
| Q33 | - |  |  | SI | Covered by |
| Q330 | - |  |  | SI | Date |
| Q331 | - |  |  | SI | Date |
| Q332 | - |  |  | SI | Date |
| Q333 | - |  |  | SI | Date |
| Q334 | - |  |  | SI | Date |
| Q335 | - |  |  | SI | Date |
| Q336 | - |  |  | SI | Date |
| Q337 | - |  |  | SI | Date |
| Q338 | - |  |  | SI | Date |
| Q339 | - |  |  | SI | Date |
| Q34 | - |  |  | SI | Parent present |
| Q340 | - |  |  | SI | Date |
| Q341 | - |  |  | SI | Date |
| Q342 | - |  |  | SI | Date |
| Q343 | - |  |  | SI | Date |
| Q344 | - |  |  | SI | Date |
| Q345 | - |  |  | SI | Date |
| Q346 | - |  |  | SI | Note |
| Q347 | - |  |  | SI | Note |
| Q348 | - |  |  | SI | Note |
| Q349 | - |  |  | SI | Note |
| Q35 | - |  |  | SI | Principles of milk preparation |
| Q350 | - |  |  | SI | Note |
| Q351 | - |  |  | SI | Note |
| Q352 | - |  |  | SI | Note |
| Q353 | - |  |  | SI | Note |
| Q354 | - |  |  | SI | Note |
| Q355 | - |  |  | SI | Note |
| Q356 | - |  |  | SI | Note |
| Q357 | - |  |  | SI | Note |
| Q358 | - |  |  | SI | Note |
| Q359 | - |  |  | SI | Note |
| Q36 | - |  |  | SI | Date |
| Q360 | - |  |  | SI | Note |
| Q361 | - |  |  | SI | Note |
| Q362 | - |  |  | SI | Note |
| Q363 | - |  |  | SI | Note |
| Q364 | - |  |  | SI | Note |
| Q365 | - |  |  | SI | Note |
| Q366 | - |  |  | SI | Note |
| Q367 | - |  |  | SI | Note |
| Q368 | - |  |  | SI | Note |
| Q369 | - |  |  | SI | Note |
| Q37 | - |  |  | SI | Note |
| Q370 | - |  |  | SI | Note |
| Q371 | - |  |  | SI | Note |
| Q372 | - |  |  | SI | Covered by |
| Q373 | - |  |  | SI | Covered by |
| Q374 | - |  |  | SI | Covered by |
| Q375 | - |  |  | SI | Covered by |
| Q376 | - |  |  | SI | Covered by |
| Q377 | - |  |  | SI | Covered by |
| Q378 | - |  |  | SI | Covered by |
| Q379 | - |  |  | SI | Covered by |
| Q38 | - |  |  | SI | Covered by |
| Q380 | - |  |  | SI | Covered by |
| Q381 | - |  |  | SI | Covered by |
| Q382 | - |  |  | SI | Covered by |
| Q383 | - |  |  | SI | Covered by |
| Q384 | - |  |  | SI | Covered by |
| Q385 | - |  |  | SI | Covered by |
| Q386 | - |  |  | SI | Covered by |
| Q387 | - |  |  | SI | Covered by |
| Q388 | - |  |  | SI | Covered by |
| Q389 | - |  |  | SI | Covered by |
| Q39 | - |  |  | SI | Parent present |
| Q390 | - |  |  | SI | Covered by |
| Q391 | - |  |  | SI | Covered by |
| Q392 | - |  |  | SI | Covered by |
| Q393 | - |  |  | SI | Covered by |
| Q394 | - |  |  | SI | Covered by |
| Q395 | - |  |  | SI | Covered by |
| Q396 | - |  |  | SI | Covered by |
| Q397 | - |  |  | SI | Covered by |
| Q398 | - |  |  | SI | Covered by |
| Q40 | - |  |  | SI | Bottle feeding techniques |
| Q40A | - |  |  | SI | Bottle feeding techniques |
| Q41 | - |  |  | SI | Date |
| Q42 | - |  |  | SI | Note |
| Q43 | - |  |  | SI | Covered by |
| Q44 | - |  |  | SI | Parent present |
| Q45 | - |  |  | SI | Handling of expressed breast milk (EBM) |
| Q46 | - |  |  | SI | Date |
| Q47 | - |  |  | SI | Note |
| Q48 | - |  |  | SI | Covered by |
| Q49 | - |  |  | SI | Parent present |
| Q50 | - |  |  | SI | Sterilization of feeding accessories |
| Q51 | - |  |  | SI | Date |
| Q52 | - |  |  | SI | Note |
| Q53 | - |  |  | SI | Covered by |
| Q54 | - |  |  | SI | Parent present |
| Q55 | - |  |  | SI | Sleeping position: supine or side lying position (... |
| Q56 | - |  |  | SI | Date |
| Q57 | - |  |  | SI | Note |
| Q58 | - |  |  | SI | Covered by |
| Q59 | - |  |  | SI | Parent present |
| Q60 | - |  |  | SI | Other points (raising the head, pillow use) |
| Q61 | - |  |  | SI | Date |
| Q62 | - |  |  | SI | Note |
| Q63 | - |  |  | SI | Covered by |
| Q64 | - |  |  | SI | Parent present |
| Q65 | - |  |  | SI | Confident with baby bath |
| Q66 | - |  |  | SI | Date |
| Q67 | - |  |  | SI | Note |
| Q68 | - |  |  | SI | Covered by |
| Q69 | - |  |  | SI | Parent present |
| Q70 | - |  |  | SI | Confident with baby care (umbilical, nappy care) |
| Q71 | - |  |  | SI | Date |
| Q72 | - |  |  | SI | Note |
| Q73 | - |  |  | SI | Covered by |
| Q74 | - |  |  | SI | Parent present |
| Q75 | - |  |  | SI | Understand about the elimination patterns (urine, ... |
| Q76 | - |  |  | SI | Date |
| Q77 | - |  |  | SI | Note |
| Q78 | - |  |  | SI | Covered by |
| Q79 | - |  |  | SI | Parent present |
| Q80 | - |  |  | SI | Being able to identify deviations from normal |
| Q81 | - |  |  | SI | Date |
| Q82 | - |  |  | SI | Note |
| Q83 | - |  |  | SI | Covered by |
| Q84 | - |  |  | SI | Parent present |
| Q85 | - |  |  | SI | Aware of swaddling techniques |
| Q86 | - |  |  | SI | Date |
| Q87 | - |  |  | SI | Note |
| Q88 | - |  |  | SI | Covered by |
| Q89 | - |  |  | SI | Parent present |
| Q90 | - |  |  | SI | Control baby's temperature (room temp, clothing la... |
| Q91 | - |  |  | SI | Date |
| Q92 | - |  |  | SI | Note |
| Q93 | - |  |  | SI | Covered by |
| Q94 | - |  |  | SI | Parent present |
| Q95 | - |  |  | SI | Infant cues (hungry, tired, pain) |
| Q96 | - |  |  | SI | Date |
| Q97 | - |  |  | SI | Note |
| Q98 | - |  |  | SI | Covered by |
| Q99 | - |  |  | SI | Parent present |
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