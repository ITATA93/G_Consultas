# SQLUser.PA_AdmBloodBags

**Schema:** SQLUser
**Columnas:** 606
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Admisión de Pacientes**. Registra episodios de atención hospitalaria.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| BLD_ParRef | bigint | PK |  | NO | PA_Adm Parent Reference |
| BLD_Childsub | double |  |  | NO | Childsub |
| BLD_Date | date |  |  | SI | Date bag was given |
| BLD_Doctor_DR | varchar |  | FK | SI | des ref to doctor |
| BLD_Number | varchar |  |  | NO | Blood Bag Number |
| BLD_Nurse_DR | varchar |  | FK | SI | des ref to nurse |
| BLD_RowId | varchar |  |  | NO | - |
| BLD_Time | time |  |  | SI | Time bag was given |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Skin Prick Test Information |
| Q04 | - |  |  | SI | Test date |
| Q05 | - |  |  | SI | Test time |
| Q06 | - |  |  | SI | Consent |
| Q07 | - |  |  | SI | Test performed on |
| Q08 | - |  |  | SI | Other test area(s) |
| Q09 | - |  |  | SI | Lancets used |
| Q10 | - |  |  | SI | Other lancet type |
| Q100 | - |  |  | SI | Hazelnut wheal (mm) |
| Q101 | - |  |  | SI | Macadamia wheal (mm) |
| Q102 | - |  |  | SI | Peanut wheal (mm) |
| Q103 | - |  |  | SI | Pecan wheal (mm) |
| Q104 | - |  |  | SI | Pine nut wheal (mm) |
| Q105 | - |  |  | SI | Pistachio wheal (mm) |
| Q106 | - |  |  | SI | Sesame wheal (mm) |
| Q107 | - |  |  | SI | Walnut wheal (mm) |
| Q108 | - |  |  | SI | Almond flare (mm) |
| Q109 | - |  |  | SI | Brazil nut flare (mm) |
| Q11 | - |  |  | SI | Test notes |
| Q110 | - |  |  | SI | Cashew flare (mm) |
| Q111 | - |  |  | SI | Hazelnut flare (mm) |
| Q112 | - |  |  | SI | Macadamia flare (mm) |
| Q113 | - |  |  | SI | Peanut flare (mm) |
| Q114 | - |  |  | SI | Pecan flare (mm) |
| Q115 | - |  |  | SI | Pine nut flare (mm) |
| Q116 | - |  |  | SI | Pistachio flare (mm) |
| Q117 | - |  |  | SI | Sesame flare (mm) |
| Q118 | - |  |  | SI | Walnut flare (mm) |
| Q119 | - |  |  | SI | Fruit and vegetable allergens |
| Q12 | - |  |  | SI | Control Tests and Results |
| Q120 | - |  |  | SI | Wheal (mm) |
| Q121 | - |  |  | SI | Flare (mm) |
| Q122 | - |  |  | SI | Celery |
| Q123 | - |  |  | SI | Green pea |
| Q124 | - |  |  | SI | Mango |
| Q125 | - |  |  | SI | Peach |
| Q126 | - |  |  | SI | Rice |
| Q127 | - |  |  | SI | Rye |
| Q128 | - |  |  | SI | Strawberry |
| Q129 | - |  |  | SI | Banana |
| Q13 | - |  |  | SI | Control |
| Q130 | - |  |  | SI | Tomato |
| Q131 | - |  |  | SI | White potato |
| Q132 | - |  |  | SI | Celery wheal (mm) |
| Q133 | - |  |  | SI | Green pea wheal (mm) |
| Q134 | - |  |  | SI | Mango wheal (mm) |
| Q135 | - |  |  | SI | Peach wheal (mm) |
| Q136 | - |  |  | SI | Rice wheal (mm) |
| Q137 | - |  |  | SI | Rye wheal (mm) |
| Q138 | - |  |  | SI | Strawberry wheal (mm) |
| Q139 | - |  |  | SI | Banana wheal (mm) |
| Q14 | - |  |  | SI | Time |
| Q140 | - |  |  | SI | Tomato wheal (mm) |
| Q141 | - |  |  | SI | White potato wheal (mm) |
| Q142 | - |  |  | SI | Celery flare (mm) |
| Q143 | - |  |  | SI | Green pea flare (mm) |
| Q144 | - |  |  | SI | Mango flare (mm) |
| Q145 | - |  |  | SI | Peach flare (mm) |
| Q146 | - |  |  | SI | Rice flare (mm) |
| Q147 | - |  |  | SI | Rye flare (mm) |
| Q148 | - |  |  | SI | Strawberry flare (mm) |
| Q149 | - |  |  | SI | Banana flare (mm) |
| Q15 | - |  |  | SI | Wheal (mm) |
| Q150 | - |  |  | SI | Tomato flare (mm) |
| Q151 | - |  |  | SI | White potato flare (mm) |
| Q152 | - |  |  | SI | Mite allergens |
| Q153 | - |  |  | SI | Wheal (mm) |
| Q154 | - |  |  | SI | Flare (mm) |
| Q155 | - |  |  | SI | D. Pteronyssinus (HDM) |
| Q156 | - |  |  | SI | Blomia tropicalis |
| Q157 | - |  |  | SI | D. Pteronyssinus (HDM) wheal (mm) |
| Q158 | - |  |  | SI | Blomia tropicalis wheal (mm) |
| Q159 | - |  |  | SI | HDM flare (mm) |
| Q16 | - |  |  | SI | Flare (mm) |
| Q160 | - |  |  | SI | Blomia tropicalis flare (mm) |
| Q161 | - |  |  | SI | Epithelia and insects allergens |
| Q162 | - |  |  | SI | Wheal (mm) |
| Q163 | - |  |  | SI | Flare (mm) |
| Q164 | - |  |  | SI | Cockroach mix |
| Q165 | - |  |  | SI | Cat hair |
| Q166 | - |  |  | SI | Dog epithelia |
| Q167 | - |  |  | SI | Feather mix |
| Q168 | - |  |  | SI | Guinea pig epithelia |
| Q169 | - |  |  | SI | Horse epithelia |
| Q17 | - |  |  | SI | Negative control |
| Q170 | - |  |  | SI | Rabbit dander |
| Q171 | - |  |  | SI | Cockroach mix wheal (mm) |
| Q172 | - |  |  | SI | Cat hair wheal (mm) |
| Q173 | - |  |  | SI | Dog epithelia wheal (mm) |
| Q174 | - |  |  | SI | Feather mix wheal (mm) |
| Q175 | - |  |  | SI | Guinea pig epithelia wheal (mm) |
| Q176 | - |  |  | SI | Horse epithelia wheal (mm) |
| Q177 | - |  |  | SI | Rabbit dander wheal (mm) |
| Q178 | - |  |  | SI | Cockroach mix flare (mm) |
| Q179 | - |  |  | SI | Cat hair flare |
| Q18 | - |  |  | SI | Histamine control |
| Q180 | - |  |  | SI | Dog epithelia flare (mm) |
| Q181 | - |  |  | SI | Feather mix flare (mm) |
| Q182 | - |  |  | SI | Guinea pig epithelia flare (mm) |
| Q183 | - |  |  | SI | Horse epithelia flare (mm) |
| Q184 | - |  |  | SI | Rabbit dander flare (mm) |
| Q185 | - |  |  | SI | Pollen-grass allergens |
| Q186 | - |  |  | SI | Wheal (mm) |
| Q187 | - |  |  | SI | Flare (mm) |
| Q188 | - |  |  | SI | Bahia / Paspalum notatum |
| Q189 | - |  |  | SI | Bermuda / Couch |
| Q19 | - |  |  | SI | Negative control time |
| Q190 | - |  |  | SI | Johnson |
| Q191 | - |  |  | SI | Rye grass |
| Q192 | - |  |  | SI | Bahia / Paspalum notatum wheal (mm) |
| Q193 | - |  |  | SI | Bermuda / Couch wheal (mm) |
| Q194 | - |  |  | SI | Johnson wheal (mm) |
| Q195 | - |  |  | SI | Rye grass wheal (mm) |
| Q196 | - |  |  | SI | Bahia / Paspalum notatum flare (mm) |
| Q197 | - |  |  | SI | Bermuda / Couch flare (mm) |
| Q198 | - |  |  | SI | Johnson flare (mm) |
| Q199 | - |  |  | SI | Rye grass flare (mm) |
| Q20 | - |  |  | SI | Histamine control time |
| Q200 | - |  |  | SI | Pollen-trees allergens flare |
| Q201 | - |  |  | SI | Wheal (mm) |
| Q202 | - |  |  | SI | Flare (mm) |
| Q203 | - |  |  | SI | Acacia spp |
| Q204 | - |  |  | SI | Birch mix |
| Q205 | - |  |  | SI | Eucalyptus |
| Q206 | - |  |  | SI | Pine tree mix |
| Q207 | - |  |  | SI | Acacia spp. wheal (mm) |
| Q208 | - |  |  | SI | Birch mix wheal (mm) |
| Q209 | - |  |  | SI | Eucalyptus wheal (mm) |
| Q21 | - |  |  | SI | Negative wheal (mm) |
| Q210 | - |  |  | SI | Pine tree mix wheal (mm) |
| Q211 | - |  |  | SI | Acacia spp. flare (mm) |
| Q212 | - |  |  | SI | Birch mix flare (mm) |
| Q213 | - |  |  | SI | Eucalyptus flare (mm) |
| Q214 | - |  |  | SI | Pine tree mix flare (mm) |
| Q215 | - |  |  | SI | Mould allergens |
| Q216 | - |  |  | SI | Wheal (mm) |
| Q217 | - |  |  | SI | Flare (mm) |
| Q218 | - |  |  | SI | Alternaria alternata |
| Q219 | - |  |  | SI | Aspergillus fumigatu |
| Q22 | - |  |  | SI | Histamine wheal (mm) |
| Q220 | - |  |  | SI | Alternaria alternata wheal |
| Q221 | - |  |  | SI | Aspergillus fumigatu wheal (mm) |
| Q222 | - |  |  | SI | Alternaria alternata flare (mm) |
| Q223 | - |  |  | SI | Aspergillus fumigatu flare (mm) |
| Q224 | - |  |  | SI | Miscellaneous allergens |
| Q225 | - |  |  | SI | Wheal (mm) |
| Q226 | - |  |  | SI | Flare (mm) |
| Q227 | - |  |  | SI | Latex |
| Q228 | - |  |  | SI | Latex wheal (mm) |
| Q229 | - |  |  | SI | Latex flare (mm) |
| Q23 | - |  |  | SI | Negative flare (mm) |
| Q230 | - |  |  | SI | Dummy1 |
| Q231 | - |  |  | SI | Dummy1 wheal (mm) |
| Q232 | - |  |  | SI | Dummy1 flare (mm) |
| Q233 | - |  |  | SI | Dummy2 |
| Q234 | - |  |  | SI | Dummy2 wheal (mm) |
| Q235 | - |  |  | SI | Dummy2 flare (mm) |
| Q236 | - |  |  | SI | Patient own product allergens |
| Q237 | - |  |  | SI | Wheal (mm) |
| Q238 | - |  |  | SI | Flare (mm) |
| Q239 | - |  |  | SI | Product1 |
| Q24 | - |  |  | SI | Histamine flare (mm) |
| Q240 | - |  |  | SI | Product1 wheal (mm) |
| Q241 | - |  |  | SI | Product1 flare (mm) |
| Q242 | - |  |  | SI | Product2 |
| Q243 | - |  |  | SI | Product2 wheal (mm) |
| Q244 | - |  |  | SI | Product2 flare (mm) |
| Q245 | - |  |  | SI | Product3 |
| Q246 | - |  |  | SI | Product3 wheal (mm) |
| Q247 | - |  |  | SI | Product3 flare (mm) |
| Q248 | - |  |  | SI | Product4 |
| Q249 | - |  |  | SI | Product4 wheal (mm) |
| Q25 | - |  |  | SI | Requested Test Panels and Results |
| Q250 | - |  |  | SI | Product4 flare (mm) |
| Q251 | - |  |  | SI | Product5 |
| Q252 | - |  |  | SI | Product5 wheal (mm) |
| Q253 | - |  |  | SI | Product5 flare (mm) |
| Q254 | - |  |  | SI | Product6 |
| Q255 | - |  |  | SI | Product6 wheal (mm) |
| Q256 | - |  |  | SI | Product6 flare (mm) |
| Q257 | - |  |  | SI | Product7 |
| Q258 | - |  |  | SI | Product7 wheal (mm) |
| Q259 | - |  |  | SI | Product7 flare (mm) |
| Q26 | - |  |  | SI | General food allergens |
| Q260 | - |  |  | SI | Product8 |
| Q261 | - |  |  | SI | Product8 wheal (mm) |
| Q262 | - |  |  | SI | Product8 flare (mm) |
| Q263 | - |  |  | SI | Product9 |
| Q264 | - |  |  | SI | Product9 wheal (mm) |
| Q265 | - |  |  | SI | Product9 flare (mm) |
| Q266 | - |  |  | SI | Product10 |
| Q267 | - |  |  | SI | Product10 wheal (mm) |
| Q268 | - |  |  | SI | Product10 flare (mm) |
| Q269 | - |  |  | SI | Control |
| Q27 | - |  |  | SI | Wheal (mm) |
| Q270 | - |  |  | SI | Control |
| Q271 | - |  |  | SI | Time |
| Q272 | - |  |  | SI | Time |
| Q273 | - |  |  | SI | Wheal (mm) |
| Q274 | - |  |  | SI | Wheal (mm) |
| Q275 | - |  |  | SI | Flare (mm) |
| Q276 | - |  |  | SI | Flare (mm) |
| Q277 | - |  |  | SI | General food allergens |
| Q278 | - |  |  | SI | General food allergens |
| Q279 | - |  |  | SI | General food allergens |
| Q28 | - |  |  | SI | Flare (mm) |
| Q280 | - |  |  | SI | General food allergens |
| Q281 | - |  |  | SI | General food allergens |
| Q282 | - |  |  | SI | Wheal (mm) |
| Q283 | - |  |  | SI | Wheal (mm) |
| Q284 | - |  |  | SI | Wheal (mm) |
| Q285 | - |  |  | SI | Wheal (mm) |
| Q286 | - |  |  | SI | Wheal (mm) |
| Q287 | - |  |  | SI | Flare (mm) |
| Q288 | - |  |  | SI | Flare (mm) |
| Q289 | - |  |  | SI | Flare (mm) |
| Q29 | - |  |  | SI | Cow's milk |
| Q290 | - |  |  | SI | Flare (mm) |
| Q291 | - |  |  | SI | Flare (mm) |
| Q292 | - |  |  | SI | Seafood allergens |
| Q293 | - |  |  | SI | Seafood allergens |
| Q294 | - |  |  | SI | Seafood allergens |
| Q295 | - |  |  | SI | Seafood allergens |
| Q296 | - |  |  | SI | Seafood allergens |
| Q297 | - |  |  | SI | Seafood allergens |
| Q298 | - |  |  | SI | Seafood allergens |
| Q299 | - |  |  | SI | Seafood allergens |
| Q30 | - |  |  | SI | Egg yolk |
| Q300 | - |  |  | SI | Wheal (mm) |
| Q301 | - |  |  | SI | Wheal (mm) |
| Q302 | - |  |  | SI | Wheal (mm) |
| Q303 | - |  |  | SI | Wheal (mm) |
| Q304 | - |  |  | SI | Wheal (mm) |
| Q305 | - |  |  | SI | Wheal (mm) |
| Q306 | - |  |  | SI | Wheal (mm) |
| Q307 | - |  |  | SI | Wheal (mm) |
| Q308 | - |  |  | SI | Flare (mm) |
| Q309 | - |  |  | SI | Flare (mm) |
| Q31 | - |  |  | SI | Egg white |
| Q310 | - |  |  | SI | Flare (mm) |
| Q311 | - |  |  | SI | Flare (mm) |
| Q312 | - |  |  | SI | Flare (mm) |
| Q313 | - |  |  | SI | Flare (mm) |
| Q314 | - |  |  | SI | Flare (mm) |
| Q315 | - |  |  | SI | Flare (mm) |
| Q316 | - |  |  | SI | Meat allergens |
| Q317 | - |  |  | SI | Meat allergens |
| Q318 | - |  |  | SI | Meat allergens |
| Q319 | - |  |  | SI | Wheal (mm) |
| Q32 | - |  |  | SI | Soy bean |
| Q320 | - |  |  | SI | Wheal (mm) |
| Q321 | - |  |  | SI | Wheal (mm) |
| Q322 | - |  |  | SI | Flare (mm) |
| Q323 | - |  |  | SI | Flare (mm) |
| Q324 | - |  |  | SI | Flare (mm) |
| Q325 | - |  |  | SI | Nuts and seeds allergens |
| Q326 | - |  |  | SI | Nuts and seeds allergens |
| Q327 | - |  |  | SI | Nuts and seeds allergens |
| Q328 | - |  |  | SI | Nuts and seeds allergens |
| Q329 | - |  |  | SI | Nuts and seeds allergens |
| Q33 | - |  |  | SI | Wheat |
| Q330 | - |  |  | SI | Nuts and seeds allergens |
| Q331 | - |  |  | SI | Nuts and seeds allergens |
| Q332 | - |  |  | SI | Nuts and seeds allergens |
| Q333 | - |  |  | SI | Nuts and seeds allergens |
| Q334 | - |  |  | SI | Nuts and seeds allergens |
| Q335 | - |  |  | SI | Nuts and seeds allergens |
| Q336 | - |  |  | SI | Wheal (mm) |
| Q337 | - |  |  | SI | Wheal (mm) |
| Q338 | - |  |  | SI | Wheal (mm) |
| Q339 | - |  |  | SI | Wheal (mm) |
| Q34 | - |  |  | SI | Cow's milk wheal (mm) |
| Q340 | - |  |  | SI | Wheal (mm) |
| Q341 | - |  |  | SI | Wheal (mm) |
| Q342 | - |  |  | SI | Wheal (mm) |
| Q343 | - |  |  | SI | Wheal (mm) |
| Q344 | - |  |  | SI | Wheal (mm) |
| Q345 | - |  |  | SI | Wheal (mm) |
| Q346 | - |  |  | SI | Wheal (mm) |
| Q347 | - |  |  | SI | Flare (mm) |
| Q348 | - |  |  | SI | Flare (mm) |
| Q349 | - |  |  | SI | Flare (mm) |
| Q35 | - |  |  | SI | Egg yolk wheal (mm) |
| Q350 | - |  |  | SI | Flare (mm) |
| Q351 | - |  |  | SI | Flare (mm) |
| Q352 | - |  |  | SI | Flare (mm) |
| Q353 | - |  |  | SI | Flare (mm) |
| Q354 | - |  |  | SI | Flare (mm) |
| Q355 | - |  |  | SI | Flare (mm) |
| Q356 | - |  |  | SI | Flare (mm) |
| Q357 | - |  |  | SI | Flare (mm) |
| Q358 | - |  |  | SI | Fruit and vegetable allergens |
| Q359 | - |  |  | SI | Fruit and vegetable allergens |
| Q36 | - |  |  | SI | Egg white wheal (mm) |
| Q360 | - |  |  | SI | Fruit and vegetable allergens |
| Q361 | - |  |  | SI | Fruit and vegetable allergens |
| Q362 | - |  |  | SI | Fruit and vegetable allergens |
| Q363 | - |  |  | SI | Fruit and vegetable allergens |
| Q364 | - |  |  | SI | Fruit and vegetable allergens |
| Q365 | - |  |  | SI | Fruit and vegetable allergens |
| Q366 | - |  |  | SI | Fruit and vegetable allergens |
| Q367 | - |  |  | SI | Fruit and vegetable allergens |
| Q368 | - |  |  | SI | Wheal (mm) |
| Q369 | - |  |  | SI | Wheal (mm) |
| Q37 | - |  |  | SI | Soy bean wheal (mm) |
| Q370 | - |  |  | SI | Wheal (mm) |
| Q371 | - |  |  | SI | Wheal (mm) |
| Q372 | - |  |  | SI | Wheal (mm) |
| Q373 | - |  |  | SI | Wheal (mm) |
| Q374 | - |  |  | SI | Wheal (mm) |
| Q375 | - |  |  | SI | Wheal (mm) |
| Q376 | - |  |  | SI | Wheal (mm) |
| Q377 | - |  |  | SI | Wheal (mm) |
| Q378 | - |  |  | SI | Flare (mm) |
| Q379 | - |  |  | SI | Flare (mm) |
| Q38 | - |  |  | SI | Wheat wheal (mm) |
| Q380 | - |  |  | SI | Flare (mm) |
| Q381 | - |  |  | SI | Flare (mm) |
| Q382 | - |  |  | SI | Flare (mm) |
| Q383 | - |  |  | SI | Flare (mm) |
| Q384 | - |  |  | SI | Flare (mm) |
| Q385 | - |  |  | SI | Flare (mm) |
| Q386 | - |  |  | SI | Flare (mm) |
| Q387 | - |  |  | SI | Flare (mm) |
| Q388 | - |  |  | SI | Mite allergens |
| Q389 | - |  |  | SI | Mite allergens |
| Q39 | - |  |  | SI | Cow's milk flare (mm) |
| Q390 | - |  |  | SI | Wheal (mm) |
| Q391 | - |  |  | SI | Wheal (mm) |
| Q392 | - |  |  | SI | Flare (mm) |
| Q393 | - |  |  | SI | Flare (mm) |
| Q394 | - |  |  | SI | Epithelia and insects allergens |
| Q395 | - |  |  | SI | Epithelia and insects allergens |
| Q396 | - |  |  | SI | Epithelia and insects allergens |
| Q397 | - |  |  | SI | Epithelia and insects allergens |
| Q398 | - |  |  | SI | Epithelia and insects allergens |
| Q399 | - |  |  | SI | Epithelia and insects allergens |
| Q40 | - |  |  | SI | Egg yolk flare (mm) |
| Q400 | - |  |  | SI | Epithelia and insects allergens |
| Q401 | - |  |  | SI | Wheal (mm) |
| Q402 | - |  |  | SI | Wheal (mm) |
| Q403 | - |  |  | SI | Wheal (mm) |
| Q404 | - |  |  | SI | Wheal (mm) |
| Q405 | - |  |  | SI | Wheal (mm) |
| Q406 | - |  |  | SI | Wheal (mm) |
| Q407 | - |  |  | SI | Wheal (mm) |
| Q408 | - |  |  | SI | Flare (mm) |
| Q409 | - |  |  | SI | Flare (mm) |
| Q41 | - |  |  | SI | Egg white flare (mm) |
| Q410 | - |  |  | SI | Flare (mm) |
| Q411 | - |  |  | SI | Flare (mm) |
| Q412 | - |  |  | SI | Flare (mm) |
| Q413 | - |  |  | SI | Flare (mm) |
| Q414 | - |  |  | SI | Flare (mm) |
| Q415 | - |  |  | SI | Pollen-grass allergens |
| Q416 | - |  |  | SI | Pollen-grass allergens |
| Q417 | - |  |  | SI | Pollen-grass allergens |
| Q418 | - |  |  | SI | Pollen-grass allergens |
| Q419 | - |  |  | SI | Wheal (mm) |
| Q42 | - |  |  | SI | Soy bean flare (mm) |
| Q420 | - |  |  | SI | Wheal (mm) |
| Q421 | - |  |  | SI | Wheal (mm) |
| Q422 | - |  |  | SI | Wheal (mm) |
| Q423 | - |  |  | SI | Flare (mm) |
| Q424 | - |  |  | SI | Flare (mm) |
| Q425 | - |  |  | SI | Flare (mm) |
| Q426 | - |  |  | SI | Flare (mm) |
| Q427 | - |  |  | SI | Pollen-trees allergens flare |
| Q428 | - |  |  | SI | Pollen-trees allergens flare |
| Q429 | - |  |  | SI | Pollen-trees allergens flare |
| Q43 | - |  |  | SI | Wheat flare (mm) |
| Q430 | - |  |  | SI | Pollen-trees allergens flare |
| Q431 | - |  |  | SI | Wheal (mm) |
| Q432 | - |  |  | SI | Wheal (mm) |
| Q433 | - |  |  | SI | Wheal (mm) |
| Q434 | - |  |  | SI | Wheal (mm) |
| Q435 | - |  |  | SI | Flare (mm) |
| Q436 | - |  |  | SI | Flare (mm) |
| Q437 | - |  |  | SI | Flare (mm) |
| Q438 | - |  |  | SI | Flare (mm) |
| Q439 | - |  |  | SI | Mould allergens |
| Q44 | - |  |  | SI | Seafood allergens |
| Q440 | - |  |  | SI | Mould allergens |
| Q441 | - |  |  | SI | Mould allergens |
| Q442 | - |  |  | SI | Mould allergens |
| Q443 | - |  |  | SI | Wheal (mm) |
| Q444 | - |  |  | SI | Wheal (mm) |
| Q445 | - |  |  | SI | Wheal (mm) |
| Q446 | - |  |  | SI | Wheal (mm) |
| Q447 | - |  |  | SI | Flare (mm) |
| Q448 | - |  |  | SI | Flare (mm) |
| Q449 | - |  |  | SI | Flare (mm) |
| Q45 | - |  |  | SI | Wheal (mm) |
| Q450 | - |  |  | SI | Flare (mm) |
| Q451 | - |  |  | SI | Patient own product allergens |
| Q452 | - |  |  | SI | Patient own product allergens |
| Q453 | - |  |  | SI | Patient own product allergens |
| Q454 | - |  |  | SI | Patient own product allergens |
| Q455 | - |  |  | SI | Patient own product allergens |
| Q456 | - |  |  | SI | Patient own product allergens |
| Q457 | - |  |  | SI | Patient own product allergens |
| Q458 | - |  |  | SI | Patient own product allergens |
| Q459 | - |  |  | SI | Patient own product allergens |
| Q46 | - |  |  | SI | Flare (mm) |
| Q460 | - |  |  | SI | Wheal (mm) |
| Q461 | - |  |  | SI | Wheal (mm) |
| Q462 | - |  |  | SI | Wheal (mm) |
| Q463 | - |  |  | SI | Wheal (mm) |
| Q464 | - |  |  | SI | Wheal (mm) |
| Q465 | - |  |  | SI | Wheal (mm) |
| Q466 | - |  |  | SI | Wheal (mm) |
| Q467 | - |  |  | SI | Wheal (mm) |
| Q468 | - |  |  | SI | Wheal (mm) |
| Q469 | - |  |  | SI | Flare (mm) |
| Q47 | - |  |  | SI | Crab |
| Q470 | - |  |  | SI | Flare (mm) |
| Q471 | - |  |  | SI | Flare (mm) |
| Q472 | - |  |  | SI | Flare (mm) |
| Q473 | - |  |  | SI | Flare (mm) |
| Q474 | - |  |  | SI | Flare (mm) |
| Q475 | - |  |  | SI | Flare (mm) |
| Q476 | - |  |  | SI | Flare (mm) |
| Q477 | - |  |  | SI | Flare (mm) |
| Q478 | - |  |  | SI | Miscellaneous allergens |
| Q479 | - |  |  | SI | Miscellaneous allergens |
| Q48 | - |  |  | SI | Lobster |
| Q480 | - |  |  | SI | Miscellaneous allergens |
| Q481 | - |  |  | SI | Wheal (mm) |
| Q482 | - |  |  | SI | Wheal (mm) |
| Q483 | - |  |  | SI | Wheal (mm) |
| Q484 | - |  |  | SI | Flare (mm) |
| Q485 | - |  |  | SI | Flare (mm) |
| Q486 | - |  |  | SI | Flare (mm) |
| Q487 | - |  |  | SI | Patient own product allergens |
| Q488 | - |  |  | SI | Negative control |
| Q489 | - |  |  | SI | Histamine control |
| Q49 | - |  |  | SI | Shrimp |
| Q490 | - |  |  | SI | Cow's milk |
| Q491 | - |  |  | SI | Egg yolk |
| Q492 | - |  |  | SI | Egg white |
| Q493 | - |  |  | SI | Soy bean |
| Q494 | - |  |  | SI | Wheat |
| Q495 | - |  |  | SI | Crab |
| Q496 | - |  |  | SI | Lobster |
| Q497 | - |  |  | SI | Shrimp |
| Q498 | - |  |  | SI | Codfish |
| Q499 | - |  |  | SI | Oyster |
| Q50 | - |  |  | SI | Codfish |
| Q500 | - |  |  | SI | Salmon |
| Q501 | - |  |  | SI | Sardine |
| Q502 | - |  |  | SI | Tuna |
| Q503 | - |  |  | SI | Beef |
| Q504 | - |  |  | SI | Chicken |
| Q505 | - |  |  | SI | Pork |
| Q506 | - |  |  | SI | Almond |
| Q507 | - |  |  | SI | Brazil nut |
| Q508 | - |  |  | SI | Cashew |
| Q509 | - |  |  | SI | Hazelnut |
| Q51 | - |  |  | SI | Oyster |
| Q510 | - |  |  | SI | Macadamia |
| Q511 | - |  |  | SI | Peanut |
| Q512 | - |  |  | SI | Pecan |
| Q513 | - |  |  | SI | Pine nut |
| Q514 | - |  |  | SI | Pistachio |
| Q515 | - |  |  | SI | Sesame |
| Q516 | - |  |  | SI | Walnut |
| Q517 | - |  |  | SI | Celery |
| Q518 | - |  |  | SI | Green pea |
| Q519 | - |  |  | SI | Mango |
| Q52 | - |  |  | SI | Salmon |
| Q520 | - |  |  | SI | Peach |
| Q521 | - |  |  | SI | Rice |
| Q522 | - |  |  | SI | Rye |
| Q523 | - |  |  | SI | Strawberry |
| Q524 | - |  |  | SI | Banana |
| Q525 | - |  |  | SI | Tomato |
| Q526 | - |  |  | SI | White potato |
| Q527 | - |  |  | SI | D. Pteronyssinus (HDM) |
| Q528 | - |  |  | SI | Blomia tropicalis |
| Q529 | - |  |  | SI | Cockroach mix |
| Q53 | - |  |  | SI | Sardine |
| Q530 | - |  |  | SI | Cat hair |
| Q531 | - |  |  | SI | Dog epithelia |
| Q532 | - |  |  | SI | Feather mix |
| Q533 | - |  |  | SI | Guinea pig epithelia |
| Q534 | - |  |  | SI | Horse epithelia |
| Q535 | - |  |  | SI | Rabbit dander |
| Q536 | - |  |  | SI | Bahia / Paspalum notatum |
| Q537 | - |  |  | SI | Bermuda / Couch |
| Q538 | - |  |  | SI | Johnson |
| Q539 | - |  |  | SI | Rye grass |
| Q54 | - |  |  | SI | Tuna |
| Q540 | - |  |  | SI | Acacia spp. |
| Q541 | - |  |  | SI | Birch mix |
| Q542 | - |  |  | SI | Eucalyptus |
| Q543 | - |  |  | SI | Pine tree mix |
| Q544 | - |  |  | SI | Alternaria alternata |
| Q545 | - |  |  | SI | Aspergillus fumigatu |
| Q546 | - |  |  | SI | Latex |
| Q547 | - |  |  | SI | Dummy1 |
| Q548 | - |  |  | SI | Dummy2 |
| Q549 | - |  |  | SI | Product1 |
| Q55 | - |  |  | SI | Crab wheal (mm) |
| Q550 | - |  |  | SI | Product2 |
| Q551 | - |  |  | SI | Product3 |
| Q552 | - |  |  | SI | Product4 |
| Q553 | - |  |  | SI | Product5 |
| Q554 | - |  |  | SI | Product6 |
| Q555 | - |  |  | SI | Product7 |
| Q556 | - |  |  | SI | Product8 |
| Q557 | - |  |  | SI | Product9 |
| Q558 | - |  |  | SI | Product10 |
| Q56 | - |  |  | SI | Lobster wheal (mm) |
| Q57 | - |  |  | SI | Shrimp wheal (mm) |
| Q58 | - |  |  | SI | Codfish wheal (mm) |
| Q59 | - |  |  | SI | Oyster wheal (mm) |
| Q60 | - |  |  | SI | Salmon wheal (mm) |
| Q61 | - |  |  | SI | Sardine wheal (mm) |
| Q62 | - |  |  | SI | Tuna wheal (mm) |
| Q63 | - |  |  | SI | Crab flare (mm) |
| Q64 | - |  |  | SI | Lobster flare (mm) |
| Q65 | - |  |  | SI | Shrimp flare (mm) |
| Q66 | - |  |  | SI | Codfish flare (mm) |
| Q67 | - |  |  | SI | Oyster flare (mm) |
| Q68 | - |  |  | SI | Salmon flare (mm) |
| Q69 | - |  |  | SI | Sardine flare (mm) |
| Q70 | - |  |  | SI | Tuna flare (mm) |
| Q71 | - |  |  | SI | Meat allergens |
| Q72 | - |  |  | SI | Wheal (mm) |
| Q73 | - |  |  | SI | Flare (mm) |
| Q74 | - |  |  | SI | Beef |
| Q75 | - |  |  | SI | Chicken |
| Q76 | - |  |  | SI | Pork |
| Q77 | - |  |  | SI | Beef wheal (mm) |
| Q78 | - |  |  | SI | Chicken wheal (mm) |
| Q79 | - |  |  | SI | Pork wheal (mm) |
| Q80 | - |  |  | SI | Beef flare (mm) |
| Q81 | - |  |  | SI | Chicken flare (mm) |
| Q82 | - |  |  | SI | Pork flare (mm) |
| Q83 | - |  |  | SI | Nuts and seeds allergens |
| Q84 | - |  |  | SI | Wheal (mm) |
| Q85 | - |  |  | SI | Flare (mm) |
| Q86 | - |  |  | SI | Almond |
| Q87 | - |  |  | SI | Brazil nut |
| Q88 | - |  |  | SI | Cashew |
| Q89 | - |  |  | SI | Hazelnut |
| Q90 | - |  |  | SI | Macadamia |
| Q91 | - |  |  | SI | Peanut |
| Q92 | - |  |  | SI | Pecan |
| Q93 | - |  |  | SI | Pine nut |
| Q94 | - |  |  | SI | Pistachio |
| Q95 | - |  |  | SI | Sesame |
| Q96 | - |  |  | SI | Walnut |
| Q97 | - |  |  | SI | Almond wheal (mm) |
| Q98 | - |  |  | SI | Brazil nut wheal (mm) |
| Q99 | - |  |  | SI | Cashew wheal (mm) |
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