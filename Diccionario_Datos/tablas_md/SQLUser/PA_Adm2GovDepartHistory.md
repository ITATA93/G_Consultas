# SQLUser.PA_Adm2GovDepartHistory

**Schema:** SQLUser
**Columnas:** 550
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Admisión de Pacientes**. Registra episodios de atención hospitalaria. Histórico de cambios.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| GDH_ParRef | bigint | PK |  | NO | PA_Adm2 Parent Reference |
| GDH_Childsub | double |  |  | NO | Childsub |
| GDH_Date | date |  |  | SI | Date |
| GDH_DateUpdated | date |  |  | SI | Date Updated |
| GDH_GovernDepart_DR | varchar |  | FK | SI | Des Ref CTNFMICategDepart |
| GDH_HospitalUpdated_DR | bigint |  | FK | SI | Des Ref CTHospital |
| GDH_LocUpdated_DR | bigint |  | FK | SI | Des Ref CTLoc |
| GDH_RowId | varchar |  |  | NO | - |
| GDH_Time | time |  |  | SI | Time  |
| GDH_TimeUpdated | time |  |  | SI | Date Updated |
| GDH_User_DR | bigint |  | FK | SI | Des Ref SSUser |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Assessment being completed by |
| Q04 | - |  |  | SI | Impacted side |
| Q05 | - |  |  | SI | The following assessment table incorporates the Mo... |
| Q06 | - |  |  | SI | Heading Legend |
| Q07 | - |  |  | SI | R1: |
| Q08 | - |  |  | SI | Angle of catch seen at velocity V2 or V3 |
| Q09 | - |  |  | SI | R2: |
| Q10 | - |  |  | SI | Full range of motion achieved when muscle is at re... |
| Q100 | - |  |  | SI | TC.MASKLRL |
| Q100ObsDR | - |  |  | SI | TC.MASKLRL DR |
| Q101 | - |  |  | SI | TC.MASKMRL |
| Q101ObsDR | - |  |  | SI | TC.MASKMRL DR |
| Q102 | - |  |  | SI | Ankle Plantarflexor Muscle Tone, MAS (Left) |
| Q102ObsDR | - |  |  | SI | Ankle Plantarflexor Muscle Tone, MAS (Left) DR |
| Q103 | - |  |  | SI | Ankle Dorsiflexor Muscle Tone - Knee at Zero degre... |
| Q103ObsDR | - |  |  | SI | Ankle Dorsiflexor Muscle Tone - Knee at Zero degre... |
| Q104 | - |  |  | SI | Ankle Dorsiflexor Muscle Tone - Knee at 90 degrees... |
| Q104ObsDR | - |  |  | SI | Ankle Dorsiflexor Muscle Tone - Knee at 90 degrees... |
| Q105 | - |  |  | SI | Forefoot Invertor Muscle Tone, MAS (Left) |
| Q105ObsDR | - |  |  | SI | Forefoot Invertor Muscle Tone, MAS (Left) DR |
| Q106 | - |  |  | SI | Forefoot Evertor Muscle Tone, MAS (Left) |
| Q106ObsDR | - |  |  | SI | Forefoot Evertor Muscle Tone, MAS (Left) DR |
| Q107 | - |  |  | SI | Hip Flexor Strength, MRC Scale (Left) |
| Q107ObsDR | - |  |  | SI | Hip Flexor Strength, MRC Scale (Left) DR |
| Q108 | - |  |  | SI | Hip Flexor Strength, KTMG Scale (Left) |
| Q108ObsDR | - |  |  | SI | Hip Flexor Strength, KTMG Scale (Left) DR |
| Q109 | - |  |  | SI | Hip Extensor Strength, MRC Scale (Left) |
| Q109ObsDR | - |  |  | SI | Hip Extensor Strength, MRC Scale (Left) DR |
| Q11 | - |  |  | SI | R2-R1: |
| Q110 | - |  |  | SI | Hip Extensor Strength, KTMG Scale (Left) |
| Q110ObsDR | - |  |  | SI | Hip Extensor Strength, KTMG Scale (Left) DR |
| Q111 | - |  |  | SI | Hip Abductor Strength, MRC Scale (Left) |
| Q111ObsDR | - |  |  | SI | Hip Abductor Strength, MRC Scale (Left) DR |
| Q112 | - |  |  | SI | Hip Abductor Strength, KTMG Scale (Left) |
| Q112ObsDR | - |  |  | SI | Hip Abductor Strength, KTMG Scale (Left) DR |
| Q113 | - |  |  | SI | Hip Adductor Strength, MRC Scale (Left) |
| Q113ObsDR | - |  |  | SI | Hip Adductor Strength, MRC Scale (Left) DR |
| Q114 | - |  |  | SI | Hip Adductor Strength, KTMG Scale (Left) |
| Q114ObsDR | - |  |  | SI | Hip Adductor Strength, KTMG Scale (Left) DR |
| Q115 | - |  |  | SI | Hip Internal Rotator Strength, MRC Scale (Left) |
| Q115ObsDR | - |  |  | SI | Hip Internal Rotator Strength, MRC Scale (Left) DR |
| Q116 | - |  |  | SI | Hip Internal Rotator Strength, KTMG Scale (Left) |
| Q116ObsDR | - |  |  | SI | Hip Internal Rotator Strength, KTMG Scale (Left) D... |
| Q117 | - |  |  | SI | Hip External Rotator Strength, MRC Scale (Left) |
| Q117ObsDR | - |  |  | SI | Hip External Rotator Strength, MRC Scale (Left) DR |
| Q118 | - |  |  | SI | Hip External Rotator Strength, KTMG Scale (Left) |
| Q118ObsDR | - |  |  | SI | Hip External Rotator Strength, KTMG Scale (Left) D... |
| Q119 | - |  |  | SI | Knee Flexor Strength, MRC Scale (Left) |
| Q119ObsDR | - |  |  | SI | Knee Flexor Strength, MRC Scale (Left) DR |
| Q12 | - |  |  | SI | Indicates the level of dynamic contracture in the ... |
| Q120 | - |  |  | SI | Knee Flexor Strength, KTMG Scale (Left) |
| Q120ObsDR | - |  |  | SI | Knee Flexor Strength, KTMG Scale (Left) DR |
| Q121 | - |  |  | SI | Knee Extensor Strength, MRC Scale (Left) |
| Q121ObsDR | - |  |  | SI | Knee Extensor Strength, MRC Scale (Left) DR |
| Q122 | - |  |  | SI | Knee Extensor Strength, KTMG Scale (Left) |
| Q122ObsDR | - |  |  | SI | Knee Extensor Strength, KTMG Scale (Left) DR |
| Q123 | - |  |  | SI | Knee Internal Rotator Strength, MRC Scale (Left) |
| Q123ObsDR | - |  |  | SI | Knee Internal Rotator Strength, MRC Scale (Left) D... |
| Q124 | - |  |  | SI | Knee (Internally Rotated) Extensor Strength, KTMG ... |
| Q124ObsDR | - |  |  | SI | Knee (Internally Rotated) Extensor Strength, KTMG ... |
| Q125 | - |  |  | SI | Knee (Externally Rotated) Extensor Strength, KTMG ... |
| Q125ObsDR | - |  |  | SI | Knee (Externally Rotated) Extensor Strength, KTMG ... |
| Q126 | - |  |  | SI | Ankle Plantar Flexor Strength, MRC Scale (Left) |
| Q126ObsDR | - |  |  | SI | Ankle Plantar Flexor Strength, MRC Scale (Left) DR |
| Q127 | - |  |  | SI | Ankle Plantar Flexor Strength, KTMG Scale (Left) |
| Q127ObsDR | - |  |  | SI | Ankle Plantar Flexor Strength, KTMG Scale (Left) D... |
| Q128 | - |  |  | SI | Ankle Dorsiflexor Strength, Knee at 0°, MRC Scale ... |
| Q128ObsDR | - |  |  | SI | Ankle Dorsiflexor Strength, Knee at 0°, MRC Scale ... |
| Q129 | - |  |  | SI | Ankle Dorsiflexor Strength, Knee at 0 degrees, KTM... |
| Q129ObsDR | - |  |  | SI | Ankle Dorsiflexor Strength, Knee at 0 degrees, KTM... |
| Q13 | - |  |  | SI | X - MTS: |
| Q130 | - |  |  | SI | Ankle Dorsiflexor Strength, Knee at 90°, MRC Scale... |
| Q130ObsDR | - |  |  | SI | Ankle Dorsiflexor Strength, Knee at 90°, MRC Scale... |
| Q131 | - |  |  | SI | Ankle Dorsiflexor Strength, Knee at 90 degrees, KT... |
| Q131ObsDR | - |  |  | SI | Ankle Dorsiflexor Strength, Knee at 90 degrees, KT... |
| Q132 | - |  |  | SI | Forefoot Invertor Strength, MRC Scale (Left) |
| Q132ObsDR | - |  |  | SI | Forefoot Invertor Strength, MRC Scale (Left) DR |
| Q133 | - |  |  | SI | Forefoot Invertor Strength, KTMG Scale (Left) |
| Q133ObsDR | - |  |  | SI | Forefoot Invertor Strength, KTMG Scale (Left) DR |
| Q134 | - |  |  | SI | Forefoot Evertors, MRC Scale (Left) |
| Q134ObsDR | - |  |  | SI | Forefoot Evertors, MRC Scale (Left) DR |
| Q135 | - |  |  | SI | Forefoot Evertor Strength, KTMG Scale (Left) |
| Q135ObsDR | - |  |  | SI | Forefoot Evertor Strength, KTMG Scale (Left) DR |
| Q136 | - |  |  | SI | Manual Muscle Test (MMT) grading |
| Q137 | - |  |  | SI | Hip |
| Q138 | - |  |  | SI | Flexors |
| Q139 | - |  |  | SI | Extensors |
| Q14 | - |  |  | SI | Modified Tardieu Scale (MTS) Quality of Muscle Rea... |
| Q140 | - |  |  | SI | Abductors |
| Q141 | - |  |  | SI | Adductors |
| Q142 | - |  |  | SI | Internal Rotators |
| Q143 | - |  |  | SI | External Rotators |
| Q144 | - |  |  | SI | Knee |
| Q145 | - |  |  | SI | Flexors |
| Q146 | - |  |  | SI | Extensors |
| Q147 | - |  |  | SI | Internal Rotators |
| Q148 | - |  |  | SI | External Rotators |
| Q149 | - |  |  | SI | Popliteal Angle |
| Q15 | - |  |  | SI | MAS: |
| Q150 | - |  |  | SI | Ankle |
| Q151 | - |  |  | SI | Plantar Flexors |
| Q152 | - |  |  | SI | Dorsiflexors (Knee at 0°) |
| Q153 | - |  |  | SI | Dorsiflexors (Knee at 90°) |
| Q154 | - |  |  | SI | Internal Rotators |
| Q155 | - |  |  | SI | External Rotators |
| Q156 | - |  |  | SI | Invertors |
| Q157 | - |  |  | SI | Evertors |
| Q158 | - |  |  | SI | Comments |
| Q159 | - |  |  | SI | Boyd & Graham's Modified Tardieu Scale (MTS) quant... |
| Q16 | - |  |  | SI | Modified Ashworth Scale |
| Q160 | - |  |  | SI | Grading is always performed at the same time of da... |
| Q161 | - |  |  | SI | The MTS is administered by applying passive stretc... |
| Q162 | - |  |  | SI | • The first stretch is ‘as slow as possible’ (refe... |
| Q163 | - |  |  | SI | • The second stretch is either at the ‘speed of th... |
| Q164 | - |  |  | SI | used to determine both the angle of muscle reactio... |
| Q165 | - |  |  | SI | The angle at which the muscle reaction occurs is t... |
| Q166 | - |  |  | SI | where 0 indicates ‘no resistance through the cours... |
| Q167 | - |  |  | SI | V (Velocity to stretch) |
| Q168 | - |  |  | SI | V1 - As slow as possible |
| Q169 | - |  |  | SI | V2 - Speed of the limb segment falling |
| Q17 | - |  |  | SI | MMT: |
| Q170 | - |  |  | SI | V3 - As fast as possible (> natural drop) |
| Q171 | - |  |  | SI | R1 (Angle of catch seen at velocity V2 or V3) |
| Q172 | - |  |  | SI | R2 (Full range of motion achieved when muscle is a... |
| Q173 | - |  |  | SI | R2 - R1 (Indicates the level of dynamic contractur... |
| Q174 | - |  |  | SI | By moving the limb at different velocities, the re... |
| Q175 | - |  |  | SI | A large difference between R1 & R2 values in the o... |
| Q176 | - |  |  | SI | A small difference in the R1 & R2 measurement in t... |
| Q177 | - |  |  | SI | The Modified Ashworth scale (MAS) measures resista... |
| Q178 | - |  |  | SI | • Place the patient in a supine position. |
| Q179 | - |  |  | SI | • If testing a muscle that primarily flexes a join... |
| Q18 | - |  |  | SI | Manual Muscle Test |
| Q180 | - |  |  | SI | flexed position and move to a position of maximal ... |
| Q181 | - |  |  | SI | • If testing a muscle that primarily extends a joi... |
| Q182 | - |  |  | SI | • Score based on the classification |
| Q183 | - |  |  | SI | The Modified Ashworth scale (MAS) measures resista... |
| Q184 | - |  |  | SI | MMT is a standard set of assessments used to measu... |
| Q185 | - |  |  | SI | There are two common grading systems used to evalu... |
| Q186 | - |  |  | SI | • Medical Research Centre (MRC) Muscle Strength Sc... |
| Q187 | - |  |  | SI | • Key to Muscle Grading (KTMG) |
| Q188 | - |  |  | SI | The scale in this tool combines the two scales so ... |
| Q189 | - |  |  | SI | • Make sure to communicate with the patient all th... |
| Q19 | - |  |  | SI | Left |
| Q190 | - |  |  | SI | • Work with the non-dominant (or non - injured) si... |
| Q191 | - |  |  | SI | • Remind your patient to breathe naturally during ... |
| Q192 | - |  |  | SI | • Make sure the patient is dressed in loose clothi... |
| Q193 | - |  |  | SI | • Place the patient in an adequately supported pos... |
| Q194 | - |  |  | SI | • Always test first in an anti-gravity position. I... |
| Q195 | - |  |  | SI | • Resistance needs to be applied directly opposite... |
| Q196 | - |  |  | SI | • Plan out the test first, testing all the muscles... |
| Q197 | - |  |  | SI | • Always provide adequate stabilisation to unrelat... |
| Q198 | - |  |  | SI | stabilisation of the shoulder will prevent extra m... |
| Q199 | - |  |  | SI | • Always test both sides in order to compare stren... |
| Q20 | - |  |  | SI | Right |
| Q200 | - |  |  | SI | • Avoid doing jerking movements when applying resi... |
| Q201 | - |  |  | SI | • Discontinue testing if patient complains of pain... |
| Q202 | - |  |  | SI | R1 hip flexors (right) |
| Q203 | - |  |  | SI | R1 hip extensors (right) |
| Q204 | - |  |  | SI | R1 hip abductors (right) |
| Q205 | - |  |  | SI | R1 hip adductors (right) |
| Q206 | - |  |  | SI | R1 hip internal rotators (right) |
| Q207 | - |  |  | SI | R1 hip external rotators (right) |
| Q208 | - |  |  | SI | R1 knee flexors (right) |
| Q209 | - |  |  | SI | R1 knee extensors (right) |
| Q21 | - |  |  | SI | R1 |
| Q210 | - |  |  | SI | R1 knee flexors with internal rotators (right) |
| Q211 | - |  |  | SI | R1 knee flexors with external rotators (right) |
| Q212 | - |  |  | SI | R1 ankle plantar flexors (right) |
| Q213 | - |  |  | SI | R1 ankle dorsiflexors - knee at 0° (right) |
| Q214 | - |  |  | SI | R1 ankle dorsiflexors - knee at 90° (right) |
| Q215 | - |  |  | SI | R1 ankle invertors (right) |
| Q216 | - |  |  | SI | R1 ankle evertors (right) |
| Q217 | - |  |  | SI | R2 hip flexors (right) |
| Q218 | - |  |  | SI | R2 hip extensors (right) |
| Q219 | - |  |  | SI | R2 hip abductors (right) |
| Q22 | - |  |  | SI | R1 |
| Q220 | - |  |  | SI | R2 hip adductors (right) |
| Q221 | - |  |  | SI | R2 shoulder hip rotators (right) |
| Q222 | - |  |  | SI | R2 hip external rotators (right) |
| Q223 | - |  |  | SI | R2 knee flexors (right) |
| Q224 | - |  |  | SI | R2 knee extensors (right) |
| Q225 | - |  |  | SI | R2 knee flexors with internal rotators (right) |
| Q226 | - |  |  | SI | R2 knee flexors with external rotators (right) |
| Q227 | - |  |  | SI | R2 ankle plantar flexors (right) |
| Q228 | - |  |  | SI | R2 ankle dorsiflexors - knee at 0° (right) |
| Q229 | - |  |  | SI | R2 ankle dorsiflexors - knee at 90° (right) |
| Q23 | - |  |  | SI | R2 |
| Q230 | - |  |  | SI | R2 ankle invertors (right) |
| Q231 | - |  |  | SI | R2 ankle evertors (right) |
| Q232 | - |  |  | SI | R2 - R1 hip flexors (right) |
| Q233 | - |  |  | SI | R2 - R1 hip extensors (right) |
| Q234 | - |  |  | SI | R2 - R1 hip abductors (right) |
| Q235 | - |  |  | SI | R2 - R1 hip adductors (right) |
| Q236 | - |  |  | SI | R2 - R1 hip internal rotators (right) |
| Q237 | - |  |  | SI | R2 - R1 hip external rotators (right) |
| Q238 | - |  |  | SI | R2 - R1 knee flexors (right) |
| Q239 | - |  |  | SI | R2 - R1 knee extensors (right) |
| Q24 | - |  |  | SI | R2 |
| Q240 | - |  |  | SI | R2 - R1 knee flexors with internal rotators (right... |
| Q241 | - |  |  | SI | R2 - R1 knee flexors with external rotators (right... |
| Q242 | - |  |  | SI | R2 - R1 ankle plantar flexors (right) |
| Q243 | - |  |  | SI | R2 - R1 ankle dorsiflexors - knee at 0° (right) |
| Q244 | - |  |  | SI | R2 - R1  ankle dorsiflexors - knee at 90° (right) |
| Q245 | - |  |  | SI | R2 - R1 ankle invertors (right) |
| Q246 | - |  |  | SI | R2 - R1 ankle evertors (right) |
| Q247 | - |  |  | SI | Hip Flexor Spasticity, MTS (Right) |
| Q247ObsDR | - |  |  | SI | Hip Flexor Spasticity, MTS (Right) DR |
| Q248 | - |  |  | SI | Hip Extensor Spasticity, MTS (Right) |
| Q248ObsDR | - |  |  | SI | Hip Extensor Spasticity, MTS (Right) DR |
| Q249 | - |  |  | SI | Hip Abductor Spasticity, MTS (Right) |
| Q249ObsDR | - |  |  | SI | Hip Abductor Spasticity, MTS (Right) DR |
| Q25 | - |  |  | SI | R2 - R1 |
| Q250 | - |  |  | SI | Hip Adductor Spasticity, MTS (Right) |
| Q250ObsDR | - |  |  | SI | Hip Adductor Spasticity, MTS (Right) DR |
| Q251 | - |  |  | SI | Hip Internal Rotator Spasticity, MTS (Right) |
| Q251ObsDR | - |  |  | SI | Hip Internal Rotator Spasticity, MTS (Right) DR |
| Q252 | - |  |  | SI | Hip External Rotator Spasticity, MTS (Right) |
| Q252ObsDR | - |  |  | SI | Hip External Rotator Spasticity, MTS (Right) DR |
| Q253 | - |  |  | SI | Knee Flexor Spasticity, MTS (Right) |
| Q253ObsDR | - |  |  | SI | Knee Flexor Spasticity, MTS (Right) DR |
| Q254 | - |  |  | SI | Knee Extensor Spasticity, MTS (Right) |
| Q254ObsDR | - |  |  | SI | Knee Extensor Spasticity, MTS (Right) DR |
| Q255 | - |  |  | SI | Knee Internal Rotator Spasticity, MTS (Right) |
| Q255ObsDR | - |  |  | SI | Knee Internal Rotator Spasticity, MTS (Right) DR |
| Q256 | - |  |  | SI | Knee External Rotator Spasticity, MTS (Right) |
| Q256ObsDR | - |  |  | SI | Knee External Rotator Spasticity, MTS (Right) DR |
| Q257 | - |  |  | SI | Ankle Plantar Flexor Spasticity, MTS (Right) |
| Q257ObsDR | - |  |  | SI | Ankle Plantar Flexor Spasticity, MTS (Right) DR |
| Q258 | - |  |  | SI | Ankle Dorsiflexor Spasticity, Knee at 0 degrees, M... |
| Q258ObsDR | - |  |  | SI | Ankle Dorsiflexor Spasticity, Knee at 0 degrees, M... |
| Q259 | - |  |  | SI | Ankle Dorsiflexor Spasticity, Knee at 90 degrees, ... |
| Q259ObsDR | - |  |  | SI | Ankle Dorsiflexor Spasticity, Knee at 90 degrees, ... |
| Q26 | - |  |  | SI | R2 - R1 |
| Q260 | - |  |  | SI | Forefoot Invertor Spasticity, MTS (Right) |
| Q260ObsDR | - |  |  | SI | Forefoot Invertor Spasticity, MTS (Right) DR |
| Q261 | - |  |  | SI | Forefoot Evertor Spasticity, MTS (Right) |
| Q261ObsDR | - |  |  | SI | Forefoot Evertor Spasticity, MTS (Right) DR |
| Q262 | - |  |  | SI | Hip Flexor Muscle Tone, MAS (Right) |
| Q262ObsDR | - |  |  | SI | Hip Flexor Muscle Tone, MAS (Right) DR |
| Q263 | - |  |  | SI | Hip Extensor Muscle Tone, MAS (Right) |
| Q263ObsDR | - |  |  | SI | Hip Extensor Muscle Tone, MAS (Right) DR |
| Q264 | - |  |  | SI | Hip Adductor Muscle Tone, MAS (Right) |
| Q264ObsDR | - |  |  | SI | Hip Adductor Muscle Tone, MAS (Right) DR |
| Q265 | - |  |  | SI | Hip Adductor Muscle Tone, MAS (Right) |
| Q265ObsDR | - |  |  | SI | Hip Adductor Muscle Tone, MAS (Right) DR |
| Q266 | - |  |  | SI | Hip Internal Rotator Muscle Tone, MAS (Right) |
| Q266ObsDR | - |  |  | SI | Hip Internal Rotator Muscle Tone, MAS (Right) DR |
| Q267 | - |  |  | SI | Hip External Rotator Muscle Tone, MAS (Right) |
| Q267ObsDR | - |  |  | SI | Hip External Rotator Muscle Tone, MAS (Right) DR |
| Q268 | - |  |  | SI | Knee Flexor Muscle Tone, MAS (Right) |
| Q268ObsDR | - |  |  | SI | Knee Flexor Muscle Tone, MAS (Right) DR |
| Q269 | - |  |  | SI | Knee Extensor Muscle Tone, MAS (Right) |
| Q269ObsDR | - |  |  | SI | Knee Extensor Muscle Tone, MAS (Right) DR |
| Q27 | - |  |  | SI | X (MTS) |
| Q270 | - |  |  | SI | TC.MASKLRR |
| Q270ObsDR | - |  |  | SI | TC.MASKLRR DR |
| Q271 | - |  |  | SI | TC.MASKMRR |
| Q271ObsDR | - |  |  | SI | TC.MASKMRR DR |
| Q272 | - |  |  | SI | Ankle Plantarflexor Muscle Tone, MAS (Right) |
| Q272ObsDR | - |  |  | SI | Ankle Plantarflexor Muscle Tone, MAS (Right) DR |
| Q273 | - |  |  | SI | Ankle Dorsiflexor Muscle Tone - Knee at Zero degre... |
| Q273ObsDR | - |  |  | SI | Ankle Dorsiflexor Muscle Tone - Knee at Zero degre... |
| Q274 | - |  |  | SI | Ankle Dorsiflexor Muscle Tone - Knee at 90 degrees... |
| Q274ObsDR | - |  |  | SI | Ankle Dorsiflexor Muscle Tone - Knee at 90 degrees... |
| Q275 | - |  |  | SI | Forefoot Invertor Muscle Tone, MAS (Right) |
| Q275ObsDR | - |  |  | SI | Forefoot Invertor Muscle Tone, MAS (Right) DR |
| Q276 | - |  |  | SI | Forefoot Evertor Muscle Tone, MAS (Right) |
| Q276ObsDR | - |  |  | SI | Forefoot Evertor Muscle Tone, MAS (Right) DR |
| Q277 | - |  |  | SI | Hip Flexor Strength, MRC Scale (Right) |
| Q277ObsDR | - |  |  | SI | Hip Flexor Strength, MRC Scale (Right) DR |
| Q278 | - |  |  | SI | Hip Flexor Strength, KTMG Scale (Right) |
| Q278ObsDR | - |  |  | SI | Hip Flexor Strength, KTMG Scale (Right) DR |
| Q279 | - |  |  | SI | Hip Extensor Strength, MRC Scale (Right) |
| Q279ObsDR | - |  |  | SI | Hip Extensor Strength, MRC Scale (Right) DR |
| Q28 | - |  |  | SI | X (MTS) |
| Q280 | - |  |  | SI | Hip Extensor Strength, KTMG Scale (Right) |
| Q280ObsDR | - |  |  | SI | Hip Extensor Strength, KTMG Scale (Right) DR |
| Q281 | - |  |  | SI | Hip Abductor Strength, MRC Scale (Right) |
| Q281ObsDR | - |  |  | SI | Hip Abductor Strength, MRC Scale (Right) DR |
| Q282 | - |  |  | SI | Hip Abductor Strength, KTMG Scale (Right) |
| Q282ObsDR | - |  |  | SI | Hip Abductor Strength, KTMG Scale (Right) DR |
| Q283 | - |  |  | SI | Hip Adductor Strength, MRC Scale (Right) |
| Q283ObsDR | - |  |  | SI | Hip Adductor Strength, MRC Scale (Right) DR |
| Q284 | - |  |  | SI | Hip Adductor Strength, KTMG Scale (Right) |
| Q284ObsDR | - |  |  | SI | Hip Adductor Strength, KTMG Scale (Right) DR |
| Q285 | - |  |  | SI | Hip Internal Rotator Strength, MRC Scale (Right) |
| Q285ObsDR | - |  |  | SI | Hip Internal Rotator Strength, MRC Scale (Right) D... |
| Q286 | - |  |  | SI | Hip Internal Rotator Strength, KTMG Scale (Right) |
| Q286ObsDR | - |  |  | SI | Hip Internal Rotator Strength, KTMG Scale (Right) ... |
| Q287 | - |  |  | SI | Hip External Rotator Strength, MRC Scale (Right) |
| Q287ObsDR | - |  |  | SI | Hip External Rotator Strength, MRC Scale (Right) D... |
| Q288 | - |  |  | SI | Hip External Rotator Strength, KTMG Scale (Right) |
| Q288ObsDR | - |  |  | SI | Hip External Rotator Strength, KTMG Scale (Right) ... |
| Q289 | - |  |  | SI | Knee Flexor Strength, MRC Scale (Right) |
| Q289ObsDR | - |  |  | SI | Knee Flexor Strength, MRC Scale (Right) DR |
| Q29 | - |  |  | SI | MAS |
| Q290 | - |  |  | SI | Knee Flexor Strength, KTMG Scale (Right) |
| Q290ObsDR | - |  |  | SI | Knee Flexor Strength, KTMG Scale (Right) DR |
| Q291 | - |  |  | SI | Knee Extensor Strength, MRC Scale (Right) |
| Q291ObsDR | - |  |  | SI | Knee Extensor Strength, MRC Scale (Right) DR |
| Q292 | - |  |  | SI | Knee Extensor Strength, KTMG Scale (Right) |
| Q292ObsDR | - |  |  | SI | Knee Extensor Strength, KTMG Scale (Right) DR |
| Q293 | - |  |  | SI | Knee Internal Rotator Strength, MRC Scale (Right) |
| Q293ObsDR | - |  |  | SI | Knee Internal Rotator Strength, MRC Scale (Right) ... |
| Q294 | - |  |  | SI | Knee (Internally Rotated) Extensor Strength, KTMG ... |
| Q294ObsDR | - |  |  | SI | Knee (Internally Rotated) Extensor Strength, KTMG ... |
| Q295 | - |  |  | SI | Knee External Rotator Strength, MRC Scale (Right) |
| Q295ObsDR | - |  |  | SI | Knee External Rotator Strength, MRC Scale (Right) ... |
| Q296 | - |  |  | SI | Knee (Externally Rotated) Extensor Strength, KTMG ... |
| Q296ObsDR | - |  |  | SI | Knee (Externally Rotated) Extensor Strength, KTMG ... |
| Q297 | - |  |  | SI | Ankle Plantar Flexor Strength, MRC Scale (Right) |
| Q297ObsDR | - |  |  | SI | Ankle Plantar Flexor Strength, MRC Scale (Right) D... |
| Q298 | - |  |  | SI | Ankle Plantar Flexor Strength, KTMG Scale (Right) |
| Q298ObsDR | - |  |  | SI | Ankle Plantar Flexor Strength, KTMG Scale (Right) ... |
| Q299 | - |  |  | SI | Ankle Dorsiflexor Strength, Knee at 0°, MRC Scale ... |
| Q299ObsDR | - |  |  | SI | Ankle Dorsiflexor Strength, Knee at 0°, MRC Scale ... |
| Q30 | - |  |  | SI | MAS |
| Q300 | - |  |  | SI | Ankle Dorsiflexor Strength, Knee at 0 degrees, KTM... |
| Q300ObsDR | - |  |  | SI | Ankle Dorsiflexor Strength, Knee at 0 degrees, KTM... |
| Q301 | - |  |  | SI | Ankle Dorsiflexor Strength, Knee at 90°, MRC Scale... |
| Q301ObsDR | - |  |  | SI | Ankle Dorsiflexor Strength, Knee at 90°, MRC Scale... |
| Q302 | - |  |  | SI | Ankle Dorsiflexor Strength, Knee at 90 degrees, KT... |
| Q302ObsDR | - |  |  | SI | Ankle Dorsiflexor Strength, Knee at 90 degrees, KT... |
| Q303 | - |  |  | SI | Forefoot Invertor Strength, MRC Scale (Right) |
| Q303ObsDR | - |  |  | SI | Forefoot Invertor Strength, MRC Scale (Right) DR |
| Q304 | - |  |  | SI | Forefoot Invertor Strength, KTMG Scale (Right) |
| Q304ObsDR | - |  |  | SI | Forefoot Invertor Strength, KTMG Scale (Right) DR |
| Q305 | - |  |  | SI | Forefoot Evertors, MRC Scale (Right) |
| Q305ObsDR | - |  |  | SI | Forefoot Evertors, MRC Scale (Right) DR |
| Q306 | - |  |  | SI | Forefoot Evertor Strength, KTMG Scale (Right) |
| Q306ObsDR | - |  |  | SI | Forefoot Evertor Strength, KTMG Scale (Right) DR |
| Q307 | - |  |  | SI | R1: |
| Q308 | - |  |  | SI | Angle of catch seen at velocity V2 or V3 |
| Q309 | - |  |  | SI | R2: |
| Q31 | - |  |  | SI | MMT MRC / KTMG |
| Q310 | - |  |  | SI | Full range of motion achieved when muscle is at re... |
| Q311 | - |  |  | SI | R2 - R1: |
| Q312 | - |  |  | SI | Indicates the level of dynamic contracture in the ... |
| Q313 | - |  |  | SI | X (MTS): |
| Q314 | - |  |  | SI | Modified Tardieu Scale (MTS) Quality of Muscle Rea... |
| Q315 | - |  |  | SI | MAS: |
| Q316 | - |  |  | SI | Modified Ashworth Scale |
| Q317 | - |  |  | SI | MTS: |
| Q318 | - |  |  | SI | Manual Muscle Test |
| Q319 | - |  |  | SI | R1: Angle of catch seen at velocity V2 or V3 |
| Q32 | - |  |  | SI | MMT MRC / KTMG |
| Q320 | - |  |  | SI | R2: Full range of motion achieved when muscle is a... |
| Q321 | - |  |  | SI | R2 - R1: Indicates the level of dynamic contractur... |
| Q322 | - |  |  | SI | X (MTS): Modified Tardieu Scale (MTS) Quality of M... |
| Q323 | - |  |  | SI | MAS: Modified Ashworth Scale |
| Q324 | - |  |  | SI | MTS: Manual Muscle Test |
| Q325 | - |  |  | SI | Score |
| Q326 | - |  |  | SI | Classification |
| Q327 | - |  |  | SI | Medical Research Council (MRC) Scale for Muscle St... |
| Q328 | - |  |  | SI | Description |
| Q329 | - |  |  | SI | 5 |
| Q33 | - |  |  | SI | R1 hip flexors (left) |
| Q330 | - |  |  | SI | Normal power |
| Q331 | - |  |  | SI | 4 |
| Q332 | - |  |  | SI | Active movement against gravity and resistance |
| Q333 | - |  |  | SI | 3 |
| Q334 | - |  |  | SI | Active movement against gravity |
| Q335 | - |  |  | SI | 2 |
| Q336 | - |  |  | SI | Active movement, with gravity eliminated |
| Q337 | - |  |  | SI | 1 |
| Q338 | - |  |  | SI | Flicker or trace of contraction |
| Q339 | - |  |  | SI | 0 |
| Q34 | - |  |  | SI | R1 hip extensors (left) |
| Q340 | - |  |  | SI | No contraction |
| Q341 | - |  |  | SI | Scale reference - Medical Research Centre (MRC) Mu... |
| Q342 | - |  |  | SI | Medical Research Council. Aids to the Investigatio... |
| Q343 | - |  |  | SI | https://mrc.ukri.org/documents/pdf/aids-to-the-exa... |
| Q344 | - |  |  | SI | Key to Muscle Grading (KTMG) |
| Q345 | - |  |  | SI | Explanation / Description |
| Q346 | - |  |  | SI | 0: Zero |
| Q347 | - |  |  | SI | No contraction felt or seen in the muscle |
| Q348 | - |  |  | SI | 1: Trace (T) |
| Q349 | - |  |  | SI | Tendon becomes prominent or feeble contraction fel... |
| Q35 | - |  |  | SI | R1 hip abductors (left) |
| Q350 | - |  |  | SI | 2+: Poor + (P+) |
| Q351 | - |  |  | SI | Moves through partial ROM against gravity (support... |
| Q352 | - |  |  | SI | 2+: Poor + (P+) |
| Q353 | - |  |  | SI | Holds against slight pressure in test position (su... |
| Q354 | - |  |  | SI | 2-: Poor - (P-) |
| Q355 | - |  |  | SI | Moves through partial ROM (supported in horizontal... |
| Q356 | - |  |  | SI | 2: Poor (P) |
| Q357 | - |  |  | SI | Movement through complete ROM for the muscle being... |
| Q358 | - |  |  | SI | 3+: Fair + (F+) |
| Q359 | - |  |  | SI | Holds test position in anti-gravity position again... |
| Q36 | - |  |  | SI | R1 hip adductors (left) |
| Q360 | - |  |  | SI | 3-: Fair - (F-) |
| Q361 | - |  |  | SI | Gradual release from test position occurs in anti-... |
| Q362 | - |  |  | SI | 3: Fair (F) |
| Q363 | - |  |  | SI | Holds test position in anti-gravity position (no a... |
| Q364 | - |  |  | SI | 4+: Good + (G+) |
| Q365 | - |  |  | SI | Holds test position in anti-gravity position again... |
| Q366 | - |  |  | SI | 4-: Good - (G-) |
| Q367 | - |  |  | SI | Holds test position in anti-gravity position again... |
| Q368 | - |  |  | SI | 4: Good (G) |
| Q369 | - |  |  | SI | Holds test position in anti-gravity position again... |
| Q37 | - |  |  | SI | R1 hip internal rotators (left) |
| Q370 | - |  |  | SI | 5: Normal (N) |
| Q371 | - |  |  | SI | Holds test position in anti-gravity position again... |
| Q372 | - |  |  | SI | Scale reference - Key to Muscle Grading |
| Q373 | - |  |  | SI | Kendall, F. P., McCreary, E. K., Provance, P. G., ... |
| Q374 | - |  |  | SI | Scale reference: |
| Q375 | - |  |  | SI | Boyd R, Graham K. Objective measurement of clinica... |
| Q376 | - |  |  | SI | Joint |
| Q377 | - |  |  | SI | Muscle Group |
| Q378 | - |  |  | SI | Hip Abductor Spasticity, MTS (Left) |
| Q378ObsDR | - |  |  | SI | Hip Abductor Spasticity, MTS (Left) DR |
| Q379 | - |  |  | SI | Knee External Rotator Strength, MRC Scale (Left) |
| Q379ObsDR | - |  |  | SI | Knee External Rotator Strength, MRC Scale (Left) D... |
| Q38 | - |  |  | SI | R1 hip external rotators (left) |
| Q39 | - |  |  | SI | R1 knee flexors (left) |
| Q40 | - |  |  | SI | R1 knee extensors (left) |
| Q41 | - |  |  | SI | R1 knee flexors with internal rotators (left) |
| Q42 | - |  |  | SI | R1 knee flexors with external rotators (left) |
| Q43 | - |  |  | SI | R1 ankle plantar flexors (left) |
| Q44 | - |  |  | SI | R1 ankle dorsiflexors - knee at 0° (left) |
| Q45 | - |  |  | SI | R1 ankle dorsiflexors - knee at 90° (left) |
| Q46 | - |  |  | SI | R1 ankle invertors (left) |
| Q47 | - |  |  | SI | R1 ankle evertors (left) |
| Q48 | - |  |  | SI | R2 hip flexors (left) |
| Q49 | - |  |  | SI | R2 hip extensors (left) |
| Q50 | - |  |  | SI | R2 hip abductors (left) |
| Q51 | - |  |  | SI | R2 hip adductors (left) |
| Q52 | - |  |  | SI | R2 shoulder hip rotators (left) |
| Q53 | - |  |  | SI | R2 hip external rotators (left) |
| Q54 | - |  |  | SI | R2 knee flexors (left) |
| Q55 | - |  |  | SI | R2 knee extensors (left) |
| Q56 | - |  |  | SI | R2 knee flexors with internal rotators (left) |
| Q57 | - |  |  | SI | R2 knee flexors with external rotators (left) |
| Q58 | - |  |  | SI | R2 ankle plantar flexors (left) |
| Q59 | - |  |  | SI | R2 ankle dorsiflexors - knee at 0° (left) |
| Q60 | - |  |  | SI | R2 ankle dorsiflexors - knee at 90° (left) |
| Q61 | - |  |  | SI | R2 ankle invertors (left) |
| Q62 | - |  |  | SI | R2 ankle evertors (left) |
| Q63 | - |  |  | SI | R2 - R1 hip flexors (left) |
| Q64 | - |  |  | SI | R2 - R1 hip extensors (left) |
| Q65 | - |  |  | SI | R2 - R1 hip abductors (left) |
| Q66 | - |  |  | SI | R2 - R1 hip adductors (left) |
| Q67 | - |  |  | SI | R2 - R1 hip internal rotators (left) |
| Q68 | - |  |  | SI | R2 - R1 hip external rotators (left) |
| Q69 | - |  |  | SI | R2 - R1 knee flexors (left) |
| Q70 | - |  |  | SI | R2 - R1 knee extensors (left) |
| Q71 | - |  |  | SI | R2 - R1 knee flexors with internal rotators (left) |
| Q72 | - |  |  | SI | R2 - R1 knee flexors with external rotators (left) |
| Q73 | - |  |  | SI | R2 - R1 ankle plantar flexors (left) |
| Q74 | - |  |  | SI | R2 - R1 ankle dorsiflexors - knee at 0° (left) |
| Q75 | - |  |  | SI | R2 - R1 ankle dorsiflexors - knee at 90° (left) |
| Q76 | - |  |  | SI | R2 - R1 ankle invertors (left) |
| Q77 | - |  |  | SI | R2 - R1 ankle evertors (left) |
| Q78 | - |  |  | SI | Hip Flexor Spasticity, MTS (Left) |
| Q78ObsDR | - |  |  | SI | Hip Flexor Spasticity, MTS (Left) DR |
| Q79 | - |  |  | SI | Hip Extensor Spasticity, MTS (Left) |
| Q79ObsDR | - |  |  | SI | Hip Extensor Spasticity, MTS (Left) DR |
| Q80 | - |  |  | SI | Hip Abductor Spasticity, MTS (Left) |
| Q80ObsDR | - |  |  | SI | Hip Abductor Spasticity, MTS (Left) DR |
| Q81 | - |  |  | SI | Hip Internal Rotator Spasticity, MTS (Left) |
| Q81ObsDR | - |  |  | SI | Hip Internal Rotator Spasticity, MTS (Left) DR |
| Q82 | - |  |  | SI | Hip External Rotator Spasticity, MTS (Left) |
| Q82ObsDR | - |  |  | SI | Hip External Rotator Spasticity, MTS (Left) DR |
| Q83 | - |  |  | SI | Knee Flexor Spasticity, MTS (Left) |
| Q83ObsDR | - |  |  | SI | Knee Flexor Spasticity, MTS (Left) DR |
| Q84 | - |  |  | SI | Knee Extensor Spasticity, MTS (Left) |
| Q84ObsDR | - |  |  | SI | Knee Extensor Spasticity, MTS (Left) DR |
| Q85 | - |  |  | SI | Knee Internal Rotator Spasticity, MTS (Left) |
| Q85ObsDR | - |  |  | SI | Knee Internal Rotator Spasticity, MTS (Left) DR |
| Q86 | - |  |  | SI | Knee External Rotator Spasticity, MTS (Left) |
| Q86ObsDR | - |  |  | SI | Knee External Rotator Spasticity, MTS (Left) DR |
| Q87 | - |  |  | SI | Ankle Plantar Flexor Spasticity, MTS (Left) |
| Q87ObsDR | - |  |  | SI | Ankle Plantar Flexor Spasticity, MTS (Left) DR |
| Q88 | - |  |  | SI | Ankle Dorsiflexor Spasticity, Knee at 0 degrees, M... |
| Q88ObsDR | - |  |  | SI | Ankle Dorsiflexor Spasticity, Knee at 0 degrees, M... |
| Q89 | - |  |  | SI | Ankle Dorsiflexor Spasticity, Knee at 90 degrees, ... |
| Q89ObsDR | - |  |  | SI | Ankle Dorsiflexor Spasticity, Knee at 90 degrees, ... |
| Q90 | - |  |  | SI | Forefoot Invertor Spasticity, MTS (Left) |
| Q90ObsDR | - |  |  | SI | Forefoot Invertor Spasticity, MTS (Left) DR |
| Q91 | - |  |  | SI | Forefoot Evertor Spasticity, MTS (Left) |
| Q91ObsDR | - |  |  | SI | Forefoot Evertor Spasticity, MTS (Left) DR |
| Q92 | - |  |  | SI | Hip Flexor Muscle Tone, MAS (Left) |
| Q92ObsDR | - |  |  | SI | Hip Flexor Muscle Tone, MAS (Left) DR |
| Q93 | - |  |  | SI | Hip Extensor Muscle Tone, MAS (Left) |
| Q93ObsDR | - |  |  | SI | Hip Extensor Muscle Tone, MAS (Left) DR |
| Q94 | - |  |  | SI | Hip Adductor Muscle Tone, MAS (Left) |
| Q94ObsDR | - |  |  | SI | Hip Adductor Muscle Tone, MAS (Left) DR |
| Q95 | - |  |  | SI | Hip Adductor Muscle Tone, MAS (Left) |
| Q95ObsDR | - |  |  | SI | Hip Adductor Muscle Tone, MAS (Left) DR |
| Q96 | - |  |  | SI | Hip Internal Rotator Muscle Tone, MAS (Left) |
| Q96ObsDR | - |  |  | SI | Hip Internal Rotator Muscle Tone, MAS (Left) DR |
| Q97 | - |  |  | SI | Hip External Rotator Muscle Tone, MAS (Left) |
| Q97ObsDR | - |  |  | SI | Hip External Rotator Muscle Tone, MAS (Left) DR |
| Q98 | - |  |  | SI | Knee Flexor Muscle Tone, MAS (Left) |
| Q98ObsDR | - |  |  | SI | Knee Flexor Muscle Tone, MAS (Left) DR |
| Q99 | - |  |  | SI | Knee Extensor Muscle Tone, MAS (Left) |
| Q99ObsDR | - |  |  | SI | Knee Extensor Muscle Tone, MAS (Left) DR |
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