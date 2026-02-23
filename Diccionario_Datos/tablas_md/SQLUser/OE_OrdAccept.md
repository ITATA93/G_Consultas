# SQLUser.OE_OrdAccept

**Schema:** SQLUser
**Columnas:** 638
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Órdenes Médicas**. Solicitudes de exámenes, procedimientos, etc.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ACC_ParRef | numeric | PK |  | NO | OE_Order Parent Reference |
| ACC_Childsub | double |  |  | NO | Childsub |
| ACC_Date | date |  |  | SI | Date Accepted |
| ACC_DoctorTime | time |  |  | SI | Time Doctor accepted |
| ACC_PharmTime | time |  |  | SI | Time Pharmacist accepted |
| ACC_RowId | varchar |  |  | NO | - |
| ACC_UserDoctor_DR | bigint |  | FK | SI | Des Ref User |
| ACC_UserPharmacist_DR | bigint |  | FK | SI | Des Ref User |
| Q01 | - |  |  | SI | Dominance |
| Q02 | - |  |  | SI | Affected Upper Limb |
| Q03 | - |  |  | SI | Previous Upper Limb Injuries / Problems |
| Q04 | - |  |  | SI | Test Position |
| Q05 | - |  |  | SI | Joint |
| Q06 | - |  |  | SI | Left |
| Q07 | - |  |  | SI | Right |
| Q08 | - |  |  | SI | SCAPULA |
| Q09 | - |  |  | SI | Scapula Position (Left) |
| Q10 | - |  |  | SI | Scapula Position (Right) |
| Q100 | - |  |  | SI | Radial Deviation (0°- 20°) - Radial flexor strengt... |
| Q101 | - |  |  | SI | Radial Deviation (0°- 20°) PROM (Left) |
| Q102 | - |  |  | SI | Radial Deviation (0°- 20°) AROM (Left) |
| Q103 | - |  |  | SI | Radial Deviation (0°- 20°) POWER (Left) |
| Q103ObsDR | - |  |  | SI | Radial Deviation (0°- 20°) POWER (Left) DR |
| Q104 | - |  |  | SI | Radial Deviation (0°- 20°) PROM (Right) |
| Q105 | - |  |  | SI | Radial Deviation (0°- 20°) AROM (Right) |
| Q106 | - |  |  | SI | Radial Deviation (0°- 20°) POWER (Right) |
| Q106ObsDR | - |  |  | SI | Radial Deviation (0°- 20°) POWER (Right) DR |
| Q107 | - |  |  | SI | Ulnar Deviation (0°- 30°) - Ulnar flexor strength |
| Q108 | - |  |  | SI | Ulnar Deviation (0°- 30°) PROM (Left) |
| Q109 | - |  |  | SI | Ulnar Deviation (0°- 30°) AROM (Left) |
| Q11 | - |  |  | SI | Scapula Movement (Left) |
| Q110 | - |  |  | SI | Ulnar Deviation (0°- 30°) POWER (Left) |
| Q110ObsDR | - |  |  | SI | Ulnar Deviation (0°- 30°) POWER (Left) DR |
| Q111 | - |  |  | SI | Ulnar Deviation (0°- 30°) PROM (Right) |
| Q112 | - |  |  | SI | Ulnar Deviation (0°- 30°) AROM (Right) |
| Q113 | - |  |  | SI | Ulnar Deviation (0°- 30°) POWER (Right) |
| Q113ObsDR | - |  |  | SI | Ulnar Deviation (0°- 30°) POWER (Right) DR |
| Q114 | - |  |  | SI | Thumb |
| Q115 | - |  |  | SI | CM Flexion (0°- 15°) |
| Q116 | - |  |  | SI | CM Flexion (0°- 15°) PROM (Left) |
| Q117 | - |  |  | SI | CM Flexion (0°- 15°) AROM (Left) |
| Q118 | - |  |  | SI | CM Flexion (0°- 15°) POWER (Left) |
| Q118ObsDR | - |  |  | SI | CM Flexion (0°- 15°) POWER (Left) DR |
| Q119 | - |  |  | SI | CM Flexion (0°- 15°) PROM (Right) |
| Q12 | - |  |  | SI | Scapula Movement (Right) |
| Q120 | - |  |  | SI | CM Flexion (0°- 15°) AROM (Right) |
| Q121 | - |  |  | SI | CM Flexion (0°- 15°) POWER (Right) |
| Q121ObsDR | - |  |  | SI | CM Flexion (0°- 15°) POWER (Right) DR |
| Q122 | - |  |  | SI | CM Extension (0°- 20°) |
| Q123 | - |  |  | SI | CM Extension (0°- 20°) PROM (Left) |
| Q124 | - |  |  | SI | CM Extension (0°- 20°) AROM (Left) |
| Q125 | - |  |  | SI | CM Extension (0°- 20°) POWER (Left) |
| Q125ObsDR | - |  |  | SI | CM Extension (0°- 20°) POWER (Left) DR |
| Q126 | - |  |  | SI | CM Extension (0°- 20°) PROM (Right) |
| Q127 | - |  |  | SI | CM Extension (0°- 20°) AROM (Right) |
| Q128 | - |  |  | SI | CM Extension (0°- 20°) POWER (Right) |
| Q128ObsDR | - |  |  | SI | CM Extension (0°- 20°) POWER (Right) DR |
| Q129 | - |  |  | SI | MP Flexion – Extension (0°- 50°) |
| Q13 | - |  |  | SI | Shoulder |
| Q130 | - |  |  | SI | MP Flexion – Extension (0°- 50°) PROM (Left) |
| Q131 | - |  |  | SI | MP Flexion – Extension (0°- 50°) AROM (Left) |
| Q132 | - |  |  | SI | MP Flexion – Extension (0°- 50°) POWER (Left) |
| Q132ObsDR | - |  |  | SI | MP Flexion – Extension (0°- 50°) POWER (Left) DR |
| Q133 | - |  |  | SI | MP Flexion – Extension (0°- 50°) PROM (Right) |
| Q134 | - |  |  | SI | MP Flexion – Extension (0°- 50°) AROM (Right) |
| Q135 | - |  |  | SI | MP Flexion – Extension (0°- 50°) POWER (Right) |
| Q135ObsDR | - |  |  | SI | MP Flexion – Extension (0°- 50°) POWER (Right) DR |
| Q136 | - |  |  | SI | IP Flexion – Extension (0°- 80°) |
| Q137 | - |  |  | SI | IP Flexion – Extension (0°- 80°) PROM (Left) |
| Q138 | - |  |  | SI | IP Flexion – Extension (0°- 80°) AROM (Left) |
| Q139 | - |  |  | SI | IP Flexion – Extension (0°- 80°) POWER (Left) |
| Q139ObsDR | - |  |  | SI | IP Flexion – Extension (0°- 80°) POWER (Left) DR |
| Q14 | - |  |  | SI | Passive Range of Movement (degrees) |
| Q140 | - |  |  | SI | IP Flexion – Extension (0°- 80°) PROM (Right) |
| Q141 | - |  |  | SI | IP Flexion – Extension (0°- 80°) AROM (Right) |
| Q142 | - |  |  | SI | IP Flexion – Extension (0°- 80°) POWER (Right) |
| Q142ObsDR | - |  |  | SI | IP Flexion – Extension (0°- 80°) POWER (Right) DR |
| Q143 | - |  |  | SI | Abduction cm (0°- 70°) |
| Q144 | - |  |  | SI | Abduction cm (0°- 70°) PROM (Left) |
| Q145 | - |  |  | SI | Abduction cm (0°- 70°) AROM (Left) |
| Q146 | - |  |  | SI | Abduction cm (0°- 70°) POWER (Left) |
| Q146ObsDR | - |  |  | SI | Abduction cm (0°- 70°) POWER (Left) DR |
| Q147 | - |  |  | SI | Abduction cm (0°- 70°) PROM (Right) |
| Q148 | - |  |  | SI | Abduction cm (0°- 70°) AROM (Right) |
| Q149 | - |  |  | SI | Abduction cm (0°- 70°) POWER (Right) |
| Q149ObsDR | - |  |  | SI | Abduction cm (0°- 70°) POWER (Right) DR |
| Q15 | - |  |  | SI | Active Range of Movement (degrees) |
| Q150 | - |  |  | SI | Opposition cm |
| Q151 | - |  |  | SI | Opposition cm PROM (Left) |
| Q152 | - |  |  | SI | Opposition cm AROM (Left) |
| Q153 | - |  |  | SI | Opposition cm POWER (Left) |
| Q153ObsDR | - |  |  | SI | Opposition cm POWER (Left) DR |
| Q154 | - |  |  | SI | Opposition cm PROM (Right) |
| Q155 | - |  |  | SI | Opposition cm AROM (Right) |
| Q156 | - |  |  | SI | Opposition cm POWER (Right) |
| Q156ObsDR | - |  |  | SI | Opposition cm POWER (Right) DR |
| Q157 | - |  |  | SI | Fingers (Measurement tip to palmar crease) |
| Q158 | - |  |  | SI | IF (2) |
| Q159 | - |  |  | SI | IF (2) PROM (Left) |
| Q16 | - |  |  | SI | Power |
| Q160 | - |  |  | SI | IF (2) AROM (Left) |
| Q161 | - |  |  | SI | IF (2) POWER (Left) |
| Q161ObsDR | - |  |  | SI | IF (2) POWER (Left) DR |
| Q162 | - |  |  | SI | IF (2) PROM (Right) |
| Q163 | - |  |  | SI | IF (2) AROM (Right) |
| Q164 | - |  |  | SI | IF (2) POWER (Right) |
| Q164ObsDR | - |  |  | SI | IF (2) POWER (Right) DR |
| Q165 | - |  |  | SI | MF (3) |
| Q166 | - |  |  | SI | MF (3) PROM (Left) |
| Q167 | - |  |  | SI | MF (3) AROM (Left) |
| Q168 | - |  |  | SI | MF (3) POWER (Left) |
| Q168ObsDR | - |  |  | SI | MF (3) POWER (Left) DR |
| Q169 | - |  |  | SI | MF (3) PROM (Right) |
| Q17 | - |  |  | SI | PROM |
| Q170 | - |  |  | SI | MF (3) AROM (Right) |
| Q171 | - |  |  | SI | MF (3) POWER (Right) |
| Q171ObsDR | - |  |  | SI | MF (3) POWER (Right) DR |
| Q172 | - |  |  | SI | RF (4) |
| Q173 | - |  |  | SI | RF (4) PROM (Left) |
| Q174 | - |  |  | SI | RF (4) AROM (Left) |
| Q175 | - |  |  | SI | RF (4) POWER (Left) |
| Q175ObsDR | - |  |  | SI | RF (4) POWER (Left) DR |
| Q176 | - |  |  | SI | RF (4) PROM (Right) |
| Q177 | - |  |  | SI | RF (4) AROM (Right) |
| Q178 | - |  |  | SI | RF (4) POWER (Right) |
| Q178ObsDR | - |  |  | SI | RF (4) POWER (Right) DR |
| Q179 | - |  |  | SI | LF (5) |
| Q18 | - |  |  | SI | AROM |
| Q180 | - |  |  | SI | LF (5) PROM (Left) |
| Q181 | - |  |  | SI | LF (5) AROM (Left) |
| Q182 | - |  |  | SI | LF (5) POWER (Left) |
| Q182ObsDR | - |  |  | SI | LF (5) POWER (Left) DR |
| Q183 | - |  |  | SI | LF (5) PROM (Right) |
| Q184 | - |  |  | SI | LF (5) AROM (Right) |
| Q185 | - |  |  | SI | LF (5) POWER (Right) |
| Q185ObsDR | - |  |  | SI | LF (5) POWER (Right) DR |
| Q186 | - |  |  | SI | General Comments |
| Q187 | - |  |  | SI | Occupational Therapist Name |
| Q188 | - |  |  | SI | Signature |
| Q188UDt | - |  |  | SI | Signature Last Updated Date |
| Q188UTm | - |  |  | SI | Signature Last Updated Time |
| Q189 | - |  |  | SI | Date |
| Q19 | - |  |  | SI | POWER |
| Q190 | - |  |  | SI | Position |
| Q191 | - |  |  | SI | Movement |
| Q192 | - |  |  | SI | LEFT |
| Q193 | - |  |  | SI | RIGHT |
| Q194 | - |  |  | SI | Left |
| Q195 | - |  |  | SI | Right |
| Q196 | - |  |  | SI | Left |
| Q197 | - |  |  | SI | Left |
| Q198 | - |  |  | SI | Left |
| Q199 | - |  |  | SI | Left |
| Q20 | - |  |  | SI | Flexion (0°- 180°) |
| Q200 | - |  |  | SI | Left |
| Q201 | - |  |  | SI | Left |
| Q202 | - |  |  | SI | Left |
| Q203 | - |  |  | SI | Left |
| Q204 | - |  |  | SI | Left |
| Q205 | - |  |  | SI | Left |
| Q206 | - |  |  | SI | Left |
| Q207 | - |  |  | SI | Left |
| Q208 | - |  |  | SI | Left |
| Q209 | - |  |  | SI | Left |
| Q21 | - |  |  | SI | Flexion (0°- 180°) PROM (Left) |
| Q210 | - |  |  | SI | Left |
| Q211 | - |  |  | SI | Left |
| Q212 | - |  |  | SI | Left |
| Q213 | - |  |  | SI | Left |
| Q214 | - |  |  | SI | Left |
| Q215 | - |  |  | SI | Left |
| Q216 | - |  |  | SI | Left |
| Q217 | - |  |  | SI | Left |
| Q218 | - |  |  | SI | Right |
| Q219 | - |  |  | SI | Right |
| Q22 | - |  |  | SI | Flexion (0°- 180°) AROM (Left) |
| Q220 | - |  |  | SI | Right |
| Q221 | - |  |  | SI | Right |
| Q222 | - |  |  | SI | Right |
| Q223 | - |  |  | SI | Right |
| Q224 | - |  |  | SI | Right |
| Q225 | - |  |  | SI | Right |
| Q226 | - |  |  | SI | Right |
| Q227 | - |  |  | SI | Right |
| Q228 | - |  |  | SI | Right |
| Q229 | - |  |  | SI | Right |
| Q23 | - |  |  | SI | Flexion (0°- 180°) POWER (Left) |
| Q230 | - |  |  | SI | Right |
| Q231 | - |  |  | SI | Right |
| Q232 | - |  |  | SI | Right |
| Q233 | - |  |  | SI | Right |
| Q234 | - |  |  | SI | Right |
| Q235 | - |  |  | SI | Right |
| Q236 | - |  |  | SI | Right |
| Q237 | - |  |  | SI | Right |
| Q238 | - |  |  | SI | Right |
| Q239 | - |  |  | SI | Right |
| Q23ObsDR | - |  |  | SI | Flexion (0°- 180°) POWER (Left) DR |
| Q24 | - |  |  | SI | Flexion (0°- 180°) PROM (Right) |
| Q240 | - |  |  | SI | Right |
| Q241 | - |  |  | SI | Date |
| Q242 | - |  |  | SI | Time |
| Q243 | - |  |  | SI | Shoulder Flexion, Passive (Left) |
| Q243ObsDR | - |  |  | SI | Shoulder Flexion, Passive (Left) DR |
| Q244 | - |  |  | SI | Shoulder Flexion, Active (Left) |
| Q244ObsDR | - |  |  | SI | Shoulder Flexion, Active (Left) DR |
| Q245 | - |  |  | SI | Shoulder Flexor Strength, KTMG Scale (Left) |
| Q245ObsDR | - |  |  | SI | Shoulder Flexor Strength, KTMG Scale (Left) DR |
| Q246 | - |  |  | SI | Shoulder Flexion, Passive (Right) |
| Q246ObsDR | - |  |  | SI | Shoulder Flexion, Passive (Right) DR |
| Q247 | - |  |  | SI | Shoulder Flexion, Active (Right) |
| Q247ObsDR | - |  |  | SI | Shoulder Flexion, Active (Right) DR |
| Q248 | - |  |  | SI | Shoulder Flexor Strength, KTMG Scale (Right) |
| Q248ObsDR | - |  |  | SI | Shoulder Flexor Strength, KTMG Scale (Right) DR |
| Q249 | - |  |  | SI | Shoulder Extension, Passive (Left) |
| Q249ObsDR | - |  |  | SI | Shoulder Extension, Passive (Left) DR |
| Q25 | - |  |  | SI | Flexion (0°- 180°) AROM (Right) |
| Q250 | - |  |  | SI | Shoulder Extension, Active (Left) |
| Q250ObsDR | - |  |  | SI | Shoulder Extension, Active (Left) DR |
| Q251 | - |  |  | SI | Shoulder Extensor Strength, KTMG Scale (Left) |
| Q251ObsDR | - |  |  | SI | Shoulder Extensor Strength, KTMG Scale (Left) DR |
| Q252 | - |  |  | SI | Shoulder Extension, Passive (Right) |
| Q252ObsDR | - |  |  | SI | Shoulder Extension, Passive (Right) DR |
| Q253 | - |  |  | SI | Shoulder Extension, Active (Right) |
| Q253ObsDR | - |  |  | SI | Shoulder Extension, Active (Right) DR |
| Q254 | - |  |  | SI | Shoulder Extensor Strength, KTMG Scale (Right) |
| Q254ObsDR | - |  |  | SI | Shoulder Extensor Strength, KTMG Scale (Right) DR |
| Q255 | - |  |  | SI | Shoulder Adduction, Passive (Left) |
| Q255ObsDR | - |  |  | SI | Shoulder Adduction, Passive (Left) DR |
| Q256 | - |  |  | SI | Shoulder Adduction, Active (Left) |
| Q256ObsDR | - |  |  | SI | Shoulder Adduction, Active (Left) DR |
| Q257 | - |  |  | SI | Shoulder Adduction, Passive (Right) |
| Q257ObsDR | - |  |  | SI | Shoulder Adduction, Passive (Right) DR |
| Q258 | - |  |  | SI | Shoulder Adduction, Active (Right) |
| Q258ObsDR | - |  |  | SI | Shoulder Adduction, Active (Right) DR |
| Q259 | - |  |  | SI | Shoulder Abduction, Passive (Left) |
| Q259ObsDR | - |  |  | SI | Shoulder Abduction, Passive (Left) DR |
| Q26 | - |  |  | SI | Flexion (0°- 180°) POWER (Right) |
| Q260 | - |  |  | SI | Shoulder Abduction, Active (Left) |
| Q260ObsDR | - |  |  | SI | Shoulder Abduction, Active (Left) DR |
| Q261 | - |  |  | SI | Shoulder Abductor Strength, KTMG Scale (Left) |
| Q261ObsDR | - |  |  | SI | Shoulder Abductor Strength, KTMG Scale (Left) DR |
| Q262 | - |  |  | SI | Shoulder Abduction, Passive (Right) |
| Q262ObsDR | - |  |  | SI | Shoulder Abduction, Passive (Right) DR |
| Q263 | - |  |  | SI | Shoulder Abduction, Active (Right) |
| Q263ObsDR | - |  |  | SI | Shoulder Abduction, Active (Right) DR |
| Q264 | - |  |  | SI | Shoulder Abductor Strength, KTMG Scale (Right) |
| Q264ObsDR | - |  |  | SI | Shoulder Abductor Strength, KTMG Scale (Right) DR |
| Q265 | - |  |  | SI | Shoulder Internal Rotation, Passive (Left) |
| Q265ObsDR | - |  |  | SI | Shoulder Internal Rotation, Passive (Left) DR |
| Q266 | - |  |  | SI | Shoulder Internal Rotation, Active (Left) |
| Q266ObsDR | - |  |  | SI | Shoulder Internal Rotation, Active (Left) DR |
| Q267 | - |  |  | SI | Shoulder Internal Rotator Strength, KTMG Scale (Le... |
| Q267ObsDR | - |  |  | SI | Shoulder Internal Rotator Strength, KTMG Scale (Le... |
| Q268 | - |  |  | SI | Shoulder Internal Rotation, Passive (Right) |
| Q268ObsDR | - |  |  | SI | Shoulder Internal Rotation, Passive (Right) DR |
| Q269 | - |  |  | SI | Shoulder Internal Rotation, Active (Right) |
| Q269ObsDR | - |  |  | SI | Shoulder Internal Rotation, Active (Right) DR |
| Q26ObsDR | - |  |  | SI | Flexion (0°- 180°) POWER (Right) DR |
| Q27 | - |  |  | SI | Extension (0°- 60°) |
| Q270 | - |  |  | SI | Shoulder Internal Rotator Strength, KTMG Scale (Ri... |
| Q270ObsDR | - |  |  | SI | Shoulder Internal Rotator Strength, KTMG Scale (Ri... |
| Q271 | - |  |  | SI | Shoulder External Rotation, Passive (Left) |
| Q271ObsDR | - |  |  | SI | Shoulder External Rotation, Passive (Left) DR |
| Q272 | - |  |  | SI | Shoulder External Rotation, Active (Left) |
| Q272ObsDR | - |  |  | SI | Shoulder External Rotation, Active (Left) DR |
| Q273 | - |  |  | SI | Shoulder External Rotator Strength, KTMG Scale (Le... |
| Q273ObsDR | - |  |  | SI | Shoulder External Rotator Strength, KTMG Scale (Le... |
| Q274 | - |  |  | SI | Shoulder External Rotation, Passive (Right) |
| Q274ObsDR | - |  |  | SI | Shoulder External Rotation, Passive (Right) DR |
| Q275 | - |  |  | SI | Shoulder External Rotation, Active (Right) |
| Q275ObsDR | - |  |  | SI | Shoulder External Rotation, Active (Right) DR |
| Q276 | - |  |  | SI | Shoulder External Rotator Strength, KTMG Scale (Ri... |
| Q276ObsDR | - |  |  | SI | Shoulder External Rotator Strength, KTMG Scale (Ri... |
| Q277 | - |  |  | SI | Elbow Flexion, Passive (Left) |
| Q277ObsDR | - |  |  | SI | Elbow Flexion, Passive (Left) DR |
| Q278 | - |  |  | SI | Elbow Flexion, Active (Left) |
| Q278ObsDR | - |  |  | SI | Elbow Flexion, Active (Left) DR |
| Q279 | - |  |  | SI | Elbow Flexor Strength, KTMG Scale (Left) |
| Q279ObsDR | - |  |  | SI | Elbow Flexor Strength, KTMG Scale (Left) DR |
| Q28 | - |  |  | SI | Extension (0°- 60°) PROM (Left) |
| Q280 | - |  |  | SI | Elbow Flexion, Passive (Right) |
| Q280ObsDR | - |  |  | SI | Elbow Flexion, Passive (Right) DR |
| Q281 | - |  |  | SI | Elbow Flexion, Active (Right) |
| Q281ObsDR | - |  |  | SI | Elbow Flexion, Active (Right) DR |
| Q282 | - |  |  | SI | Elbow Flexor Strength, KTMG Scale (Right) |
| Q282ObsDR | - |  |  | SI | Elbow Flexor Strength, KTMG Scale (Right) DR |
| Q283 | - |  |  | SI | Elbow Extension, Passive (Left) |
| Q283ObsDR | - |  |  | SI | Elbow Extension, Passive (Left) DR |
| Q284 | - |  |  | SI | Elbow Extension, Active (Left) |
| Q284ObsDR | - |  |  | SI | Elbow Extension, Active (Left) DR |
| Q285 | - |  |  | SI | Elbow Extensor Strength, KTMG Scale (Left) |
| Q285ObsDR | - |  |  | SI | Elbow Extensor Strength, KTMG Scale (Left) DR |
| Q286 | - |  |  | SI | Elbow Extension, Passive (Right) |
| Q286ObsDR | - |  |  | SI | Elbow Extension, Passive (Right) DR |
| Q287 | - |  |  | SI | Elbow Extension, Active (Right) |
| Q287ObsDR | - |  |  | SI | Elbow Extension, Active (Right) DR |
| Q288 | - |  |  | SI | Elbow Extensor Strength, KTMG Scale (Right) |
| Q288ObsDR | - |  |  | SI | Elbow Extensor Strength, KTMG Scale (Right) DR |
| Q289 | - |  |  | SI | Forearm Supination, Passive (Left) |
| Q289ObsDR | - |  |  | SI | Forearm Supination, Passive (Left) DR |
| Q29 | - |  |  | SI | Extension (0°- 60°) AROM (Left) |
| Q290 | - |  |  | SI | Forearm Supination, Active (Left) |
| Q290ObsDR | - |  |  | SI | Forearm Supination, Active (Left) DR |
| Q291 | - |  |  | SI | Forearm Supinator Strength, KTMG Scale (Left) |
| Q291ObsDR | - |  |  | SI | Forearm Supinator Strength, KTMG Scale (Left) DR |
| Q292 | - |  |  | SI | Forearm Supination, Passive (Right) |
| Q292ObsDR | - |  |  | SI | Forearm Supination, Passive (Right) DR |
| Q293 | - |  |  | SI | Forearm Supination, Active (Right) |
| Q293ObsDR | - |  |  | SI | Forearm Supination, Active (Right) DR |
| Q294 | - |  |  | SI | Forearm Supinator Strength, KTMG Scale (Right) |
| Q294ObsDR | - |  |  | SI | Forearm Supinator Strength, KTMG Scale (Right) DR |
| Q295 | - |  |  | SI | Forearm Pronation, Passive (Left) |
| Q295ObsDR | - |  |  | SI | Forearm Pronation, Passive (Left) DR |
| Q296 | - |  |  | SI | Forearm Pronation, Active (Left) |
| Q296ObsDR | - |  |  | SI | Forearm Pronation, Active (Left) DR |
| Q297 | - |  |  | SI | Forearm Pronator Strength, KTMG Scale (Left) |
| Q297ObsDR | - |  |  | SI | Forearm Pronator Strength, KTMG Scale (Left) DR |
| Q298 | - |  |  | SI | Forearm Pronation, Passive (Right) |
| Q298ObsDR | - |  |  | SI | Forearm Pronation, Passive (Right) DR |
| Q299 | - |  |  | SI | Forearm Pronation, Active (Right) |
| Q299ObsDR | - |  |  | SI | Forearm Pronation, Active (Right) DR |
| Q30 | - |  |  | SI | Extension (0°- 60°) POWER (Left) |
| Q300 | - |  |  | SI | Forearm Pronator Strength, KTMG Scale (Right) |
| Q300ObsDR | - |  |  | SI | Forearm Pronator Strength, KTMG Scale (Right) DR |
| Q301 | - |  |  | SI | Wrist Palmar Flexion, Passive (Left) |
| Q301ObsDR | - |  |  | SI | Wrist Palmar Flexion, Passive (Left) DR |
| Q302 | - |  |  | SI | Wrist Palmar Flexion, Active (Left) |
| Q302ObsDR | - |  |  | SI | Wrist Palmar Flexion, Active (Left) DR |
| Q303 | - |  |  | SI | Wrist Palmar Flexor Strength, KTMG Scale (Left) |
| Q303ObsDR | - |  |  | SI | Wrist Palmar Flexor Strength, KTMG Scale (Left) DR |
| Q304 | - |  |  | SI | Wrist Palmar Flexion, Passive (Right) |
| Q304ObsDR | - |  |  | SI | Wrist Palmar Flexion, Passive (Right) DR |
| Q305 | - |  |  | SI | Wrist Palmar Flexion, Active (Right) |
| Q305ObsDR | - |  |  | SI | Wrist Palmar Flexion, Active (Right) DR |
| Q306 | - |  |  | SI | Wrist Palmar Flexor Strength, KTMG Scale (Right) |
| Q306ObsDR | - |  |  | SI | Wrist Palmar Flexor Strength, KTMG Scale (Right) D... |
| Q307 | - |  |  | SI | Wrist Dorsiflexion, Passive (Left) |
| Q307ObsDR | - |  |  | SI | Wrist Dorsiflexion, Passive (Left) DR |
| Q308 | - |  |  | SI | Wrist Dorsiflexion, Active (Left) |
| Q308ObsDR | - |  |  | SI | Wrist Dorsiflexion, Active (Left) DR |
| Q309 | - |  |  | SI | Wrist Dorsiflexor Strength, KTMG Scale (Left) |
| Q309ObsDR | - |  |  | SI | Wrist Dorsiflexor Strength, KTMG Scale (Left) DR |
| Q30ObsDR | - |  |  | SI | Extension (0°- 60°) POWER (Left) DR |
| Q31 | - |  |  | SI | Extension (0°- 60°) PROM (Right) |
| Q310 | - |  |  | SI | Wrist Dorsiflexion, Passive (Right) |
| Q310ObsDR | - |  |  | SI | Wrist Dorsiflexion, Passive (Right) DR |
| Q311 | - |  |  | SI | Wrist Dorsiflexion, Active (Right) |
| Q311ObsDR | - |  |  | SI | Wrist Dorsiflexion, Active (Right) DR |
| Q312 | - |  |  | SI | Wrist Dorsiflexor Strength, KTMG Scale (Right) |
| Q312ObsDR | - |  |  | SI | Wrist Dorsiflexor Strength, KTMG Scale (Right) DR |
| Q313 | - |  |  | SI | Radial Flexion, Passive (Left) |
| Q313ObsDR | - |  |  | SI | Radial Flexion, Passive (Left) DR |
| Q314 | - |  |  | SI | Radial Flexion, Active (Left) |
| Q314ObsDR | - |  |  | SI | Radial Flexion, Active (Left) DR |
| Q315 | - |  |  | SI | Wrist Radial Flexor Strength, KTMG Scale (Left) |
| Q315ObsDR | - |  |  | SI | Wrist Radial Flexor Strength, KTMG Scale (Left) DR |
| Q316 | - |  |  | SI | Radial Flexion, Passive (Right) |
| Q316ObsDR | - |  |  | SI | Radial Flexion, Passive (Right) DR |
| Q317 | - |  |  | SI | Radial Flexion, Active (Right) |
| Q317ObsDR | - |  |  | SI | Radial Flexion, Active (Right) DR |
| Q318 | - |  |  | SI | Wrist Radial Flexor Strength, KTMG Scale (Right) |
| Q318ObsDR | - |  |  | SI | Wrist Radial Flexor Strength, KTMG Scale (Right) D... |
| Q319 | - |  |  | SI | Ulnar Flexion, Passive (Left) |
| Q319ObsDR | - |  |  | SI | Ulnar Flexion, Passive (Left) DR |
| Q32 | - |  |  | SI | Extension (0°- 60°) AROM (Right) |
| Q320 | - |  |  | SI | Ulnar Flexion, Active (Left) |
| Q320ObsDR | - |  |  | SI | Ulnar Flexion, Active (Left) DR |
| Q321 | - |  |  | SI | Wrist Ulnar Flexor Strength, KTMG Scale (Left) |
| Q321ObsDR | - |  |  | SI | Wrist Ulnar Flexor Strength, KTMG Scale (Left) DR |
| Q322 | - |  |  | SI | Ulnar Flexion, Passive (Right) |
| Q322ObsDR | - |  |  | SI | Ulnar Flexion, Passive (Right) DR |
| Q323 | - |  |  | SI | Ulnar Flexion, Active (Right) |
| Q323ObsDR | - |  |  | SI | Ulnar Flexion, Active (Right) DR |
| Q324 | - |  |  | SI | Wrist Ulnar Flexor Strength, KTMG Scale (Right) |
| Q324ObsDR | - |  |  | SI | Wrist Ulnar Flexor Strength, KTMG Scale (Right) DR |
| Q325 | - |  |  | SI | Carpometacarpal Flexion, Passive (Left) |
| Q325ObsDR | - |  |  | SI | Carpometacarpal Flexion, Passive (Left) DR |
| Q326 | - |  |  | SI | Carpometacarpal Flexion, Active (Left) |
| Q326ObsDR | - |  |  | SI | Carpometacarpal Flexion, Active (Left) DR |
| Q327 | - |  |  | SI | Carpometacarpal Flexion, Passive (Right) |
| Q327ObsDR | - |  |  | SI | Carpometacarpal Flexion, Passive (Right) DR |
| Q328 | - |  |  | SI | Carpometacarpal Flexion, Active (Right) |
| Q328ObsDR | - |  |  | SI | Carpometacarpal Flexion, Active (Right) DR |
| Q329 | - |  |  | SI | Carpometacarpal Extension, Passive (Left) |
| Q329ObsDR | - |  |  | SI | Carpometacarpal Extension, Passive (Left) DR |
| Q33 | - |  |  | SI | Extension (0°- 60°) POWER (Right) |
| Q330 | - |  |  | SI | Carpometacarpal Extension, Active (Left) |
| Q330ObsDR | - |  |  | SI | Carpometacarpal Extension, Active (Left) DR |
| Q331 | - |  |  | SI | Carpometacarpal Extension, Passive (Right) |
| Q331ObsDR | - |  |  | SI | Carpometacarpal Extension, Passive (Right) DR |
| Q332 | - |  |  | SI | Carpometacarpal Extension, Active (Right) |
| Q332ObsDR | - |  |  | SI | Carpometacarpal Extension, Active (Right) DR |
| Q333 | - |  |  | SI | Metacarpophalangeal Flexion-Extension, Passive (Le... |
| Q333ObsDR | - |  |  | SI | Metacarpophalangeal Flexion-Extension, Passive (Le... |
| Q334 | - |  |  | SI | Metacarpophalangeal Flexion-Extension, Active (Lef... |
| Q334ObsDR | - |  |  | SI | Metacarpophalangeal Flexion-Extension, Active (Lef... |
| Q335 | - |  |  | SI | Metacarpophalangeal Flexion-Extension, Passive (Ri... |
| Q335ObsDR | - |  |  | SI | Metacarpophalangeal Flexion-Extension, Passive (Ri... |
| Q336 | - |  |  | SI | Metacarpophalangeal Flexion-Extension, Active (Rig... |
| Q336ObsDR | - |  |  | SI | Metacarpophalangeal Flexion-Extension, Active (Rig... |
| Q337 | - |  |  | SI | Interphalangeal Flexion-Extension, Passive (Left) |
| Q337ObsDR | - |  |  | SI | Interphalangeal Flexion-Extension, Passive (Left) ... |
| Q338 | - |  |  | SI | Interphalangeal Flexion-Extension, Active (Left) |
| Q338ObsDR | - |  |  | SI | Interphalangeal Flexion-Extension, Active (Left) D... |
| Q339 | - |  |  | SI | Interphalangeal Flexion-Extension, Passive (Right) |
| Q339ObsDR | - |  |  | SI | Interphalangeal Flexion-Extension, Passive (Right)... |
| Q33ObsDR | - |  |  | SI | Extension (0°- 60°) POWER (Right) DR |
| Q34 | - |  |  | SI | Abduction (0°- 180°) |
| Q340 | - |  |  | SI | Interphalangeal Flexion-Extension, Active (Right) |
| Q340ObsDR | - |  |  | SI | Interphalangeal Flexion-Extension, Active (Right) ... |
| Q341 | - |  |  | SI | Thumb Abduction, Passive (Left) |
| Q341ObsDR | - |  |  | SI | Thumb Abduction, Passive (Left) DR |
| Q342 | - |  |  | SI | Thumb Abduction, Active (Left) |
| Q342ObsDR | - |  |  | SI | Thumb Abduction, Active (Left) DR |
| Q343 | - |  |  | SI | Thumb Abductor Strength, KTMG Scale (Left) |
| Q343ObsDR | - |  |  | SI | Thumb Abductor Strength, KTMG Scale (Left) DR |
| Q344 | - |  |  | SI | Thumb Abduction, Passive (Right) |
| Q344ObsDR | - |  |  | SI | Thumb Abduction, Passive (Right) DR |
| Q345 | - |  |  | SI | Thumb Abduction, Active (Right) |
| Q345ObsDR | - |  |  | SI | Thumb Abduction, Active (Right) DR |
| Q346 | - |  |  | SI | Thumb Abductor Strength, KTMG Scale (Right) |
| Q346ObsDR | - |  |  | SI | Thumb Abductor Strength, KTMG Scale (Right) DR |
| Q347 | - |  |  | SI | Thumb Opposition, Passive (Left) |
| Q347ObsDR | - |  |  | SI | Thumb Opposition, Passive (Left) DR |
| Q348 | - |  |  | SI | Thumb Opposition, Active (Left) |
| Q348ObsDR | - |  |  | SI | Thumb Opposition, Active (Left) DR |
| Q349 | - |  |  | SI | Thumb Opposer Strength, KTMG Scale (Left) |
| Q349ObsDR | - |  |  | SI | Thumb Opposer Strength, KTMG Scale (Left) DR |
| Q35 | - |  |  | SI | Abduction (0°- 180°)  PROM (Left) |
| Q350 | - |  |  | SI | Thumb Opposition, Passive (Right) |
| Q350ObsDR | - |  |  | SI | Thumb Opposition, Passive (Right) DR |
| Q351 | - |  |  | SI | Thumb Opposition, Active (Right) |
| Q351ObsDR | - |  |  | SI | Thumb Opposition, Active (Right) DR |
| Q352 | - |  |  | SI | Thumb Opposer Strength, KTMG Scale (Right) |
| Q352ObsDR | - |  |  | SI | Thumb Opposer Strength, KTMG Scale (Right) DR |
| Q353 | - |  |  | SI | Index Finger Pulp to Palm, Passive (Left) |
| Q353ObsDR | - |  |  | SI | Index Finger Pulp to Palm, Passive (Left) DR |
| Q354 | - |  |  | SI | Index Finger Pulp to Palm, Active (Left) |
| Q354ObsDR | - |  |  | SI | Index Finger Pulp to Palm, Active (Left) DR |
| Q355 | - |  |  | SI | Index Finger Pulp to Palm, Passive (Right) |
| Q355ObsDR | - |  |  | SI | Index Finger Pulp to Palm, Passive (Right) DR |
| Q356 | - |  |  | SI | Index Finger Pulp to Palm, Active (Right) |
| Q356ObsDR | - |  |  | SI | Index Finger Pulp to Palm, Active (Right) DR |
| Q357 | - |  |  | SI | Middle Finger Pulp to Palm, Passive (Left) |
| Q357ObsDR | - |  |  | SI | Middle Finger Pulp to Palm, Passive (Left) DR |
| Q358 | - |  |  | SI | Middle Finger Pulp to Palm, Active (Left) |
| Q358ObsDR | - |  |  | SI | Middle Finger Pulp to Palm, Active (Left) DR |
| Q359 | - |  |  | SI | Middle Finger Pulp to Palm, Passive (Right) |
| Q359ObsDR | - |  |  | SI | Middle Finger Pulp to Palm, Passive (Right) DR |
| Q36 | - |  |  | SI | Abduction (0°- 180°) AROM (Left) |
| Q360 | - |  |  | SI | Middle Finger Pulp to Palm, Active (Right) |
| Q360ObsDR | - |  |  | SI | Middle Finger Pulp to Palm, Active (Right) DR |
| Q361 | - |  |  | SI | Ring Finger Pulp to Palm, Passive (Left) |
| Q361ObsDR | - |  |  | SI | Ring Finger Pulp to Palm, Passive (Left) DR |
| Q362 | - |  |  | SI | Ring Finger Pulp to Palm, Active (Left) |
| Q362ObsDR | - |  |  | SI | Ring Finger Pulp to Palm, Active (Left) DR |
| Q363 | - |  |  | SI | Ring Finger Pulp to Palm, Passive (Right) |
| Q363ObsDR | - |  |  | SI | Ring Finger Pulp to Palm, Passive (Right) DR |
| Q364 | - |  |  | SI | Ring Finger Pulp to Palm, Active (Right) |
| Q364ObsDR | - |  |  | SI | Ring Finger Pulp to Palm, Active (Right) DR |
| Q365 | - |  |  | SI | Little Finger Pulp to Palm, Passive (Left) |
| Q365ObsDR | - |  |  | SI | Little Finger Pulp to Palm, Passive (Left) DR |
| Q366 | - |  |  | SI | Little Finger Pulp to Palm, Active (Left) |
| Q366ObsDR | - |  |  | SI | Little Finger Pulp to Palm, Active (Left) DR |
| Q367 | - |  |  | SI | Little Finger Pulp to Palm, Passive (Right) |
| Q367ObsDR | - |  |  | SI | Little Finger Pulp to Palm, Passive (Right) DR |
| Q368 | - |  |  | SI | Little Finger Pulp to Palm, Active (Right) |
| Q368ObsDR | - |  |  | SI | Little Finger Pulp to Palm, Active (Right) DR |
| Q369 | - |  |  | SI | Shoulder Adductor Strength, KTMG Scale (Left) |
| Q369ObsDR | - |  |  | SI | Shoulder Adductor Strength, KTMG Scale (Left) DR |
| Q37 | - |  |  | SI | Abduction (0°- 180°) POWER (Left) |
| Q370 | - |  |  | SI | Shoulder Adductor Strength, KTMG Scale (Right) |
| Q370ObsDR | - |  |  | SI | Shoulder Adductor Strength, KTMG Scale (Right) DR |
| Q371 | - |  |  | SI | Adduction |
| Q372 | - |  |  | SI | Right |
| Q373 | - |  |  | SI | Left |
| Q374 | - |  |  | SI | (Scale from Kendall FP et al. Muscles, testing and... |
| Q375 | - |  |  | SI | Thumb Carpometacarpal Flexor Strength, Modified Lo... |
| Q375ObsDR | - |  |  | SI | Thumb Carpometacarpal Flexor Strength, Modified Lo... |
| Q376 | - |  |  | SI | Thumb Carpometacarpal Flexor Strength, Modified Lo... |
| Q376ObsDR | - |  |  | SI | Thumb Carpometacarpal Flexor Strength, Modified Lo... |
| Q377 | - |  |  | SI | Thumb Carpometacarpal Extensor Strength, Modified ... |
| Q377ObsDR | - |  |  | SI | Thumb Carpometacarpal Extensor Strength, Modified ... |
| Q378 | - |  |  | SI | Thumb Carpometacarpal Extensor Strength, Modified ... |
| Q378ObsDR | - |  |  | SI | Thumb Carpometacarpal Extensor Strength, Modified ... |
| Q379 | - |  |  | SI | Thumb Metacarpophalangeal Flexor Strength, Modifie... |
| Q379ObsDR | - |  |  | SI | Thumb Metacarpophalangeal Flexor Strength, Modifie... |
| Q37ObsDR | - |  |  | SI | Abduction (0°- 180°) POWER (Left) DR |
| Q38 | - |  |  | SI | Abduction (0°- 180°) PROM (Right) |
| Q380 | - |  |  | SI | Thumb Interphalangeal Flexion - Extension Strength... |
| Q380ObsDR | - |  |  | SI | Thumb Interphalangeal Flexion - Extension Strength... |
| Q381 | - |  |  | SI | Thumb Interphalangeal Flexion - Extension Strength... |
| Q381ObsDR | - |  |  | SI | Thumb Interphalangeal Flexion - Extension Strength... |
| Q382 | - |  |  | SI | MP Flexion |
| Q383 | - |  |  | SI | Left |
| Q384 | - |  |  | SI | Right |
| Q385 | - |  |  | SI | Thumb Flexor Strength, KTMG Scale (Right) |
| Q385ObsDR | - |  |  | SI | Thumb Flexor Strength, KTMG Scale (Right) DR |
| Q386 | - |  |  | SI | MP Extension |
| Q387 | - |  |  | SI | Thumb Extensor Strength, KTMG Scale (Left) |
| Q387ObsDR | - |  |  | SI | Thumb Extensor Strength, KTMG Scale (Left) DR |
| Q388 | - |  |  | SI | Thumb Extensor Strength, KTMG Scale (Right) |
| Q388ObsDR | - |  |  | SI | Thumb Extensor Strength, KTMG Scale (Right) DR |
| Q389 | - |  |  | SI | Left |
| Q39 | - |  |  | SI | Abduction (0°- 180°) AROM (Right) |
| Q390 | - |  |  | SI | Right |
| Q391 | - |  |  | SI | IP Flexion |
| Q392 | - |  |  | SI | Left |
| Q393 | - |  |  | SI | Thumb Interphalangeal Flexor Strength, KTMG Scale ... |
| Q393ObsDR | - |  |  | SI | Thumb Interphalangeal Flexor Strength, KTMG Scale ... |
| Q394 | - |  |  | SI | Right |
| Q395 | - |  |  | SI | Thumb Interphalangeal Flexor Strength, KTMG Scale ... |
| Q395ObsDR | - |  |  | SI | Thumb Interphalangeal Flexor Strength, KTMG Scale ... |
| Q396 | - |  |  | SI | IP Extension |
| Q397 | - |  |  | SI | Left |
| Q398 | - |  |  | SI | Thumb Interphalangeal Extensor Strength, KTMG Scal... |
| Q398ObsDR | - |  |  | SI | Thumb Interphalangeal Extensor Strength, KTMG Scal... |
| Q399 | - |  |  | SI | Right |
| Q40 | - |  |  | SI | Abduction (0°- 180°) POWER (Right) |
| Q400 | - |  |  | SI | Thumb Interphalangeal Extensor Strength, KTMG Scal... |
| Q400ObsDR | - |  |  | SI | Thumb Interphalangeal Extensor Strength, KTMG Scal... |
| Q40ObsDR | - |  |  | SI | Abduction (0°- 180°) POWER (Right) DR |
| Q41 | - |  |  | SI | Internal Rotation (0°- 70°) |
| Q42 | - |  |  | SI | Internal Rotation (0°- 70°) PROM (Left) |
| Q43 | - |  |  | SI | Internal Rotation (0°- 70°) AROM (Left) |
| Q44 | - |  |  | SI | Internal Rotation (0°- 70°) POWER (Left) |
| Q44ObsDR | - |  |  | SI | Internal Rotation (0°- 70°) POWER (Left) DR |
| Q45 | - |  |  | SI | Internal Rotation (0°- 70°) PROM (Right) |
| Q46 | - |  |  | SI | Internal Rotation (0°- 70°) AROM (Right) |
| Q47 | - |  |  | SI | Internal Rotation (0°- 70°) POWER (Right) |
| Q47ObsDR | - |  |  | SI | Internal Rotation (0°- 70°) POWER (Right) DR |
| Q48 | - |  |  | SI | External Rotation (0°- 90°) |
| Q49 | - |  |  | SI | External Rotation (0°- 90°) PROM (Left) |
| Q50 | - |  |  | SI | External Rotation (0°- 90°) AROM (Left) |
| Q51 | - |  |  | SI | External Rotation (0°- 90°) POWER (Left) |
| Q51ObsDR | - |  |  | SI | External Rotation (0°- 90°) POWER (Left) DR |
| Q52 | - |  |  | SI | External Rotation (0°- 90°) PROM (Right) |
| Q53 | - |  |  | SI | External Rotation (0°- 90°) AROM (Right) |
| Q54 | - |  |  | SI | External Rotation (0°- 90°) POWER (Right) |
| Q54ObsDR | - |  |  | SI | External Rotation (0°- 90°) POWER (Right) DR |
| Q55 | - |  |  | SI | Elbow |
| Q56 | - |  |  | SI | Flexion (0°- 150°) |
| Q57 | - |  |  | SI | Flexion (0°- 150°) PROM (Left) |
| Q58 | - |  |  | SI | Flexion (0°- 150°) AROM (Left) |
| Q59 | - |  |  | SI | Flexion (0°- 150°) POWER (Left) |
| Q59ObsDR | - |  |  | SI | Flexion (0°- 150°) POWER (Left) DR |
| Q60 | - |  |  | SI | Flexion (0°- 150°) PROM (Right) |
| Q61 | - |  |  | SI | Flexion (0°- 150°) AROM (Right) |
| Q62 | - |  |  | SI | Flexion (0°- 150°) POWER (Right) |
| Q62ObsDR | - |  |  | SI | Flexion (0°- 150°) POWER (Right) DR |
| Q63 | - |  |  | SI | Extension (150°- 0°) |
| Q64 | - |  |  | SI | Extension (150°- 0°) PROM (Left) |
| Q65 | - |  |  | SI | Extension (150°- 0°) AROM (Left) |
| Q66 | - |  |  | SI | Extension (150°- 0°) POWER (Left) |
| Q66ObsDR | - |  |  | SI | Extension (150°- 0°) POWER (Left) DR |
| Q67 | - |  |  | SI | Extension (150°- 0°) PROM (Right) |
| Q68 | - |  |  | SI | Extension (150°- 0°) AROM (Right) |
| Q69 | - |  |  | SI | Extension (150°- 0°) POWER (Right) |
| Q69ObsDR | - |  |  | SI | Extension (150°- 0°) POWER (Right) DR |
| Q70 | - |  |  | SI | Forearm |
| Q71 | - |  |  | SI | Supination (0°- 80°) |
| Q72 | - |  |  | SI | Supination (0°- 80°) PROM (Left) |
| Q73 | - |  |  | SI | Supination (0°- 80°) AROM (Left) |
| Q74 | - |  |  | SI | Supination (0°- 80°) POWER (Left) |
| Q74ObsDR | - |  |  | SI | Supination (0°- 80°) POWER (Left) DR |
| Q75 | - |  |  | SI | Supination (0°- 80°) PROM (Right) |
| Q76 | - |  |  | SI | Supination (0°- 80°) AROM (Right) |
| Q77 | - |  |  | SI | Supination (0°- 80°) POWER (Right) |
| Q77ObsDR | - |  |  | SI | Supination (0°- 80°) POWER (Right) DR |
| Q78 | - |  |  | SI | Pronation (0°- 80°) |
| Q79 | - |  |  | SI | Pronation (0°- 80°) PROM (Left) |
| Q80 | - |  |  | SI | Pronation (0°- 80°) AROM (Left) |
| Q81 | - |  |  | SI | Pronation (0°- 80°) POWER (Left) |
| Q81ObsDR | - |  |  | SI | Pronation (0°- 80°) POWER (Left) DR |
| Q82 | - |  |  | SI | Pronation (0°- 80°) PROM (Right) |
| Q83 | - |  |  | SI | Pronation (0°- 80°) AROM (Right) |
| Q84 | - |  |  | SI | Pronation (0°- 80°) POWER (Right) |
| Q84ObsDR | - |  |  | SI | Pronation (0°- 80°) POWER (Right) DR |
| Q85 | - |  |  | SI | Wrist |
| Q86 | - |  |  | SI | Flexion (0°- 80°) - Wrist palmar flexor |
| Q87 | - |  |  | SI | Flexion (0°- 80°) PROM (Left) |
| Q88 | - |  |  | SI | Flexion (0°- 80°) AROM (Left) |
| Q89 | - |  |  | SI | Flexion (0°- 80°) POWER (Left) |
| Q89ObsDR | - |  |  | SI | Flexion (0°- 80°) POWER (Left) DR |
| Q90 | - |  |  | SI | Flexion (0°- 80°) PROM (Right) |
| Q91 | - |  |  | SI | Flexion (0°- 80°) AROM (Right) |
| Q92 | - |  |  | SI | Flexion (0°- 80°) POWER (Right) |
| Q92ObsDR | - |  |  | SI | Flexion (0°- 80°) POWER (Right) DR |
| Q93 | - |  |  | SI | Extension (0°- 70°) - Wrist dorsiflexor strength |
| Q94 | - |  |  | SI | Extension (0°- 70°) PROM (Left) |
| Q95 | - |  |  | SI | Extension (0°- 70°) AROM (Left) |
| Q96 | - |  |  | SI | Extension (0°- 70°) POWER (Left) |
| Q96ObsDR | - |  |  | SI | Extension (0°- 70°) POWER (Left) DR |
| Q97 | - |  |  | SI | Extension (0°- 70°) PROM (Right) |
| Q98 | - |  |  | SI | Extension (0°- 70°) AROM (Right) |
| Q99 | - |  |  | SI | Extension (0°- 70°) POWER (Right) |
| Q99ObsDR | - |  |  | SI | Extension (0°- 70°) POWER (Right) DR |
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