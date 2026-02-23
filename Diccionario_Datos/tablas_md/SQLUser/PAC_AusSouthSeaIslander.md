# SQLUser.PAC_AusSouthSeaIslander

**Schema:** SQLUser
**Columnas:** 401
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ASSIS_RowId | bigint | PK |  | NO | - |
| ASSIS_Code | varchar |  |  | NO | Code |
| ASSIS_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| ASSIS_CreatedDate | date |  |  | SI | Created Date |
| ASSIS_CreatedTime | time |  |  | SI | Created Time |
| ASSIS_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ASSIS_DateFrom | date |  |  | SI | Date From |
| ASSIS_DateTo | date |  |  | SI | Date To |
| ASSIS_Desc | varchar |  |  | NO | Description |
| ASSIS_NationalCode | varchar |  |  | SI | NationalCode |
| ASSIS_Owner | varchar |  |  | SI | Owner |
| ASSIS_UpdatedDate | date |  |  | SI | Updated Date |
| ASSIS_UpdatedTime | time |  |  | SI | Updated Time |
| ASSIS_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | What has been your level of interest in the past 1... |
| Q04 | - |  |  | SI | What has been your level of interest in the past y... |
| Q05 | - |  |  | SI | Do you currently participate in this activity? |
| Q06 | - |  |  | SI | Would you like to pursue this in the future? |
| Q07 | - |  |  | SI | Gardening Yardwork |
| Q08 | - |  |  | SI | Activity |
| Q09 | - |  |  | SI | Garden Yardwork- What has been your level of inter... |
| Q10 | - |  |  | SI | Garden YardWork- What has been your level of inter... |
| Q100 | - |  |  | SI | Speeches / Lectures- What has been your level of i... |
| Q101 | - |  |  | SI | Speeches / Lectures- Do you currently participate ... |
| Q102 | - |  |  | SI | Speeches / Lectures- Would you like to pursue this... |
| Q103 | - |  |  | SI | Swimming |
| Q104 | - |  |  | SI | Swimming- What has been your level of interest in ... |
| Q105 | - |  |  | SI | Swimming- What has been your level of interest in ... |
| Q106 | - |  |  | SI | Swimming- Do you currently participate in this act... |
| Q107 | - |  |  | SI | Swimming- Would you like to pursue this in the fut... |
| Q108 | - |  |  | SI | Bowling |
| Q109 | - |  |  | SI | Bowling- What has been your level of interest in t... |
| Q11 | - |  |  | SI | Gardening YardWork- Do you currently participate i... |
| Q110 | - |  |  | SI | Bowling- What has been your level of interest in t... |
| Q111 | - |  |  | SI | Bowling- Do you currently participate in this acti... |
| Q112 | - |  |  | SI | Bowling- Would you like to pursue this in the futu... |
| Q113 | - |  |  | SI | Visiting |
| Q114 | - |  |  | SI | Visiting- What has been your level of interest in ... |
| Q115 | - |  |  | SI | Visiting- What has been your level of interest in ... |
| Q116 | - |  |  | SI | Visiting- Do you currently participate in this act... |
| Q117 | - |  |  | SI | Visiting- Would you like to pursue this in the fut... |
| Q118 | - |  |  | SI | Mending |
| Q119 | - |  |  | SI | Mending- What has been your level of interest in t... |
| Q12 | - |  |  | SI | Garden Yardwork- Would you like to pursue this in ... |
| Q120 | - |  |  | SI | Mending- What has been your level of interest in t... |
| Q121 | - |  |  | SI | Mending- Do you currently participate in this acti... |
| Q122 | - |  |  | SI | Mending- Would you like to pursue this in the futu... |
| Q123 | - |  |  | SI | Checkers / Chess |
| Q124 | - |  |  | SI | Checkers / Chess- What has been your level of inte... |
| Q125 | - |  |  | SI | Checkers / Chess- What has been your level of inte... |
| Q126 | - |  |  | SI | Checkers / Chess- Do you currently participate in ... |
| Q127 | - |  |  | SI | Checkers / Chess- Would you like to pursue this in... |
| Q128 | - |  |  | SI | Barbecues |
| Q129 | - |  |  | SI | Barbecues- What has been your level of interest in... |
| Q13 | - |  |  | SI | Sewing / Needling work |
| Q130 | - |  |  | SI | Barbecues- What has been your level of interest in... |
| Q131 | - |  |  | SI | Barbecues- Do you currently participate in this ac... |
| Q132 | - |  |  | SI | Barbecues- Would you like to pursue this in the fu... |
| Q133 | - |  |  | SI | Reading |
| Q134 | - |  |  | SI | Reading- What has been your level of interest in t... |
| Q135 | - |  |  | SI | Reading- What has been your level of interest in t... |
| Q136 | - |  |  | SI | Reading- Do you currently participate in this acti... |
| Q137 | - |  |  | SI | Reading- Would you like to pursue this in the futu... |
| Q138 | - |  |  | SI | Traveling |
| Q139 | - |  |  | SI | Traveling- What has been your level of interest in... |
| Q14 | - |  |  | SI | Sewing / Needling work- What has been your level o... |
| Q140 | - |  |  | SI | Traveling- What has been your level of interest in... |
| Q141 | - |  |  | SI | Traveling- Do you currently participate in this ac... |
| Q142 | - |  |  | SI | Traveling- Would you like to pursue this in the fu... |
| Q143 | - |  |  | SI | Parties |
| Q144 | - |  |  | SI | Parties- What has been your level of interest in t... |
| Q145 | - |  |  | SI | Parties- What has been your level of interest in t... |
| Q146 | - |  |  | SI | Parties- Do you currently participate in this acti... |
| Q147 | - |  |  | SI | Parties- Would you like to pursue this in the futu... |
| Q148 | - |  |  | SI | Wrestling |
| Q149 | - |  |  | SI | Wrestling- What has been your level of interest in... |
| Q15 | - |  |  | SI | Sewing / Needling work- What has been your level o... |
| Q150 | - |  |  | SI | Wrestling- What has been your level of interest in... |
| Q151 | - |  |  | SI | Wrestling- Do you currently participate in this ac... |
| Q152 | - |  |  | SI | Wrestling- Would you like to pursue this in the fu... |
| Q153 | - |  |  | SI | Housecleaning |
| Q154 | - |  |  | SI | Housecleaning- What has been your level of interes... |
| Q155 | - |  |  | SI | Housecleaning- What has been your level of interes... |
| Q156 | - |  |  | SI | Housecleaning- Do you currently participate in thi... |
| Q157 | - |  |  | SI | Housecleaning- Would you like to pursue this in th... |
| Q158 | - |  |  | SI | Model Building |
| Q159 | - |  |  | SI | Model Building- What has been your level of intere... |
| Q16 | - |  |  | SI | Sewing / Needling Work- Do you currently participa... |
| Q160 | - |  |  | SI | Model Building- What has been your level of intere... |
| Q161 | - |  |  | SI | Model Building- Do you currently participate in th... |
| Q162 | - |  |  | SI | Model Building- Would you like to pursue this in t... |
| Q163 | - |  |  | SI | Television |
| Q164 | - |  |  | SI | Television- What has been your level of interest i... |
| Q165 | - |  |  | SI | Television- What has been your level of interest i... |
| Q166 | - |  |  | SI | Television- Do you currently participate in this a... |
| Q167 | - |  |  | SI | Television- Would you like to pursue this in the f... |
| Q168 | - |  |  | SI | Concerts |
| Q169 | - |  |  | SI | Concerts- What has been your level of interest in ... |
| Q17 | - |  |  | SI | Sewing / Needling-Would you like to pursue this in... |
| Q170 | - |  |  | SI | Concerts- What has been your level of interest in ... |
| Q171 | - |  |  | SI | Concerts- Do you currently participate in this act... |
| Q172 | - |  |  | SI | Concerts- Would you like to pursue this in the fut... |
| Q173 | - |  |  | SI | Pottery |
| Q174 | - |  |  | SI | Pottery- What has been your level of interest in t... |
| Q175 | - |  |  | SI | Pottery- What has been your level of interest in t... |
| Q176 | - |  |  | SI | Pottery- Do you currently participate in this acti... |
| Q177 | - |  |  | SI | Pottery- Would you like to pursue this in the futu... |
| Q178 | - |  |  | SI | Camping |
| Q179 | - |  |  | SI | Camping- What has been your level of interest in t... |
| Q18 | - |  |  | SI | Playing cards |
| Q180 | - |  |  | SI | Camping- What has been your level of interest in t... |
| Q181 | - |  |  | SI | Camping- Do you currently participate in this acti... |
| Q182 | - |  |  | SI | Camping- Would you like to pursue this in the futu... |
| Q183 | - |  |  | SI | Laundry / Ironing |
| Q184 | - |  |  | SI | Laundry / Ironing- What has been your level of int... |
| Q185 | - |  |  | SI | Laundry / Ironing- What has been your level of int... |
| Q186 | - |  |  | SI | Laundry / Ironing- Do you currently participate in... |
| Q187 | - |  |  | SI | Laundry / Ironing- Would you like to pursue this i... |
| Q188 | - |  |  | SI | Politics |
| Q189 | - |  |  | SI | Politics- What has been your level of interest in ... |
| Q19 | - |  |  | SI | Playing cards- What has been your level of interes... |
| Q190 | - |  |  | SI | Politics- What has been your level of interest in ... |
| Q191 | - |  |  | SI | Politics- Do you currently participate in this act... |
| Q192 | - |  |  | SI | Politics- Would you like to pursue this in the fut... |
| Q193 | - |  |  | SI | Table Games |
| Q194 | - |  |  | SI | Table Games- What has been your level of interest ... |
| Q195 | - |  |  | SI | Table Games- What has been your level of interest ... |
| Q196 | - |  |  | SI | Table Games- Do you currently participate in this ... |
| Q197 | - |  |  | SI | Table Games- Would you like to pursue this in the ... |
| Q198 | - |  |  | SI | Home Decorating |
| Q199 | - |  |  | SI | Home Decorating- What has been your level of inter... |
| Q20 | - |  |  | SI | Playing cards- What has been your level of interes... |
| Q200 | - |  |  | SI | Home Decorating- What has been your level of inter... |
| Q201 | - |  |  | SI | Home Decorating- Do you currently participate in t... |
| Q202 | - |  |  | SI | Home Decorating- Would you like to pursue this in ... |
| Q203 | - |  |  | SI | Clubs / Lodge |
| Q204 | - |  |  | SI | Clubs / Lodge- What has been your level of interes... |
| Q205 | - |  |  | SI | Clubs / Lodge- What has been your level of interes... |
| Q206 | - |  |  | SI | Clubs / Lodge- Do you currently participate in thi... |
| Q207 | - |  |  | SI | Clubs / Lodge- Would you like to pursue this in th... |
| Q208 | - |  |  | SI | Singing |
| Q209 | - |  |  | SI | Singing- What has been your level of interest in t... |
| Q21 | - |  |  | SI | Playing cards- Do you currently participate in thi... |
| Q210 | - |  |  | SI | Singing- What has been your level of interest in t... |
| Q211 | - |  |  | SI | Singing- Do you currently participate in this acti... |
| Q212 | - |  |  | SI | Singing- Would you like to pursue this in the futu... |
| Q213 | - |  |  | SI | Scouting |
| Q214 | - |  |  | SI | Scouting- What has been your level of interest in ... |
| Q215 | - |  |  | SI | Scouting- What has been your level of interest in ... |
| Q216 | - |  |  | SI | Scouting- Do you currently participate in this act... |
| Q217 | - |  |  | SI | Scouting- Would you like to pursue this in the fut... |
| Q218 | - |  |  | SI | Clothes |
| Q219 | - |  |  | SI | Clothes- What has been your level of interest in t... |
| Q22 | - |  |  | SI | Playing cards- Would you like to pursue this in th... |
| Q220 | - |  |  | SI | Clothes- What has been your level of interest in t... |
| Q221 | - |  |  | SI | Clothes- Do you currently participate in this acti... |
| Q222 | - |  |  | SI | Clothes- Would you like to pursue this in the futu... |
| Q223 | - |  |  | SI | Handicrafts |
| Q224 | - |  |  | SI | Handicrafts- What has been your level of interest ... |
| Q225 | - |  |  | SI | Handicrafts- What has been your level of interest ... |
| Q226 | - |  |  | SI | Handicrafts- Do you currently participate in this ... |
| Q227 | - |  |  | SI | Handicrafts- Would you like to pursue this in the ... |
| Q228 | - |  |  | SI | Hairstyling |
| Q229 | - |  |  | SI | Hairstyling- What has been your level of interest ... |
| Q23 | - |  |  | SI | Foreign Languages |
| Q230 | - |  |  | SI | Hairstyling- What has been your level of interest ... |
| Q231 | - |  |  | SI | Hairstyling- Do you currently participate in this ... |
| Q232 | - |  |  | SI | Hairstyling- Would you like to pursue this in the ... |
| Q233 | - |  |  | SI | Cycling |
| Q234 | - |  |  | SI | Cycling- What has been your level of interest in t... |
| Q235 | - |  |  | SI | Cycling- What has been your level of interest in t... |
| Q236 | - |  |  | SI | Cycling- Do you currently participate in this acti... |
| Q237 | - |  |  | SI | Cycling- Would you like to pursue this in the futu... |
| Q238 | - |  |  | SI | Attending Plays |
| Q239 | - |  |  | SI | Attending Plays- What has been your level of inter... |
| Q24 | - |  |  | SI | Foreign Languanges- What has been your level of in... |
| Q240 | - |  |  | SI | Attending Plays- What has been your level of inter... |
| Q241 | - |  |  | SI | Attending Plays- Do you currently participate in t... |
| Q242 | - |  |  | SI | Attending Plays- Would you like to pursue this in ... |
| Q243 | - |  |  | SI | Bird Watching |
| Q244 | - |  |  | SI | Bird Watching- What has been your level of interes... |
| Q245 | - |  |  | SI | Bird Watching- What has been your level of interes... |
| Q246 | - |  |  | SI | Bird Watching- Do you currently participate in thi... |
| Q247 | - |  |  | SI | Bird Watching- Would you like to pursue this in th... |
| Q248 | - |  |  | SI | Dating |
| Q249 | - |  |  | SI | Dating- What has been your level of interest in th... |
| Q25 | - |  |  | SI | Foreign Languages- What has been your level of int... |
| Q250 | - |  |  | SI | Dating- What has been your level of interest in th... |
| Q251 | - |  |  | SI | Dating- Do you currently participate in this activ... |
| Q252 | - |  |  | SI | Dating- Would you like to pursue this in the futur... |
| Q253 | - |  |  | SI | Auto-racing |
| Q254 | - |  |  | SI | Auto-racing- What has been your level of interest ... |
| Q255 | - |  |  | SI | Auto-racing- What has been your level of interest ... |
| Q256 | - |  |  | SI | Auto-racing- Do you currently participate in this ... |
| Q257 | - |  |  | SI | Auto-racing- Would you like to pursue this in the ... |
| Q258 | - |  |  | SI | Home Repairs |
| Q259 | - |  |  | SI | Home Repairs- What has been your level of interest... |
| Q26 | - |  |  | SI | Foreign Languages- Do you currently participate in... |
| Q260 | - |  |  | SI | Home Repairs- What has been your level of interest... |
| Q261 | - |  |  | SI | Home Repairs- Do you currently participate in this... |
| Q262 | - |  |  | SI | Home Repairs- Would you like to pursue this in the... |
| Q263 | - |  |  | SI | Exercise |
| Q264 | - |  |  | SI | Exercise- What has been your level of interest in ... |
| Q265 | - |  |  | SI | Exercise- What has been your level of interest in ... |
| Q266 | - |  |  | SI | Exercise- Do you currently participate in this act... |
| Q267 | - |  |  | SI | Exercise- Would you like to pursue this in the fut... |
| Q268 | - |  |  | SI | Hunting |
| Q269 | - |  |  | SI | Hunting- What has been your level of interest in t... |
| Q27 | - |  |  | SI | Foreign Languages- Would you like to pursue this i... |
| Q270 | - |  |  | SI | Hunting- What has been your level of interest in t... |
| Q271 | - |  |  | SI | Hunting- Do you currently participate in this acti... |
| Q272 | - |  |  | SI | Hunting- Would you like to pursue this in the futu... |
| Q273 | - |  |  | SI | Woodworking |
| Q274 | - |  |  | SI | Woodworking- What has been your level of interest ... |
| Q275 | - |  |  | SI | Woodworking- What has been your level of interest ... |
| Q276 | - |  |  | SI | Woodworking- Do you currently participate in this ... |
| Q277 | - |  |  | SI | Woodworking- Would you like to pursue this in the ... |
| Q278 | - |  |  | SI | Pool |
| Q279 | - |  |  | SI | Pool- What has been your level of interest in the ... |
| Q28 | - |  |  | SI | Church Activities |
| Q280 | - |  |  | SI | Pool- What has been your level of interest in the ... |
| Q281 | - |  |  | SI | Pool- Do you currently participate in this activit... |
| Q282 | - |  |  | SI | Pool- Would you like to pursue this in the future? |
| Q283 | - |  |  | SI | Driving |
| Q284 | - |  |  | SI | Driving- What has been your level of interest in t... |
| Q285 | - |  |  | SI | Driving- What has been your level of interest in t... |
| Q286 | - |  |  | SI | Driving- Do you currently participate in this acti... |
| Q287 | - |  |  | SI | Driving- Would you like to pursue this in the futu... |
| Q288 | - |  |  | SI | Child care |
| Q289 | - |  |  | SI | Child Care- What has been your level of interest i... |
| Q29 | - |  |  | SI | Church Activities- What has been your level of int... |
| Q290 | - |  |  | SI | Child Care- What has been your level of interest i... |
| Q291 | - |  |  | SI | Child Care- Do you currently participate in this a... |
| Q292 | - |  |  | SI | Child Care- Would you like to pursue this in the f... |
| Q293 | - |  |  | SI | Tennis |
| Q294 | - |  |  | SI | Tennis- What has been your level of interest in th... |
| Q295 | - |  |  | SI | Tennis- What has been your level of interest in th... |
| Q296 | - |  |  | SI | Tennis- Do you currently participate in this activ... |
| Q297 | - |  |  | SI | Tennis- Would you like to pursue this in the futur... |
| Q298 | - |  |  | SI | Cooking / Baking |
| Q299 | - |  |  | SI | Cooking / Baking- What has been your level of inte... |
| Q30 | - |  |  | SI | Church Activities- What has been your level of int... |
| Q300 | - |  |  | SI | Cooking / Baking- What has been your level of inte... |
| Q301 | - |  |  | SI | Cooking / Baking- Do you currently participate in ... |
| Q302 | - |  |  | SI | Cooking / Baking- Would you like to pursue this in... |
| Q303 | - |  |  | SI | Basketball |
| Q304 | - |  |  | SI | Basketball- What has been your level of interest i... |
| Q305 | - |  |  | SI | Basketball- What has been your level of interest i... |
| Q306 | - |  |  | SI | Basketball- Do you currently participate in this a... |
| Q307 | - |  |  | SI | Basketball- Would you like to pursue this in the f... |
| Q308 | - |  |  | SI | History |
| Q309 | - |  |  | SI | History- What has been your level of interest in t... |
| Q31 | - |  |  | SI | Church Activities- Do you currently participate in... |
| Q310 | - |  |  | SI | History- What has been your level of interest in t... |
| Q311 | - |  |  | SI | History- Do you currently participate in this acti... |
| Q312 | - |  |  | SI | History- Would you like to pursue this in the futu... |
| Q313 | - |  |  | SI | Collecting |
| Q314 | - |  |  | SI | Collecting- What has been your level of interest i... |
| Q315 | - |  |  | SI | Collecting- What has been your level of interest i... |
| Q316 | - |  |  | SI | Collecting- Do you currently participate in this a... |
| Q317 | - |  |  | SI | Collecting- Do you currently participate in this a... |
| Q318 | - |  |  | SI | Fishing |
| Q319 | - |  |  | SI | Fishing- What has been your level of interest in t... |
| Q32 | - |  |  | SI | Church Activities- Would you like to pursue this i... |
| Q320 | - |  |  | SI | Fishing- What has been your level of interest in t... |
| Q321 | - |  |  | SI | Fishing- Do you currently participate in this acti... |
| Q322 | - |  |  | SI | Fishing- Would you like to pursue this in the futu... |
| Q323 | - |  |  | SI | Science |
| Q324 | - |  |  | SI | Science- What has been your level of interest in t... |
| Q325 | - |  |  | SI | Science- What has been your level of interest in t... |
| Q326 | - |  |  | SI | Science- Do you currently participate in this acti... |
| Q327 | - |  |  | SI | Science- Would you like to pursue this in the futu... |
| Q328 | - |  |  | SI | Leatherwork |
| Q329 | - |  |  | SI | Leatherwork- What has been your level of interest ... |
| Q33 | - |  |  | SI | Radio |
| Q330 | - |  |  | SI | Leatherwork- What has been your level of interest ... |
| Q331 | - |  |  | SI | Leatherwork- Do you currently participate in this ... |
| Q332 | - |  |  | SI | Leatherwork- Would you like to pursue this in the ... |
| Q333 | - |  |  | SI | Shopping |
| Q334 | - |  |  | SI | Shopping- What has been your level of interest in ... |
| Q335 | - |  |  | SI | Shopping- What has been your level of interest in ... |
| Q336 | - |  |  | SI | Shopping- Do you currently participate in this act... |
| Q337 | - |  |  | SI | Shopping- Would you like to pursue this in the fut... |
| Q338 | - |  |  | SI | Photography |
| Q339 | - |  |  | SI | Photography- What has been your level of interest ... |
| Q34 | - |  |  | SI | Radio- What has been your level of interest in the... |
| Q340 | - |  |  | SI | Photography- What has been your level of interest ... |
| Q341 | - |  |  | SI | Photography- Do you currently participate in this ... |
| Q342 | - |  |  | SI | Photography- Would you like to pursue this in the ... |
| Q343 | - |  |  | SI | Painting / Drawing |
| Q344 | - |  |  | SI | Painting / Drawing- What has been your level of in... |
| Q345 | - |  |  | SI | Painting / Drawing- What has been your level of in... |
| Q346 | - |  |  | SI | Painting / Drawing- Do you currently participate i... |
| Q347 | - |  |  | SI | Painting / Drawing- Would you like to pursue this ... |
| Q35 | - |  |  | SI | Radio- What has been your level of interest in the... |
| Q36 | - |  |  | SI | Radio- Do you currently participate in this activi... |
| Q37 | - |  |  | SI | Radio- Would you like to pursue this in the future... |
| Q38 | - |  |  | SI | Walking |
| Q39 | - |  |  | SI | Walking- What has been your level of interest in t... |
| Q40 | - |  |  | SI | Walking- What has been your level of interest in t... |
| Q41 | - |  |  | SI | Walking- Do you currently participate in this acti... |
| Q42 | - |  |  | SI | Walking- Would you like to pursue this in the futu... |
| Q43 | - |  |  | SI | Car Repair |
| Q44 | - |  |  | SI | Car Repair- What has been your level of interest i... |
| Q45 | - |  |  | SI | Car Repair- What has been your level of interest i... |
| Q46 | - |  |  | SI | Car Repair- Do you currently participate in this a... |
| Q47 | - |  |  | SI | Car Repair- Would you like to pursue this in the f... |
| Q48 | - |  |  | SI | Writing |
| Q49 | - |  |  | SI | Writing- What has been your level of interest in t... |
| Q50 | - |  |  | SI | Writing- What has been your level of interest in t... |
| Q51 | - |  |  | SI | Writing- Do you currently participate in this acti... |
| Q52 | - |  |  | SI | Writing- Would you like to pursue this in the futu... |
| Q53 | - |  |  | SI | Dancing |
| Q54 | - |  |  | SI | Dancing- What has been your level of interest in t... |
| Q55 | - |  |  | SI | Dancing- What has been your level of interest in t... |
| Q56 | - |  |  | SI | Dancing- Do you currently participate in this acti... |
| Q57 | - |  |  | SI | Dancing- Would you like to pursue this in the futu... |
| Q58 | - |  |  | SI | Golf |
| Q59 | - |  |  | SI | Golf- What has been your level of interest in the ... |
| Q60 | - |  |  | SI | Golf- What has been your level of interest in the ... |
| Q61 | - |  |  | SI | Golf- Do you currently participate in this activit... |
| Q62 | - |  |  | SI | Golf- Would you like to pursue this in the future? |
| Q63 | - |  |  | SI | Football |
| Q64 | - |  |  | SI | Football- What has been your level of interest in ... |
| Q65 | - |  |  | SI | Football- What has been your level of interest in ... |
| Q66 | - |  |  | SI | Football- Do you currently participate in this act... |
| Q67 | - |  |  | SI | Football- Would you like to pursue this in the fut... |
| Q68 | - |  |  | SI | Listening to Popular Music |
| Q69 | - |  |  | SI | Listening to Popular Music- What has been your lev... |
| Q70 | - |  |  | SI | Listening to Popular Music- What has been your lev... |
| Q71 | - |  |  | SI | Listening to Popular Music- Do you currently parti... |
| Q72 | - |  |  | SI | Listening to Popular Music- Would you like to purs... |
| Q73 | - |  |  | SI | Puzzles |
| Q74 | - |  |  | SI | Puzzles- What has been your level of interest in t... |
| Q75 | - |  |  | SI | Puzzles- What has been your level of interest in t... |
| Q76 | - |  |  | SI | Puzzles- Do you currently participate in this acti... |
| Q77 | - |  |  | SI | Puzzles- Would you like to pursue this in the futu... |
| Q78 | - |  |  | SI | Holiday Activities |
| Q79 | - |  |  | SI | Holiday Activiites- What has been your level of in... |
| Q80 | - |  |  | SI | Holiday Activities- What has been your level of in... |
| Q81 | - |  |  | SI | Holiday Activities- Do you currently participate i... |
| Q82 | - |  |  | SI | Holiday Activities- Would you like to pursue this ... |
| Q83 | - |  |  | SI | Pets / Livestock |
| Q84 | - |  |  | SI | Pets / Livestock- What has been your level of inte... |
| Q85 | - |  |  | SI | Pets / Livestock- What has been your level of inte... |
| Q86 | - |  |  | SI | Pets / Livestock- Do you currently participate in ... |
| Q87 | - |  |  | SI | Pets / Livestock- Would you like to pursue this in... |
| Q88 | - |  |  | SI | Movies |
| Q89 | - |  |  | SI | Movies- What has been your level of interest in th... |
| Q90 | - |  |  | SI | Movies- What has been your level of interest in th... |
| Q91 | - |  |  | SI | Movies- Do you currently participate in this activ... |
| Q92 | - |  |  | SI | Movies- Would you like to pursue this in the futur... |
| Q93 | - |  |  | SI | Listening to Classical Music |
| Q94 | - |  |  | SI | Listening to Classical Music- What has been your l... |
| Q95 | - |  |  | SI | Listening to Classical Music- What has been your l... |
| Q96 | - |  |  | SI | Listening to Classical Music- Do you currently par... |
| Q97 | - |  |  | SI | Listening to Classical Music- Would you like to pu... |
| Q98 | - |  |  | SI | Speeches / Lectures |
| Q99 | - |  |  | SI | Lectures- What has been your level of interest in ... |
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