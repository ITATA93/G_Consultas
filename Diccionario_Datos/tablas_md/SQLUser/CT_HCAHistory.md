# SQLUser.CT_HCAHistory

**Schema:** SQLUser
**Columnas:** 429
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema. Histórico de cambios.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| HCAHIST_RowId | bigint | PK |  | NO | - |
| HCAHIST_CTZip_DR | bigint |  | FK | SI | Des Ref CTZip |
| HCAHIST_ChangeDate | date |  |  | SI | Change Date From |
| HCAHIST_ChangeDateTo | date |  |  | SI | Change Date To |
| HCAHIST_ChangeTime | time |  |  | SI | Change Time From |
| HCAHIST_ChangeTimeTo | time |  |  | SI | Change Time To |
| HCAHIST_ChangeUser_DR | bigint |  | FK | SI | Des Ref User |
| HCAHIST_ComponentID | varchar |  |  | SI | ComponentID  |
| HCAHIST_CreatedDate | date |  |  | SI | Created Date |
| HCAHIST_CreatedTime | time |  |  | SI | Created Time |
| HCAHIST_CreatedUser_DR | bigint |  | FK | SI | Created User |
| HCAHIST_FromHCA_DR | bigint |  | FK | SI | Des Ref CTHealthCareArea |
| HCAHIST_PACClinic_DR | bigint |  | FK | SI | Des Ref PACClinic |
| HCAHIST_PACRefDoctor_DR | bigint |  | FK | SI | Des Ref PACRefDoctor |
| HCAHIST_ToHCA_DR | bigint |  | FK | SI | Des Ref CTHealthCareArea |
| HCAHIST_UpdatedDate | date |  |  | SI | Updated Date |
| HCAHIST_UpdatedTime | time |  |  | SI | Updated Time |
| HCAHIST_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Substance |
| Q02 | - |  |  | SI | Concentration |
| Q03 | - |  |  | SI | Reactivity at 48 hours |
| Q04 | - |  |  | SI | Reactivity at 72 hours |
| Q05 | - |  |  | SI | Reactivity at 96 hours |
| Q06 | - |  |  | SI | Nickel sulphate |
| Q07 | - |  |  | SI | 200 µg/cm2 |
| Q08 | - |  |  | SI | Nickel sulphate |
| Q09 | - |  |  | SI | Nickel sulphate |
| Q10 | - |  |  | SI | Wool alcohols |
| Q100 | - |  |  | SI | 27 µg/cm2 |
| Q101 | - |  |  | SI | Thiuram mix |
| Q102 | - |  |  | SI | Diazolidinyl urea |
| Q103 | - |  |  | SI | 550 µg/cm2 |
| Q104 | - |  |  | SI | Diazolidinyl urea |
| Q105 | - |  |  | SI | Diazolidinyl urea |
| Q106 | - |  |  | SI | Quinoline mix |
| Q107 | - |  |  | SI | 190 µg/cm2 |
| Q108 | - |  |  | SI | Quinoline mix |
| Q109 | - |  |  | SI | Quinoline mix |
| Q11 | - |  |  | SI | 1000 µg/cm2 |
| Q110 | - |  |  | SI | Tixocortol - 21 - pivalate |
| Q111 | - |  |  | SI | 3 µg/cm2 |
| Q112 | - |  |  | SI | Tixocortol - 21 - pivalate |
| Q113 | - |  |  | SI | Tixocortol - 21 - pivalate |
| Q114 | - |  |  | SI | Gold sodium thiosulfate |
| Q115 | - |  |  | SI | 75 µg/cm2 |
| Q116 | - |  |  | SI | Gold sodium thiosulfate |
| Q117 | - |  |  | SI | Gold sodium thiosulfate |
| Q118 | - |  |  | SI | Imidazolidinyl urea |
| Q119 | - |  |  | SI | 600 µg/cm2 |
| Q12 | - |  |  | SI | Wool alcohols |
| Q120 | - |  |  | SI | Imidazolidinyl urea |
| Q121 | - |  |  | SI | Imidazolidinyl urea |
| Q122 | - |  |  | SI | Budesonide |
| Q123 | - |  |  | SI | 1 µg/cm2 |
| Q124 | - |  |  | SI | Budesonide |
| Q125 | - |  |  | SI | Budesonide |
| Q126 | - |  |  | SI | Hydrocortisone - 17 - butyrate |
| Q127 | - |  |  | SI | 20 µg/cm2 |
| Q128 | - |  |  | SI | Hydrocortisone - 17 - butyrate |
| Q129 | - |  |  | SI | Hydrocortisone - 17 - butyrate |
| Q13 | - |  |  | SI | Wool alcohols |
| Q130 | - |  |  | SI | Mercaptobenzothiazole |
| Q131 | - |  |  | SI | 75 µg/cm2 |
| Q132 | - |  |  | SI | Mercaptobenzothiazole |
| Q133 | - |  |  | SI | Mercaptobenzothiazole |
| Q134 | - |  |  | SI | Bacitracin |
| Q135 | - |  |  | SI | 600 µg/cm2 |
| Q136 | - |  |  | SI | Bacitracin |
| Q137 | - |  |  | SI | Bacitracin |
| Q138 | - |  |  | SI | Parthenolide |
| Q139 | - |  |  | SI | 3 µg/cm2 |
| Q14 | - |  |  | SI | Neomycin sulfate |
| Q140 | - |  |  | SI | Parthenolide |
| Q141 | - |  |  | SI | Parthenolide |
| Q142 | - |  |  | SI | Disperse blue 106 |
| Q143 | - |  |  | SI | 50 µg/cm2 |
| Q144 | - |  |  | SI | Disperse Blue 106 |
| Q145 | - |  |  | SI | Disperse Blue 106 |
| Q146 | - |  |  | SI | 2 - Bromo - 2 - Nitropropane -1 , 3 - diol |
| Q147 | - |  |  | SI | 250 µg/cm2 |
| Q148 | - |  |  | SI | 2 - Bromo - 2 - Nitropropane -1 , 3 - diol |
| Q149 | - |  |  | SI | 2 - Bromo - 2 - Nitropropane -1 , 3 - diol |
| Q15 | - |  |  | SI | 600 µg/cm2 |
| Q150 | - |  |  | SI | Comments |
| Q151 | - |  |  | SI | Date |
| Q152 | - |  |  | SI | Time |
| Q153 | - |  |  | SI | Nickel sulphate |
| Q154 | - |  |  | SI | Wool alcohols |
| Q155 | - |  |  | SI | Neomycin sulfate |
| Q156 | - |  |  | SI | Potassium dichromate |
| Q157 | - |  |  | SI | Caine mix |
| Q158 | - |  |  | SI | Fragrance mix |
| Q159 | - |  |  | SI | Colophony |
| Q16 | - |  |  | SI | Neomycin sulfate |
| Q160 | - |  |  | SI | Paraben mix |
| Q161 | - |  |  | SI | Negative control |
| Q162 | - |  |  | SI | Balsam of peru |
| Q163 | - |  |  | SI | Ethylenediamine dihydrochloride |
| Q164 | - |  |  | SI | Cobalt dichloride |
| Q165 | - |  |  | SI | p-tert butylphenol formaldehyde resin |
| Q166 | - |  |  | SI | Epoxy resin |
| Q167 | - |  |  | SI | Carba mix |
| Q168 | - |  |  | SI | Black rubber mix |
| Q169 | - |  |  | SI | Cl+ me- isothiazolinone |
| Q17 | - |  |  | SI | Neomycin sulfate |
| Q170 | - |  |  | SI | Quaternium - 15 |
| Q171 | - |  |  | SI | Methyldibromo glutaronitrile |
| Q172 | - |  |  | SI | p - phenylenediamine |
| Q173 | - |  |  | SI | Formaldehyde |
| Q174 | - |  |  | SI | Mercapto mix |
| Q175 | - |  |  | SI | Thimerosal |
| Q176 | - |  |  | SI | Thiuram mix |
| Q177 | - |  |  | SI | Diazolidinyl urea |
| Q178 | - |  |  | SI | Quinoline mix |
| Q179 | - |  |  | SI | Tixocortol - 21 - pivalate |
| Q18 | - |  |  | SI | Potassium dichromate |
| Q180 | - |  |  | SI | Gold sodium thiosulfate |
| Q181 | - |  |  | SI | Imidazolidinyl urea |
| Q182 | - |  |  | SI | Budesonide |
| Q183 | - |  |  | SI | Hydrocortisone - 17 - butyrate |
| Q184 | - |  |  | SI | Mercaptobenzothiazole |
| Q185 | - |  |  | SI | Bacitracin |
| Q186 | - |  |  | SI | Parthenolide |
| Q187 | - |  |  | SI | Disperse blue 106 |
| Q188 | - |  |  | SI | 2 - Bromo - 2 - Nitropropane -1 , 3 - diol |
| Q189 | - |  |  | SI | Comments |
| Q19 | - |  |  | SI | 54 µg/cm2 |
| Q190 | - |  |  | SI | Substance |
| Q191 | - |  |  | SI | Substance |
| Q192 | - |  |  | SI | Substance |
| Q193 | - |  |  | SI | Substance |
| Q194 | - |  |  | SI | Substance |
| Q195 | - |  |  | SI | Substance |
| Q196 | - |  |  | SI | Substance |
| Q197 | - |  |  | SI | Substance |
| Q198 | - |  |  | SI | Substance |
| Q199 | - |  |  | SI | Substance |
| Q20 | - |  |  | SI | Potassium dichromate |
| Q200 | - |  |  | SI | Substance |
| Q201 | - |  |  | SI | Substance |
| Q202 | - |  |  | SI | Substance |
| Q203 | - |  |  | SI | Substance |
| Q204 | - |  |  | SI | Substance |
| Q205 | - |  |  | SI | Substance |
| Q206 | - |  |  | SI | Substance |
| Q207 | - |  |  | SI | Substance |
| Q208 | - |  |  | SI | Substance |
| Q209 | - |  |  | SI | Substance |
| Q21 | - |  |  | SI | Potassium dichromate |
| Q210 | - |  |  | SI | Substance |
| Q211 | - |  |  | SI | Substance |
| Q212 | - |  |  | SI | Substance |
| Q213 | - |  |  | SI | Substance |
| Q214 | - |  |  | SI | Substance |
| Q215 | - |  |  | SI | Substance |
| Q216 | - |  |  | SI | Substance |
| Q217 | - |  |  | SI | Substance |
| Q218 | - |  |  | SI | Substance |
| Q219 | - |  |  | SI | Substance |
| Q22 | - |  |  | SI | Caine mix |
| Q220 | - |  |  | SI | Substance |
| Q221 | - |  |  | SI | Substance |
| Q222 | - |  |  | SI | Substance |
| Q223 | - |  |  | SI | Substance |
| Q224 | - |  |  | SI | Substance |
| Q225 | - |  |  | SI | Substance |
| Q226 | - |  |  | SI | Substance |
| Q227 | - |  |  | SI | Concentration |
| Q228 | - |  |  | SI | Concentration |
| Q229 | - |  |  | SI | Concentration |
| Q23 | - |  |  | SI | 630 µg/cm2 |
| Q230 | - |  |  | SI | Concentration |
| Q231 | - |  |  | SI | Concentration |
| Q232 | - |  |  | SI | Concentration |
| Q233 | - |  |  | SI | Concentration |
| Q234 | - |  |  | SI | Concentration |
| Q235 | - |  |  | SI | Concentration |
| Q236 | - |  |  | SI | Concentration |
| Q237 | - |  |  | SI | Concentration |
| Q238 | - |  |  | SI | Concentration |
| Q239 | - |  |  | SI | Concentration |
| Q24 | - |  |  | SI | Caine mix |
| Q240 | - |  |  | SI | Concentration |
| Q241 | - |  |  | SI | Concentration |
| Q242 | - |  |  | SI | Concentration |
| Q243 | - |  |  | SI | Concentration |
| Q244 | - |  |  | SI | Concentration |
| Q245 | - |  |  | SI | Concentration |
| Q246 | - |  |  | SI | Concentration |
| Q247 | - |  |  | SI | Concentration |
| Q248 | - |  |  | SI | Concentration |
| Q249 | - |  |  | SI | Concentration |
| Q25 | - |  |  | SI | Caine mix |
| Q250 | - |  |  | SI | Concentration |
| Q251 | - |  |  | SI | Concentration |
| Q252 | - |  |  | SI | Concentration |
| Q253 | - |  |  | SI | Concentration |
| Q254 | - |  |  | SI | Concentration |
| Q255 | - |  |  | SI | Concentration |
| Q256 | - |  |  | SI | Concentration |
| Q257 | - |  |  | SI | Concentration |
| Q258 | - |  |  | SI | Concentration |
| Q259 | - |  |  | SI | Concentration |
| Q26 | - |  |  | SI | Fragrance mix |
| Q260 | - |  |  | SI | Concentration |
| Q261 | - |  |  | SI | Concentration |
| Q262 | - |  |  | SI | Concentration |
| Q263 | - |  |  | SI | Reactivity at 48 hours |
| Q264 | - |  |  | SI | Reactivity at 48 hours |
| Q265 | - |  |  | SI | Reactivity at 48 hours |
| Q266 | - |  |  | SI | Reactivity at 48 hours |
| Q267 | - |  |  | SI | Reactivity at 48 hours |
| Q268 | - |  |  | SI | Reactivity at 48 hours |
| Q269 | - |  |  | SI | Reactivity at 48 hours |
| Q27 | - |  |  | SI | 430 µg/cm2 |
| Q270 | - |  |  | SI | Reactivity at 48 hours |
| Q271 | - |  |  | SI | Reactivity at 48 hours |
| Q272 | - |  |  | SI | Reactivity at 48 hours |
| Q273 | - |  |  | SI | Reactivity at 48 hours |
| Q274 | - |  |  | SI | Reactivity at 48 hours |
| Q275 | - |  |  | SI | Reactivity at 48 hours |
| Q276 | - |  |  | SI | Reactivity at 48 hours |
| Q277 | - |  |  | SI | Reactivity at 48 hours |
| Q278 | - |  |  | SI | Reactivity at 48 hours |
| Q279 | - |  |  | SI | Reactivity at 48 hours |
| Q28 | - |  |  | SI | Fragrance mix |
| Q280 | - |  |  | SI | Reactivity at 48 hours |
| Q281 | - |  |  | SI | Reactivity at 48 hours |
| Q282 | - |  |  | SI | Reactivity at 48 hours |
| Q283 | - |  |  | SI | Reactivity at 48 hours |
| Q284 | - |  |  | SI | Reactivity at 48 hours |
| Q285 | - |  |  | SI | Reactivity at 48 hours |
| Q286 | - |  |  | SI | Reactivity at 48 hours |
| Q287 | - |  |  | SI | Reactivity at 48 hours |
| Q288 | - |  |  | SI | Reactivity at 48 hours |
| Q289 | - |  |  | SI | Reactivity at 48 hours |
| Q29 | - |  |  | SI | Fragrance mix |
| Q290 | - |  |  | SI | Reactivity at 48 hours |
| Q291 | - |  |  | SI | Reactivity at 48 hours |
| Q292 | - |  |  | SI | Reactivity at 48 hours |
| Q293 | - |  |  | SI | Reactivity at 48 hours |
| Q294 | - |  |  | SI | Reactivity at 48 hours |
| Q295 | - |  |  | SI | Reactivity at 48 hours |
| Q296 | - |  |  | SI | Reactivity at 48 hours |
| Q297 | - |  |  | SI | Reactivity at 48 hours |
| Q298 | - |  |  | SI | Reactivity at 48 hours |
| Q299 | - |  |  | SI | Reactivity at 48 hours |
| Q30 | - |  |  | SI | Colophony |
| Q300 | - |  |  | SI | Reactivity at 72 hours |
| Q301 | - |  |  | SI | Reactivity at 72 hours |
| Q302 | - |  |  | SI | Reactivity at 72 hours |
| Q303 | - |  |  | SI | Reactivity at 72 hours |
| Q304 | - |  |  | SI | Reactivity at 72 hours |
| Q305 | - |  |  | SI | Reactivity at 72 hours |
| Q306 | - |  |  | SI | Reactivity at 72 hours |
| Q307 | - |  |  | SI | Reactivity at 72 hours |
| Q308 | - |  |  | SI | Reactivity at 72 hours |
| Q309 | - |  |  | SI | Reactivity at 72 hours |
| Q31 | - |  |  | SI | 1200 µg/cm2 |
| Q310 | - |  |  | SI | Reactivity at 72 hours |
| Q311 | - |  |  | SI | Reactivity at 72 hours |
| Q312 | - |  |  | SI | Reactivity at 72 hours |
| Q313 | - |  |  | SI | Reactivity at 72 hours |
| Q314 | - |  |  | SI | Reactivity at 72 hours |
| Q315 | - |  |  | SI | Reactivity at 72 hours |
| Q316 | - |  |  | SI | Reactivity at 72 hours |
| Q317 | - |  |  | SI | Reactivity at 72 hours |
| Q318 | - |  |  | SI | Reactivity at 72 hours |
| Q319 | - |  |  | SI | Reactivity at 72 hours |
| Q32 | - |  |  | SI | Colophony |
| Q320 | - |  |  | SI | Reactivity at 72 hours |
| Q321 | - |  |  | SI | Reactivity at 72 hours |
| Q322 | - |  |  | SI | Reactivity at 72 hours |
| Q323 | - |  |  | SI | Reactivity at 72 hours |
| Q324 | - |  |  | SI | Reactivity at 72 hours |
| Q325 | - |  |  | SI | Reactivity at 72 hours |
| Q326 | - |  |  | SI | Reactivity at 72 hours |
| Q327 | - |  |  | SI | Reactivity at 72 hours |
| Q328 | - |  |  | SI | Reactivity at 72 hours |
| Q329 | - |  |  | SI | Reactivity at 72 hours |
| Q33 | - |  |  | SI | Colophony |
| Q330 | - |  |  | SI | Reactivity at 72 hours |
| Q331 | - |  |  | SI | Reactivity at 72 hours |
| Q332 | - |  |  | SI | Reactivity at 72 hours |
| Q333 | - |  |  | SI | Reactivity at 72 hours |
| Q334 | - |  |  | SI | Reactivity at 72 hours |
| Q335 | - |  |  | SI | Reactivity at 72 hours |
| Q336 | - |  |  | SI | Reactivity at 96 hours |
| Q337 | - |  |  | SI | Reactivity at 96 hours |
| Q338 | - |  |  | SI | Reactivity at 96 hours |
| Q339 | - |  |  | SI | Reactivity at 96 hours |
| Q34 | - |  |  | SI | Paraben mix |
| Q340 | - |  |  | SI | Reactivity at 96 hours |
| Q341 | - |  |  | SI | Reactivity at 96 hours |
| Q342 | - |  |  | SI | Reactivity at 96 hours |
| Q343 | - |  |  | SI | Reactivity at 96 hours |
| Q344 | - |  |  | SI | Reactivity at 96 hours |
| Q345 | - |  |  | SI | Reactivity at 96 hours |
| Q346 | - |  |  | SI | Reactivity at 96 hours |
| Q347 | - |  |  | SI | Reactivity at 96 hours |
| Q348 | - |  |  | SI | Reactivity at 96 hours |
| Q349 | - |  |  | SI | Reactivity at 96 hours |
| Q35 | - |  |  | SI | 1000 µg/cm2 |
| Q350 | - |  |  | SI | Reactivity at 96 hours |
| Q351 | - |  |  | SI | Reactivity at 96 hours |
| Q352 | - |  |  | SI | Reactivity at 96 hours |
| Q353 | - |  |  | SI | Reactivity at 96 hours |
| Q354 | - |  |  | SI | Reactivity at 96 hours |
| Q355 | - |  |  | SI | Reactivity at 96 hours |
| Q356 | - |  |  | SI | Reactivity at 96 hours |
| Q357 | - |  |  | SI | Reactivity at 96 hours |
| Q358 | - |  |  | SI | Reactivity at 96 hours |
| Q359 | - |  |  | SI | Reactivity at 96 hours |
| Q36 | - |  |  | SI | Paraben mix |
| Q360 | - |  |  | SI | Reactivity at 96 hours |
| Q361 | - |  |  | SI | Reactivity at 96 hours |
| Q362 | - |  |  | SI | Reactivity at 96 hours |
| Q363 | - |  |  | SI | Reactivity at 96 hours |
| Q364 | - |  |  | SI | Reactivity at 96 hours |
| Q365 | - |  |  | SI | Reactivity at 96 hours |
| Q366 | - |  |  | SI | Reactivity at 96 hours |
| Q367 | - |  |  | SI | Reactivity at 96 hours |
| Q368 | - |  |  | SI | Reactivity at 96 hours |
| Q369 | - |  |  | SI | Reactivity at 96 hours |
| Q37 | - |  |  | SI | Paraben mix |
| Q370 | - |  |  | SI | Reactivity at 96 hours |
| Q371 | - |  |  | SI | Reactivity at 96 hours |
| Q38 | - |  |  | SI | Negative control |
| Q39 | - |  |  | SI | µg/cm2 |
| Q40 | - |  |  | SI | Negative control |
| Q41 | - |  |  | SI | Negative control |
| Q42 | - |  |  | SI | Balsam of peru |
| Q43 | - |  |  | SI | 800 µg/cm2 |
| Q44 | - |  |  | SI | Balsam of peru |
| Q45 | - |  |  | SI | Balsam of peru |
| Q46 | - |  |  | SI | Ethylenediamine dihydrochloride |
| Q47 | - |  |  | SI | 50 µg/cm2 |
| Q48 | - |  |  | SI | Ethylenediamine dihydrochloride |
| Q49 | - |  |  | SI | Ethylenediamine dihydrochloride |
| Q50 | - |  |  | SI | Cobalt dichloride |
| Q51 | - |  |  | SI | 20 µg/cm2 |
| Q52 | - |  |  | SI | Cobalt dichloride |
| Q53 | - |  |  | SI | Cobalt dichloride |
| Q54 | - |  |  | SI | p-tert butylphenol formaldehyde resin |
| Q55 | - |  |  | SI | 45 µg/cm2 |
| Q56 | - |  |  | SI | p-tert butylphenol formaldehyde resin |
| Q57 | - |  |  | SI | p-tert butylphenol formaldehyde resin |
| Q58 | - |  |  | SI | Epoxy resin |
| Q59 | - |  |  | SI | 50 µg/cm2 |
| Q60 | - |  |  | SI | Epoxy resin |
| Q61 | - |  |  | SI | Epoxy resin |
| Q62 | - |  |  | SI | Carba mix |
| Q63 | - |  |  | SI | 250 µg/cm2 |
| Q64 | - |  |  | SI | Carba mix |
| Q65 | - |  |  | SI | Carba mix |
| Q66 | - |  |  | SI | Black rubber mix |
| Q67 | - |  |  | SI | 75 µg/cm2 |
| Q68 | - |  |  | SI | Black rubber mix |
| Q69 | - |  |  | SI | Black rubber mix |
| Q70 | - |  |  | SI | Cl+ me- isothiazolinone |
| Q71 | - |  |  | SI | 4 µg/cm2 |
| Q72 | - |  |  | SI | Cl+ me - isothiazolinone |
| Q73 | - |  |  | SI | Cl+ me - isothiazolinone |
| Q74 | - |  |  | SI | Quaternium - 15 |
| Q75 | - |  |  | SI | 100 µg/cm2 |
| Q76 | - |  |  | SI | Quaternium - 15 |
| Q77 | - |  |  | SI | Quaternium - 15 |
| Q78 | - |  |  | SI | Methyldibromo glutaronitrile |
| Q79 | - |  |  | SI | 5 µg/cm2 |
| Q80 | - |  |  | SI | Methyldibromo glutaronitrile |
| Q81 | - |  |  | SI | Methyldibromo glutaronitrile |
| Q82 | - |  |  | SI | p - phenylenediamine |
| Q83 | - |  |  | SI | 80 µg/cm2 |
| Q84 | - |  |  | SI | p - phenylenediamine |
| Q85 | - |  |  | SI | p - phenylenediamine |
| Q86 | - |  |  | SI | Formaldehyde |
| Q87 | - |  |  | SI | 180 µg/cm2 |
| Q88 | - |  |  | SI | Formaldehyde |
| Q89 | - |  |  | SI | Formaldehyde |
| Q90 | - |  |  | SI | Mercapto mix |
| Q91 | - |  |  | SI | 75 µg/cm2 |
| Q92 | - |  |  | SI | Mercapto mix |
| Q93 | - |  |  | SI | Mercapto mix |
| Q94 | - |  |  | SI | Thimerosal |
| Q95 | - |  |  | SI | 7 µg/cm2 |
| Q96 | - |  |  | SI | Thimerosal |
| Q97 | - |  |  | SI | Thimerosal |
| Q98 | - |  |  | SI | Thiuram mix |
| Q99 | - |  |  | SI | Thiuram mix |
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