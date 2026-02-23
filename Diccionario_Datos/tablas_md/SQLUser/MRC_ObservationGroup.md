# SQLUser.MRC_ObservationGroup

**Schema:** SQLUser
**Columnas:** 397
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Registros Médicos**. Parámetros de historia clínica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| GRP_RowId | bigint | PK |  | NO | - |
| GRP_AllowToAddToOtherGroup | varchar |  |  | SI | AllowToAddToOtherGroup |
| GRP_BPSameLine | varchar |  |  | SI | BP Same Line
Display Systolic and Diastolic Items... |
| GRP_Code | varchar |  |  | NO | Code |
| GRP_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| GRP_CreatedDate | date |  |  | SI | Created Date |
| GRP_CreatedTime | time |  |  | SI | Created Time |
| GRP_CreatedUser_DR | bigint |  | FK | SI | Created User |
| GRP_Deprecated | bit |  |  | SI | Deprecated |
| GRP_DeprecatedReason | varchar |  |  | SI | Deprecated Reason |
| GRP_Desc | varchar |  |  | NO | Description |
| GRP_DisableEWSScore | varchar |  |  | SI | Disable EWS Score Calculation |
| GRP_EnableEWS | varchar |  |  | SI | Enable EWS Completeness Warnings |
| GRP_MarkSize | varchar |  |  | SI | MarkSize |
| GRP_ObsStatus_DR | bigint |  | FK | SI | Des Ref ObsStatus |
| GRP_Owner | varchar |  |  | SI | Owner |
| GRP_Purpose | varchar |  |  | SI | Purpose |
| GRP_TableIVDrugs | varchar |  |  | SI | Table IV Drugs |
| GRP_UpdatedDate | date |  |  | SI | Updated Date |
| GRP_UpdatedTime | time |  |  | SI | Updated Time |
| GRP_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| GRP_YAxis1Interval | double |  |  | SI | Y Axis1 Interval |
| GRP_YAxis1Max | double |  |  | SI | Y Axis 1 Max |
| GRP_YAxis1Min | double |  |  | SI | Y Axis 1 Min Value |
| GRP_YAxis2Interval | double |  |  | SI | Y Axis 2 Interval |
| GRP_YAxis2Max | double |  |  | SI | Y Axis 2 Max Value |
| GRP_YAxis2Min | double |  |  | SI | Y Axis 2 Min Value |
| Q01 | - |  |  | SI | Ciclo Nº |
| Q02 | - |  |  | SI | Basal |
| Q03 | - |  |  | SI | Fertilización In Vitro |
| Q04 | - |  |  | SI | Coito Dirigido |
| Q05 | - |  |  | SI | IIU |
| Q06 | - |  |  | SI | Fecha de menstruación |
| Q07 | - |  |  | SI | Esquema |
| Q08 | - |  |  | SI | Clomifeno1 |
| Q09 | - |  |  | SI | FSH |
| Q10 | - |  |  | SI | hCG |
| Q100 | - |  |  | SI | I18 |
| Q101 | - |  |  | SI | D1 |
| Q102 | - |  |  | SI | D2 |
| Q103 | - |  |  | SI | D3 |
| Q104 | - |  |  | SI | D4 |
| Q105 | - |  |  | SI | D5 |
| Q106 | - |  |  | SI | D6 |
| Q107 | - |  |  | SI | D7 |
| Q108 | - |  |  | SI | D8 |
| Q109 | - |  |  | SI | D9 |
| Q11 | - |  |  | SI | Otros |
| Q110 | - |  |  | SI | D10 |
| Q111 | - |  |  | SI | D11 |
| Q112 | - |  |  | SI | D12 |
| Q113 | - |  |  | SI | D13 |
| Q114 | - |  |  | SI | D14 |
| Q115 | - |  |  | SI | D15 |
| Q116 | - |  |  | SI | D16 |
| Q117 | - |  |  | SI | D17 |
| Q118 | - |  |  | SI | D18 |
| Q119 | - |  |  | SI | end1 |
| Q12 | - |  |  | SI | Clomifeno2 |
| Q120 | - |  |  | SI | end2 |
| Q121 | - |  |  | SI | end3 |
| Q122 | - |  |  | SI | end4 |
| Q123 | - |  |  | SI | end5 |
| Q124 | - |  |  | SI | end6 |
| Q125 | - |  |  | SI | end7 |
| Q126 | - |  |  | SI | end8 |
| Q127 | - |  |  | SI | end9 |
| Q128 | - |  |  | SI | end10 |
| Q129 | - |  |  | SI | end11 |
| Q13 | - |  |  | SI | Clomifeno3 |
| Q130 | - |  |  | SI | end12 |
| Q131 | - |  |  | SI | end13 |
| Q132 | - |  |  | SI | end14 |
| Q133 | - |  |  | SI | end14 |
| Q134 | - |  |  | SI | end15 |
| Q135 | - |  |  | SI | end16 |
| Q136 | - |  |  | SI | end17 |
| Q138 | - |  |  | SI | end18 |
| Q139 | - |  |  | SI | ll1 |
| Q14 | - |  |  | SI | Clomifeno4 |
| Q140 | - |  |  | SI | ll2 |
| Q141 | - |  |  | SI | ll3 |
| Q142 | - |  |  | SI | ll4 |
| Q143 | - |  |  | SI | ll5 |
| Q144 | - |  |  | SI | ll6 |
| Q145 | - |  |  | SI | ll7 |
| Q146 | - |  |  | SI | ll8 |
| Q147 | - |  |  | SI | ll9 |
| Q148 | - |  |  | SI | ll10 |
| Q149 | - |  |  | SI | ll11 |
| Q15 | - |  |  | SI | Clomifeno5 |
| Q150 | - |  |  | SI | ll12 |
| Q151 | - |  |  | SI | ll13 |
| Q152 | - |  |  | SI | ll14 |
| Q153 | - |  |  | SI | ll15 |
| Q154 | - |  |  | SI | ll16 |
| Q155 | - |  |  | SI | ll17 |
| Q156 | - |  |  | SI | ll18 |
| Q157 | - |  |  | SI | Observaciones |
| Q158 | - |  |  | SI | Conclusión |
| Q159 | - |  |  | SI | I19 |
| Q16 | - |  |  | SI | Clomifeno6 |
| Q160 | - |  |  | SI | I20 |
| Q161 | - |  |  | SI | I21 |
| Q162 | - |  |  | SI | I22 |
| Q163 | - |  |  | SI | I23 |
| Q164 | - |  |  | SI | I24 |
| Q165 | - |  |  | SI | I25 |
| Q166 | - |  |  | SI | I26 |
| Q167 | - |  |  | SI | I27 |
| Q168 | - |  |  | SI | I28 |
| Q169 | - |  |  | SI | I29 |
| Q17 | - |  |  | SI | Clomifeno7 |
| Q170 | - |  |  | SI | I30 |
| Q171 | - |  |  | SI | I31 |
| Q172 | - |  |  | SI | I32 |
| Q173 | - |  |  | SI | I33 |
| Q174 | - |  |  | SI | I24 |
| Q175 | - |  |  | SI | I35 |
| Q176 | - |  |  | SI | I36 |
| Q177 | - |  |  | SI | I37 |
| Q178 | - |  |  | SI | I38 |
| Q179 | - |  |  | SI | I39 |
| Q18 | - |  |  | SI | Clomifeno8 |
| Q180 | - |  |  | SI | I40 |
| Q181 | - |  |  | SI | I41 |
| Q182 | - |  |  | SI | I42 |
| Q184 | - |  |  | SI | I44 |
| Q186 | - |  |  | SI | I46 |
| Q187 | - |  |  | SI | I47 |
| Q188 | - |  |  | SI | I48 |
| Q189 | - |  |  | SI | I49 |
| Q19 | - |  |  | SI | Clomifeno9 |
| Q190 | - |  |  | SI | I50 |
| Q191 | - |  |  | SI | I51 |
| Q192 | - |  |  | SI | I52 |
| Q193 | - |  |  | SI | I53 |
| Q194 | - |  |  | SI | I54 |
| Q195 | - |  |  | SI | I55 |
| Q196 | - |  |  | SI | I56 |
| Q197 | - |  |  | SI | I57 |
| Q198 | - |  |  | SI | I58 |
| Q199 | - |  |  | SI | I59 |
| Q20 | - |  |  | SI | Clomifeno10 |
| Q200 | - |  |  | SI | I60 |
| Q201 | - |  |  | SI | I61 |
| Q202 | - |  |  | SI | I62 |
| Q203 | - |  |  | SI | I63 |
| Q204 | - |  |  | SI | I64 |
| Q205 | - |  |  | SI | I65 |
| Q206 | - |  |  | SI | I66 |
| Q207 | - |  |  | SI | I67 |
| Q208 | - |  |  | SI | I68 |
| Q209 | - |  |  | SI | I69 |
| Q21 | - |  |  | SI | Clomifeno11 |
| Q210 | - |  |  | SI | I70 |
| Q211 | - |  |  | SI | I71 |
| Q212 | - |  |  | SI | I72 |
| Q213 | - |  |  | SI | I73 |
| Q214 | - |  |  | SI | I74 |
| Q215 | - |  |  | SI | I75 |
| Q216 | - |  |  | SI | I76 |
| Q217 | - |  |  | SI | I77 |
| Q218 | - |  |  | SI | I78 |
| Q219 | - |  |  | SI | I79 |
| Q22 | - |  |  | SI | Clomifeno12 |
| Q220 | - |  |  | SI | I80 |
| Q221 | - |  |  | SI | I81 |
| Q222 | - |  |  | SI | I81 |
| Q223 | - |  |  | SI | I83 |
| Q224 | - |  |  | SI | I84 |
| Q225 | - |  |  | SI | I85 |
| Q226 | - |  |  | SI | I86 |
| Q227 | - |  |  | SI | I87 |
| Q228 | - |  |  | SI | I88 |
| Q229 | - |  |  | SI | I89 |
| Q23 | - |  |  | SI | Clomifeno13 |
| Q230 | - |  |  | SI | I90 |
| Q231 | - |  |  | SI | I91 |
| Q232 | - |  |  | SI | I92 |
| Q233 | - |  |  | SI | I93 |
| Q234 | - |  |  | SI | I94 |
| Q235 | - |  |  | SI | I95 |
| Q236 | - |  |  | SI | I96 |
| Q237 | - |  |  | SI | I97 |
| Q238 | - |  |  | SI | I98 |
| Q239 | - |  |  | SI | I99 |
| Q24 | - |  |  | SI | Clomifeno14 |
| Q240 | - |  |  | SI | I100 |
| Q241 | - |  |  | SI | i101 |
| Q242 | - |  |  | SI | l102 |
| Q243 | - |  |  | SI | I103 |
| Q244 | - |  |  | SI | I104 |
| Q245 | - |  |  | SI | I105 |
| Q246 | - |  |  | SI | I106 |
| Q247 | - |  |  | SI | I107 |
| Q248 | - |  |  | SI | I108 |
| Q249 | - |  |  | SI | I109 |
| Q25 | - |  |  | SI | Clomifeno15 |
| Q250 | - |  |  | SI | I110 |
| Q251 | - |  |  | SI | I111 |
| Q253 | - |  |  | SI | I112 |
| Q254 | - |  |  | SI | I114 |
| Q255 | - |  |  | SI | I115 |
| Q256 | - |  |  | SI | I116 |
| Q257 | - |  |  | SI | I117 |
| Q258 | - |  |  | SI | I118 |
| Q259 | - |  |  | SI | I119 |
| Q26 | - |  |  | SI | Clomifeno16 |
| Q260 | - |  |  | SI | I120 |
| Q261 | - |  |  | SI | I121 |
| Q262 | - |  |  | SI | I122 |
| Q263 | - |  |  | SI | I123 |
| Q264 | - |  |  | SI | I124 |
| Q265 | - |  |  | SI | I125 |
| Q266 | - |  |  | SI | I126 |
| Q267 | - |  |  | SI | I127 |
| Q268 | - |  |  | SI | I128 |
| Q269 | - |  |  | SI | I129 |
| Q27 | - |  |  | SI | Clomifeno17 |
| Q270 | - |  |  | SI | I130 |
| Q271 | - |  |  | SI | I131 |
| Q272 | - |  |  | SI | I132 |
| Q273 | - |  |  | SI | I133 |
| Q274 | - |  |  | SI | I134 |
| Q275 | - |  |  | SI | I135 |
| Q276 | - |  |  | SI | I136 |
| Q277 | - |  |  | SI | I137 |
| Q278 | - |  |  | SI | I138 |
| Q279 | - |  |  | SI | I139 |
| Q28 | - |  |  | SI | Clomifeno18 |
| Q280 | - |  |  | SI | I140 |
| Q281 | - |  |  | SI | I141 |
| Q282 | - |  |  | SI | I142 |
| Q283 | - |  |  | SI | I143 |
| Q284 | - |  |  | SI | I144 |
| Q285 | - |  |  | SI | I145 |
| Q286 | - |  |  | SI | I146 |
| Q287 | - |  |  | SI | I147 |
| Q288 | - |  |  | SI | I148 |
| Q289 | - |  |  | SI | I149 |
| Q29 | - |  |  | SI | FSH1 |
| Q290 | - |  |  | SI | I150 |
| Q291 | - |  |  | SI | I151 |
| Q292 | - |  |  | SI | I152 |
| Q293 | - |  |  | SI | I153 |
| Q294 | - |  |  | SI | I154 |
| Q295 | - |  |  | SI | I155 |
| Q296 | - |  |  | SI | I156 |
| Q297 | - |  |  | SI | I157 |
| Q298 | - |  |  | SI | I157 |
| Q299 | - |  |  | SI | I159 |
| Q30 | - |  |  | SI | FSH2 |
| Q300 | - |  |  | SI | I160 |
| Q301 | - |  |  | SI | I161 |
| Q302 | - |  |  | SI | I162 |
| Q303 | - |  |  | SI | I163 |
| Q304 | - |  |  | SI | I164 |
| Q305 | - |  |  | SI | I165 |
| Q306 | - |  |  | SI | I166 |
| Q307 | - |  |  | SI | I167 |
| Q308 | - |  |  | SI | I168 |
| Q309 | - |  |  | SI | I169 |
| Q31 | - |  |  | SI | FSH3 |
| Q310 | - |  |  | SI | I170 |
| Q311 | - |  |  | SI | I171 |
| Q312 | - |  |  | SI | I172 |
| Q313 | - |  |  | SI | I173 |
| Q314 | - |  |  | SI | I174 |
| Q315 | - |  |  | SI | i175 |
| Q316 | - |  |  | SI | I176 |
| Q317 | - |  |  | SI | I177 |
| Q318 | - |  |  | SI | I178 |
| Q319 | - |  |  | SI | I178 |
| Q32 | - |  |  | SI | FSH4 |
| Q320 | - |  |  | SI | I180 |
| Q321 | - |  |  | SI | I181 |
| Q322 | - |  |  | SI | I182 |
| Q323 | - |  |  | SI | I183 |
| Q324 | - |  |  | SI | D19 |
| Q325 | - |  |  | SI | D20 |
| Q326 | - |  |  | SI | D21 |
| Q327 | - |  |  | SI | D22 |
| Q328 | - |  |  | SI | D23 |
| Q329 | - |  |  | SI | D24 |
| Q33 | - |  |  | SI | FSH5 |
| Q330 | - |  |  | SI | D25 |
| Q331 | - |  |  | SI | D26 |
| Q332 | - |  |  | SI | D27 |
| Q333 | - |  |  | SI | D28 |
| Q334 | - |  |  | SI | D29 |
| Q34 | - |  |  | SI | FSH6 |
| Q35 | - |  |  | SI | FSH7 |
| Q36 | - |  |  | SI | FSH8 |
| Q37 | - |  |  | SI | FSH9 |
| Q38 | - |  |  | SI | FSH10 |
| Q39 | - |  |  | SI | FSH11 |
| Q40 | - |  |  | SI | FSH12 |
| Q41 | - |  |  | SI | FSH13 |
| Q42 | - |  |  | SI | FSH14 |
| Q43 | - |  |  | SI | FSH15 |
| Q44 | - |  |  | SI | FSH16 |
| Q45 | - |  |  | SI | FSH17 |
| Q46 | - |  |  | SI | FSH18 |
| Q47 | - |  |  | SI | hCG1 |
| Q48 | - |  |  | SI | hCG2 |
| Q49 | - |  |  | SI | hCG3 |
| Q50 | - |  |  | SI | hCG4 |
| Q51 | - |  |  | SI | hCG5 |
| Q52 | - |  |  | SI | hCG6 |
| Q53 | - |  |  | SI | hCG7 |
| Q54 | - |  |  | SI | hCG8 |
| Q55 | - |  |  | SI | hCG9 |
| Q56 | - |  |  | SI | hCG10 |
| Q57 | - |  |  | SI | hCG11 |
| Q58 | - |  |  | SI | hCG12 |
| Q59 | - |  |  | SI | hCG13 |
| Q60 | - |  |  | SI | hCG14 |
| Q61 | - |  |  | SI | hCG15 |
| Q62 | - |  |  | SI | hCG16 |
| Q63 | - |  |  | SI | hCG17 |
| Q64 | - |  |  | SI | hCG18 |
| Q65 | - |  |  | SI | Otros1 |
| Q66 | - |  |  | SI | Otros2 |
| Q67 | - |  |  | SI | Otros3 |
| Q68 | - |  |  | SI | Otros4 |
| Q69 | - |  |  | SI | Otros5 |
| Q70 | - |  |  | SI | Otros6 |
| Q71 | - |  |  | SI | Otros7 |
| Q72 | - |  |  | SI | Otros8 |
| Q73 | - |  |  | SI | Otros9 |
| Q74 | - |  |  | SI | Otros10 |
| Q75 | - |  |  | SI | Otros11 |
| Q76 | - |  |  | SI | Otros12 |
| Q77 | - |  |  | SI | Otros13 |
| Q78 | - |  |  | SI | Otros14 |
| Q79 | - |  |  | SI | Otros15 |
| Q80 | - |  |  | SI | Otros16 |
| Q81 | - |  |  | SI | Otros17 |
| Q82 | - |  |  | SI | Otros18 |
| Q83 | - |  |  | SI | I1 |
| Q84 | - |  |  | SI | I2 |
| Q85 | - |  |  | SI | I3 |
| Q86 | - |  |  | SI | I4 |
| Q87 | - |  |  | SI | I5 |
| Q88 | - |  |  | SI | I6 |
| Q89 | - |  |  | SI | I7 |
| Q90 | - |  |  | SI | I8 |
| Q91 | - |  |  | SI | I9 |
| Q92 | - |  |  | SI | I10 |
| Q93 | - |  |  | SI | I11 |
| Q94 | - |  |  | SI | I12 |
| Q95 | - |  |  | SI | I13 |
| Q96 | - |  |  | SI | I14 |
| Q97 | - |  |  | SI | I15 |
| Q98 | - |  |  | SI | I16 |
| Q99 | - |  |  | SI | I17 |
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