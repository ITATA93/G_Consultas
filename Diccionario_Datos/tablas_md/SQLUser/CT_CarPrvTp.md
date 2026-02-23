# SQLUser.CT_CarPrvTp

**Schema:** SQLUser
**Columnas:** 337
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de Profesionales**. Médicos y personal de salud.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTCPT_RowId | bigint | PK |  | NO | - |
| CTCPT_ARCIM_DR | varchar |  | FK | SI | Des Ref ARCIM |
| CTCPT_ActiveFlag | varchar |  |  | NO | Active Flag |
| CTCPT_Code | varchar |  |  | NO | Care Provider Type Code |
| CTCPT_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| CTCPT_CreatedDate | date |  |  | SI | Created Date |
| CTCPT_CreatedTime | time |  |  | SI | Created Time |
| CTCPT_CreatedUser_DR | bigint |  | FK | SI | Created User |
| CTCPT_DateFrom | date |  |  | SI | Date From |
| CTCPT_DateTo | date |  |  | SI | Date To |
| CTCPT_Desc | varchar |  |  | NO | Care Provider Type Description |
| CTCPT_InternalType | varchar |  |  | SI | Internal Type |
| CTCPT_Owner | varchar |  |  | SI | Owner |
| CTCPT_UpdatedDate | date |  |  | SI | Updated Date |
| CTCPT_UpdatedTime | time |  |  | SI | Updated Time |
| CTCPT_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Fecha Evaluación |
| Q02 | - |  |  | SI | Raza |
| Q03 | - |  |  | SI | Año de Educación |
| Q04 | - |  |  | SI | Dominancia |
| Q05 | - |  |  | SI | PRACTICA: Tetera (Nominación) |
| Q06 | - |  |  | SI | PRACTICA: Tetera Resultado (Nominación) |
| Q07 | - |  |  | SI | PRACTICA: Frutilla (Nominación) |
| Q08 | - |  |  | SI | PRACTICA: Frutilla resultado (Nominación) |
| Q09 | - |  |  | SI | 1.Corona (Nominación) |
| Q10 | - |  |  | SI | 1.Corona Resultado (Nominación) |
| Q100 | - |  |  | SI | 4.Bicicleta (Comprensión) |
| Q101 | - |  |  | SI | 4.Bicicleta Resulado (Comprensión) |
| Q102 | - |  |  | SI | 5.Televisor (Repetición) |
| Q103 | - |  |  | SI | 5.Televisor Resultado (Repetición) |
| Q104 | - |  |  | SI | 5.Televisor (Comprensión) |
| Q105 | - |  |  | SI | 5.Televisor Resultado (Comprensión) |
| Q106 | - |  |  | SI | 6.Cuaderno (Repetición) |
| Q107 | - |  |  | SI | 6.Cuaderno Resultado (Repetición) |
| Q108 | - |  |  | SI | 6.Cuaderno (Comprensión) |
| Q109 | - |  |  | SI | 6.Cuaderno Resultado (Comprensión) |
| Q11 | - |  |  | SI | 2.Cebolla (Nominación) |
| Q110 | - |  |  | SI | 7.Conejo (Repetición) |
| Q111 | - |  |  | SI | 7.Conejo Resultado (Repetición) |
| Q112 | - |  |  | SI | 7.Conejo (Comprensión) |
| Q113 | - |  |  | SI | 7.Conejo Resultado (Comprensión) |
| Q114 | - |  |  | SI | 8.Micrófono (Repetición) |
| Q115 | - |  |  | SI | 8.Micrófono Resultado (Repetición) |
| Q116 | - |  |  | SI | 8.Micrófono (Comprensión) |
| Q117 | - |  |  | SI | 8.Micrófono Resultado (Comprensión) |
| Q118 | - |  |  | SI | 9.Cigarro (Repetición) |
| Q119 | - |  |  | SI | 9.Cigarro Resultado (Repetición) |
| Q12 | - |  |  | SI | 2.Cebolla Resultado (Nominación) |
| Q120 | - |  |  | SI | 9.Cigarro (Comprensión) |
| Q121 | - |  |  | SI | 9.Cigarro Resultado (Comprensión) |
| Q122 | - |  |  | SI | 10.Plátano (Repetición) |
| Q123 | - |  |  | SI | 10.Plátano Resultado (Repetición) |
| Q124 | - |  |  | SI | 10.Plátano (Comprensión) |
| Q125 | - |  |  | SI | 10.Plátano Resultado (Comprensión) |
| Q126 | - |  |  | SI | SubTotal 1 al 10 (Repetición) |
| Q127 | - |  |  | SI | SubTotal 1 al 10 (Comprensión) |
| Q128 | - |  |  | SI | 11.Espinas (Repetición) |
| Q129 | - |  |  | SI | 11.Espinas Resultado (Repetición) |
| Q13 | - |  |  | SI | 3.Espada (Nominación) |
| Q130 | - |  |  | SI | 11.Espinas (Comprensión) |
| Q131 | - |  |  | SI | 11.Espinas Resultado (Comprensión) |
| Q132 | - |  |  | SI | 12.Zapatilla (Repetición) |
| Q133 | - |  |  | SI | 12.Zapatilla Resultado (Repetición) |
| Q134 | - |  |  | SI | 12.Zapatilla (Comprensión) |
| Q135 | - |  |  | SI | 12.Zapatilla Resultado (Comprensión) |
| Q136 | - |  |  | SI | 13.Termómetro (Repetición) |
| Q137 | - |  |  | SI | 13.Termómetro Resultado (Repetición) |
| Q138 | - |  |  | SI | 13.Termómetro (Comprensión) |
| Q139 | - |  |  | SI | 13.Termómetro Resultado (Comprensión) |
| Q14 | - |  |  | SI | 3.Espada Resultado (Nominación) |
| Q140 | - |  |  | SI | 14.Coliflo (Repetición) |
| Q141 | - |  |  | SI | 14.Coliflo Resultado (Repetición) |
| Q142 | - |  |  | SI | 14.Coliflo (Comprensión) |
| Q143 | - |  |  | SI | 14.Coliflo Resultado (Comprensión) |
| Q144 | - |  |  | SI | 15.Interruptor (Repetición) |
| Q145 | - |  |  | SI | 15.Interruptor Resultado (Repetición) |
| Q146 | - |  |  | SI | 15.Interruptor (Comprensión) |
| Q147 | - |  |  | SI | 15.Interruptor resultado (Comprensión) |
| Q148 | - |  |  | SI | 16.Abeja (Repetición) |
| Q149 | - |  |  | SI | 16.Abeja Resultado (Repetición) |
| Q15 | - |  |  | SI | 4.Bicicleta (Nominación) |
| Q150 | - |  |  | SI | 16.Abeja (Comprensión) |
| Q151 | - |  |  | SI | 16.Abeja Resultado (Comprensión) |
| Q152 | - |  |  | SI | 17.Dinosaurio (Repetición) |
| Q153 | - |  |  | SI | 17.Dinosaurio Resultado (Repetición) |
| Q154 | - |  |  | SI | 17.Dinosaurio (Comprensión) |
| Q155 | - |  |  | SI | 17.Dinosaurio Resultado (Comprensión) |
| Q156 | - |  |  | SI | 18.Rastrillo (Repetición) |
| Q157 | - |  |  | SI | 18.Rastrillo Resultado (Repetición) |
| Q158 | - |  |  | SI | 18.Rastrillo (Comprensión) |
| Q159 | - |  |  | SI | 18.Rastrillo Resultado (Comprensión) |
| Q16 | - |  |  | SI | 4.Bicicleta Resultado (Nominación) |
| Q160 | - |  |  | SI | 19.Raqueta (Repetición) |
| Q161 | - |  |  | SI | 19.Raqueta Resultado (Repetición) |
| Q162 | - |  |  | SI | 19.Raqueta (Comprensión) |
| Q163 | - |  |  | SI | 19.Raqueta Resultado (Comprensión) |
| Q164 | - |  |  | SI | 20.Leopardo (Repetición) |
| Q165 | - |  |  | SI | 20.Leopardo Resultado (Repetición) |
| Q166 | - |  |  | SI | 20.Leopardo (Comprensión) |
| Q167 | - |  |  | SI | 20.Leopardo Resultado (Comprensión) |
| Q168 | - |  |  | SI | SubTotal 11 al 20 (Repetición) |
| Q169 | - |  |  | SI | SubTotal 11 al 20 (Comprensión) |
| Q17 | - |  |  | SI | 5.Televisor (Nominación) |
| Q170 | - |  |  | SI | 21.Espárrago (Repetición) |
| Q171 | - |  |  | SI | 21.Espárrago Resultado (Repetición) |
| Q172 | - |  |  | SI | 21.Espárrago (Comprensión) |
| Q173 | - |  |  | SI | 21.Espárrago resultado (Comprensión) |
| Q174 | - |  |  | SI | 22.Jeroglífico (Repetición) |
| Q175 | - |  |  | SI | 22.Jeroglífico Resultado (Repetición) |
| Q176 | - |  |  | SI | 22.Jeroglífico (Comprensión) |
| Q177 | - |  |  | SI | 22.Jeroglífico Resultado (Comprensión) |
| Q178 | - |  |  | SI | 23.Rinoceronte (Repetición) |
| Q179 | - |  |  | SI | 23.Rinoceronte resultado (Repetición) |
| Q18 | - |  |  | SI | 5.Televisor Resultado (Nominación) |
| Q180 | - |  |  | SI | 23.Rinoceronte (Comprensión) |
| Q181 | - |  |  | SI | 23.Rinoceronte Resultado (Comprensión) |
| Q182 | - |  |  | SI | 24.Limusina (Repetición) |
| Q183 | - |  |  | SI | 24.Limusina Resultado (Repetición) |
| Q184 | - |  |  | SI | 24.Limusina (Comprensión) |
| Q185 | - |  |  | SI | 24.Limusina Resultado (Comprensión) |
| Q186 | - |  |  | SI | 25.Hipopótamo (Repetición) |
| Q187 | - |  |  | SI | 25.Hipopótamo Resultado (Repetición) |
| Q188 | - |  |  | SI | 25.Hipopótamo (Comprensión) |
| Q189 | - |  |  | SI | 25.Hipopótamo Resultado (Comprensión) |
| Q19 | - |  |  | SI | 6.Cuaderno (Nominación) |
| Q190 | - |  |  | SI | 26.Destornillador (Repetición) |
| Q191 | - |  |  | SI | 26.Destornillador resultado (Repetición) |
| Q192 | - |  |  | SI | 26.Destornillador (Comprensión) |
| Q193 | - |  |  | SI | 26.Destornillador Resultado (Comprensión) |
| Q194 | - |  |  | SI | 27.Estetoscopio (Repetición) |
| Q195 | - |  |  | SI | 27.Estetoscopio Resultado (Repetición) |
| Q196 | - |  |  | SI | 27.Estetoscopio (Comprensión) |
| Q197 | - |  |  | SI | 27.Estetoscopio Resultado (Comprensión) |
| Q198 | - |  |  | SI | 28.Máscara (Repetición) |
| Q199 | - |  |  | SI | 28.Máscara Resultado (Repetición) |
| Q20 | - |  |  | SI | 6.Cuaderno Resultado (Nominación) |
| Q200 | - |  |  | SI | 28.Máscara (Comprensión) |
| Q201 | - |  |  | SI | 28.Máscara Resultado (Comprensión) |
| Q202 | - |  |  | SI | 29.Cuncuna (Repetición) |
| Q203 | - |  |  | SI | 29.Cuncuna Resultado (Repetición) |
| Q204 | - |  |  | SI | 29.Cuncuna (Comprensión) |
| Q205 | - |  |  | SI | 29.Cuncuna Resultado (Comprensión) |
| Q206 | - |  |  | SI | 30.Resbalín (Repetición) |
| Q207 | - |  |  | SI | 30.Resbalín Resultado (Repetición) |
| Q208 | - |  |  | SI | 30.Resbalín (Comprensión) |
| Q209 | - |  |  | SI | 30.Resbalín Resultado (Comprensión) |
| Q21 | - |  |  | SI | 7.Conejo (Nominación) |
| Q210 | - |  |  | SI | SubTotal 21 al 30 (Repetición) |
| Q211 | - |  |  | SI | SubTotal 21 al 30 (Comprensión) |
| Q212 | - |  |  | SI | TOTAL (REPETICIÓN) |
| Q213 | - |  |  | SI | TOTAL (COMPRENSIÓN) |
| Q214 | - |  |  | SI | PRACTICA: Tetera (Semántica) - [C] |
| Q215 | - |  |  | SI | PRACTICA: Tetera Comentario (Semántica) |
| Q216 | - |  |  | SI | PRACTICA: Frutilla (Semántica) - [A] |
| Q217 | - |  |  | SI | PRACTICA: Frutilla Comentario (Semántica) |
| Q218 | - |  |  | SI | 1.Corona (Semántica) - [A] |
| Q219 | - |  |  | SI | 1.Corona Comentario (Semántica) |
| Q22 | - |  |  | SI | 7.Conejo Resultado (Nominación) |
| Q220 | - |  |  | SI | 2.Cebolla (Semántica) - [B] |
| Q221 | - |  |  | SI | 2.Cebolla Comentario (Semántica) |
| Q222 | - |  |  | SI | 3.Espada (Semántica) - [C] |
| Q223 | - |  |  | SI | 3.Espada Comentario (Semántica) |
| Q224 | - |  |  | SI | 4.Bicicleta (Semántica) - [C] |
| Q225 | - |  |  | SI | 4.Bicicleta Comentario (Semántica) |
| Q226 | - |  |  | SI | 5.Televisor (Semántica) - [C] |
| Q227 | - |  |  | SI | 5.Televisor Comentario (Semántica) |
| Q228 | - |  |  | SI | 6.Cuaderno (Semántica) - [A] |
| Q229 | - |  |  | SI | 6.Cuaderno Comentario (Semántica) |
| Q23 | - |  |  | SI | 8.Micrófono (Nominación) |
| Q230 | - |  |  | SI | 7.Conejo (Semántica) - [D] |
| Q231 | - |  |  | SI | 7.Conejo Comentario (Semántica) |
| Q232 | - |  |  | SI | 8.Micrófono (Semántica) - [A] |
| Q233 | - |  |  | SI | 8.Micrófono Comentario (Semántica) |
| Q234 | - |  |  | SI | 9.Cigarro (Semántica) - [B] |
| Q235 | - |  |  | SI | 9.Cigarro Comentario (Semántica) |
| Q236 | - |  |  | SI | 10.Plátano (Semántica) - [C] |
| Q237 | - |  |  | SI | 10.Plátano Comentario (Semántica) |
| Q238 | - |  |  | SI | 11.Espinas (Semántica) - [A] |
| Q239 | - |  |  | SI | 11.Espinas Comentario (Semántica) |
| Q24 | - |  |  | SI | 8.Micrófono Resultado (Nominación) |
| Q240 | - |  |  | SI | 12.Zapatilla (Semántica) - [A] |
| Q241 | - |  |  | SI | 12.Zapatilla Comentario (Semántica) |
| Q242 | - |  |  | SI | 13.Termómetro (Semántica) - [C] |
| Q243 | - |  |  | SI | 13.Termómetro Comentario (Semántica) |
| Q244 | - |  |  | SI | 14.Coliflor (Semántica) - [A] |
| Q245 | - |  |  | SI | 14.Coliflor Comentario (Semántica) |
| Q246 | - |  |  | SI | 15.Interruptor (Semántica) - [C] |
| Q247 | - |  |  | SI | 15.Interruptor Comentario (Semántica) |
| Q248 | - |  |  | SI | 16.Abeja (Semántica) - [D] |
| Q249 | - |  |  | SI | 16.Abeja Comentario (Semántica) |
| Q25 | - |  |  | SI | 9.Cigarro (Nominación) |
| Q250 | - |  |  | SI | 17.Dinosaurio (Semántica) - [C] |
| Q251 | - |  |  | SI | 17.Dinosaurio Comentario (Semántica) |
| Q252 | - |  |  | SI | 18.Rastrillo (Semántica) - [D] |
| Q253 | - |  |  | SI | 18.Rastrillo Comentario (Semántica) |
| Q254 | - |  |  | SI | 19.Raqueta (Semántica) - [C] |
| Q255 | - |  |  | SI | 19.Raqueta Comentario (Semántica) |
| Q256 | - |  |  | SI | 20.Leopardo (Semántica) - [D] |
| Q257 | - |  |  | SI | 20.Leopardo Comentario (Semántica) |
| Q258 | - |  |  | SI | 21.Espárrago (Semántica) - [C] |
| Q259 | - |  |  | SI | 21.Espárrago Comentario (Semántica) |
| Q26 | - |  |  | SI | 9.Cigarro Resultado (Nominación) |
| Q260 | - |  |  | SI | 22.Jeroglífico (Semántica) - [B] |
| Q261 | - |  |  | SI | 22.Jeroglífico Comentario (Semántica) |
| Q262 | - |  |  | SI | 23.Rinoceronte (Semántica) - [A] |
| Q263 | - |  |  | SI | 23.Rinoceronte Comentario (Semántica) |
| Q264 | - |  |  | SI | 24.Limusina (Semántica) - [C] |
| Q265 | - |  |  | SI | 24.Limusina Comentario (Semántica) |
| Q266 | - |  |  | SI | 25.Hipopótamo (Semántica) - [B] |
| Q267 | - |  |  | SI | 25.Hipopótamo Comentario (Semántica) |
| Q268 | - |  |  | SI | 26.Destornillador (Semántica) - [B] |
| Q269 | - |  |  | SI | 26.Destornillador Comentario (Semántica) |
| Q27 | - |  |  | SI | 10.Plátano (Nominación) |
| Q270 | - |  |  | SI | 27.Estetoscopio (Semántica) - [D] |
| Q271 | - |  |  | SI | 27.Estetoscopio Comentario (Semántica) |
| Q272 | - |  |  | SI | 28.Máscara (Semántica) - [C] |
| Q273 | - |  |  | SI | 28.Máscara Comentario (Semántica) |
| Q274 | - |  |  | SI | 29.Cuncuna (Semántica) - [B] |
| Q275 | - |  |  | SI | 29.Cuncuna Comentario (Semántica) |
| Q276 | - |  |  | SI | 30.Resbalín (Semántica) - [A] |
| Q277 | - |  |  | SI | 30.Resbalín Comentario (Semántica) |
| Q278 | - |  |  | SI | SubTotal 01 al 10 (Semántica) |
| Q279 | - |  |  | SI | SubTotal 11 al 20 (Semántica) |
| Q28 | - |  |  | SI | 10.Plátano Resultado (Nominación) |
| Q280 | - |  |  | SI | SubTotal 21 al 30 (Semántica) |
| Q281 | - |  |  | SI | TOTAL (SEMÁNTICA) |
| Q29 | - |  |  | SI | 11.Espinas (Nominación) |
| Q30 | - |  |  | SI | 11.Espinas Resultado (Nominación) |
| Q31 | - |  |  | SI | 12.Zapatilla (Nominación) |
| Q32 | - |  |  | SI | 12.Zapatilla Resultado (Nominación) |
| Q33 | - |  |  | SI | 13.Termómetro (Nominación) |
| Q34 | - |  |  | SI | 13.Termómetro Resultado (Nominación) |
| Q35 | - |  |  | SI | 14.Coliflor (Nominación) |
| Q36 | - |  |  | SI | 14.Coliflor Resultado (Nominación) |
| Q37 | - |  |  | SI | 15.Interruptor (Nominación) |
| Q38 | - |  |  | SI | 15.Interruptor Resultado (Nominación) |
| Q39 | - |  |  | SI | 16.Abeja (Nominación) |
| Q40 | - |  |  | SI | 16.Abeja Resultado (Nominación) |
| Q41 | - |  |  | SI | 17.Dinosaurio (Nominación) |
| Q42 | - |  |  | SI | 17.Dinosaurio Resultado (Nominación) |
| Q43 | - |  |  | SI | 18.Rastrillo (Nominación) |
| Q44 | - |  |  | SI | 18.Rastrillo Resultado (Nominación) |
| Q45 | - |  |  | SI | 19.Raqueta (Nominación) |
| Q46 | - |  |  | SI | 19.Raqueta Resultado (Nominación) |
| Q47 | - |  |  | SI | 20.Leopardo (Nominación) |
| Q48 | - |  |  | SI | 20.Leopardo Resultado (Nominación) |
| Q49 | - |  |  | SI | 21.Espárrago (Nominación) |
| Q50 | - |  |  | SI | 21.Espárrago Resultado (Nominación) |
| Q51 | - |  |  | SI | 22.Jeroglífico (Nominación) |
| Q52 | - |  |  | SI | 22.Jeroglífico Resultado (Nominación) |
| Q53 | - |  |  | SI | 23.Rinoceronte (Nominación) |
| Q54 | - |  |  | SI | 23.Rinoceronte Resultado (Nominación) |
| Q55 | - |  |  | SI | 24.Limusina (Nominación) |
| Q56 | - |  |  | SI | 24.Limusina Resultado (Nominación) |
| Q57 | - |  |  | SI | 25.Hipopótamo (Nominación) |
| Q58 | - |  |  | SI | 25.Hipopótamo Resultado (Nominación) |
| Q59 | - |  |  | SI | 26.Destornillador (Nominación) |
| Q60 | - |  |  | SI | 26.Destornillador Resultado (Nominación) |
| Q61 | - |  |  | SI | 27.Estetoscopio (Nominación) |
| Q62 | - |  |  | SI | 27.Estetoscopio Resultado (Nominación) |
| Q63 | - |  |  | SI | 28.Máscara (Nominación) |
| Q64 | - |  |  | SI | 28.Máscara Resultado (Nominación) |
| Q65 | - |  |  | SI | 29.Cuncuna (Nominación) |
| Q66 | - |  |  | SI | 29.Cuncuna resultado (Nominación) |
| Q67 | - |  |  | SI | 30.Resbalín (Nominación) |
| Q68 | - |  |  | SI | 30.Resbalín Resultado (Nominación) |
| Q69 | - |  |  | SI | SubTotal 01 al 10 (Nominación) |
| Q70 | - |  |  | SI | SubTotal 11 al 20 (Nominación) |
| Q71 | - |  |  | SI | SubTotal 21 al 30 (Nominación) |
| Q72 | - |  |  | SI | TOTAL (NOMINACIÓN) |
| Q73 | - |  |  | SI | INSTRUCIONES |
| Q74 | - |  |  | SI | 1. NOMINACIÓN |
| Q75 | - |  |  | SI | 2. REPETICIÓN |
| Q76 | - |  |  | SI | 3. TAREA DE COMPRENSIÓN |
| Q77 | - |  |  | SI | 4. TAREA DE ASOCIACIÓN SEMÁNTICA |
| Q78 | - |  |  | SI | PRACTICA: Tetera (Repetición) |
| Q79 | - |  |  | SI | PRACTICA: Tetera Resultado (Repetición) |
| Q80 | - |  |  | SI | PRACTICA: Tetera (Comprensión) |
| Q81 | - |  |  | SI | PRACTICA: Tetera Resultado (Comprensión) |
| Q82 | - |  |  | SI | PRACTICA: Frutilla (Repetición) |
| Q83 | - |  |  | SI | PRACTICA: Frutilla Resultado (Repetición) |
| Q84 | - |  |  | SI | PRACTICA: Frutilla (Comprensión) |
| Q85 | - |  |  | SI | PRACTICA: Frutilla Resultado (Comprensión) |
| Q86 | - |  |  | SI | 1.Corona (Repetición) |
| Q87 | - |  |  | SI | 1.Corona Resultado (Repetición) |
| Q88 | - |  |  | SI | 1.Corona (Comprensión) |
| Q89 | - |  |  | SI | 1.Corona Resultado (Comprensión) |
| Q90 | - |  |  | SI | 2.Cebolla (Repetición) |
| Q91 | - |  |  | SI | 2.Cebolla Resultado (Repetición) |
| Q92 | - |  |  | SI | 2.Cebolla (Comprensión) |
| Q93 | - |  |  | SI | 2.Cebolla Resultado (Comprensión) |
| Q94 | - |  |  | SI | 3.Espada (Repetición) |
| Q95 | - |  |  | SI | 3.Espada Resultado (Repetición) |
| Q96 | - |  |  | SI | 3.Espada (Comprensión) |
| Q97 | - |  |  | SI | 3.Espada Resultado (Comprensión) |
| Q98 | - |  |  | SI | 4.Bicicleta (Repetición) |
| Q99 | - |  |  | SI | 4.Bicicleta Resultado (Repetición) |
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