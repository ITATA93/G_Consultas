# SQLUser.CT_Zip

**Schema:** SQLUser
**Columnas:** 477
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTZIP_RowId | bigint | PK |  | NO | - |
| CTZIP_Active | varchar |  |  | SI | Active |
| CTZIP_CITYAREA_DR | bigint |  | FK | SI | Des Ref to CT_CityArea |
| CTZIP_CITY_DR | bigint |  | FK | SI | Des Ref CT_CITY |
| CTZIP_CityAreaDesc | varchar |  |  | SI | City Area Desc |
| CTZIP_CityDesc | varchar |  |  | SI | City Description |
| CTZIP_Code | varchar |  |  | SI | Postal Zip Code Table Code |
| CTZIP_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| CTZIP_Complement | varchar |  |  | SI | Complement |
| CTZIP_CreatedDate | date |  |  | SI | Created Date |
| CTZIP_CreatedTime | time |  |  | SI | Created Time |
| CTZIP_CreatedUser_DR | bigint |  | FK | SI | Created User |
| CTZIP_DateFrom | date |  |  | SI | Date From |
| CTZIP_DateTo | date |  |  | SI | Date To |
| CTZIP_Desc | varchar |  |  | SI | Postal Zip Code Table Desc |
| CTZIP_ForeignPostCode | varchar |  |  | SI | Foreign Post Code |
| CTZIP_HCA_DR | bigint |  | FK | SI | Des Ref HCA |
| CTZIP_HCRegion_DR | bigint |  | FK | SI | Health Care Region Des ref |
| CTZIP_LocalAuth_DR | bigint |  | FK | SI | Des Ref LocalAuth |
| CTZIP_NoFixedAddress | varchar |  |  | SI | No Fixed Address |
| CTZIP_Owner | varchar |  |  | SI | Owner |
| CTZIP_Province_DR | bigint |  | FK | SI | Des Ref Province |
| CTZIP_Region_DR | bigint |  | FK | SI | Des Ref Region |
| CTZIP_Remark | varchar |  |  | SI | Remark |
| CTZIP_Type | varchar |  |  | SI | Type |
| CTZIP_UpdatedDate | date |  |  | SI | Updated Date |
| CTZIP_UpdatedTime | time |  |  | SI | Updated Time |
| CTZIP_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q1 | - |  |  | SI | Date |
| Q10 | - |  |  | SI | Left buttock |
| Q100 | - |  |  | SI | Head 15 years |
| Q101 | - |  |  | SI | Neck 15 years |
| Q102 | - |  |  | SI | Anterior trunk 15 years |
| Q103 | - |  |  | SI | Posterior trunk 15 years |
| Q104 | - |  |  | SI | Right buttock 15 years |
| Q105 | - |  |  | SI | Left buttock 15 years |
| Q106 | - |  |  | SI | Genitalia 15 years |
| Q107 | - |  |  | SI | Right upper arm 15 years |
| Q108 | - |  |  | SI | Left upper arm 15 years |
| Q109 | - |  |  | SI | Right lower arm 15 years |
| Q11 | - |  |  | SI | Genitalia |
| Q110 | - |  |  | SI | Left lower arm 15 years |
| Q111 | - |  |  | SI | Right hand 15 years |
| Q112 | - |  |  | SI | Left hand 15 years |
| Q113 | - |  |  | SI | Right thigh 15 years |
| Q114 | - |  |  | SI | Left thigh 15 years |
| Q115 | - |  |  | SI | Right leg 15 years |
| Q116 | - |  |  | SI | Left leg 15 years |
| Q117 | - |  |  | SI | Right foot 15 years |
| Q118 | - |  |  | SI | Left foot 15 years |
| Q119 | - |  |  | SI | Head Adult |
| Q12 | - |  |  | SI | Right upper arm |
| Q120 | - |  |  | SI | Neck Adult |
| Q121 | - |  |  | SI | Anterior trunk Adult |
| Q122 | - |  |  | SI | Posterior trunk Adult |
| Q123 | - |  |  | SI | Right buttock Adult |
| Q124 | - |  |  | SI | Left buttock Adult |
| Q125 | - |  |  | SI | Genitalia Adult |
| Q126 | - |  |  | SI | Right upper arm Adult |
| Q127 | - |  |  | SI | Left upper arm Adult |
| Q128 | - |  |  | SI | Right lower arm Adult |
| Q129 | - |  |  | SI | Left lower arm Adult |
| Q13 | - |  |  | SI | Left upper arm |
| Q130 | - |  |  | SI | Right hand Adult |
| Q131 | - |  |  | SI | Left hand Adult |
| Q132 | - |  |  | SI | Right thigh Adult |
| Q133 | - |  |  | SI | Left thigh Adult |
| Q134 | - |  |  | SI | Right leg Adult |
| Q135 | - |  |  | SI | Left leg Adult |
| Q136 | - |  |  | SI | Right foot Adult |
| Q137 | - |  |  | SI | Left foot Adult |
| Q138 | - |  |  | SI | Second Degree Total (% body surface area) |
| Q139 | - |  |  | SI | Third Degree Total (% body surface area) |
| Q14 | - |  |  | SI | Right lower arm |
| Q140 | - |  |  | SI | Total |
| Q141 | - |  |  | SI | Degree of burn |
| Q142 | - |  |  | SI | Area % for all ages |
| Q143 | - |  |  | SI | Neck = 1 |
| Q144 | - |  |  | SI | Anterior Trunk = 13 |
| Q145 | - |  |  | SI | Posterior Trunk = 13 |
| Q146 | - |  |  | SI | One anterior upper arm = 2 |
| Q147 | - |  |  | SI | One posterior lower arm = 1.5 |
| Q148 | - |  |  | SI | One anterior hand = 1.5 |
| Q149 | - |  |  | SI | One posterior upper arm = 2 |
| Q15 | - |  |  | SI | Left lower arm |
| Q150 | - |  |  | SI | One posterior hand = 1.5 |
| Q151 | - |  |  | SI | Buttock = 2.5 |
| Q152 | - |  |  | SI | Genitalia = 1 |
| Q153 | - |  |  | SI | Injury to Area % |
| Q154 | - |  |  | SI | Head (A) |
| Q155 | - |  |  | SI | Neck |
| Q156 | - |  |  | SI | Anterior Trunk |
| Q157 | - |  |  | SI | Posterior Trunk |
| Q158 | - |  |  | SI | Right Arm |
| Q159 | - |  |  | SI | Left Arm |
| Q16 | - |  |  | SI | Right hand |
| Q160 | - |  |  | SI | Buttocks |
| Q161 | - |  |  | SI | Genitalia |
| Q162 | - |  |  | SI | Right Upper Leg (B) |
| Q163 | - |  |  | SI | Right Lower Leg (C) |
| Q164 | - |  |  | SI | Total Burn Surface Area |
| Q165 | - |  |  | SI | Notes |
| Q166 | - |  |  | SI | Left Upper Leg (B) |
| Q167 | - |  |  | SI | Left Lower Leg (C) |
| Q168 | - |  |  | SI | &lt |
| Q169 | - |  |  | SI | 19 |
| Q17 | - |  |  | SI | Left hand |
| Q170 | - |  |  | SI | 2 |
| Q171 | - |  |  | SI | 13 |
| Q172 | - |  |  | SI | 2.5 |
| Q173 | - |  |  | SI | 2.5 |
| Q174 | - |  |  | SI | 1 |
| Q175 | - |  |  | SI | 4 |
| Q176 | - |  |  | SI | 4 |
| Q177 | - |  |  | SI | 3 |
| Q178 | - |  |  | SI | 3 |
| Q179 | - |  |  | SI | 2.5 |
| Q18 | - |  |  | SI | Right thigh |
| Q180 | - |  |  | SI | 2.5 |
| Q181 | - |  |  | SI | 5.5 |
| Q182 | - |  |  | SI | 5.5 |
| Q183 | - |  |  | SI | 5 |
| Q184 | - |  |  | SI | 5 |
| Q185 | - |  |  | SI | 3.5 |
| Q186 | - |  |  | SI | 3.5 |
| Q187 | - |  |  | SI | 13 |
| Q188 | - |  |  | SI | 1 to 4 years |
| Q189 | - |  |  | SI | 17 |
| Q19 | - |  |  | SI | Left thigh |
| Q190 | - |  |  | SI | 2 |
| Q191 | - |  |  | SI | 13 |
| Q192 | - |  |  | SI | 13 |
| Q193 | - |  |  | SI | 2.5 |
| Q194 | - |  |  | SI | 2.5 |
| Q195 | - |  |  | SI | 1 |
| Q196 | - |  |  | SI | 4 |
| Q197 | - |  |  | SI | 4 |
| Q198 | - |  |  | SI | 3 |
| Q199 | - |  |  | SI | 3 |
| Q2 | - |  |  | SI | Time |
| Q20 | - |  |  | SI | Right leg |
| Q200 | - |  |  | SI | 2.5 |
| Q201 | - |  |  | SI | 2.5 |
| Q202 | - |  |  | SI | 6.5 |
| Q203 | - |  |  | SI | 6.5 |
| Q204 | - |  |  | SI | 5 |
| Q205 | - |  |  | SI | 5 |
| Q206 | - |  |  | SI | 3.5 |
| Q207 | - |  |  | SI | 3.5 |
| Q208 | - |  |  | SI | 5 to 9 years |
| Q209 | - |  |  | SI | 13 |
| Q21 | - |  |  | SI | Left leg |
| Q210 | - |  |  | SI | 2 |
| Q211 | - |  |  | SI | 13 |
| Q212 | - |  |  | SI | 13 |
| Q213 | - |  |  | SI | 2.5 |
| Q214 | - |  |  | SI | 2.5 |
| Q215 | - |  |  | SI | 1 |
| Q216 | - |  |  | SI | 4 |
| Q217 | - |  |  | SI | 4 |
| Q218 | - |  |  | SI | 3 |
| Q219 | - |  |  | SI | 3 |
| Q22 | - |  |  | SI | Right foot |
| Q220 | - |  |  | SI | 2.5 |
| Q221 | - |  |  | SI | 2.5 |
| Q222 | - |  |  | SI | 8 |
| Q223 | - |  |  | SI | 8 |
| Q224 | - |  |  | SI | 5.5 |
| Q225 | - |  |  | SI | 5.5 |
| Q226 | - |  |  | SI | 3.5 |
| Q227 | - |  |  | SI | 3.5 |
| Q228 | - |  |  | SI | 10 to 14 years |
| Q229 | - |  |  | SI | 11 |
| Q23 | - |  |  | SI | Left foot |
| Q230 | - |  |  | SI | 2 |
| Q231 | - |  |  | SI | 13 |
| Q232 | - |  |  | SI | 13 |
| Q233 | - |  |  | SI | 2.5 |
| Q234 | - |  |  | SI | 2.5 |
| Q235 | - |  |  | SI | 1 |
| Q236 | - |  |  | SI | 4 |
| Q237 | - |  |  | SI | 4 |
| Q238 | - |  |  | SI | 3 |
| Q239 | - |  |  | SI | 3 |
| Q24 | - |  |  | SI | Head 0-1 years |
| Q240 | - |  |  | SI | 2.5 |
| Q241 | - |  |  | SI | 2.5 |
| Q242 | - |  |  | SI | 8.5 |
| Q243 | - |  |  | SI | 8.5 |
| Q244 | - |  |  | SI | 6 |
| Q245 | - |  |  | SI | 6 |
| Q246 | - |  |  | SI | 3.5 |
| Q247 | - |  |  | SI | 3.5 |
| Q248 | - |  |  | SI | 15 to 17 years |
| Q249 | - |  |  | SI | 9 |
| Q25 | - |  |  | SI | Neck 0-1 years |
| Q250 | - |  |  | SI | 2 |
| Q251 | - |  |  | SI | 13 |
| Q252 | - |  |  | SI | 13 |
| Q253 | - |  |  | SI | 2.5 |
| Q254 | - |  |  | SI | 2.5 |
| Q255 | - |  |  | SI | 1 |
| Q256 | - |  |  | SI | 4 |
| Q257 | - |  |  | SI | 4 |
| Q258 | - |  |  | SI | 3 |
| Q259 | - |  |  | SI | 3 |
| Q26 | - |  |  | SI | Anterior trunk 0-1 years |
| Q260 | - |  |  | SI | 2.5 |
| Q261 | - |  |  | SI | 2.5 |
| Q262 | - |  |  | SI | 9 |
| Q263 | - |  |  | SI | 9 |
| Q264 | - |  |  | SI | 6.5 |
| Q265 | - |  |  | SI | 6.5 |
| Q266 | - |  |  | SI | 3.5 |
| Q267 | - |  |  | SI | 3.5 |
| Q268 | - |  |  | SI | &gt |
| Q269 | - |  |  | SI | 7 |
| Q27 | - |  |  | SI | Posterior trunk 0-1 years |
| Q270 | - |  |  | SI | 2 |
| Q271 | - |  |  | SI | 13 |
| Q272 | - |  |  | SI | 13 |
| Q273 | - |  |  | SI | 2.5 |
| Q274 | - |  |  | SI | 2.5 |
| Q275 | - |  |  | SI | 1 |
| Q276 | - |  |  | SI | 4 |
| Q277 | - |  |  | SI | 4 |
| Q278 | - |  |  | SI | 3 |
| Q279 | - |  |  | SI | 3 |
| Q28 | - |  |  | SI | Right buttock 0-1 years |
| Q280 | - |  |  | SI | 2.5 |
| Q281 | - |  |  | SI | 2.5 |
| Q282 | - |  |  | SI | 9.5 |
| Q283 | - |  |  | SI | 9.5 |
| Q284 | - |  |  | SI | 7 |
| Q285 | - |  |  | SI | 7 |
| Q286 | - |  |  | SI | 3.5 |
| Q287 | - |  |  | SI | 3.5 |
| Q288 | - |  |  | SI | Burn Assesment Record |
| Q289 | - |  |  | SI | Head |
| Q29 | - |  |  | SI | Left buttock 0-1 years |
| Q290 | - |  |  | SI | Head |
| Q291 | - |  |  | SI | Head |
| Q292 | - |  |  | SI | Head |
| Q293 | - |  |  | SI | Head |
| Q294 | - |  |  | SI | Head |
| Q295 | - |  |  | SI | Neck |
| Q296 | - |  |  | SI | Neck |
| Q297 | - |  |  | SI | Neck |
| Q298 | - |  |  | SI | Neck |
| Q299 | - |  |  | SI | Neck |
| Q3 | - |  |  | SI | Age range |
| Q30 | - |  |  | SI | Genitalia 0-1 years |
| Q300 | - |  |  | SI | Neck |
| Q301 | - |  |  | SI | Anterior Trunk |
| Q302 | - |  |  | SI | Anterior Trunk |
| Q303 | - |  |  | SI | Anterior Trunk |
| Q304 | - |  |  | SI | Anterior Trunk |
| Q305 | - |  |  | SI | Anterior Trunk |
| Q306 | - |  |  | SI | Anterior Trunk |
| Q307 | - |  |  | SI | Posterior Trunk |
| Q308 | - |  |  | SI | Posterior Trunk |
| Q309 | - |  |  | SI | Posterior Trunk |
| Q31 | - |  |  | SI | Right upper arm 0-1 years |
| Q310 | - |  |  | SI | Posterior Trunk |
| Q311 | - |  |  | SI | Posterior Trunk |
| Q312 | - |  |  | SI | Posterior Trunk |
| Q313 | - |  |  | SI | Right Buttock |
| Q314 | - |  |  | SI | Right Buttock |
| Q315 | - |  |  | SI | Right Buttock |
| Q316 | - |  |  | SI | Right Buttock |
| Q317 | - |  |  | SI | Right Buttock |
| Q318 | - |  |  | SI | Right Buttock |
| Q319 | - |  |  | SI | Left Buttock |
| Q32 | - |  |  | SI | Left upper arm 0-1 years |
| Q320 | - |  |  | SI | Left Buttock |
| Q321 | - |  |  | SI | Left Buttock |
| Q322 | - |  |  | SI | Left Buttock |
| Q323 | - |  |  | SI | Left Buttock |
| Q324 | - |  |  | SI | Left Buttock |
| Q325 | - |  |  | SI | Genitalia |
| Q326 | - |  |  | SI | Genitalia |
| Q327 | - |  |  | SI | Genitalia |
| Q328 | - |  |  | SI | Genitalia |
| Q329 | - |  |  | SI | Genitalia |
| Q33 | - |  |  | SI | Right lower arm 0-1 years |
| Q330 | - |  |  | SI | Genitalia |
| Q331 | - |  |  | SI | Right upper arm |
| Q332 | - |  |  | SI | Right upper arm |
| Q333 | - |  |  | SI | Right upper arm |
| Q334 | - |  |  | SI | Right upper arm |
| Q335 | - |  |  | SI | Right upper arm |
| Q336 | - |  |  | SI | Right upper arm |
| Q337 | - |  |  | SI | Left upper arm |
| Q338 | - |  |  | SI | Left upper arm |
| Q339 | - |  |  | SI | Left upper arm |
| Q34 | - |  |  | SI | Left lower arm 0-1 years |
| Q340 | - |  |  | SI | Left upper arm |
| Q341 | - |  |  | SI | Left upper arm |
| Q342 | - |  |  | SI | Left upper arm |
| Q343 | - |  |  | SI | Right lower arm |
| Q344 | - |  |  | SI | Right lower arm |
| Q345 | - |  |  | SI | Right lower arm |
| Q346 | - |  |  | SI | Right lower arm |
| Q347 | - |  |  | SI | Right lower arm |
| Q348 | - |  |  | SI | Right lower arm |
| Q349 | - |  |  | SI | Left lower arm |
| Q35 | - |  |  | SI | Right hand 0-1 years |
| Q350 | - |  |  | SI | Left lower arm |
| Q351 | - |  |  | SI | Left lower arm |
| Q352 | - |  |  | SI | Left lower arm |
| Q353 | - |  |  | SI | Left lower arm |
| Q354 | - |  |  | SI | Left lower arm |
| Q355 | - |  |  | SI | Right hand |
| Q356 | - |  |  | SI | Right hand |
| Q357 | - |  |  | SI | Right hand |
| Q358 | - |  |  | SI | Right hand |
| Q359 | - |  |  | SI | Right hand |
| Q36 | - |  |  | SI | Left hand 0-1 years |
| Q360 | - |  |  | SI | Right hand |
| Q361 | - |  |  | SI | Left hand |
| Q362 | - |  |  | SI | Left hand |
| Q363 | - |  |  | SI | Left hand |
| Q364 | - |  |  | SI | Left hand |
| Q365 | - |  |  | SI | Left hand |
| Q366 | - |  |  | SI | Left hand |
| Q367 | - |  |  | SI | Right thigh |
| Q368 | - |  |  | SI | Right thigh |
| Q369 | - |  |  | SI | Right thigh |
| Q37 | - |  |  | SI | Right thigh 0-1 years |
| Q370 | - |  |  | SI | Right thigh |
| Q371 | - |  |  | SI | Right thigh |
| Q372 | - |  |  | SI | Right thigh |
| Q373 | - |  |  | SI | Left thigh |
| Q374 | - |  |  | SI | Left thigh |
| Q375 | - |  |  | SI | Left thigh |
| Q376 | - |  |  | SI | Left thigh |
| Q377 | - |  |  | SI | Left thigh |
| Q378 | - |  |  | SI | Left thigh |
| Q379 | - |  |  | SI | Right leg |
| Q38 | - |  |  | SI | Left thigh 0-1 years |
| Q380 | - |  |  | SI | Right leg |
| Q381 | - |  |  | SI | Right leg |
| Q382 | - |  |  | SI | Right leg |
| Q383 | - |  |  | SI | Right leg |
| Q384 | - |  |  | SI | Right leg |
| Q385 | - |  |  | SI | Left leg |
| Q386 | - |  |  | SI | Left leg |
| Q387 | - |  |  | SI | Left leg |
| Q388 | - |  |  | SI | Left leg |
| Q389 | - |  |  | SI | Left leg |
| Q39 | - |  |  | SI | Right leg 0-1 years |
| Q390 | - |  |  | SI | Left leg |
| Q391 | - |  |  | SI | Right foot |
| Q392 | - |  |  | SI | Right foot |
| Q393 | - |  |  | SI | Right foot |
| Q394 | - |  |  | SI | Right foot |
| Q395 | - |  |  | SI | Right foot |
| Q396 | - |  |  | SI | Right foot |
| Q397 | - |  |  | SI | Left foot |
| Q398 | - |  |  | SI | Left foot |
| Q399 | - |  |  | SI | Left foot |
| Q4 | - |  |  | SI | Area |
| Q40 | - |  |  | SI | Left leg 0-1 years |
| Q400 | - |  |  | SI | Left foot |
| Q401 | - |  |  | SI | Left foot |
| Q402 | - |  |  | SI | Left foot |
| Q403 | - |  |  | SI | Modification of Berkow's method for estimating bod... |
| Q404 | - |  |  | SI | 1. Berkow SG. A Method Of Estimating The Extensive... |
| Q405 | - |  |  | SI | 2. Lund CC, Browder NC. The estimation of areas of... |
| Q406 | - |  |  | SI | Burn Type |
| Q407 | - |  |  | SI | Other Burn type |
| Q408 | - |  |  | SI | Burn Incident Date |
| Q409 | - |  |  | SI | Burn Incident Time |
| Q41 | - |  |  | SI | Right foot 0-1 years |
| Q42 | - |  |  | SI | Left foot 0-1 years |
| Q43 | - |  |  | SI | Head 1-4 years |
| Q44 | - |  |  | SI | Neck 1-4 years |
| Q45 | - |  |  | SI | Anterior trunk 1-4 years |
| Q46 | - |  |  | SI | Posterior trunk 1-4 years |
| Q47 | - |  |  | SI | Right buttock 1-4 years |
| Q48 | - |  |  | SI | Left buttock 1-4 years |
| Q49 | - |  |  | SI | Genitalia 1-4 years |
| Q5 | - |  |  | SI | Head |
| Q50 | - |  |  | SI | Right upper arm 1-4 years |
| Q51 | - |  |  | SI | Left upper arm 1-4 years |
| Q52 | - |  |  | SI | Right lower arm 1-4 years |
| Q53 | - |  |  | SI | Left lower arm 1-4 years |
| Q54 | - |  |  | SI | Right hand 1-4 years |
| Q55 | - |  |  | SI | Left hand 1-4 years |
| Q56 | - |  |  | SI | Right thigh 1-4 years |
| Q57 | - |  |  | SI | Left thigh 1-4 years |
| Q58 | - |  |  | SI | Right leg 1-4 years |
| Q59 | - |  |  | SI | Left leg 1-4 years |
| Q6 | - |  |  | SI | Neck |
| Q60 | - |  |  | SI | Right foot 1-4 years |
| Q61 | - |  |  | SI | Left foot 1-4 years |
| Q62 | - |  |  | SI | Head 5-9 years |
| Q63 | - |  |  | SI | Neck 5-9 years |
| Q64 | - |  |  | SI | Anterior trunk 5-9 years |
| Q65 | - |  |  | SI | Posterior trunk 5-9 years |
| Q66 | - |  |  | SI | Right buttock 5-9 years |
| Q67 | - |  |  | SI | Left buttock 5-9 years |
| Q68 | - |  |  | SI | Genitalia 5-9 years |
| Q69 | - |  |  | SI | Right upper arm 5-9 years |
| Q7 | - |  |  | SI | Anterior trunk |
| Q70 | - |  |  | SI | Left upper arm 5-9 years |
| Q71 | - |  |  | SI | Right lower arm 5-9 years |
| Q72 | - |  |  | SI | Left lower arm 5-9 years |
| Q73 | - |  |  | SI | Right hand 5-9 years |
| Q74 | - |  |  | SI | Left hand 5-9 years |
| Q75 | - |  |  | SI | Right thigh 5-9 years |
| Q76 | - |  |  | SI | Left thigh 5-9 years |
| Q77 | - |  |  | SI | Right leg 5-9 years |
| Q78 | - |  |  | SI | Left leg 5-9 years |
| Q79 | - |  |  | SI | Right foot 5-9 years |
| Q8 | - |  |  | SI | Posterior trunk |
| Q80 | - |  |  | SI | Left foot 5-9 years |
| Q81 | - |  |  | SI | Head 10-14 years |
| Q82 | - |  |  | SI | Neck 10-14 years |
| Q83 | - |  |  | SI | Anterior trunk 10-14 years |
| Q84 | - |  |  | SI | Posterior trunk 10-14 years |
| Q85 | - |  |  | SI | Right buttock 10-14 years |
| Q86 | - |  |  | SI | Left buttock 10-14 years |
| Q87 | - |  |  | SI | Genitalia 10-14 years |
| Q88 | - |  |  | SI | Right upper arm 10-14 years |
| Q89 | - |  |  | SI | Left upper arm 10-14 years |
| Q9 | - |  |  | SI | Right buttock |
| Q90 | - |  |  | SI | Right lower arm 10-14 years |
| Q91 | - |  |  | SI | Left lower arm 10-14 years |
| Q92 | - |  |  | SI | Right hand 10-14 years |
| Q93 | - |  |  | SI | Left hand 10-14 years |
| Q94 | - |  |  | SI | Right thigh 10-14 years |
| Q95 | - |  |  | SI | Left thigh 10-14 years |
| Q96 | - |  |  | SI | Right leg 10-14 years |
| Q97 | - |  |  | SI | Left leg 10-14 years |
| Q98 | - |  |  | SI | Right foot 10-14 years |
| Q99 | - |  |  | SI | Left foot 10-14 years |
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