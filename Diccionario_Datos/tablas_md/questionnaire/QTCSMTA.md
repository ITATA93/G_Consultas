# questionnaire.QTCSMTA

> Spasticity and Muscle Tone Assessment - Lower Limb

**Schema:** questionnaire
**Columnas:** 540
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Spasticity and Muscle Tone Assessment - Lower Limb

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | Assessment being completed by |
| Q04 | varchar |  |  | SI | Impacted side |
| Q05 | varchar |  |  | SI | The following assessment table incorporates the Mo... |
| Q06 | varchar |  |  | SI | Heading Legend |
| Q07 | varchar |  |  | SI | R1: |
| Q08 | varchar |  |  | SI | Angle of catch seen at velocity V2 or V3 |
| Q09 | varchar |  |  | SI | R2: |
| Q10 | varchar |  |  | SI | Full range of motion achieved when muscle is at re... |
| Q100 | varchar |  |  | SI | TC.MASKLRL |
| Q100ObsDR | varchar |  | FK | SI | TC.MASKLRL DR |
| Q101 | varchar |  |  | SI | TC.MASKMRL |
| Q101ObsDR | varchar |  | FK | SI | TC.MASKMRL DR |
| Q102 | varchar |  |  | SI | Ankle Plantarflexor Muscle Tone, MAS (Left) |
| Q102ObsDR | varchar |  | FK | SI | Ankle Plantarflexor Muscle Tone, MAS (Left) DR |
| Q103 | varchar |  |  | SI | Ankle Dorsiflexor Muscle Tone - Knee at Zero degre... |
| Q103ObsDR | varchar |  | FK | SI | Ankle Dorsiflexor Muscle Tone - Knee at Zero degre... |
| Q104 | varchar |  |  | SI | Ankle Dorsiflexor Muscle Tone - Knee at 90 degrees... |
| Q104ObsDR | varchar |  | FK | SI | Ankle Dorsiflexor Muscle Tone - Knee at 90 degrees... |
| Q105 | varchar |  |  | SI | Forefoot Invertor Muscle Tone, MAS (Left) |
| Q105ObsDR | varchar |  | FK | SI | Forefoot Invertor Muscle Tone, MAS (Left) DR |
| Q106 | varchar |  |  | SI | Forefoot Evertor Muscle Tone, MAS (Left) |
| Q106ObsDR | varchar |  | FK | SI | Forefoot Evertor Muscle Tone, MAS (Left) DR |
| Q107 | varchar |  |  | SI | Hip Flexor Strength, MRC Scale (Left) |
| Q107ObsDR | varchar |  | FK | SI | Hip Flexor Strength, MRC Scale (Left) DR |
| Q108 | varchar |  |  | SI | Hip Flexor Strength, KTMG Scale (Left) |
| Q108ObsDR | varchar |  | FK | SI | Hip Flexor Strength, KTMG Scale (Left) DR |
| Q109 | varchar |  |  | SI | Hip Extensor Strength, MRC Scale (Left) |
| Q109ObsDR | varchar |  | FK | SI | Hip Extensor Strength, MRC Scale (Left) DR |
| Q11 | varchar |  |  | SI | R2-R1: |
| Q110 | varchar |  |  | SI | Hip Extensor Strength, KTMG Scale (Left) |
| Q110ObsDR | varchar |  | FK | SI | Hip Extensor Strength, KTMG Scale (Left) DR |
| Q111 | varchar |  |  | SI | Hip Abductor Strength, MRC Scale (Left) |
| Q111ObsDR | varchar |  | FK | SI | Hip Abductor Strength, MRC Scale (Left) DR |
| Q112 | varchar |  |  | SI | Hip Abductor Strength, KTMG Scale (Left) |
| Q112ObsDR | varchar |  | FK | SI | Hip Abductor Strength, KTMG Scale (Left) DR |
| Q113 | varchar |  |  | SI | Hip Adductor Strength, MRC Scale (Left) |
| Q113ObsDR | varchar |  | FK | SI | Hip Adductor Strength, MRC Scale (Left) DR |
| Q114 | varchar |  |  | SI | Hip Adductor Strength, KTMG Scale (Left) |
| Q114ObsDR | varchar |  | FK | SI | Hip Adductor Strength, KTMG Scale (Left) DR |
| Q115 | varchar |  |  | SI | Hip Internal Rotator Strength, MRC Scale (Left) |
| Q115ObsDR | varchar |  | FK | SI | Hip Internal Rotator Strength, MRC Scale (Left) DR |
| Q116 | varchar |  |  | SI | Hip Internal Rotator Strength, KTMG Scale (Left) |
| Q116ObsDR | varchar |  | FK | SI | Hip Internal Rotator Strength, KTMG Scale (Left) D... |
| Q117 | varchar |  |  | SI | Hip External Rotator Strength, MRC Scale (Left) |
| Q117ObsDR | varchar |  | FK | SI | Hip External Rotator Strength, MRC Scale (Left) DR |
| Q118 | varchar |  |  | SI | Hip External Rotator Strength, KTMG Scale (Left) |
| Q118ObsDR | varchar |  | FK | SI | Hip External Rotator Strength, KTMG Scale (Left) D... |
| Q119 | varchar |  |  | SI | Knee Flexor Strength, MRC Scale (Left) |
| Q119ObsDR | varchar |  | FK | SI | Knee Flexor Strength, MRC Scale (Left) DR |
| Q12 | varchar |  |  | SI | Indicates the level of dynamic contracture in the ... |
| Q120 | varchar |  |  | SI | Knee Flexor Strength, KTMG Scale (Left) |
| Q120ObsDR | varchar |  | FK | SI | Knee Flexor Strength, KTMG Scale (Left) DR |
| Q121 | varchar |  |  | SI | Knee Extensor Strength, MRC Scale (Left) |
| Q121ObsDR | varchar |  | FK | SI | Knee Extensor Strength, MRC Scale (Left) DR |
| Q122 | varchar |  |  | SI | Knee Extensor Strength, KTMG Scale (Left) |
| Q122ObsDR | varchar |  | FK | SI | Knee Extensor Strength, KTMG Scale (Left) DR |
| Q123 | varchar |  |  | SI | Knee Internal Rotator Strength, MRC Scale (Left) |
| Q123ObsDR | varchar |  | FK | SI | Knee Internal Rotator Strength, MRC Scale (Left) D... |
| Q124 | varchar |  |  | SI | Knee (Internally Rotated) Extensor Strength, KTMG ... |
| Q124ObsDR | varchar |  | FK | SI | Knee (Internally Rotated) Extensor Strength, KTMG ... |
| Q125 | varchar |  |  | SI | Knee (Externally Rotated) Extensor Strength, KTMG ... |
| Q125ObsDR | varchar |  | FK | SI | Knee (Externally Rotated) Extensor Strength, KTMG ... |
| Q126 | varchar |  |  | SI | Ankle Plantar Flexor Strength, MRC Scale (Left) |
| Q126ObsDR | varchar |  | FK | SI | Ankle Plantar Flexor Strength, MRC Scale (Left) DR |
| Q127 | varchar |  |  | SI | Ankle Plantar Flexor Strength, KTMG Scale (Left) |
| Q127ObsDR | varchar |  | FK | SI | Ankle Plantar Flexor Strength, KTMG Scale (Left) D... |
| Q128 | varchar |  |  | SI | Ankle Dorsiflexor Strength, Knee at 0°, MRC Scale ... |
| Q128ObsDR | varchar |  | FK | SI | Ankle Dorsiflexor Strength, Knee at 0°, MRC Scale ... |
| Q129 | varchar |  |  | SI | Ankle Dorsiflexor Strength, Knee at 0 degrees, KTM... |
| Q129ObsDR | varchar |  | FK | SI | Ankle Dorsiflexor Strength, Knee at 0 degrees, KTM... |
| Q13 | varchar |  |  | SI | X - MTS: |
| Q130 | varchar |  |  | SI | Ankle Dorsiflexor Strength, Knee at 90°, MRC Scale... |
| Q130ObsDR | varchar |  | FK | SI | Ankle Dorsiflexor Strength, Knee at 90°, MRC Scale... |
| Q131 | varchar |  |  | SI | Ankle Dorsiflexor Strength, Knee at 90 degrees, KT... |
| Q131ObsDR | varchar |  | FK | SI | Ankle Dorsiflexor Strength, Knee at 90 degrees, KT... |
| Q132 | varchar |  |  | SI | Forefoot Invertor Strength, MRC Scale (Left) |
| Q132ObsDR | varchar |  | FK | SI | Forefoot Invertor Strength, MRC Scale (Left) DR |
| Q133 | varchar |  |  | SI | Forefoot Invertor Strength, KTMG Scale (Left) |
| Q133ObsDR | varchar |  | FK | SI | Forefoot Invertor Strength, KTMG Scale (Left) DR |
| Q134 | varchar |  |  | SI | Forefoot Evertors, MRC Scale (Left) |
| Q134ObsDR | varchar |  | FK | SI | Forefoot Evertors, MRC Scale (Left) DR |
| Q135 | varchar |  |  | SI | Forefoot Evertor Strength, KTMG Scale (Left) |
| Q135ObsDR | varchar |  | FK | SI | Forefoot Evertor Strength, KTMG Scale (Left) DR |
| Q136 | varchar |  |  | SI | Manual Muscle Test (MMT) grading |
| Q137 | varchar |  |  | SI | Hip |
| Q138 | varchar |  |  | SI | Flexors |
| Q139 | varchar |  |  | SI | Extensors |
| Q14 | varchar |  |  | SI | Modified Tardieu Scale (MTS) Quality of Muscle Rea... |
| Q140 | varchar |  |  | SI | Abductors |
| Q141 | varchar |  |  | SI | Adductors |
| Q142 | varchar |  |  | SI | Internal Rotators |
| Q143 | varchar |  |  | SI | External Rotators |
| Q144 | varchar |  |  | SI | Knee |
| Q145 | varchar |  |  | SI | Flexors |
| Q146 | varchar |  |  | SI | Extensors |
| Q147 | varchar |  |  | SI | Internal Rotators |
| Q148 | varchar |  |  | SI | External Rotators |
| Q149 | varchar |  |  | SI | Popliteal Angle |
| Q15 | varchar |  |  | SI | MAS: |
| Q150 | varchar |  |  | SI | Ankle |
| Q151 | varchar |  |  | SI | Plantar Flexors |
| Q152 | varchar |  |  | SI | Dorsiflexors (Knee at 0°) |
| Q153 | varchar |  |  | SI | Dorsiflexors (Knee at 90°) |
| Q154 | varchar |  |  | SI | Internal Rotators |
| Q155 | varchar |  |  | SI | External Rotators |
| Q156 | varchar |  |  | SI | Invertors |
| Q157 | varchar |  |  | SI | Evertors |
| Q158 | varchar |  |  | SI | Comments |
| Q159 | varchar |  |  | SI | Boyd & Graham's Modified Tardieu Scale (MTS) quant... |
| Q16 | varchar |  |  | SI | Modified Ashworth Scale |
| Q160 | varchar |  |  | SI | Grading is always performed at the same time of da... |
| Q161 | varchar |  |  | SI | The MTS is administered by applying passive stretc... |
| Q162 | varchar |  |  | SI | • The first stretch is ‘as slow as possible’ (refe... |
| Q163 | varchar |  |  | SI | • The second stretch is either at the ‘speed of th... |
| Q164 | varchar |  |  | SI | used to determine both the angle of muscle reactio... |
| Q165 | varchar |  |  | SI | The angle at which the muscle reaction occurs is t... |
| Q166 | varchar |  |  | SI | where 0 indicates ‘no resistance through the cours... |
| Q167 | varchar |  |  | SI | V (Velocity to stretch) |
| Q168 | varchar |  |  | SI | V1 - As slow as possible |
| Q169 | varchar |  |  | SI | V2 - Speed of the limb segment falling |
| Q17 | varchar |  |  | SI | MMT: |
| Q170 | varchar |  |  | SI | V3 - As fast as possible (> natural drop) |
| Q171 | varchar |  |  | SI | R1 (Angle of catch seen at velocity V2 or V3) |
| Q172 | varchar |  |  | SI | R2 (Full range of motion achieved when muscle is a... |
| Q173 | varchar |  |  | SI | R2 - R1 (Indicates the level of dynamic contractur... |
| Q174 | varchar |  |  | SI | By moving the limb at different velocities, the re... |
| Q175 | varchar |  |  | SI | A large difference between R1 & R2 values in the o... |
| Q176 | varchar |  |  | SI | A small difference in the R1 & R2 measurement in t... |
| Q177 | varchar |  |  | SI | The Modified Ashworth scale (MAS) measures resista... |
| Q178 | varchar |  |  | SI | • Place the patient in a supine position. |
| Q179 | varchar |  |  | SI | • If testing a muscle that primarily flexes a join... |
| Q18 | varchar |  |  | SI | Manual Muscle Test |
| Q180 | varchar |  |  | SI | flexed position and move to a position of maximal ... |
| Q181 | varchar |  |  | SI | • If testing a muscle that primarily extends a joi... |
| Q182 | varchar |  |  | SI | • Score based on the classification |
| Q183 | varchar |  |  | SI | The Modified Ashworth scale (MAS) measures resista... |
| Q184 | varchar |  |  | SI | MMT is a standard set of assessments used to measu... |
| Q185 | varchar |  |  | SI | There are two common grading systems used to evalu... |
| Q186 | varchar |  |  | SI | • Medical Research Centre (MRC) Muscle Strength Sc... |
| Q187 | varchar |  |  | SI | • Key to Muscle Grading (KTMG) |
| Q188 | varchar |  |  | SI | The scale in this tool combines the two scales so ... |
| Q189 | varchar |  |  | SI | • Make sure to communicate with the patient all th... |
| Q19 | varchar |  |  | SI | Left |
| Q190 | varchar |  |  | SI | • Work with the non-dominant (or non - injured) si... |
| Q191 | varchar |  |  | SI | • Remind your patient to breathe naturally during ... |
| Q192 | varchar |  |  | SI | • Make sure the patient is dressed in loose clothi... |
| Q193 | varchar |  |  | SI | • Place the patient in an adequately supported pos... |
| Q194 | varchar |  |  | SI | • Always test first in an anti-gravity position. I... |
| Q195 | varchar |  |  | SI | • Resistance needs to be applied directly opposite... |
| Q196 | varchar |  |  | SI | • Plan out the test first, testing all the muscles... |
| Q197 | varchar |  |  | SI | • Always provide adequate stabilisation to unrelat... |
| Q198 | varchar |  |  | SI | stabilisation of the shoulder will prevent extra m... |
| Q199 | varchar |  |  | SI | • Always test both sides in order to compare stren... |
| Q20 | varchar |  |  | SI | Right |
| Q200 | varchar |  |  | SI | • Avoid doing jerking movements when applying resi... |
| Q201 | varchar |  |  | SI | • Discontinue testing if patient complains of pain... |
| Q202 | numeric |  |  | SI | R1 hip flexors (right) |
| Q203 | numeric |  |  | SI | R1 hip extensors (right) |
| Q204 | numeric |  |  | SI | R1 hip abductors (right) |
| Q205 | numeric |  |  | SI | R1 hip adductors (right) |
| Q206 | numeric |  |  | SI | R1 hip internal rotators (right) |
| Q207 | numeric |  |  | SI | R1 hip external rotators (right) |
| Q208 | numeric |  |  | SI | R1 knee flexors (right) |
| Q209 | numeric |  |  | SI | R1 knee extensors (right) |
| Q21 | varchar |  |  | SI | R1 |
| Q210 | numeric |  |  | SI | R1 knee flexors with internal rotators (right) |
| Q211 | numeric |  |  | SI | R1 knee flexors with external rotators (right) |
| Q212 | numeric |  |  | SI | R1 ankle plantar flexors (right) |
| Q213 | numeric |  |  | SI | R1 ankle dorsiflexors - knee at 0° (right) |
| Q214 | numeric |  |  | SI | R1 ankle dorsiflexors - knee at 90° (right) |
| Q215 | numeric |  |  | SI | R1 ankle invertors (right) |
| Q216 | numeric |  |  | SI | R1 ankle evertors (right) |
| Q217 | numeric |  |  | SI | R2 hip flexors (right) |
| Q218 | numeric |  |  | SI | R2 hip extensors (right) |
| Q219 | numeric |  |  | SI | R2 hip abductors (right) |
| Q22 | varchar |  |  | SI | R1 |
| Q220 | numeric |  |  | SI | R2 hip adductors (right) |
| Q221 | numeric |  |  | SI | R2 shoulder hip rotators (right) |
| Q222 | numeric |  |  | SI | R2 hip external rotators (right) |
| Q223 | numeric |  |  | SI | R2 knee flexors (right) |
| Q224 | numeric |  |  | SI | R2 knee extensors (right) |
| Q225 | numeric |  |  | SI | R2 knee flexors with internal rotators (right) |
| Q226 | numeric |  |  | SI | R2 knee flexors with external rotators (right) |
| Q227 | numeric |  |  | SI | R2 ankle plantar flexors (right) |
| Q228 | numeric |  |  | SI | R2 ankle dorsiflexors - knee at 0° (right) |
| Q229 | numeric |  |  | SI | R2 ankle dorsiflexors - knee at 90° (right) |
| Q23 | varchar |  |  | SI | R2 |
| Q230 | numeric |  |  | SI | R2 ankle invertors (right) |
| Q231 | numeric |  |  | SI | R2 ankle evertors (right) |
| Q232 | varchar |  |  | SI | R2 - R1 hip flexors (right) |
| Q233 | varchar |  |  | SI | R2 - R1 hip extensors (right) |
| Q234 | varchar |  |  | SI | R2 - R1 hip abductors (right) |
| Q235 | varchar |  |  | SI | R2 - R1 hip adductors (right) |
| Q236 | varchar |  |  | SI | R2 - R1 hip internal rotators (right) |
| Q237 | varchar |  |  | SI | R2 - R1 hip external rotators (right) |
| Q238 | varchar |  |  | SI | R2 - R1 knee flexors (right) |
| Q239 | varchar |  |  | SI | R2 - R1 knee extensors (right) |
| Q24 | varchar |  |  | SI | R2 |
| Q240 | varchar |  |  | SI | R2 - R1 knee flexors with internal rotators (right... |
| Q241 | varchar |  |  | SI | R2 - R1 knee flexors with external rotators (right... |
| Q242 | varchar |  |  | SI | R2 - R1 ankle plantar flexors (right) |
| Q243 | varchar |  |  | SI | R2 - R1 ankle dorsiflexors - knee at 0° (right) |
| Q244 | varchar |  |  | SI | R2 - R1  ankle dorsiflexors - knee at 90° (right) |
| Q245 | varchar |  |  | SI | R2 - R1 ankle invertors (right) |
| Q246 | varchar |  |  | SI | R2 - R1 ankle evertors (right) |
| Q247 | varchar |  |  | SI | Hip Flexor Spasticity, MTS (Right) |
| Q247ObsDR | varchar |  | FK | SI | Hip Flexor Spasticity, MTS (Right) DR |
| Q248 | varchar |  |  | SI | Hip Extensor Spasticity, MTS (Right) |
| Q248ObsDR | varchar |  | FK | SI | Hip Extensor Spasticity, MTS (Right) DR |
| Q249 | varchar |  |  | SI | Hip Abductor Spasticity, MTS (Right) |
| Q249ObsDR | varchar |  | FK | SI | Hip Abductor Spasticity, MTS (Right) DR |
| Q25 | varchar |  |  | SI | R2 - R1 |
| Q250 | varchar |  |  | SI | Hip Adductor Spasticity, MTS (Right) |
| Q250ObsDR | varchar |  | FK | SI | Hip Adductor Spasticity, MTS (Right) DR |
| Q251 | varchar |  |  | SI | Hip Internal Rotator Spasticity, MTS (Right) |
| Q251ObsDR | varchar |  | FK | SI | Hip Internal Rotator Spasticity, MTS (Right) DR |
| Q252 | varchar |  |  | SI | Hip External Rotator Spasticity, MTS (Right) |
| Q252ObsDR | varchar |  | FK | SI | Hip External Rotator Spasticity, MTS (Right) DR |
| Q253 | varchar |  |  | SI | Knee Flexor Spasticity, MTS (Right) |
| Q253ObsDR | varchar |  | FK | SI | Knee Flexor Spasticity, MTS (Right) DR |
| Q254 | varchar |  |  | SI | Knee Extensor Spasticity, MTS (Right) |
| Q254ObsDR | varchar |  | FK | SI | Knee Extensor Spasticity, MTS (Right) DR |
| Q255 | varchar |  |  | SI | Knee Internal Rotator Spasticity, MTS (Right) |
| Q255ObsDR | varchar |  | FK | SI | Knee Internal Rotator Spasticity, MTS (Right) DR |
| Q256 | varchar |  |  | SI | Knee External Rotator Spasticity, MTS (Right) |
| Q256ObsDR | varchar |  | FK | SI | Knee External Rotator Spasticity, MTS (Right) DR |
| Q257 | varchar |  |  | SI | Ankle Plantar Flexor Spasticity, MTS (Right) |
| Q257ObsDR | varchar |  | FK | SI | Ankle Plantar Flexor Spasticity, MTS (Right) DR |
| Q258 | varchar |  |  | SI | Ankle Dorsiflexor Spasticity, Knee at 0 degrees, M... |
| Q258ObsDR | varchar |  | FK | SI | Ankle Dorsiflexor Spasticity, Knee at 0 degrees, M... |
| Q259 | varchar |  |  | SI | Ankle Dorsiflexor Spasticity, Knee at 90 degrees, ... |
| Q259ObsDR | varchar |  | FK | SI | Ankle Dorsiflexor Spasticity, Knee at 90 degrees, ... |
| Q26 | varchar |  |  | SI | R2 - R1 |
| Q260 | varchar |  |  | SI | Forefoot Invertor Spasticity, MTS (Right) |
| Q260ObsDR | varchar |  | FK | SI | Forefoot Invertor Spasticity, MTS (Right) DR |
| Q261 | varchar |  |  | SI | Forefoot Evertor Spasticity, MTS (Right) |
| Q261ObsDR | varchar |  | FK | SI | Forefoot Evertor Spasticity, MTS (Right) DR |
| Q262 | varchar |  |  | SI | Hip Flexor Muscle Tone, MAS (Right) |
| Q262ObsDR | varchar |  | FK | SI | Hip Flexor Muscle Tone, MAS (Right) DR |
| Q263 | varchar |  |  | SI | Hip Extensor Muscle Tone, MAS (Right) |
| Q263ObsDR | varchar |  | FK | SI | Hip Extensor Muscle Tone, MAS (Right) DR |
| Q264 | varchar |  |  | SI | Hip Adductor Muscle Tone, MAS (Right) |
| Q264ObsDR | varchar |  | FK | SI | Hip Adductor Muscle Tone, MAS (Right) DR |
| Q265 | varchar |  |  | SI | Hip Adductor Muscle Tone, MAS (Right) |
| Q265ObsDR | varchar |  | FK | SI | Hip Adductor Muscle Tone, MAS (Right) DR |
| Q266 | varchar |  |  | SI | Hip Internal Rotator Muscle Tone, MAS (Right) |
| Q266ObsDR | varchar |  | FK | SI | Hip Internal Rotator Muscle Tone, MAS (Right) DR |
| Q267 | varchar |  |  | SI | Hip External Rotator Muscle Tone, MAS (Right) |
| Q267ObsDR | varchar |  | FK | SI | Hip External Rotator Muscle Tone, MAS (Right) DR |
| Q268 | varchar |  |  | SI | Knee Flexor Muscle Tone, MAS (Right) |
| Q268ObsDR | varchar |  | FK | SI | Knee Flexor Muscle Tone, MAS (Right) DR |
| Q269 | varchar |  |  | SI | Knee Extensor Muscle Tone, MAS (Right) |
| Q269ObsDR | varchar |  | FK | SI | Knee Extensor Muscle Tone, MAS (Right) DR |
| Q27 | varchar |  |  | SI | X (MTS) |
| Q270 | varchar |  |  | SI | TC.MASKLRR |
| Q270ObsDR | varchar |  | FK | SI | TC.MASKLRR DR |
| Q271 | varchar |  |  | SI | TC.MASKMRR |
| Q271ObsDR | varchar |  | FK | SI | TC.MASKMRR DR |
| Q272 | varchar |  |  | SI | Ankle Plantarflexor Muscle Tone, MAS (Right) |
| Q272ObsDR | varchar |  | FK | SI | Ankle Plantarflexor Muscle Tone, MAS (Right) DR |
| Q273 | varchar |  |  | SI | Ankle Dorsiflexor Muscle Tone - Knee at Zero degre... |
| Q273ObsDR | varchar |  | FK | SI | Ankle Dorsiflexor Muscle Tone - Knee at Zero degre... |
| Q274 | varchar |  |  | SI | Ankle Dorsiflexor Muscle Tone - Knee at 90 degrees... |
| Q274ObsDR | varchar |  | FK | SI | Ankle Dorsiflexor Muscle Tone - Knee at 90 degrees... |
| Q275 | varchar |  |  | SI | Forefoot Invertor Muscle Tone, MAS (Right) |
| Q275ObsDR | varchar |  | FK | SI | Forefoot Invertor Muscle Tone, MAS (Right) DR |
| Q276 | varchar |  |  | SI | Forefoot Evertor Muscle Tone, MAS (Right) |
| Q276ObsDR | varchar |  | FK | SI | Forefoot Evertor Muscle Tone, MAS (Right) DR |
| Q277 | varchar |  |  | SI | Hip Flexor Strength, MRC Scale (Right) |
| Q277ObsDR | varchar |  | FK | SI | Hip Flexor Strength, MRC Scale (Right) DR |
| Q278 | varchar |  |  | SI | Hip Flexor Strength, KTMG Scale (Right) |
| Q278ObsDR | varchar |  | FK | SI | Hip Flexor Strength, KTMG Scale (Right) DR |
| Q279 | varchar |  |  | SI | Hip Extensor Strength, MRC Scale (Right) |
| Q279ObsDR | varchar |  | FK | SI | Hip Extensor Strength, MRC Scale (Right) DR |
| Q28 | varchar |  |  | SI | X (MTS) |
| Q280 | varchar |  |  | SI | Hip Extensor Strength, KTMG Scale (Right) |
| Q280ObsDR | varchar |  | FK | SI | Hip Extensor Strength, KTMG Scale (Right) DR |
| Q281 | varchar |  |  | SI | Hip Abductor Strength, MRC Scale (Right) |
| Q281ObsDR | varchar |  | FK | SI | Hip Abductor Strength, MRC Scale (Right) DR |
| Q282 | varchar |  |  | SI | Hip Abductor Strength, KTMG Scale (Right) |
| Q282ObsDR | varchar |  | FK | SI | Hip Abductor Strength, KTMG Scale (Right) DR |
| Q283 | varchar |  |  | SI | Hip Adductor Strength, MRC Scale (Right) |
| Q283ObsDR | varchar |  | FK | SI | Hip Adductor Strength, MRC Scale (Right) DR |
| Q284 | varchar |  |  | SI | Hip Adductor Strength, KTMG Scale (Right) |
| Q284ObsDR | varchar |  | FK | SI | Hip Adductor Strength, KTMG Scale (Right) DR |
| Q285 | varchar |  |  | SI | Hip Internal Rotator Strength, MRC Scale (Right) |
| Q285ObsDR | varchar |  | FK | SI | Hip Internal Rotator Strength, MRC Scale (Right) D... |
| Q286 | varchar |  |  | SI | Hip Internal Rotator Strength, KTMG Scale (Right) |
| Q286ObsDR | varchar |  | FK | SI | Hip Internal Rotator Strength, KTMG Scale (Right) ... |
| Q287 | varchar |  |  | SI | Hip External Rotator Strength, MRC Scale (Right) |
| Q287ObsDR | varchar |  | FK | SI | Hip External Rotator Strength, MRC Scale (Right) D... |
| Q288 | varchar |  |  | SI | Hip External Rotator Strength, KTMG Scale (Right) |
| Q288ObsDR | varchar |  | FK | SI | Hip External Rotator Strength, KTMG Scale (Right) ... |
| Q289 | varchar |  |  | SI | Knee Flexor Strength, MRC Scale (Right) |
| Q289ObsDR | varchar |  | FK | SI | Knee Flexor Strength, MRC Scale (Right) DR |
| Q29 | varchar |  |  | SI | MAS |
| Q290 | varchar |  |  | SI | Knee Flexor Strength, KTMG Scale (Right) |
| Q290ObsDR | varchar |  | FK | SI | Knee Flexor Strength, KTMG Scale (Right) DR |
| Q291 | varchar |  |  | SI | Knee Extensor Strength, MRC Scale (Right) |
| Q291ObsDR | varchar |  | FK | SI | Knee Extensor Strength, MRC Scale (Right) DR |
| Q292 | varchar |  |  | SI | Knee Extensor Strength, KTMG Scale (Right) |
| Q292ObsDR | varchar |  | FK | SI | Knee Extensor Strength, KTMG Scale (Right) DR |
| Q293 | varchar |  |  | SI | Knee Internal Rotator Strength, MRC Scale (Right) |
| Q293ObsDR | varchar |  | FK | SI | Knee Internal Rotator Strength, MRC Scale (Right) ... |
| Q294 | varchar |  |  | SI | Knee (Internally Rotated) Extensor Strength, KTMG ... |
| Q294ObsDR | varchar |  | FK | SI | Knee (Internally Rotated) Extensor Strength, KTMG ... |
| Q295 | varchar |  |  | SI | Knee External Rotator Strength, MRC Scale (Right) |
| Q295ObsDR | varchar |  | FK | SI | Knee External Rotator Strength, MRC Scale (Right) ... |
| Q296 | varchar |  |  | SI | Knee (Externally Rotated) Extensor Strength, KTMG ... |
| Q296ObsDR | varchar |  | FK | SI | Knee (Externally Rotated) Extensor Strength, KTMG ... |
| Q297 | varchar |  |  | SI | Ankle Plantar Flexor Strength, MRC Scale (Right) |
| Q297ObsDR | varchar |  | FK | SI | Ankle Plantar Flexor Strength, MRC Scale (Right) D... |
| Q298 | varchar |  |  | SI | Ankle Plantar Flexor Strength, KTMG Scale (Right) |
| Q298ObsDR | varchar |  | FK | SI | Ankle Plantar Flexor Strength, KTMG Scale (Right) ... |
| Q299 | varchar |  |  | SI | Ankle Dorsiflexor Strength, Knee at 0°, MRC Scale ... |
| Q299ObsDR | varchar |  | FK | SI | Ankle Dorsiflexor Strength, Knee at 0°, MRC Scale ... |
| Q30 | varchar |  |  | SI | MAS |
| Q300 | varchar |  |  | SI | Ankle Dorsiflexor Strength, Knee at 0 degrees, KTM... |
| Q300ObsDR | varchar |  | FK | SI | Ankle Dorsiflexor Strength, Knee at 0 degrees, KTM... |
| Q301 | varchar |  |  | SI | Ankle Dorsiflexor Strength, Knee at 90°, MRC Scale... |
| Q301ObsDR | varchar |  | FK | SI | Ankle Dorsiflexor Strength, Knee at 90°, MRC Scale... |
| Q302 | varchar |  |  | SI | Ankle Dorsiflexor Strength, Knee at 90 degrees, KT... |
| Q302ObsDR | varchar |  | FK | SI | Ankle Dorsiflexor Strength, Knee at 90 degrees, KT... |
| Q303 | varchar |  |  | SI | Forefoot Invertor Strength, MRC Scale (Right) |
| Q303ObsDR | varchar |  | FK | SI | Forefoot Invertor Strength, MRC Scale (Right) DR |
| Q304 | varchar |  |  | SI | Forefoot Invertor Strength, KTMG Scale (Right) |
| Q304ObsDR | varchar |  | FK | SI | Forefoot Invertor Strength, KTMG Scale (Right) DR |
| Q305 | varchar |  |  | SI | Forefoot Evertors, MRC Scale (Right) |
| Q305ObsDR | varchar |  | FK | SI | Forefoot Evertors, MRC Scale (Right) DR |
| Q306 | varchar |  |  | SI | Forefoot Evertor Strength, KTMG Scale (Right) |
| Q306ObsDR | varchar |  | FK | SI | Forefoot Evertor Strength, KTMG Scale (Right) DR |
| Q307 | varchar |  |  | SI | R1: |
| Q308 | varchar |  |  | SI | Angle of catch seen at velocity V2 or V3 |
| Q309 | varchar |  |  | SI | R2: |
| Q31 | varchar |  |  | SI | MMT MRC / KTMG |
| Q310 | varchar |  |  | SI | Full range of motion achieved when muscle is at re... |
| Q311 | varchar |  |  | SI | R2 - R1: |
| Q312 | varchar |  |  | SI | Indicates the level of dynamic contracture in the ... |
| Q313 | varchar |  |  | SI | X (MTS): |
| Q314 | varchar |  |  | SI | Modified Tardieu Scale (MTS) Quality of Muscle Rea... |
| Q315 | varchar |  |  | SI | MAS: |
| Q316 | varchar |  |  | SI | Modified Ashworth Scale |
| Q317 | varchar |  |  | SI | MTS: |
| Q318 | varchar |  |  | SI | Manual Muscle Test |
| Q319 | varchar |  |  | SI | R1: Angle of catch seen at velocity V2 or V3 |
| Q32 | varchar |  |  | SI | MMT MRC / KTMG |
| Q320 | varchar |  |  | SI | R2: Full range of motion achieved when muscle is a... |
| Q321 | varchar |  |  | SI | R2 - R1: Indicates the level of dynamic contractur... |
| Q322 | varchar |  |  | SI | X (MTS): Modified Tardieu Scale (MTS) Quality of M... |
| Q323 | varchar |  |  | SI | MAS: Modified Ashworth Scale  |
| Q324 | varchar |  |  | SI | MTS: Manual Muscle Test |
| Q325 | varchar |  |  | SI | Score |
| Q326 | varchar |  |  | SI | Classification |
| Q327 | varchar |  |  | SI | Medical Research Council (MRC) Scale for Muscle St... |
| Q328 | varchar |  |  | SI | Description |
| Q329 | varchar |  |  | SI | 5 |
| Q33 | numeric |  |  | SI | R1 hip flexors (left) |
| Q330 | varchar |  |  | SI | Normal power |
| Q331 | varchar |  |  | SI | 4 |
| Q332 | varchar |  |  | SI | Active movement against gravity and resistance |
| Q333 | varchar |  |  | SI | 3 |
| Q334 | varchar |  |  | SI | Active movement against gravity |
| Q335 | varchar |  |  | SI | 2 |
| Q336 | varchar |  |  | SI | Active movement, with gravity eliminated |
| Q337 | varchar |  |  | SI | 1 |
| Q338 | varchar |  |  | SI | Flicker or trace of contraction |
| Q339 | varchar |  |  | SI | 0 |
| Q34 | numeric |  |  | SI | R1 hip extensors (left) |
| Q340 | varchar |  |  | SI | No contraction |
| Q341 | varchar |  |  | SI | Scale reference - Medical Research Centre (MRC) Mu... |
| Q342 | varchar |  |  | SI | Medical Research Council. Aids to the Investigatio... |
| Q343 | varchar |  |  | SI | https://mrc.ukri.org/documents/pdf/aids-to-the-exa... |
| Q344 | varchar |  |  | SI | Key to Muscle Grading (KTMG) |
| Q345 | varchar |  |  | SI | Explanation / Description |
| Q346 | varchar |  |  | SI | 0: Zero |
| Q347 | varchar |  |  | SI | No contraction felt or seen in the muscle |
| Q348 | varchar |  |  | SI | 1: Trace (T) |
| Q349 | varchar |  |  | SI | Tendon becomes prominent or feeble contraction fel... |
| Q35 | numeric |  |  | SI | R1 hip abductors (left) |
| Q350 | varchar |  |  | SI | 2+: Poor + (P+) |
| Q351 | varchar |  |  | SI | Moves through partial ROM against gravity (support... |
| Q352 | varchar |  |  | SI | 2+: Poor + (P+) |
| Q353 | varchar |  |  | SI | Holds against slight pressure in test position (su... |
| Q354 | varchar |  |  | SI | 2-: Poor - (P-) |
| Q355 | varchar |  |  | SI | Moves through partial ROM (supported in horizontal... |
| Q356 | varchar |  |  | SI | 2: Poor (P) |
| Q357 | varchar |  |  | SI | Movement through complete ROM for the muscle being... |
| Q358 | varchar |  |  | SI | 3+: Fair + (F+) |
| Q359 | varchar |  |  | SI | Holds test position in anti-gravity position again... |
| Q36 | numeric |  |  | SI | R1 hip adductors (left) |
| Q360 | varchar |  |  | SI | 3-: Fair - (F-) |
| Q361 | varchar |  |  | SI | Gradual release from test position occurs in anti-... |
| Q362 | varchar |  |  | SI | 3: Fair (F) |
| Q363 | varchar |  |  | SI | Holds test position in anti-gravity position (no a... |
| Q364 | varchar |  |  | SI | 4+: Good + (G+) |
| Q365 | varchar |  |  | SI | Holds test position in anti-gravity position again... |
| Q366 | varchar |  |  | SI | 4-: Good - (G-) |
| Q367 | varchar |  |  | SI | Holds test position in anti-gravity position again... |
| Q368 | varchar |  |  | SI | 4: Good (G) |
| Q369 | varchar |  |  | SI | Holds test position in anti-gravity position again... |
| Q37 | numeric |  |  | SI | R1 hip internal rotators (left) |
| Q370 | varchar |  |  | SI | 5: Normal (N) |
| Q371 | varchar |  |  | SI | Holds test position in anti-gravity position again... |
| Q372 | varchar |  |  | SI | Scale reference - Key to Muscle Grading |
| Q373 | varchar |  |  | SI | Kendall, F. P., McCreary, E. K., Provance, P. G., ... |
| Q374 | varchar |  |  | SI | Scale reference: |
| Q375 | varchar |  |  | SI | Boyd R, Graham K. Objective measurement of clinica... |
| Q376 | varchar |  |  | SI | Joint |
| Q377 | varchar |  |  | SI | Muscle Group |
| Q378 | varchar |  |  | SI | Hip Abductor Spasticity, MTS (Left) |
| Q378ObsDR | varchar |  | FK | SI | Hip Abductor Spasticity, MTS (Left) DR |
| Q379 | varchar |  |  | SI | Knee External Rotator Strength, MRC Scale (Left) |
| Q379ObsDR | varchar |  | FK | SI | Knee External Rotator Strength, MRC Scale (Left) D... |
| Q38 | numeric |  |  | SI | R1 hip external rotators (left) |
| Q39 | numeric |  |  | SI | R1 knee flexors (left) |
| Q40 | numeric |  |  | SI | R1 knee extensors (left) |
| Q41 | numeric |  |  | SI | R1 knee flexors with internal rotators (left) |
| Q42 | numeric |  |  | SI | R1 knee flexors with external rotators (left) |
| Q43 | numeric |  |  | SI | R1 ankle plantar flexors (left) |
| Q44 | numeric |  |  | SI | R1 ankle dorsiflexors - knee at 0° (left) |
| Q45 | numeric |  |  | SI | R1 ankle dorsiflexors - knee at 90° (left) |
| Q46 | numeric |  |  | SI | R1 ankle invertors (left) |
| Q47 | numeric |  |  | SI | R1 ankle evertors (left) |
| Q48 | numeric |  |  | SI | R2 hip flexors (left) |
| Q49 | numeric |  |  | SI | R2 hip extensors (left) |
| Q50 | numeric |  |  | SI | R2 hip abductors (left) |
| Q51 | numeric |  |  | SI | R2 hip adductors (left) |
| Q52 | numeric |  |  | SI | R2 shoulder hip rotators (left) |
| Q53 | numeric |  |  | SI | R2 hip external rotators (left) |
| Q54 | numeric |  |  | SI | R2 knee flexors (left) |
| Q55 | numeric |  |  | SI | R2 knee extensors (left) |
| Q56 | numeric |  |  | SI | R2 knee flexors with internal rotators (left) |
| Q57 | numeric |  |  | SI | R2 knee flexors with external rotators (left) |
| Q58 | numeric |  |  | SI | R2 ankle plantar flexors (left) |
| Q59 | numeric |  |  | SI | R2 ankle dorsiflexors - knee at 0° (left) |
| Q60 | numeric |  |  | SI | R2 ankle dorsiflexors - knee at 90° (left) |
| Q61 | numeric |  |  | SI | R2 ankle invertors (left) |
| Q62 | numeric |  |  | SI | R2 ankle evertors (left) |
| Q63 | varchar |  |  | SI | R2 - R1 hip flexors (left) |
| Q64 | varchar |  |  | SI | R2 - R1 hip extensors (left) |
| Q65 | varchar |  |  | SI | R2 - R1 hip abductors (left) |
| Q66 | varchar |  |  | SI | R2 - R1 hip adductors (left) |
| Q67 | varchar |  |  | SI | R2 - R1 hip internal rotators (left) |
| Q68 | varchar |  |  | SI | R2 - R1 hip external rotators (left) |
| Q69 | varchar |  |  | SI | R2 - R1 knee flexors (left) |
| Q70 | varchar |  |  | SI | R2 - R1 knee extensors (left) |
| Q71 | varchar |  |  | SI | R2 - R1 knee flexors with internal rotators (left) |
| Q72 | varchar |  |  | SI | R2 - R1 knee flexors with external rotators (left) |
| Q73 | varchar |  |  | SI | R2 - R1 ankle plantar flexors (left) |
| Q74 | varchar |  |  | SI | R2 - R1 ankle dorsiflexors - knee at 0° (left) |
| Q75 | varchar |  |  | SI | R2 - R1 ankle dorsiflexors - knee at 90° (left) |
| Q76 | varchar |  |  | SI | R2 - R1 ankle invertors (left) |
| Q77 | varchar |  |  | SI | R2 - R1 ankle evertors (left) |
| Q78 | varchar |  |  | SI | Hip Flexor Spasticity, MTS (Left) |
| Q78ObsDR | varchar |  | FK | SI | Hip Flexor Spasticity, MTS (Left) DR |
| Q79 | varchar |  |  | SI | Hip Extensor Spasticity, MTS (Left) |
| Q79ObsDR | varchar |  | FK | SI | Hip Extensor Spasticity, MTS (Left) DR |
| Q80 | varchar |  |  | SI | Hip Abductor Spasticity, MTS (Left) |
| Q80ObsDR | varchar |  | FK | SI | Hip Abductor Spasticity, MTS (Left) DR |
| Q81 | varchar |  |  | SI | Hip Internal Rotator Spasticity, MTS (Left) |
| Q81ObsDR | varchar |  | FK | SI | Hip Internal Rotator Spasticity, MTS (Left) DR |
| Q82 | varchar |  |  | SI | Hip External Rotator Spasticity, MTS (Left) |
| Q82ObsDR | varchar |  | FK | SI | Hip External Rotator Spasticity, MTS (Left) DR |
| Q83 | varchar |  |  | SI | Knee Flexor Spasticity, MTS (Left) |
| Q83ObsDR | varchar |  | FK | SI | Knee Flexor Spasticity, MTS (Left) DR |
| Q84 | varchar |  |  | SI | Knee Extensor Spasticity, MTS (Left) |
| Q84ObsDR | varchar |  | FK | SI | Knee Extensor Spasticity, MTS (Left) DR |
| Q85 | varchar |  |  | SI | Knee Internal Rotator Spasticity, MTS (Left) |
| Q85ObsDR | varchar |  | FK | SI | Knee Internal Rotator Spasticity, MTS (Left) DR |
| Q86 | varchar |  |  | SI | Knee External Rotator Spasticity, MTS (Left) |
| Q86ObsDR | varchar |  | FK | SI | Knee External Rotator Spasticity, MTS (Left) DR |
| Q87 | varchar |  |  | SI | Ankle Plantar Flexor Spasticity, MTS (Left) |
| Q87ObsDR | varchar |  | FK | SI | Ankle Plantar Flexor Spasticity, MTS (Left) DR |
| Q88 | varchar |  |  | SI | Ankle Dorsiflexor Spasticity, Knee at 0 degrees, M... |
| Q88ObsDR | varchar |  | FK | SI | Ankle Dorsiflexor Spasticity, Knee at 0 degrees, M... |
| Q89 | varchar |  |  | SI | Ankle Dorsiflexor Spasticity, Knee at 90 degrees, ... |
| Q89ObsDR | varchar |  | FK | SI | Ankle Dorsiflexor Spasticity, Knee at 90 degrees, ... |
| Q90 | varchar |  |  | SI | Forefoot Invertor Spasticity, MTS (Left) |
| Q90ObsDR | varchar |  | FK | SI | Forefoot Invertor Spasticity, MTS (Left) DR |
| Q91 | varchar |  |  | SI | Forefoot Evertor Spasticity, MTS (Left) |
| Q91ObsDR | varchar |  | FK | SI | Forefoot Evertor Spasticity, MTS (Left) DR |
| Q92 | varchar |  |  | SI | Hip Flexor Muscle Tone, MAS (Left) |
| Q92ObsDR | varchar |  | FK | SI | Hip Flexor Muscle Tone, MAS (Left) DR |
| Q93 | varchar |  |  | SI | Hip Extensor Muscle Tone, MAS (Left) |
| Q93ObsDR | varchar |  | FK | SI | Hip Extensor Muscle Tone, MAS (Left) DR |
| Q94 | varchar |  |  | SI | Hip Adductor Muscle Tone, MAS (Left) |
| Q94ObsDR | varchar |  | FK | SI | Hip Adductor Muscle Tone, MAS (Left) DR |
| Q95 | varchar |  |  | SI | Hip Adductor Muscle Tone, MAS (Left) |
| Q95ObsDR | varchar |  | FK | SI | Hip Adductor Muscle Tone, MAS (Left) DR |
| Q96 | varchar |  |  | SI | Hip Internal Rotator Muscle Tone, MAS (Left) |
| Q96ObsDR | varchar |  | FK | SI | Hip Internal Rotator Muscle Tone, MAS (Left) DR |
| Q97 | varchar |  |  | SI | Hip External Rotator Muscle Tone, MAS (Left) |
| Q97ObsDR | varchar |  | FK | SI | Hip External Rotator Muscle Tone, MAS (Left) DR |
| Q98 | varchar |  |  | SI | Knee Flexor Muscle Tone, MAS (Left) |
| Q98ObsDR | varchar |  | FK | SI | Knee Flexor Muscle Tone, MAS (Left) DR |
| Q99 | varchar |  |  | SI | Knee Extensor Muscle Tone, MAS (Left) |
| Q99ObsDR | varchar |  | FK | SI | Knee Extensor Muscle Tone, MAS (Left) DR |
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