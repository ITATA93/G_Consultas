# SQLUser.OR_AnaestAirwayCircuit

**Schema:** SQLUser
**Columnas:** 517
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Pabellón Quirúrgico**. Gestión de cirugías.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ANACIRC_ParRef | varchar | PK |  | NO | MR_Adm Parent Reference |
| ANACIRC_Childsub | double |  |  | NO | Childsub |
| ANACIRC_RowId | varchar |  |  | NO | - |
| ANACIRC_Type_DR | bigint |  | FK | SI | Des Ref ORCAirwayCircuit |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Allergen being tested |
| Q04 | - |  |  | SI | Date of last Skin Prick Test (SPT) to allergen |
| Q05 | - |  |  | SI | Size of wheal (mm) |
| Q06 | - |  |  | SI | Size of flare (mm) |
| Q07 | - |  |  | SI | Family provided food for challenge |
| Q08 | - |  |  | SI | Previous reaction to allergen |
| Q09 | - |  |  | SI | Worst documented reaction to allergen |
| Q10 | - |  |  | SI | Other reaction to allergen |
| Q100 | - |  |  | SI | 5 - Time |
| Q101 | - |  |  | SI | 5 - Skin - Pruritus |
| Q102 | - |  |  | SI | 5 - Skin - Urticaria / Angioedema |
| Q103 | - |  |  | SI | 5 - Skin - Rash |
| Q104 | - |  |  | SI | 5 - Upper Resp - Sneezing / Itching |
| Q105 | - |  |  | SI | 5 - Lower Resp - Wheezing |
| Q106 | - |  |  | SI | 5 - Lower Resp - Laryngeal |
| Q107 | - |  |  | SI | 5 - GIT - Subjective |
| Q108 | - |  |  | SI | 5 - GIT - Objective |
| Q109 | - |  |  | SI | 5 - CVS |
| Q11 | - |  |  | SI | Last clinical reaction to allergen |
| Q110 | - |  |  | SI | 5 - Notes |
| Q111 | - |  |  | SI | 6 - Dose |
| Q112 | - |  |  | SI | 6 - Time |
| Q113 | - |  |  | SI | 6 - Skin - Pruritus |
| Q114 | - |  |  | SI | 6 - Skin - Urticaria / Angioedema |
| Q115 | - |  |  | SI | 6 - Skin - Rash |
| Q116 | - |  |  | SI | 6 - Upper Resp - Sneezing / Itching |
| Q117 | - |  |  | SI | 6 - Lower Resp - Wheezing |
| Q118 | - |  |  | SI | 6 - Lower Resp - Laryngeal |
| Q119 | - |  |  | SI | 6 - GIT - Subjective |
| Q12 | - |  |  | SI | Patient had allergen in question since booking |
| Q120 | - |  |  | SI | 6 - GIT - Objective |
| Q121 | - |  |  | SI | 6 - CVS |
| Q122 | - |  |  | SI | 6 - Notes |
| Q123 | - |  |  | SI | 7 - Dose |
| Q124 | - |  |  | SI | 7 - Time |
| Q125 | - |  |  | SI | 7 - Skin - Pruritus |
| Q126 | - |  |  | SI | 7 - Skin - Urticaria / Angioedema |
| Q127 | - |  |  | SI | 7 - Skin - Rash |
| Q128 | - |  |  | SI | 7 - Upper Resp - Sneezing / Itching |
| Q129 | - |  |  | SI | 7 - Lower Resp - Wheezing |
| Q13 | - |  |  | SI | Did the patient react |
| Q130 | - |  |  | SI | 7 - Lower Resp - Laryngeal |
| Q131 | - |  |  | SI | 7 - GIT - Subjective |
| Q132 | - |  |  | SI | 7 - GIT - Objective |
| Q133 | - |  |  | SI | 7 - CVS |
| Q134 | - |  |  | SI | 7 - Notes |
| Q135 | - |  |  | SI | 8 - Dose |
| Q136 | - |  |  | SI | 8 - Time |
| Q137 | - |  |  | SI | 8 - Skin - Pruritus |
| Q138 | - |  |  | SI | 8 - Skin - Urticaria / Angioedema |
| Q139 | - |  |  | SI | 8 - Skin - Rash |
| Q14 | - |  |  | SI | Clinician notified |
| Q140 | - |  |  | SI | 8 - Upper Resp - Sneezing / Itching |
| Q141 | - |  |  | SI | 8 - Lower Resp - Wheezing |
| Q142 | - |  |  | SI | 8 - Lower Resp - Laryngeal |
| Q143 | - |  |  | SI | 8 - GIT - Subjective |
| Q144 | - |  |  | SI | 8 - GIT - Objective |
| Q145 | - |  |  | SI | 8 - CVS |
| Q146 | - |  |  | SI | 8 - Notes |
| Q147 | - |  |  | SI | 9 - Dose |
| Q148 | - |  |  | SI | 9 - Time |
| Q149 | - |  |  | SI | 9 - Skin - Pruritus |
| Q15 | - |  |  | SI | Notified clinician |
| Q150 | - |  |  | SI | 9 - Skin - Urticaria / Angioedema |
| Q151 | - |  |  | SI | 9 - Skin - Rash |
| Q152 | - |  |  | SI | 9 - Upper Resp - Sneezing / Itching |
| Q153 | - |  |  | SI | 9 - Lower Resp - Wheezing |
| Q154 | - |  |  | SI | 9 - Lower Resp - Laryngeal |
| Q155 | - |  |  | SI | 9 - GIT - Subjective |
| Q156 | - |  |  | SI | 9 - GIT - Objective |
| Q157 | - |  |  | SI | 9 - CVS |
| Q158 | - |  |  | SI | 9 - Notes |
| Q159 | - |  |  | SI | 10 - Dose |
| Q16 | - |  |  | SI | Discussion details |
| Q160 | - |  |  | SI | 10 - Time |
| Q161 | - |  |  | SI | 10 - Skin - Pruritus |
| Q162 | - |  |  | SI | 10 - Skin - Urticaria / Angioedema |
| Q163 | - |  |  | SI | 10 - Skin - Rash |
| Q164 | - |  |  | SI | 10 - Upper Resp - Sneezing / Itching |
| Q165 | - |  |  | SI | 10 - Lower Resp - Wheezing |
| Q166 | - |  |  | SI | 10 - Lower Resp - Laryngeal |
| Q167 | - |  |  | SI | 10 - GIT - Subjective |
| Q168 | - |  |  | SI | 10 - GIT - Objective |
| Q169 | - |  |  | SI | 10 - CVS |
| Q17 | - |  |  | SI | Type of reaction |
| Q170 | - |  |  | SI | 10 - Notes |
| Q171 | - |  |  | SI | 11 - Dose |
| Q172 | - |  |  | SI | 11 - Time |
| Q173 | - |  |  | SI | 11 - Skin - Pruritus |
| Q174 | - |  |  | SI | 11 - Skin - Urticaria / Angioedema |
| Q175 | - |  |  | SI | 11 - Skin - Rash |
| Q176 | - |  |  | SI | 11 - Upper Resp - Sneezing / Itching |
| Q177 | - |  |  | SI | 11 - Lower Resp - Wheezing |
| Q178 | - |  |  | SI | 11 - Lower Resp - Laryngeal |
| Q179 | - |  |  | SI | 11 - GIT - Subjective |
| Q18 | - |  |  | SI | History notes |
| Q180 | - |  |  | SI | 11 - GIT - Objective |
| Q181 | - |  |  | SI | 11 - CVS |
| Q182 | - |  |  | SI | 11 - Notes |
| Q183 | - |  |  | SI | 12 - Dose |
| Q184 | - |  |  | SI | 12 - Time |
| Q185 | - |  |  | SI | 12 - Skin - Pruritus |
| Q186 | - |  |  | SI | 12 - Skin - Urticaria / Angioedema |
| Q187 | - |  |  | SI | 12 - Skin - Rash |
| Q188 | - |  |  | SI | 12 - Upper Resp - Sneezing / Itching |
| Q189 | - |  |  | SI | 12 - Lower Resp - Wheezing |
| Q19 | - |  |  | SI | Patient feeling unwell today |
| Q190 | - |  |  | SI | 12 - Lower Resp - Laryngeal |
| Q191 | - |  |  | SI | 12 - GIT - Subjective |
| Q192 | - |  |  | SI | 12 - GIT - Objective |
| Q193 | - |  |  | SI | 12 - CVS |
| Q194 | - |  |  | SI | 12 - Notes |
| Q195 | - |  |  | SI | 13 - Dose |
| Q196 | - |  |  | SI | 13 - Time |
| Q197 | - |  |  | SI | 13 - Skin - Pruritus |
| Q198 | - |  |  | SI | 13 - Skin - Urticaria / Angioedema |
| Q199 | - |  |  | SI | 13 - Skin - Rash |
| Q20 | - |  |  | SI | Patient has had anti-histamines or steroids in the... |
| Q200 | - |  |  | SI | 13 - Upper Resp - Sneezing / Itching |
| Q201 | - |  |  | SI | 13 - Lower Resp - Wheezing |
| Q202 | - |  |  | SI | 13 - Lower Resp - Laryngeal |
| Q203 | - |  |  | SI | 13 - GIT - Subjective |
| Q204 | - |  |  | SI | 13 - GIT - Objective |
| Q205 | - |  |  | SI | 13 - CVS |
| Q206 | - |  |  | SI | 13 - Notes |
| Q207 | - |  |  | SI | 14 - Dose |
| Q208 | - |  |  | SI | 14 - Time |
| Q209 | - |  |  | SI | 14 - Skin - Pruritus |
| Q21 | - |  |  | SI | Patient has had a recent exacerbation of asthma |
| Q210 | - |  |  | SI | 14 - Skin - Urticaria / Angioedema |
| Q211 | - |  |  | SI | 14 - Skin - Rash |
| Q212 | - |  |  | SI | 14 - Upper Resp - Sneezing / Itching |
| Q213 | - |  |  | SI | 14 - Lower Resp - Wheezing |
| Q214 | - |  |  | SI | 14 - Lower Resp - Laryngeal |
| Q215 | - |  |  | SI | 14 - GIT - Subjective |
| Q216 | - |  |  | SI | 14 - GIT - Objective |
| Q217 | - |  |  | SI | 14 - CVS |
| Q218 | - |  |  | SI | 14 - Notes |
| Q219 | - |  |  | SI | 15 - Dose |
| Q22 | - |  |  | SI | Patient has had a flare up of eczema recently |
| Q220 | - |  |  | SI | 15 - Time |
| Q221 | - |  |  | SI | 15 - Skin - Pruritus |
| Q222 | - |  |  | SI | 15 - Skin - Urticaria / Angioedema |
| Q223 | - |  |  | SI | 15 - Skin - Rash |
| Q224 | - |  |  | SI | 15 - Upper Resp - Sneezing / Itching |
| Q225 | - |  |  | SI | 15 - Lower Resp - Wheezing |
| Q226 | - |  |  | SI | 15 - Lower Resp - Laryngeal |
| Q227 | - |  |  | SI | 15 - GIT - Subjective |
| Q228 | - |  |  | SI | 15 - GIT - Objective |
| Q229 | - |  |  | SI | 15 - CVS |
| Q23 | - |  |  | SI | Patient is safe to have food challenge today |
| Q230 | - |  |  | SI | 15 - Notes |
| Q231 | - |  |  | SI | Total dose consumed |
| Q232 | - |  |  | SI | Variation from protocol |
| Q233 | - |  |  | SI | Variation from protocol details |
| Q234 | - |  |  | SI | Skin - Pruritus |
| Q235 | - |  |  | SI | 0 = Absent |
| Q236 | - |  |  | SI | 1 = Mild, occasional scratching |
| Q237 | - |  |  | SI | 2 = Moderate, scratching continuously for >2 minut... |
| Q238 | - |  |  | SI | 3 = Severe, hard continuous scratching, excoriatio... |
| Q239 | - |  |  | SI | Skin - Urticaria / Angioedema |
| Q24 | - |  |  | SI | If any of the above is YES, notify treating doctor... |
| Q240 | - |  |  | SI | 0 = Absent |
| Q241 | - |  |  | SI | 1 = Mild, <3 hives, or mild lip oedema |
| Q242 | - |  |  | SI | 2 = Moderate, <10 hives but >3, or significant lip... |
| Q243 | - |  |  | SI | 3 = Severe, generalised involvement |
| Q244 | - |  |  | SI | Skin - Rash |
| Q245 | - |  |  | SI | 0 = Absent |
| Q246 | - |  |  | SI | 1 = Mild, a few areas of faint erythema |
| Q247 | - |  |  | SI | 2 = Moderate areas of erythema |
| Q248 | - |  |  | SI | 3 = Severe generalised erythema (>50%) |
| Q249 | - |  |  | SI | Upper Respiratory - Sneezing / Itching |
| Q25 | - |  |  | SI | Clinician notified |
| Q250 | - |  |  | SI | 0 = Absent |
| Q251 | - |  |  | SI | 1 = Mild rare burst, occasional sniffing |
| Q252 | - |  |  | SI | 2 = Moderate bursts <10, intermittent rubbing of n... |
| Q253 | - |  |  | SI | 3 = Severe continuous rubbing of nose and/or eyes,... |
| Q254 | - |  |  | SI | Lower Respiratory - Wheezing |
| Q255 | - |  |  | SI | 1 = Absent |
| Q256 | - |  |  | SI | 2 = Mild expiratory wheezing to auscultation |
| Q257 | - |  |  | SI | 3 = Moderate inspiratory and expiratory wheezing |
| Q258 | - |  |  | SI | 4 = Severe use of accessory muscles, audible wheez... |
| Q259 | - |  |  | SI | Lower Respiratory - Laryngeal |
| Q26 | - |  |  | SI | Recent history notes |
| Q260 | - |  |  | SI | 0 = Absent |
| Q261 | - |  |  | SI | 1 = Mild, >3 discrete episodes of throat clearing ... |
| Q262 | - |  |  | SI | 2 = Moderate hoarseness, frequent dry cough |
| Q263 | - |  |  | SI | 3 = Severe stridor |
| Q264 | - |  |  | SI | Gastrointestinal (GIT) - Subjective complaints |
| Q265 | - |  |  | SI | 0 = Absent |
| Q266 | - |  |  | SI | 1 = Mild complaints of nausea or abdominal pain, i... |
| Q267 | - |  |  | SI | 2 = Moderate frequent complaints of nausea or pain... |
| Q268 | - |  |  | SI | 3 = Severe - notably distressed due to GI symptoms... |
| Q269 | - |  |  | SI | Gastrointestinal (GIT) - Objective complaints |
| Q27 | - |  |  | SI | Anaphylaxis kit |
| Q270 | - |  |  | SI | 0 = Absent |
| Q271 | - |  |  | SI | 1 = Mild, 1 episode of emesis or diarrhoea |
| Q272 | - |  |  | SI | 2 = Moderate, 2-3 episodes of emesis or diarrhoea ... |
| Q273 | - |  |  | SI | 3 = Severe, >3 episodes of emesis or diarrhoea or ... |
| Q274 | - |  |  | SI | Cardiovascular |
| Q275 | - |  |  | SI | 0 = Normal heart rate or blood pressure (BP) for a... |
| Q276 | - |  |  | SI | 1 = Mild subjective response (weak/dizzy), or tach... |
| Q277 | - |  |  | SI | 2 = Moderate - drop in BP and/or >20% from baselin... |
| Q278 | - |  |  | SI | 3 = Severe - cardiovascular collapse, signs of imp... |
| Q279 | - |  |  | SI | Outcome |
| Q28 | - |  |  | SI | Oral food challenge kit |
| Q280 | - |  |  | SI | Treatment of reaction |
| Q281 | - |  |  | SI | Challenge outcome notes |
| Q282 | - |  |  | SI | Medical follow up required |
| Q283 | - |  |  | SI | Follow up notes |
| Q284 | - |  |  | SI | Upcoming challenge |
| Q285 | - |  |  | SI | Upcoming challenge notes |
| Q286 | - |  |  | SI | Recipe needed for upcoming challenge |
| Q287 | - |  |  | SI | Recipe notes |
| Q288 | - |  |  | SI | New prescription adrenaline auto-injector |
| Q289 | - |  |  | SI | New prescription note |
| Q29 | - |  |  | SI | Medical staff and team leader aware of impending f... |
| Q290 | - |  |  | SI | New action plan given |
| Q291 | - |  |  | SI | New action plan notes |
| Q292 | - |  |  | SI | If passed challenge - recipe and information given |
| Q293 | - |  |  | SI | Information provided |
| Q294 | - |  |  | SI | Additional discharge advice provided and follow up... |
| Q295 | - |  |  | SI | Outcome of Challenge Description |
| Q296 | - |  |  | SI | Tolerated |
| Q297 | - |  |  | SI | • Successful completion |
| Q298 | - |  |  | SI | • Call admitting medical officer |
| Q299 | - |  |  | SI | Not Tolerated |
| Q30 | - |  |  | SI | Nursing staff 2:1 available |
| Q300 | - |  |  | SI | • Unsuccessful challenge |
| Q301 | - |  |  | SI | • Review by admitting doctor, observations for 2 h... |
| Q302 | - |  |  | SI | • Follow up outpatient appointment made |
| Q303 | - |  |  | SI | Dose Not Reached |
| Q304 | - |  |  | SI | • Need to rechallenge |
| Q305 | - |  |  | SI | Equivocal |
| Q306 | - |  |  | SI | • Unclear if reacted, need to rechallenge |
| Q307 | - |  |  | SI | 1 - Dose |
| Q308 | - |  |  | SI | 1 - Time |
| Q309 | - |  |  | SI | 1 - Skin - Pruritus |
| Q31 | - |  |  | SI | Monitor for blood pressure and oxygen saturation |
| Q310 | - |  |  | SI | 1 - Skin - Urticaria / Angioedema |
| Q311 | - |  |  | SI | 1 - Skin - Rash |
| Q312 | - |  |  | SI | 1 - Upper Resp - Sneezing / Itching |
| Q313 | - |  |  | SI | 1 - Lower Resp - Wheezing |
| Q314 | - |  |  | SI | 1 - Lower Resp - Laryngeal |
| Q315 | - |  |  | SI | 1 - GIT - Subjective |
| Q316 | - |  |  | SI | 1 - GIT - Objective |
| Q317 | - |  |  | SI | 1 - CVS |
| Q318 | - |  |  | SI | 2 - Dose |
| Q319 | - |  |  | SI | 2 - Time |
| Q32 | - |  |  | SI | Emergency equipment accessible and in working orde... |
| Q320 | - |  |  | SI | 2 - Skin - Pruritus |
| Q321 | - |  |  | SI | 2 - Skin - Urticaria / Angioedema |
| Q322 | - |  |  | SI | 2 - Skin - Rash |
| Q323 | - |  |  | SI | 2 - Upper Resp - Sneezing / Itching |
| Q324 | - |  |  | SI | 2 - Lower Resp - Wheezing |
| Q325 | - |  |  | SI | 2 - Lower Resp - Laryngeal |
| Q326 | - |  |  | SI | 2 - GIT - Subjective |
| Q327 | - |  |  | SI | 2 - GIT - Objective |
| Q328 | - |  |  | SI | 2 - CVS |
| Q329 | - |  |  | SI | 3 - Dose |
| Q33 | - |  |  | SI | Equipment / Resources notes |
| Q330 | - |  |  | SI | 3 - Time |
| Q331 | - |  |  | SI | 3 - Skin - Pruritus |
| Q332 | - |  |  | SI | 3 - Skin - Urticaria / Angioedema |
| Q333 | - |  |  | SI | 3 - Skin - Rash |
| Q334 | - |  |  | SI | 3 - Upper Resp - Sneezing / Itching |
| Q335 | - |  |  | SI | 3 - Lower Resp - Wheezing |
| Q336 | - |  |  | SI | 3 - Lower Resp - Laryngeal |
| Q337 | - |  |  | SI | 3 - GIT - Subjective |
| Q338 | - |  |  | SI | 3 - GIT - Objective |
| Q339 | - |  |  | SI | 3 - CVS |
| Q34 | - |  |  | SI | Adrenaline (epinephrine) dose calculated and drawn... |
| Q340 | - |  |  | SI | 4 - Dose |
| Q341 | - |  |  | SI | 4 - Time |
| Q342 | - |  |  | SI | 4 - Skin - Pruritus |
| Q343 | - |  |  | SI | 4 - Skin - Urticaria / Angioedema |
| Q344 | - |  |  | SI | 4 - Skin - Rash |
| Q345 | - |  |  | SI | 4 - Upper Resp - Sneezing / Itching |
| Q346 | - |  |  | SI | 4 - Lower Resp - Wheezing |
| Q347 | - |  |  | SI | 4 - Lower Resp - Laryngeal |
| Q348 | - |  |  | SI | 4 - GIT - Subjective |
| Q349 | - |  |  | SI | 4 - GIT - Objective |
| Q35 | - |  |  | SI | Loratadine dose ordered and accessible (for relief... |
| Q350 | - |  |  | SI | 4 - CVS |
| Q351 | - |  |  | SI | 5 - Dose |
| Q352 | - |  |  | SI | 5 - Time |
| Q353 | - |  |  | SI | 5 - Skin - Pruritus |
| Q354 | - |  |  | SI | 5 - Skin - Urticaria / Angioedema |
| Q355 | - |  |  | SI | 5 - Skin - Rash |
| Q356 | - |  |  | SI | 5 - Upper Resp - Sneezing / Itching |
| Q357 | - |  |  | SI | 5 - Lower Resp - Wheezing |
| Q358 | - |  |  | SI | 5 - Lower Resp - Laryngeal |
| Q359 | - |  |  | SI | 5 - GIT - Subjective |
| Q36 | - |  |  | SI | Verbal consent to perform challenge obtained and d... |
| Q360 | - |  |  | SI | 5 - GIT - Objective |
| Q361 | - |  |  | SI | 5 - CVS |
| Q362 | - |  |  | SI | 6 - Dose |
| Q363 | - |  |  | SI | 6 - Time |
| Q364 | - |  |  | SI | 6 - Skin - Pruritus |
| Q365 | - |  |  | SI | 6 - Skin - Urticaria / Angioedema |
| Q366 | - |  |  | SI | 6 - Skin - Rash |
| Q367 | - |  |  | SI | 6 - Upper Resp - Sneezing / Itching |
| Q368 | - |  |  | SI | 6 - Lower Resp - Wheezing |
| Q369 | - |  |  | SI | 6 - Lower Resp - Laryngeal |
| Q37 | - |  |  | SI | Medication notes |
| Q370 | - |  |  | SI | 6 - GIT - Subjective |
| Q371 | - |  |  | SI | 6 - GIT - Objective |
| Q372 | - |  |  | SI | 6 - CVS |
| Q373 | - |  |  | SI | 7 - Dose |
| Q374 | - |  |  | SI | 7 - Time |
| Q375 | - |  |  | SI | 7 - Skin - Pruritus |
| Q376 | - |  |  | SI | 7 - Skin - Urticaria / Angioedema |
| Q377 | - |  |  | SI | 7 - Skin - Rash |
| Q378 | - |  |  | SI | 7 - Upper Resp - Sneezing / Itching |
| Q379 | - |  |  | SI | 7 - Lower Resp - Wheezing |
| Q38 | - |  |  | SI | The information below to be completed with each do... |
| Q380 | - |  |  | SI | 7 - Lower Resp - Laryngeal |
| Q381 | - |  |  | SI | 7 - GIT - Subjective |
| Q382 | - |  |  | SI | 7 - GIT - Objective |
| Q383 | - |  |  | SI | 7 - CVS |
| Q384 | - |  |  | SI | 8 - Dose |
| Q385 | - |  |  | SI | 8 - Time |
| Q386 | - |  |  | SI | 8 - Skin - Pruritus |
| Q387 | - |  |  | SI | 8 - Skin - Urticaria / Angioedema |
| Q388 | - |  |  | SI | 8 - Skin - Rash |
| Q389 | - |  |  | SI | 8 - Upper Resp - Sneezing / Itching |
| Q39 | - |  |  | SI | Dose |
| Q390 | - |  |  | SI | 8 - Lower Resp - Wheezing |
| Q391 | - |  |  | SI | 8 - GIT - Subjective |
| Q392 | - |  |  | SI | 8 - GIT - Objective |
| Q393 | - |  |  | SI | 8 - CVS |
| Q394 | - |  |  | SI | 9 - Dose |
| Q395 | - |  |  | SI | 9 - Time |
| Q396 | - |  |  | SI | 9 - Skin - Pruritus |
| Q397 | - |  |  | SI | 9 - Skin - Urticaria / Angioedema |
| Q398 | - |  |  | SI | 9 - Skin - Rash |
| Q399 | - |  |  | SI | 9 - Upper Resp - Sneezing / Itching |
| Q40 | - |  |  | SI | Time |
| Q400 | - |  |  | SI | 9 - Lower Resp - Wheezing |
| Q401 | - |  |  | SI | 9 - Lower Resp - Laryngeal |
| Q402 | - |  |  | SI | 9 - GIT - Subjective |
| Q403 | - |  |  | SI | 9 - GIT - Objective |
| Q404 | - |  |  | SI | 9 - CVS |
| Q405 | - |  |  | SI | 8 - Lower Resp - Laryngeal |
| Q406 | - |  |  | SI | 10 - Dose |
| Q407 | - |  |  | SI | 10 - Time |
| Q408 | - |  |  | SI | 10 - Skin - Pruritus |
| Q409 | - |  |  | SI | 10 - Skin - Urticaria / Angioedema |
| Q41 | - |  |  | SI | Skin - Pruritus |
| Q410 | - |  |  | SI | 10 - Skin - Rash |
| Q411 | - |  |  | SI | 10 - Upper Resp - Sneezing / Itching |
| Q412 | - |  |  | SI | 10 - Lower Resp - Wheezing |
| Q413 | - |  |  | SI | 10 - Lower Resp - Laryngeal |
| Q414 | - |  |  | SI | 10 - GIT - Subjective |
| Q415 | - |  |  | SI | 10 - GIT - Objective |
| Q416 | - |  |  | SI | 10 - CVS |
| Q417 | - |  |  | SI | 11 - Dose |
| Q418 | - |  |  | SI | 11 - Time |
| Q419 | - |  |  | SI | 11 - Skin - Pruritus |
| Q42 | - |  |  | SI | Skin - Urticaria / Angioedema |
| Q420 | - |  |  | SI | 11 - Skin - Urticaria / Angioedema |
| Q421 | - |  |  | SI | 11 - Skin - Rash |
| Q422 | - |  |  | SI | 11 - Upper Resp - Sneezing / Itching |
| Q423 | - |  |  | SI | 11 - Lower Resp - Wheezing |
| Q424 | - |  |  | SI | 11 - Lower Resp - Laryngeal |
| Q425 | - |  |  | SI | 11 - GIT - Subjective |
| Q426 | - |  |  | SI | 11 - GIT - Objective |
| Q427 | - |  |  | SI | 11 - CVS |
| Q428 | - |  |  | SI | 12 - Dose |
| Q429 | - |  |  | SI | 12 - Time |
| Q43 | - |  |  | SI | Skin - Rash |
| Q430 | - |  |  | SI | 12 - Skin - Pruritus |
| Q431 | - |  |  | SI | 12 - Skin - Urticaria / Angioedema |
| Q432 | - |  |  | SI | 12 - Skin - Rash |
| Q433 | - |  |  | SI | 12 - Upper Resp - Sneezing / Itching |
| Q434 | - |  |  | SI | 12 - Lower Resp - Wheezing |
| Q435 | - |  |  | SI | 12 - Lower Resp - Laryngeal |
| Q436 | - |  |  | SI | 12 - GIT - Subjective |
| Q437 | - |  |  | SI | 12 - GIT - Objective |
| Q438 | - |  |  | SI | 12 - CVS |
| Q439 | - |  |  | SI | 13 - Dose |
| Q44 | - |  |  | SI | Upper Resp - Sneezing / Itching |
| Q440 | - |  |  | SI | 13 - Time |
| Q441 | - |  |  | SI | 13 - Skin - Pruritus |
| Q442 | - |  |  | SI | 13 - Skin - Urticaria / Angioedema |
| Q443 | - |  |  | SI | 13 - Skin - Rash |
| Q444 | - |  |  | SI | 13 - Upper Resp - Sneezing / Itching |
| Q445 | - |  |  | SI | 13 - Lower Resp - Wheezing |
| Q446 | - |  |  | SI | 13 - Lower Resp - Laryngeal |
| Q447 | - |  |  | SI | 13 - GIT - Subjective |
| Q448 | - |  |  | SI | 13 - GIT - Objective |
| Q449 | - |  |  | SI | 13 - CVS |
| Q45 | - |  |  | SI | Lower Resp - Wheezing |
| Q450 | - |  |  | SI | 14 - Dose |
| Q451 | - |  |  | SI | 14 - Time |
| Q452 | - |  |  | SI | 14 - Skin - Pruritus |
| Q453 | - |  |  | SI | 14 - Skin - Urticaria / Angioedema |
| Q454 | - |  |  | SI | 14 - Skin - Rash |
| Q455 | - |  |  | SI | 14 - Upper Resp - Sneezing / Itching |
| Q456 | - |  |  | SI | 14 - Lower Resp - Wheezing |
| Q457 | - |  |  | SI | 14 - Lower Resp - Laryngeal |
| Q458 | - |  |  | SI | 14 - GIT - Subjective |
| Q459 | - |  |  | SI | 14 - GIT - Objective |
| Q46 | - |  |  | SI | Lower Resp - Laryngeal |
| Q460 | - |  |  | SI | 14 - CVS |
| Q461 | - |  |  | SI | 15 - Dose |
| Q462 | - |  |  | SI | 15 - Time |
| Q463 | - |  |  | SI | 15 - Skin - Pruritus |
| Q464 | - |  |  | SI | 15 - Skin - Urticaria / Angioedema |
| Q465 | - |  |  | SI | 15 - Skin - Rash |
| Q466 | - |  |  | SI | 15 - Upper Resp - Sneezing / Itching |
| Q467 | - |  |  | SI | 15 -Lower Resp - Wheezing |
| Q468 | - |  |  | SI | 15 - Lower Resp - Laryngeal |
| Q469 | - |  |  | SI | 15 - GIT - Subjective |
| Q47 | - |  |  | SI | GIT - Subjective |
| Q470 | - |  |  | SI | 15 - GIT - Objective |
| Q471 | - |  |  | SI | 15 - CVS |
| Q472 | - |  |  | SI | Other treatment of reaction |
| Q473 | - |  |  | SI | Follow up notes |
| Q48 | - |  |  | SI | GIT - Objective |
| Q49 | - |  |  | SI | CVS |
| Q50 | - |  |  | SI | Notes |
| Q51 | - |  |  | SI | 1 - Dose |
| Q52 | - |  |  | SI | 1 - Time |
| Q53 | - |  |  | SI | 1 - Skin - Pruritus |
| Q54 | - |  |  | SI | 1 - Skin - Urticaria / Angioedema |
| Q55 | - |  |  | SI | 1 - Skin - Rash |
| Q56 | - |  |  | SI | 1 - Upper Resp - Sneezing / Itching |
| Q57 | - |  |  | SI | 1 - Lower Resp - Wheezing |
| Q58 | - |  |  | SI | 1 - Lower Resp - Laryngeal |
| Q59 | - |  |  | SI | 1 - GIT - Subjective |
| Q60 | - |  |  | SI | 1 - GIT - Objective |
| Q61 | - |  |  | SI | 1 - CVS |
| Q62 | - |  |  | SI | 1 - Notes |
| Q63 | - |  |  | SI | 2 - Dose |
| Q64 | - |  |  | SI | 2 - Time |
| Q65 | - |  |  | SI | 2 - Skin - Pruritus |
| Q66 | - |  |  | SI | 2 - Skin - Urticaria / Angioedema |
| Q67 | - |  |  | SI | 2 - Skin - Rash |
| Q68 | - |  |  | SI | 2 - Upper Resp - Sneezing / Itching |
| Q69 | - |  |  | SI | 2 - Lower Resp - Wheezing |
| Q70 | - |  |  | SI | 2 - Lower Resp - Laryngeal |
| Q71 | - |  |  | SI | 2 - GIT - Subjective |
| Q72 | - |  |  | SI | 2 - GIT - Objective |
| Q73 | - |  |  | SI | 2 - CVS |
| Q74 | - |  |  | SI | 2 - Notes |
| Q75 | - |  |  | SI | 3 - Dose |
| Q76 | - |  |  | SI | 3 - Time |
| Q77 | - |  |  | SI | 3 - Skin - Pruritus |
| Q78 | - |  |  | SI | 3 - Skin - Urticaria / Angioedema |
| Q79 | - |  |  | SI | 3 - Skin - Rash |
| Q80 | - |  |  | SI | 3 - Upper Resp - Sneezing / Itching |
| Q81 | - |  |  | SI | 3 - Lower Resp - Wheezing |
| Q82 | - |  |  | SI | 3 - Lower Resp - Laryngeal |
| Q83 | - |  |  | SI | 3 - GIT - Subjective |
| Q84 | - |  |  | SI | 3 - GIT - Objective |
| Q85 | - |  |  | SI | 3 - CVS |
| Q86 | - |  |  | SI | 3 - Notes |
| Q87 | - |  |  | SI | 4 - Dose |
| Q88 | - |  |  | SI | 4 - Time |
| Q89 | - |  |  | SI | 4 - Skin - Pruritus |
| Q90 | - |  |  | SI | 4 - Skin - Urticaria / Angioedema |
| Q91 | - |  |  | SI | 4 - Skin - Rash |
| Q92 | - |  |  | SI | 4 - Upper Resp - Sneezing / Itching |
| Q93 | - |  |  | SI | 4 - Lower Resp - Wheezing |
| Q94 | - |  |  | SI | 4 - Lower Resp - Laryngeal |
| Q95 | - |  |  | SI | 4 - GIT - Subjective |
| Q96 | - |  |  | SI | 4 - GIT - Objective |
| Q97 | - |  |  | SI | 4 - CVS |
| Q98 | - |  |  | SI | 4 - Notes |
| Q99 | - |  |  | SI | 5 - Dose |
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