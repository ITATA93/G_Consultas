# SQLUser.PA_Adm2GroupNumber

**Schema:** SQLUser
**Columnas:** 927
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Admisión de Pacientes**. Registra episodios de atención hospitalaria.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| GRP_ParRef | bigint | PK |  | NO | PA_Adm2 Parent Reference |
| GRP_CheckBox1 | varchar |  |  | SI | CheckBox1 |
| GRP_CheckBox2 | varchar |  |  | SI | CheckBox2 |
| GRP_CheckBox3 | varchar |  |  | SI | CheckBox3 |
| GRP_CheckBox4 | varchar |  |  | SI | CheckBox4 |
| GRP_CheckBox5 | varchar |  |  | SI | CheckBox5 |
| GRP_CheckBox6 | varchar |  |  | SI | CheckBox6 |
| GRP_CheckBox7 | varchar |  |  | SI | CheckBox7 |
| GRP_CheckBox8 | varchar |  |  | SI | CheckBox8 |
| GRP_CheckBox9 | varchar |  |  | SI | CheckBox9 |
| GRP_Childsub | double |  |  | NO | Childsub |
| GRP_Code1_DR | bigint |  | FK | SI | Des Ref BillGrpType |
| GRP_Code2_DR | bigint |  | FK | SI | Des Ref BillGrpType |
| GRP_Code3_DR | bigint |  | FK | SI | Des Ref BillGrpType |
| GRP_Code4_DR | bigint |  | FK | SI | Des Ref BillGrpType |
| GRP_Code5_DR | bigint |  | FK | SI | Des Ref BillGrpType |
| GRP_Code6_DR | bigint |  | FK | SI | Des Ref BillGrpType |
| GRP_Code7_DR | bigint |  | FK | SI | Des Ref BillGrpType |
| GRP_Code8_DR | bigint |  | FK | SI | Des Ref BillGrpType |
| GRP_Date1 | date |  |  | SI | Date1 |
| GRP_Date2 | date |  |  | SI | Date2 |
| GRP_Date3 | date |  |  | SI | Date3 |
| GRP_DateFrom | date |  |  | SI | DateFrom |
| GRP_DateTo | date |  |  | SI | DateTo |
| GRP_DiagnosisGrp1_DR | bigint |  | FK | SI | Diagnosis Group 1 DR |
| GRP_Diagnosis_DR | bigint |  | FK | SI | Diagnosis DR |
| GRP_ExemptionReason_DR | bigint |  | FK | SI | Des Ref ExemptionReason |
| GRP_Hospital_DR | bigint |  | FK | SI | Hospital |
| GRP_Location_DR | bigint |  | FK | SI | Location |
| GRP_Number | varchar |  |  | SI | Number |
| GRP_Payor_DR | bigint |  | FK | SI | Des Ref Payor |
| GRP_Plan_DR | bigint |  | FK | SI | Des Ref Plan |
| GRP_Priority_DR | bigint |  | FK | SI | Des Ref Priority |
| GRP_RefClinic_DR | bigint |  | FK | SI | Referred By Clinic DR |
| GRP_Region_DR | bigint |  | FK | SI | Region DR |
| GRP_ResponsibleGP_DR | bigint |  | FK | SI | Des Ref ResponsibleGP |
| GRP_RowId | varchar |  |  | NO | - |
| GRP_SessionType_DR | bigint |  | FK | SI | Session Type DR |
| GRP_Text1 | varchar |  |  | SI | Text1 |
| GRP_Text10 | varchar |  |  | SI | Text10 |
| GRP_Text11 | varchar |  |  | SI | Text11 |
| GRP_Text12 | varchar |  |  | SI | Text12 |
| GRP_Text13 | varchar |  |  | SI | Text13 |
| GRP_Text2 | varchar |  |  | SI | Text2 |
| GRP_Text3 | varchar |  |  | SI | Text3 |
| GRP_Text4 | varchar |  |  | SI | Text4 |
| GRP_Text5 | varchar |  |  | SI | Text5 |
| GRP_Text6 | varchar |  |  | SI | Text6 |
| GRP_Text7 | varchar |  |  | SI | Text7 |
| GRP_Text8 | varchar |  |  | SI | Text8 |
| GRP_Text9 | varchar |  |  | SI | Text9 |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Assessment completed by |
| Q04 | - |  |  | SI | Impacted side |
| Q05 | - |  |  | SI | The following assessment table incorporates the Mo... |
| Q06 | - |  |  | SI | Legend |
| Q07 | - |  |  | SI | R1: Angle of catch seen at velocity V2 or V3) |
| Q08 | - |  |  | SI | R2: Full range of motion achieved when muscle is a... |
| Q09 | - |  |  | SI | R2-R1: Indicates the level of dynamic contracture ... |
| Q10 | - |  |  | SI | X - MTS: Modified Tardieu Scale (MTS) Quality of M... |
| Q100 | - |  |  | SI | R2 shoulder protractors (left) |
| Q101 | - |  |  | SI | R2 shoulder abductors (left) |
| Q102 | - |  |  | SI | R2 shoulder adductors (left) |
| Q103 | - |  |  | SI | R2 shoulder internal rotation (left) |
| Q104 | - |  |  | SI | R2 shoulder external rotation (left) |
| Q105 | - |  |  | SI | R2 elbow flexors (left) |
| Q106 | - |  |  | SI | R2 elbow extensors (left) |
| Q107 | - |  |  | SI | R2 forearm pronators (left) |
| Q108 | - |  |  | SI | R2 forearm supinators (left) |
| Q109 | - |  |  | SI | R2 wrist palmar flexors (left) |
| Q11 | - |  |  | SI | MAS: Modified Ashworth Scale |
| Q110 | - |  |  | SI | R2 wrist dorsiflexors (left) |
| Q111 | - |  |  | SI | R2 ulnar flexors (left) |
| Q112 | - |  |  | SI | R2 radial flexors (left) |
| Q113 | - |  |  | SI | R2 finger metacarpophalangeal flexors (left) |
| Q114 | - |  |  | SI | R2 finger metacarpophalangeal extensors (left) |
| Q115 | - |  |  | SI | R2 finger proximal interphalangeal flexors (left) |
| Q116 | - |  |  | SI | R2 finger proximal interphalangeal extensors (left... |
| Q117 | - |  |  | SI | R2 finger distal interphalangeal flexors (left) |
| Q118 | - |  |  | SI | R2 finger distal interphalangeal flexors (left) |
| Q119 | - |  |  | SI | R2 finger distal interphalangeal extensors (left) |
| Q12 | - |  |  | SI | MMT: Manual Muscle Test |
| Q120 | - |  |  | SI | R2 finger abductors (left) |
| Q121 | - |  |  | SI | R2 finger adductors (left) |
| Q122 | - |  |  | SI | R2 finger metacarpophalangeal flexors (left) |
| Q123 | - |  |  | SI | R2 thumb metacarpophalangeal extensors (left) |
| Q124 | - |  |  | SI | R2 thumb proximal interphalangeal flexors (left) |
| Q125 | - |  |  | SI | R2 thumb proximal interphalangeal extensors (left) |
| Q126 | - |  |  | SI | R2 thumb abductors (left) |
| Q127 | - |  |  | SI | R2 thumb adductors (left) |
| Q128 | - |  |  | SI | R2 thumb opposers (left) |
| Q129 | - |  |  | SI | R2-R1 shoulder flexors (left) |
| Q13 | - |  |  | SI | MMT: Manual Muscle Test |
| Q130 | - |  |  | SI | R2-R1 shoulder extensors (left) |
| Q131 | - |  |  | SI | R2-R1 shoulder retractors (left) |
| Q132 | - |  |  | SI | R2-R1 shoulder protractors (left) |
| Q133 | - |  |  | SI | R2-R1 shoulder abductors (left) |
| Q134 | - |  |  | SI | R2-R1 shoulder adductors (left) |
| Q135 | - |  |  | SI | R2-R1 shoulder internal rotation (left) |
| Q136 | - |  |  | SI | R2-R1 shoulder external rotation (left) |
| Q137 | - |  |  | SI | R2-R1 elbow flexors (left) |
| Q138 | - |  |  | SI | R2-R1 elbow extensors (left) |
| Q139 | - |  |  | SI | R2-R1 forearm pronators (left) |
| Q14 | - |  |  | SI | Manual Muscle Test (MMT) grading |
| Q140 | - |  |  | SI | R2-R1 forearm supinators (left) |
| Q141 | - |  |  | SI | R2-R1 wrist palmar flexors (left) |
| Q142 | - |  |  | SI | R2-R1 wrist dorsiflexors (left) |
| Q143 | - |  |  | SI | R2-R1 ulnar flexors (left) |
| Q144 | - |  |  | SI | R2-R1 radial flexors (left) |
| Q145 | - |  |  | SI | R2-R1 finger metacarpophalangeal flexors (left) |
| Q146 | - |  |  | SI | R2-R1 finger metacarpophalangeal extensors (left) |
| Q147 | - |  |  | SI | R2-R1 finger proximal interphalangeal flexors (lef... |
| Q148 | - |  |  | SI | R2-R1 finger proximal interphalangeal extensors (l... |
| Q149 | - |  |  | SI | R2-R1 finger distal interphalangeal flexors (left) |
| Q15 | - |  |  | SI | Left |
| Q150 | - |  |  | SI | R2-R1 finger distal interphalangeal extensors (lef... |
| Q151 | - |  |  | SI | R2-R1 finger abductors (left) |
| Q152 | - |  |  | SI | R2-R1 finger adductors (left) |
| Q153 | - |  |  | SI | R2-R1 finger metacarpophalangeal flexors (left) |
| Q154 | - |  |  | SI | R2-R1 thumb  metacarpophalangeal extensors (left) |
| Q155 | - |  |  | SI | R2-R1 thumb proximal interphalangeal flexors (left... |
| Q156 | - |  |  | SI | R2-R1 thumb proximal interphalangeal extensors (le... |
| Q157 | - |  |  | SI | R2-R1 thumb abductors (left) |
| Q158 | - |  |  | SI | R2-R1 thumb adductors (left) |
| Q159 | - |  |  | SI | R2 - R1 thumb opposers (left) |
| Q16 | - |  |  | SI | Right |
| Q160 | - |  |  | SI | R1 shoulder flexors (right) |
| Q161 | - |  |  | SI | R2 shoulder flexors (right) |
| Q162 | - |  |  | SI | R2-R1 shoulder flexors (right) |
| Q163 | - |  |  | SI | R1 shoulder extensors (right) |
| Q164 | - |  |  | SI | R2 shoulder extensors (right) |
| Q165 | - |  |  | SI | R2-R1 shoulder extensors (right) |
| Q166 | - |  |  | SI | R1 shoulder retractors (right) |
| Q167 | - |  |  | SI | R2 shoulder retractors (right) |
| Q168 | - |  |  | SI | R2-R1 shoulder retractors (right) |
| Q169 | - |  |  | SI | R1 shoulder protractors (right) |
| Q17 | - |  |  | SI | R1 |
| Q170 | - |  |  | SI | R2 shoulder protractors (right) |
| Q171 | - |  |  | SI | R2-R1 shoulder protractors (right) |
| Q172 | - |  |  | SI | R1 shoulder abductors (right) |
| Q173 | - |  |  | SI | R2 shoulder abductors (right) |
| Q174 | - |  |  | SI | R2-R1 shoulder abductors (right) |
| Q175 | - |  |  | SI | R1 shoulder adductors (right) |
| Q176 | - |  |  | SI | R2 shoulder adductors (right) |
| Q177 | - |  |  | SI | R2-R1 shoulder adductors (right) |
| Q178 | - |  |  | SI | R1 shoulder external rotation (right) |
| Q179 | - |  |  | SI | R2 shoulder external rotation (right) |
| Q18 | - |  |  | SI | R1 |
| Q180 | - |  |  | SI | R2-R1 shoulder external rotation (right) |
| Q181 | - |  |  | SI | R1 elbow flexors (right) |
| Q182 | - |  |  | SI | R2 elbow flexors (right) |
| Q183 | - |  |  | SI | R2-R1 elbow flexors (right) |
| Q184 | - |  |  | SI | R1 elbow extensors (right) |
| Q185 | - |  |  | SI | R2 elbow extensors (right) |
| Q186 | - |  |  | SI | R2-R1 elbow extensors (right) |
| Q187 | - |  |  | SI | R1 forearm pronators (right) |
| Q188 | - |  |  | SI | R2 forearm pronators (right) |
| Q189 | - |  |  | SI | R2-R1 forearm pronators (right) |
| Q19 | - |  |  | SI | R2 |
| Q190 | - |  |  | SI | R1 forearm supinators (right) |
| Q191 | - |  |  | SI | R2 forearm supinators (right) |
| Q192 | - |  |  | SI | R2-R1 forearm supinators (right) |
| Q193 | - |  |  | SI | R1 wrist flexors (right) |
| Q194 | - |  |  | SI | R2 wrist flexors (right) |
| Q195 | - |  |  | SI | R2-R1 wrist flexors (right) |
| Q196 | - |  |  | SI | R1 wrist extensors (right) |
| Q197 | - |  |  | SI | R2 wrist extensors (right) |
| Q198 | - |  |  | SI | R2-R1 wrist extensors (right) |
| Q199 | - |  |  | SI | R1 ulnar flexors (right) |
| Q20 | - |  |  | SI | R2 |
| Q200 | - |  |  | SI | R2 ulnar flexors (right) |
| Q201 | - |  |  | SI | R2-R1 ulnar flexors (right) |
| Q202 | - |  |  | SI | R1 radial flexors (right) |
| Q203 | - |  |  | SI | R2 radial flexors (right) |
| Q204 | - |  |  | SI | R2-R1 radial flexors (right) |
| Q205 | - |  |  | SI | R1 metacarpophalangeal flexors (right) |
| Q206 | - |  |  | SI | R2 metacarpophalangeal flexors (right) |
| Q207 | - |  |  | SI | R2-R1 metacarpophalangeal flexors (right) |
| Q208 | - |  |  | SI | R1 metacarpophalangeal extensors (right) |
| Q209 | - |  |  | SI | R2 metacarpophalangeal extensors (right) |
| Q21 | - |  |  | SI | R2-R1 |
| Q210 | - |  |  | SI | R2-R1 metacarpophalangeal extensors (right) |
| Q211 | - |  |  | SI | R1 proximal  interphalangeal flexors (right) |
| Q212 | - |  |  | SI | R2 proximal interphalangeal flexors (right) |
| Q213 | - |  |  | SI | R2-R1 proximal interphalangeal flexors (right) |
| Q214 | - |  |  | SI | R1 proximal interphalangeal extensors (right) |
| Q215 | - |  |  | SI | R2 proximal interphalangeal extensors (right) |
| Q216 | - |  |  | SI | R2-R1 proximal interphalangeal extensors (right) |
| Q217 | - |  |  | SI | R1 distal interphalangeal flexors (right) |
| Q218 | - |  |  | SI | R2 distal interphalangeal flexors (right) |
| Q219 | - |  |  | SI | R2-R1 distal interphalangeal flexors (right) |
| Q22 | - |  |  | SI | R2-R1 |
| Q220 | - |  |  | SI | R1 distal interphalangeal extensors (right) |
| Q221 | - |  |  | SI | R2 distal interphalangeal extensors (right) |
| Q222 | - |  |  | SI | R2-R1 distal interphalangeal extensors (right) |
| Q223 | - |  |  | SI | R1 finger abductors (right) |
| Q224 | - |  |  | SI | R2 finger abductors (right) |
| Q225 | - |  |  | SI | R2-R1 finger abductors (right) |
| Q226 | - |  |  | SI | R1 finger adductors (right) |
| Q227 | - |  |  | SI | R2 finger adductors (right) |
| Q228 | - |  |  | SI | R2-R1 finger adductors (right) |
| Q229 | - |  |  | SI | R1 finger metacarpophalangeal flexors (right) |
| Q23 | - |  |  | SI | X (MTS) |
| Q230 | - |  |  | SI | R2 finger metacarpophalangeal flexors (right) |
| Q231 | - |  |  | SI | R2-R1 finger metacarpophalangeal flexors (right) |
| Q232 | - |  |  | SI | R1 thumb metacarpophalangeal extensors (right) |
| Q233 | - |  |  | SI | R2 thumb metacarpophalangeal extensors (right) |
| Q234 | - |  |  | SI | R2-R1 thumb  metacarpophalangeal extensors (right) |
| Q235 | - |  |  | SI | R1 thumb proximal  interphalangeal flexors (right) |
| Q236 | - |  |  | SI | R2 thumb proximal interphalangeal flexors (right) |
| Q237 | - |  |  | SI | R2-R1 thumb proximal interphalangeal flexors (righ... |
| Q238 | - |  |  | SI | R1 thumb proximal interphalangeal extensors (right... |
| Q239 | - |  |  | SI | R2 thumb proximal interphalangeal extensors (right... |
| Q24 | - |  |  | SI | X (MTS) |
| Q240 | - |  |  | SI | R2-R1 thumb proximal interphalangeal extensors (ri... |
| Q241 | - |  |  | SI | R1 thumb abductors (right) |
| Q242 | - |  |  | SI | R2 thumb abductors (right) |
| Q243 | - |  |  | SI | R2-R1 thumb abductors (right) |
| Q244 | - |  |  | SI | R1 thumb adductors (right) |
| Q245 | - |  |  | SI | R2 thumb adductors (right) |
| Q246 | - |  |  | SI | R2-R1 thumb adductors (right) |
| Q247 | - |  |  | SI | R1 thumb opposers (right) |
| Q248 | - |  |  | SI | R2 thumb opposers (right) |
| Q249 | - |  |  | SI | R2 - R1 thumb opposers (right) |
| Q25 | - |  |  | SI | MAS |
| Q250 | - |  |  | SI | Shoulder Flexor Spasticity, MTS (Left) |
| Q250ObsDR | - |  |  | SI | Shoulder Flexor Spasticity, MTS (Left) DR |
| Q251 | - |  |  | SI | Shoulder Extensor Spasticity, MTS (Left) |
| Q251ObsDR | - |  |  | SI | Shoulder Extensor Spasticity, MTS (Left) DR |
| Q252 | - |  |  | SI | Shoulder Abductor Spasticity, MTS (Left) |
| Q252ObsDR | - |  |  | SI | Shoulder Abductor Spasticity, MTS (Left) DR |
| Q253 | - |  |  | SI | Shoulder Adductor Spasticity, MTS (Left) |
| Q253ObsDR | - |  |  | SI | Shoulder Adductor Spasticity, MTS (Left) DR |
| Q254 | - |  |  | SI | Shoulder Internal Rotator Spasticity, MTS (Left) |
| Q254ObsDR | - |  |  | SI | Shoulder Internal Rotator Spasticity, MTS (Left) D... |
| Q255 | - |  |  | SI | Shoulder External Rotator Spasticity, MTS (Left) |
| Q255ObsDR | - |  |  | SI | Shoulder External Rotator Spasticity, MTS (Left) D... |
| Q256 | - |  |  | SI | Elbow Flexor Spasticity, MTS (Left) |
| Q256ObsDR | - |  |  | SI | Elbow Flexor Spasticity, MTS (Left) DR |
| Q257 | - |  |  | SI | Elbow Extensor Spasticity, MTS (Left) |
| Q257ObsDR | - |  |  | SI | Elbow Extensor Spasticity, MTS (Left) DR |
| Q258 | - |  |  | SI | Forearm Pronator Spasticity, MTS (Left) |
| Q258ObsDR | - |  |  | SI | Forearm Pronator Spasticity, MTS (Left) DR |
| Q259 | - |  |  | SI | Forearm Supinator Spasticity, MTS (Left) |
| Q259ObsDR | - |  |  | SI | Forearm Supinator Spasticity, MTS (Left) DR |
| Q26 | - |  |  | SI | MAS |
| Q260 | - |  |  | SI | Wrist Plantar Flexor Spasticity, MTS (Left) |
| Q260ObsDR | - |  |  | SI | Wrist Plantar Flexor Spasticity, MTS (Left) DR |
| Q261 | - |  |  | SI | Wrist Dorsiflexor Spasticity, MTS (Left) |
| Q261ObsDR | - |  |  | SI | Wrist Dorsiflexor Spasticity, MTS (Left) DR |
| Q262 | - |  |  | SI | Wrist Ulnar Flexor Spasticity, MTS (Left) |
| Q262ObsDR | - |  |  | SI | Wrist Ulnar Flexor Spasticity, MTS (Left) DR |
| Q263 | - |  |  | SI | Wrist Radial Flexor Spasticity, MTS (Left) |
| Q263ObsDR | - |  |  | SI | Wrist Radial Flexor Spasticity, MTS (Left) DR |
| Q264 | - |  |  | SI | Finger Metacarpophalangeal Flexor Spasticity, MTS ... |
| Q264ObsDR | - |  |  | SI | Finger Metacarpophalangeal Flexor Spasticity, MTS ... |
| Q265 | - |  |  | SI | Finger Metacarpophalangeal  Extensor Spasticity, M... |
| Q265ObsDR | - |  |  | SI | Finger Metacarpophalangeal  Extensor Spasticity, M... |
| Q266 | - |  |  | SI | Finger Proximal Interphalangeal Extensor Spasticit... |
| Q266ObsDR | - |  |  | SI | Finger Proximal Interphalangeal Extensor Spasticit... |
| Q267 | - |  |  | SI | Finger Distal Interphalangeal Flexor Spasticity, M... |
| Q267ObsDR | - |  |  | SI | Finger Distal Interphalangeal Flexor Spasticity, M... |
| Q268 | - |  |  | SI | Thumb Metacarpophalangeal Flexor Spasticity, MTS (... |
| Q268ObsDR | - |  |  | SI | Thumb Metacarpophalangeal Flexor Spasticity, MTS (... |
| Q269 | - |  |  | SI | Thumb Metacarpophalangeal Extensor Spasticity, MTS... |
| Q269ObsDR | - |  |  | SI | Thumb Metacarpophalangeal Extensor Spasticity, MTS... |
| Q27 | - |  |  | SI | MMT MRC / KTMG |
| Q270 | - |  |  | SI | Thumb Proximal Interphalangeal Flexor Spasticity, ... |
| Q270ObsDR | - |  |  | SI | Thumb Proximal Interphalangeal Flexor Spasticity, ... |
| Q271 | - |  |  | SI | Thumb Proximal Interphalangeal Extensor Spasticity... |
| Q271ObsDR | - |  |  | SI | Thumb Proximal Interphalangeal Extensor Spasticity... |
| Q272 | - |  |  | SI | Thumb Opposer Spasticity, MTS (Left) |
| Q272ObsDR | - |  |  | SI | Thumb Opposer Spasticity, MTS (Left) DR |
| Q273 | - |  |  | SI | Finger Distal Interphalangeal Extensor Spasticity,... |
| Q273ObsDR | - |  |  | SI | Finger Distal Interphalangeal Extensor Spasticity,... |
| Q274 | - |  |  | SI | Shoulder Flexor Muscle Tone, MAS (Left) |
| Q274ObsDR | - |  |  | SI | Shoulder Flexor Muscle Tone, MAS (Left) DR |
| Q275 | - |  |  | SI | Shoulder Extensor Muscle Tone, MAS (Left) |
| Q275ObsDR | - |  |  | SI | Shoulder Extensor Muscle Tone, MAS (Left) DR |
| Q276 | - |  |  | SI | Shoulder Abductor Muscle Tone, MAS (Left) |
| Q276ObsDR | - |  |  | SI | Shoulder Abductor Muscle Tone, MAS (Left) DR |
| Q277 | - |  |  | SI | Shoulder Adductor Muscle Tone, MAS (Left) |
| Q277ObsDR | - |  |  | SI | Shoulder Adductor Muscle Tone, MAS (Left) DR |
| Q278 | - |  |  | SI | Shoulder Internal Rotator  Muscle Tone, MAS (Left) |
| Q278ObsDR | - |  |  | SI | Shoulder Internal Rotator  Muscle Tone, MAS (Left)... |
| Q279 | - |  |  | SI | Shoulder External Rotator Muscle Tone, MAS (Left) |
| Q279ObsDR | - |  |  | SI | Shoulder External Rotator Muscle Tone, MAS (Left) ... |
| Q28 | - |  |  | SI | MMT MRC / KTMG |
| Q280 | - |  |  | SI | Elbow Flexor Muscle Tone, MAS (Left) |
| Q280ObsDR | - |  |  | SI | Elbow Flexor Muscle Tone, MAS (Left) DR |
| Q281 | - |  |  | SI | Elbow Extensor Muscle Tone, MAS (Left) |
| Q281ObsDR | - |  |  | SI | Elbow Extensor Muscle Tone, MAS (Left) DR |
| Q282 | - |  |  | SI | Forearm Pronator Muscle Tone, MAS (Left) |
| Q282ObsDR | - |  |  | SI | Forearm Pronator Muscle Tone, MAS (Left) DR |
| Q283 | - |  |  | SI | Forearm Supinator Muscle Tone, MAS (Left) |
| Q283ObsDR | - |  |  | SI | Forearm Supinator Muscle Tone, MAS (Left) DR |
| Q284 | - |  |  | SI | Wrist Plantar Flexor Muscle Tone, MAS (Left) |
| Q284ObsDR | - |  |  | SI | Wrist Plantar Flexor Muscle Tone, MAS (Left) DR |
| Q285 | - |  |  | SI | Wrist Dorsiflexor Muscle Tone, MAS (Left) |
| Q285ObsDR | - |  |  | SI | Wrist Dorsiflexor Muscle Tone, MAS (Left) DR |
| Q286 | - |  |  | SI | Wrist Ulnar Flexor Muscle Tone, MAS (Left) |
| Q286ObsDR | - |  |  | SI | Wrist Ulnar Flexor Muscle Tone, MAS (Left) DR |
| Q287 | - |  |  | SI | Wrist Radial Flexor Muscle Tone, MAS (Left) |
| Q287ObsDR | - |  |  | SI | Wrist Radial Flexor Muscle Tone, MAS (Left) DR |
| Q288 | - |  |  | SI | Finger Metacarpophalangeal Flexor Muscle Tone, MAS... |
| Q288ObsDR | - |  |  | SI | Finger Metacarpophalangeal Flexor Muscle Tone, MAS... |
| Q289 | - |  |  | SI | Finger Metacarpophalangeal Extensor Muscle Tone, M... |
| Q289ObsDR | - |  |  | SI | Finger Metacarpophalangeal Extensor Muscle Tone, M... |
| Q29 | - |  |  | SI | Shoulder |
| Q290 | - |  |  | SI | Finger Metacarpophalangeal Extensor Muscle Tone, M... |
| Q290ObsDR | - |  |  | SI | Finger Metacarpophalangeal Extensor Muscle Tone, M... |
| Q291 | - |  |  | SI | Finger Proximal Interphalangeal Extensor Muscle To... |
| Q291ObsDR | - |  |  | SI | Finger Proximal Interphalangeal Extensor Muscle To... |
| Q292 | - |  |  | SI | Finger Distal Interphalangeal Flexor Muscle Tone, ... |
| Q292ObsDR | - |  |  | SI | Finger Distal Interphalangeal Flexor Muscle Tone, ... |
| Q293 | - |  |  | SI | Finger Distal Interphalangeal Extensor Muscle Tone... |
| Q293ObsDR | - |  |  | SI | Finger Distal Interphalangeal Extensor Muscle Tone... |
| Q294 | - |  |  | SI | Finger Abductor Muscle Tone, MAS (Left) |
| Q294ObsDR | - |  |  | SI | Finger Abductor Muscle Tone, MAS (Left) DR |
| Q295 | - |  |  | SI | Finger Adductor Muscle Tone, MAS (Left) |
| Q295ObsDR | - |  |  | SI | Finger Adductor Muscle Tone, MAS (Left) DR |
| Q296 | - |  |  | SI | Thumb Metacarpophalangeal Flexor Muscle Tone, MAS ... |
| Q296ObsDR | - |  |  | SI | Thumb Metacarpophalangeal Flexor Muscle Tone, MAS ... |
| Q297 | - |  |  | SI | Thumb Metacarpophalangeal Extensor Muscle Tone, MA... |
| Q297ObsDR | - |  |  | SI | Thumb Metacarpophalangeal Extensor Muscle Tone, MA... |
| Q298 | - |  |  | SI | Thumb Proximal Interphalangeal Flexor Muscle Tone,... |
| Q298ObsDR | - |  |  | SI | Thumb Proximal Interphalangeal Flexor Muscle Tone,... |
| Q299 | - |  |  | SI | Thumb Proximal Interphalangeal Extensor Muscle Ton... |
| Q299ObsDR | - |  |  | SI | Thumb Proximal Interphalangeal Extensor Muscle Ton... |
| Q30 | - |  |  | SI | Retractors |
| Q300 | - |  |  | SI | Thumb Abductor Muscle Tone, MAS (Left) |
| Q300ObsDR | - |  |  | SI | Thumb Abductor Muscle Tone, MAS (Left) DR |
| Q301 | - |  |  | SI | Thumb Adductor Muscle Tone, MAS (Left) |
| Q301ObsDR | - |  |  | SI | Thumb Adductor Muscle Tone, MAS (Left) DR |
| Q302 | - |  |  | SI | Thumb Opposer  Muscle Tone, MAS (Left) |
| Q302ObsDR | - |  |  | SI | Thumb Opposer  Muscle Tone, MAS (Left) DR |
| Q303 | - |  |  | SI | Shoulder Flexor Strength, MRC Scale (Left) |
| Q303ObsDR | - |  |  | SI | Shoulder Flexor Strength, MRC Scale (Left) DR |
| Q304 | - |  |  | SI | Shoulder Flexor Strength, KTMG Scale (Left) |
| Q304ObsDR | - |  |  | SI | Shoulder Flexor Strength, KTMG Scale (Left) DR |
| Q305 | - |  |  | SI | Shoulder Extensor Strength, MRC Scale (Left) |
| Q305ObsDR | - |  |  | SI | Shoulder Extensor Strength, MRC Scale (Left) DR |
| Q306 | - |  |  | SI | Shoulder Extensor Strength, KTMG Scale (Left) |
| Q306ObsDR | - |  |  | SI | Shoulder Extensor Strength, KTMG Scale (Left) DR |
| Q307 | - |  |  | SI | Shoulder Retractor Strength, MRC Scale (Left) |
| Q307ObsDR | - |  |  | SI | Shoulder Retractor Strength, MRC Scale (Left) DR |
| Q308 | - |  |  | SI | Shoulder Retractor Strength, KTMG Scale (Left) |
| Q308ObsDR | - |  |  | SI | Shoulder Retractor Strength, KTMG Scale (Left) DR |
| Q309 | - |  |  | SI | Shoulder Protractor Strength, MRC Scale (Left) |
| Q309ObsDR | - |  |  | SI | Shoulder Protractor Strength, MRC Scale (Left) DR |
| Q31 | - |  |  | SI | Protractors |
| Q310 | - |  |  | SI | Shoulder Protractor Strength, KTMG Scale (Left) |
| Q310ObsDR | - |  |  | SI | Shoulder Protractor Strength, KTMG Scale (Left) DR |
| Q311 | - |  |  | SI | Shoulder Abductor Strength, MRC Scale (Left) |
| Q311ObsDR | - |  |  | SI | Shoulder Abductor Strength, MRC Scale (Left) DR |
| Q312 | - |  |  | SI | Shoulder Abductor Strength, KTMG Scale (Left) |
| Q312ObsDR | - |  |  | SI | Shoulder Abductor Strength, KTMG Scale (Left) DR |
| Q313 | - |  |  | SI | Shoulder Adductor Strength, MRC Scale (Left) |
| Q313ObsDR | - |  |  | SI | Shoulder Adductor Strength, MRC Scale (Left) DR |
| Q314 | - |  |  | SI | Shoulder Adductor Strength, KTMG Scale (Left) |
| Q314ObsDR | - |  |  | SI | Shoulder Adductor Strength, KTMG Scale (Left) DR |
| Q315 | - |  |  | SI | Shoulder Internal Rotator Strength, MRC Scale (Lef... |
| Q315ObsDR | - |  |  | SI | Shoulder Internal Rotator Strength, MRC Scale (Lef... |
| Q316 | - |  |  | SI | Shoulder Internal Rotator Strength, KTMG Scale (Le... |
| Q316ObsDR | - |  |  | SI | Shoulder Internal Rotator Strength, KTMG Scale (Le... |
| Q317 | - |  |  | SI | Shoulder External Rotator Strength, MRC Scale (Lef... |
| Q317ObsDR | - |  |  | SI | Shoulder External Rotator Strength, MRC Scale (Lef... |
| Q318 | - |  |  | SI | Shoulder External Rotator Strength, KTMG Scale (Le... |
| Q318ObsDR | - |  |  | SI | Shoulder External Rotator Strength, KTMG Scale (Le... |
| Q319 | - |  |  | SI | Elbow Flexor Strength, MRC Scale (Left) |
| Q319ObsDR | - |  |  | SI | Elbow Flexor Strength, MRC Scale (Left) DR |
| Q32 | - |  |  | SI | Flexors |
| Q320 | - |  |  | SI | Elbow Flexor Strength, KTMG Scale (Left) |
| Q320ObsDR | - |  |  | SI | Elbow Flexor Strength, KTMG Scale (Left) DR |
| Q321 | - |  |  | SI | Elbow Extensor Strength, MRC Scale (Left) |
| Q321ObsDR | - |  |  | SI | Elbow Extensor Strength, MRC Scale (Left) DR |
| Q322 | - |  |  | SI | Elbow Extensor Strength, KTMG Scale (Left) |
| Q322ObsDR | - |  |  | SI | Elbow Extensor Strength, KTMG Scale (Left) DR |
| Q323 | - |  |  | SI | Elbow Extensor Strength, MRC Scale (Left) |
| Q323ObsDR | - |  |  | SI | Elbow Extensor Strength, MRC Scale (Left) DR |
| Q324 | - |  |  | SI | Elbow Extensor Strength, KTMG Scale (Left) |
| Q324ObsDR | - |  |  | SI | Elbow Extensor Strength, KTMG Scale (Left) DR |
| Q325 | - |  |  | SI | Forearm Pronator Strength, KTMG Scale (Left) |
| Q325ObsDR | - |  |  | SI | Forearm Pronator Strength, KTMG Scale (Left) DR |
| Q326 | - |  |  | SI | Forearm Supinator Strength, MRC Scale (Left) |
| Q326ObsDR | - |  |  | SI | Forearm Supinator Strength, MRC Scale (Left) DR |
| Q327 | - |  |  | SI | Forearm Supinator Strength, KTMG Scale (Left) |
| Q327ObsDR | - |  |  | SI | Forearm Supinator Strength, KTMG Scale (Left) DR |
| Q328 | - |  |  | SI | Wrist Palmar Flexor Strength, MRC Scale (Left) |
| Q328ObsDR | - |  |  | SI | Wrist Palmar Flexor Strength, MRC Scale (Left) DR |
| Q329 | - |  |  | SI | Wrist Palmar Flexor Strength, KTMG Scale (Left) |
| Q329ObsDR | - |  |  | SI | Wrist Palmar Flexor Strength, KTMG Scale (Left) DR |
| Q33 | - |  |  | SI | Extensors |
| Q330 | - |  |  | SI | Wrist Dorsiflexor Strength, MRC Scale (Left) |
| Q330ObsDR | - |  |  | SI | Wrist Dorsiflexor Strength, MRC Scale (Left) DR |
| Q331 | - |  |  | SI | Wrist Dorsiflexor Strength, KTMG Scale (Left) |
| Q331ObsDR | - |  |  | SI | Wrist Dorsiflexor Strength, KTMG Scale (Left) DR |
| Q332 | - |  |  | SI | Wrist Ulnar Flexor Strength, MRC Scale (Left) |
| Q332ObsDR | - |  |  | SI | Wrist Ulnar Flexor Strength, MRC Scale (Left) DR |
| Q333 | - |  |  | SI | Wrist Ulnar Flexor Strength, KTMG Scale (Left) |
| Q333ObsDR | - |  |  | SI | Wrist Ulnar Flexor Strength, KTMG Scale (Left) DR |
| Q334 | - |  |  | SI | Wrist Radial Flexor Strength, MRC Scale (Left) |
| Q334ObsDR | - |  |  | SI | Wrist Radial Flexor Strength, MRC Scale (Left) DR |
| Q335 | - |  |  | SI | Wrist Radial Flexor Strength, KTMG Scale (Left) |
| Q335ObsDR | - |  |  | SI | Wrist Radial Flexor Strength, KTMG Scale (Left) DR |
| Q336 | - |  |  | SI | Finger Flexor Strength, MRC Scale (Left) |
| Q336ObsDR | - |  |  | SI | Finger Flexor Strength, MRC Scale (Left) DR |
| Q337 | - |  |  | SI | Finger Flexor Strength, KTMG Scale (Left) |
| Q337ObsDR | - |  |  | SI | Finger Flexor Strength, KTMG Scale (Left) DR |
| Q338 | - |  |  | SI | Finger Extensor Strength, MRC Scale (Left) |
| Q338ObsDR | - |  |  | SI | Finger Extensor Strength, MRC Scale (Left) DR |
| Q339 | - |  |  | SI | Finger Extensor Strength, KTMG Scale (Left) |
| Q339ObsDR | - |  |  | SI | Finger Extensor Strength, KTMG Scale (Left) DR |
| Q34 | - |  |  | SI | Abductors |
| Q340 | - |  |  | SI | Finger Proximal Interphalangeal Flexor Strength, M... |
| Q340ObsDR | - |  |  | SI | Finger Proximal Interphalangeal Flexor Strength, M... |
| Q341 | - |  |  | SI | Finger Proximal Interphalangeal Flexor Strength, K... |
| Q341ObsDR | - |  |  | SI | Finger Proximal Interphalangeal Flexor Strength, K... |
| Q342 | - |  |  | SI | Finger Proximal Interphalangeal Extensor Strength,... |
| Q342ObsDR | - |  |  | SI | Finger Proximal Interphalangeal Extensor Strength,... |
| Q343 | - |  |  | SI | Finger Proximal Interphalangeal Extensor Strength,... |
| Q343ObsDR | - |  |  | SI | Finger Proximal Interphalangeal Extensor Strength,... |
| Q344 | - |  |  | SI | Finger Distal Interphalangeal Flexor Strength, MRC... |
| Q344ObsDR | - |  |  | SI | Finger Distal Interphalangeal Flexor Strength, MRC... |
| Q345 | - |  |  | SI | Finger Distal Interphalangeal Flexor Strength, KTM... |
| Q345ObsDR | - |  |  | SI | Finger Distal Interphalangeal Flexor Strength, KTM... |
| Q346 | - |  |  | SI | Finger Distal Interphalangeal Extensor Strength, M... |
| Q346ObsDR | - |  |  | SI | Finger Distal Interphalangeal Extensor Strength, M... |
| Q347 | - |  |  | SI | Finger Distal Interphalangeal Extensor Strength, K... |
| Q347ObsDR | - |  |  | SI | Finger Distal Interphalangeal Extensor Strength, K... |
| Q348 | - |  |  | SI | Finger Abductor Strength, MRC Scale (Left) |
| Q348ObsDR | - |  |  | SI | Finger Abductor Strength, MRC Scale (Left) DR |
| Q349 | - |  |  | SI | Finger Abductor Strength, KTMG Scale (Left) |
| Q349ObsDR | - |  |  | SI | Finger Abductor Strength, KTMG Scale (Left) DR |
| Q35 | - |  |  | SI | Internal Rotators |
| Q350 | - |  |  | SI | Fingers Adductor Strength, MRC Scale (Left) |
| Q350ObsDR | - |  |  | SI | Fingers Adductor Strength, MRC Scale (Left) DR |
| Q351 | - |  |  | SI | Finger Adductor Strength, KTMG Scale (Left) |
| Q351ObsDR | - |  |  | SI | Finger Adductor Strength, KTMG Scale (Left) DR |
| Q352 | - |  |  | SI | Thumb Flexor Strength, MRC Scale (Left) |
| Q352ObsDR | - |  |  | SI | Thumb Flexor Strength, MRC Scale (Left) DR |
| Q353 | - |  |  | SI | Thumb Flexor Strength, KTMG Scale (Left) |
| Q353ObsDR | - |  |  | SI | Thumb Flexor Strength, KTMG Scale (Left) DR |
| Q354 | - |  |  | SI | Thumb Extensor Strength, MRC Scale (Left) |
| Q354ObsDR | - |  |  | SI | Thumb Extensor Strength, MRC Scale (Left) DR |
| Q355 | - |  |  | SI | Thumb Extensor Strength, KTMG Scale (Left) |
| Q355ObsDR | - |  |  | SI | Thumb Extensor Strength, KTMG Scale (Left) DR |
| Q356 | - |  |  | SI | Thumb Interphalangeal Flexor Strength, MRC Scale (... |
| Q356ObsDR | - |  |  | SI | Thumb Interphalangeal Flexor Strength, MRC Scale (... |
| Q357 | - |  |  | SI | Thumb Interphalangeal Flexor Strength, KTMG Scale ... |
| Q357ObsDR | - |  |  | SI | Thumb Interphalangeal Flexor Strength, KTMG Scale ... |
| Q358 | - |  |  | SI | Thumb Interphalangeal Extensor Strength, MRC Scale... |
| Q358ObsDR | - |  |  | SI | Thumb Interphalangeal Extensor Strength, MRC Scale... |
| Q359 | - |  |  | SI | Thumb Interphalangeal Extensor Strength, KTMG Scal... |
| Q359ObsDR | - |  |  | SI | Thumb Interphalangeal Extensor Strength, KTMG Scal... |
| Q36 | - |  |  | SI | External Rotators |
| Q360 | - |  |  | SI | Thumb Abductor Strength, MRC Scale (Left) |
| Q360ObsDR | - |  |  | SI | Thumb Abductor Strength, MRC Scale (Left) DR |
| Q361 | - |  |  | SI | Thumb Abductor Strength, KTMG Scale (Left) |
| Q361ObsDR | - |  |  | SI | Thumb Abductor Strength, KTMG Scale (Left) DR |
| Q362 | - |  |  | SI | Thumb Adductor Strength, MRC Scale (Left) |
| Q362ObsDR | - |  |  | SI | Thumb Adductor Strength, MRC Scale (Left) DR |
| Q363 | - |  |  | SI | Thumb Adductor Strength, KTMG Scale (Left) |
| Q363ObsDR | - |  |  | SI | Thumb Adductor Strength, KTMG Scale (Left) DR |
| Q364 | - |  |  | SI | Thumb Opposer Strength, MRC Scale (Left) |
| Q364ObsDR | - |  |  | SI | Thumb Opposer Strength, MRC Scale (Left) DR |
| Q365 | - |  |  | SI | Thumb Opposer Strength, KTMG Scale (Left) |
| Q365ObsDR | - |  |  | SI | Thumb Opposer Strength, KTMG Scale (Left) DR |
| Q366 | - |  |  | SI | Shoulder Flexor Spasticity, MTS (Right) |
| Q366ObsDR | - |  |  | SI | Shoulder Flexor Spasticity, MTS (Right) DR |
| Q367 | - |  |  | SI | Shoulder Extensor Spasticity, MTS (Right) |
| Q367ObsDR | - |  |  | SI | Shoulder Extensor Spasticity, MTS (Right) DR |
| Q368 | - |  |  | SI | Shoulder Abductor Spasticity, MTS (Right) |
| Q368ObsDR | - |  |  | SI | Shoulder Abductor Spasticity, MTS (Right) DR |
| Q369 | - |  |  | SI | Shoulder Adductor Spasticity, MTS (Right) |
| Q369ObsDR | - |  |  | SI | Shoulder Adductor Spasticity, MTS (Right) DR |
| Q37 | - |  |  | SI | Elbow |
| Q370 | - |  |  | SI | Shoulder Internal Rotator Spasticity, MTS (Right) |
| Q370ObsDR | - |  |  | SI | Shoulder Internal Rotator Spasticity, MTS (Right) ... |
| Q371 | - |  |  | SI | Shoulder External Rotator Spasticity, MTS (Right) |
| Q371ObsDR | - |  |  | SI | Shoulder External Rotator Spasticity, MTS (Right) ... |
| Q372 | - |  |  | SI | Elbow Flexor Spasticity, MTS (Right) |
| Q372ObsDR | - |  |  | SI | Elbow Flexor Spasticity, MTS (Right) DR |
| Q373 | - |  |  | SI | Elbow Extensor Spasticity, MTS (Right) |
| Q373ObsDR | - |  |  | SI | Elbow Extensor Spasticity, MTS (Right) DR |
| Q374 | - |  |  | SI | Forearm Pronator Spasticity, MTS (Righ) |
| Q374ObsDR | - |  |  | SI | Forearm Pronator Spasticity, MTS (Righ) DR |
| Q375 | - |  |  | SI | Forearm Supinator Spasticity, MTS (Right) |
| Q375ObsDR | - |  |  | SI | Forearm Supinator Spasticity, MTS (Right) DR |
| Q376 | - |  |  | SI | Wrist Plantar Flexor Spasticity, MTS (Right) |
| Q376ObsDR | - |  |  | SI | Wrist Plantar Flexor Spasticity, MTS (Right) DR |
| Q377 | - |  |  | SI | Wrist Dorsiflexor Spasticity, MTS (Right) |
| Q377ObsDR | - |  |  | SI | Wrist Dorsiflexor Spasticity, MTS (Right) DR |
| Q378 | - |  |  | SI | Wrist Ulnar Flexor Spasticity, MTS (Right) |
| Q378ObsDR | - |  |  | SI | Wrist Ulnar Flexor Spasticity, MTS (Right) DR |
| Q379 | - |  |  | SI | Wrist Radial Flexor Spasticity, MTS (Right) |
| Q379ObsDR | - |  |  | SI | Wrist Radial Flexor Spasticity, MTS (Right) DR |
| Q38 | - |  |  | SI | Flexors |
| Q380 | - |  |  | SI | Finger Metacarpophalangeal Flexor Spasticity, MTS ... |
| Q380ObsDR | - |  |  | SI | Finger Metacarpophalangeal Flexor Spasticity, MTS ... |
| Q381 | - |  |  | SI | Finger Metacarpophalangeal Extensor Spasticity, MT... |
| Q381ObsDR | - |  |  | SI | Finger Metacarpophalangeal Extensor Spasticity, MT... |
| Q382 | - |  |  | SI | Finger Proximal Interphalangeal Flexor Spasticity,... |
| Q382ObsDR | - |  |  | SI | Finger Proximal Interphalangeal Flexor Spasticity,... |
| Q383 | - |  |  | SI | Finger Proximal Interphalangeal Extensor Spasticit... |
| Q383ObsDR | - |  |  | SI | Finger Proximal Interphalangeal Extensor Spasticit... |
| Q384 | - |  |  | SI | Finger Distal Interphalangeal Flexor Spasticity, M... |
| Q384ObsDR | - |  |  | SI | Finger Distal Interphalangeal Flexor Spasticity, M... |
| Q385 | - |  |  | SI | Finger Distal Interphalangeal Extensor Spasticity,... |
| Q385ObsDR | - |  |  | SI | Finger Distal Interphalangeal Extensor Spasticity,... |
| Q386 | - |  |  | SI | Finger Abductor Muscle Tone, MTS (Right) |
| Q386ObsDR | - |  |  | SI | Finger Abductor Muscle Tone, MTS (Right) DR |
| Q387 | - |  |  | SI | Finger Adductor Muscle Tone, MTS (Right) |
| Q387ObsDR | - |  |  | SI | Finger Adductor Muscle Tone, MTS (Right) DR |
| Q388 | - |  |  | SI | Thumb Metacarpophalangeal Flexor Spasticity, MTS (... |
| Q388ObsDR | - |  |  | SI | Thumb Metacarpophalangeal Flexor Spasticity, MTS (... |
| Q389 | - |  |  | SI | Thumb Metacarpophalangeal Extensor Spasticity, MTS... |
| Q389ObsDR | - |  |  | SI | Thumb Metacarpophalangeal Extensor Spasticity, MTS... |
| Q39 | - |  |  | SI | Extensors |
| Q390 | - |  |  | SI | Thumb Proximal Interphalangeal Flexor Spasticity, ... |
| Q390ObsDR | - |  |  | SI | Thumb Proximal Interphalangeal Flexor Spasticity, ... |
| Q391 | - |  |  | SI | Thumb Proximal Interphalangeal Extensor Spasticity... |
| Q391ObsDR | - |  |  | SI | Thumb Proximal Interphalangeal Extensor Spasticity... |
| Q392 | - |  |  | SI | Thumb Abductor Spasticity, MTS (Right) |
| Q392ObsDR | - |  |  | SI | Thumb Abductor Spasticity, MTS (Right) DR |
| Q393 | - |  |  | SI | Thumb Adductor Spasticity, MTS (Right) |
| Q393ObsDR | - |  |  | SI | Thumb Adductor Spasticity, MTS (Right) DR |
| Q394 | - |  |  | SI | Thumb Opposer Spasticity, MTS (Right) |
| Q394ObsDR | - |  |  | SI | Thumb Opposer Spasticity, MTS (Right) DR |
| Q395 | - |  |  | SI | Shoulder Flexor Muscle Tone, MAS (Right) |
| Q395ObsDR | - |  |  | SI | Shoulder Flexor Muscle Tone, MAS (Right) DR |
| Q396 | - |  |  | SI | Shoulder Extensor Muscle Tone, MAS (Right) |
| Q396ObsDR | - |  |  | SI | Shoulder Extensor Muscle Tone, MAS (Right) DR |
| Q397 | - |  |  | SI | Shoulder Abductor Muscle Tone, MAS (Right) |
| Q397ObsDR | - |  |  | SI | Shoulder Abductor Muscle Tone, MAS (Right) DR |
| Q398 | - |  |  | SI | Shoulder Adductor Muscle Tone, MAS (Right) |
| Q398ObsDR | - |  |  | SI | Shoulder Adductor Muscle Tone, MAS (Right) DR |
| Q399 | - |  |  | SI | Shoulder External Rotator Muscle Tone, MAS (Right) |
| Q399ObsDR | - |  |  | SI | Shoulder External Rotator Muscle Tone, MAS (Right)... |
| Q40 | - |  |  | SI | Forearm |
| Q400 | - |  |  | SI | Elbow Flexor Muscle Tone, MAS (Right) |
| Q400ObsDR | - |  |  | SI | Elbow Flexor Muscle Tone, MAS (Right) DR |
| Q401 | - |  |  | SI | Elbow Extensor Muscle Tone, MAS (Right) |
| Q401ObsDR | - |  |  | SI | Elbow Extensor Muscle Tone, MAS (Right) DR |
| Q402 | - |  |  | SI | Forearm Pronator Muscle Tone, MAS (Right) |
| Q402ObsDR | - |  |  | SI | Forearm Pronator Muscle Tone, MAS (Right) DR |
| Q403 | - |  |  | SI | Wrist Plantar Flexor Muscle Tone, MAS (Right) |
| Q403ObsDR | - |  |  | SI | Wrist Plantar Flexor Muscle Tone, MAS (Right) DR |
| Q404 | - |  |  | SI | Wrist Dorsiflexor Muscle Tone, MAS (Right) |
| Q404ObsDR | - |  |  | SI | Wrist Dorsiflexor Muscle Tone, MAS (Right) DR |
| Q405 | - |  |  | SI | Wrist Ulnar Flexor Muscle Tone, MAS (Right) |
| Q405ObsDR | - |  |  | SI | Wrist Ulnar Flexor Muscle Tone, MAS (Right) DR |
| Q406 | - |  |  | SI | Wrist Radial Flexor Muscle Tone, MAS (Right) |
| Q406ObsDR | - |  |  | SI | Wrist Radial Flexor Muscle Tone, MAS (Right) DR |
| Q407 | - |  |  | SI | Finger Metacarpophalangeal Flexor Muscle Tone, MAS... |
| Q407ObsDR | - |  |  | SI | Finger Metacarpophalangeal Flexor Muscle Tone, MAS... |
| Q408 | - |  |  | SI | Finger Metacarpophalangeal Extensor Muscle Tone, M... |
| Q408ObsDR | - |  |  | SI | Finger Metacarpophalangeal Extensor Muscle Tone, M... |
| Q409 | - |  |  | SI | Finger Proximal Interphalangeal Flexor Muscle Tone... |
| Q409ObsDR | - |  |  | SI | Finger Proximal Interphalangeal Flexor Muscle Tone... |
| Q41 | - |  |  | SI | Adductors |
| Q410 | - |  |  | SI | Finger Proximal Interphalangeal Extensor Muscle To... |
| Q410ObsDR | - |  |  | SI | Finger Proximal Interphalangeal Extensor Muscle To... |
| Q411 | - |  |  | SI | Finger Distal Interphalangeal Flexor Muscle Tone, ... |
| Q411ObsDR | - |  |  | SI | Finger Distal Interphalangeal Flexor Muscle Tone, ... |
| Q412 | - |  |  | SI | Finger Abductor Muscle Tone, MAS (Right) |
| Q412ObsDR | - |  |  | SI | Finger Abductor Muscle Tone, MAS (Right) DR |
| Q413 | - |  |  | SI | Finger Adductor Muscle Tone, MAS (Right) |
| Q413ObsDR | - |  |  | SI | Finger Adductor Muscle Tone, MAS (Right) DR |
| Q414 | - |  |  | SI | Thumb Metacarpophalangeal Flexor Muscle Tone, MAS ... |
| Q414ObsDR | - |  |  | SI | Thumb Metacarpophalangeal Flexor Muscle Tone, MAS ... |
| Q415 | - |  |  | SI | Thumb Metacarpophalangeal Extensor Muscle Tone, MA... |
| Q415ObsDR | - |  |  | SI | Thumb Metacarpophalangeal Extensor Muscle Tone, MA... |
| Q416 | - |  |  | SI | Thumb Proximal Interphalangeal Flexor Muscle Tone,... |
| Q416ObsDR | - |  |  | SI | Thumb Proximal Interphalangeal Flexor Muscle Tone,... |
| Q417 | - |  |  | SI | Thumb Proximal Interphalangeal Extensor Muscle Ton... |
| Q417ObsDR | - |  |  | SI | Thumb Proximal Interphalangeal Extensor Muscle Ton... |
| Q418 | - |  |  | SI | Thumb Abductor Muscle Tone, MAS (Right) |
| Q418ObsDR | - |  |  | SI | Thumb Abductor Muscle Tone, MAS (Right) DR |
| Q419 | - |  |  | SI | Thumb Adductor Muscle Tone, MAS (Right) |
| Q419ObsDR | - |  |  | SI | Thumb Adductor Muscle Tone, MAS (Right) DR |
| Q42 | - |  |  | SI | Pronators |
| Q420 | - |  |  | SI | Thumb Opposer Muscle Tone, MAS (Right) |
| Q420ObsDR | - |  |  | SI | Thumb Opposer Muscle Tone, MAS (Right) DR |
| Q421 | - |  |  | SI | Shoulder Flexor Strength, MRC Scale (Right) |
| Q421ObsDR | - |  |  | SI | Shoulder Flexor Strength, MRC Scale (Right) DR |
| Q422 | - |  |  | SI | Shoulder Flexor Strength, KTMG Scale (Right) |
| Q422ObsDR | - |  |  | SI | Shoulder Flexor Strength, KTMG Scale (Right) DR |
| Q423 | - |  |  | SI | Shoulder Extensor Strength, MRC Scale (Right) |
| Q423ObsDR | - |  |  | SI | Shoulder Extensor Strength, MRC Scale (Right) DR |
| Q424 | - |  |  | SI | Shoulder Extensor Strength, KTMG Scale (Right) |
| Q424ObsDR | - |  |  | SI | Shoulder Extensor Strength, KTMG Scale (Right) DR |
| Q425 | - |  |  | SI | Shoulder Retractor Strength, MRC Scale (Right) |
| Q425ObsDR | - |  |  | SI | Shoulder Retractor Strength, MRC Scale (Right) DR |
| Q426 | - |  |  | SI | Shoulder Retractor Strength, KTMG Scale (Right) |
| Q426ObsDR | - |  |  | SI | Shoulder Retractor Strength, KTMG Scale (Right) DR |
| Q427 | - |  |  | SI | Shoulder Protractor Strength, MRC Scale (Right) |
| Q427ObsDR | - |  |  | SI | Shoulder Protractor Strength, MRC Scale (Right) DR |
| Q428 | - |  |  | SI | Shoulder Protractor Strength, KTMG Scale (Right) |
| Q428ObsDR | - |  |  | SI | Shoulder Protractor Strength, KTMG Scale (Right) D... |
| Q429 | - |  |  | SI | Shoulder Abductor Strength, MRC Scale (Right) |
| Q429ObsDR | - |  |  | SI | Shoulder Abductor Strength, MRC Scale (Right) DR |
| Q43 | - |  |  | SI | Supinators |
| Q430 | - |  |  | SI | Shoulder Abductor Strength, KTMG Scale (Right) |
| Q430ObsDR | - |  |  | SI | Shoulder Abductor Strength, KTMG Scale (Right) DR |
| Q431 | - |  |  | SI | Shoulder Adductor Strength, MRC Scale (Right) |
| Q431ObsDR | - |  |  | SI | Shoulder Adductor Strength, MRC Scale (Right) DR |
| Q432 | - |  |  | SI | Shoulder Adductor Strength, KTMG Scale (Right) |
| Q432ObsDR | - |  |  | SI | Shoulder Adductor Strength, KTMG Scale (Right) DR |
| Q433 | - |  |  | SI | Shoulder Internal Rotator Strength, MRC Scale (Rig... |
| Q433ObsDR | - |  |  | SI | Shoulder Internal Rotator Strength, MRC Scale (Rig... |
| Q434 | - |  |  | SI | Shoulder Internal Rotator Strength, KTMG Scale (Ri... |
| Q434ObsDR | - |  |  | SI | Shoulder Internal Rotator Strength, KTMG Scale (Ri... |
| Q435 | - |  |  | SI | Shoulder External Rotator Strength, MRC Scale (Rig... |
| Q435ObsDR | - |  |  | SI | Shoulder External Rotator Strength, MRC Scale (Rig... |
| Q436 | - |  |  | SI | Shoulder External Rotator Strength, KTMG Scale (Ri... |
| Q436ObsDR | - |  |  | SI | Shoulder External Rotator Strength, KTMG Scale (Ri... |
| Q437 | - |  |  | SI | Elbow Flexor Strength, MRC Scale (Right) |
| Q437ObsDR | - |  |  | SI | Elbow Flexor Strength, MRC Scale (Right) DR |
| Q438 | - |  |  | SI | Elbow Flexor Strength, KTMG Scale (Right) |
| Q438ObsDR | - |  |  | SI | Elbow Flexor Strength, KTMG Scale (Right) DR |
| Q439 | - |  |  | SI | Elbow Extensor Strength, MRC Scale (Right) |
| Q439ObsDR | - |  |  | SI | Elbow Extensor Strength, MRC Scale (Right) DR |
| Q44 | - |  |  | SI | Wrist |
| Q440 | - |  |  | SI | Elbow Extensor Strength, KTMG Scale (Right) |
| Q440ObsDR | - |  |  | SI | Elbow Extensor Strength, KTMG Scale (Right) DR |
| Q441 | - |  |  | SI | Forearm Pronator Strength, MRC Scale (Right) |
| Q441ObsDR | - |  |  | SI | Forearm Pronator Strength, MRC Scale (Right) DR |
| Q442 | - |  |  | SI | Forearm Pronator Strength, KTMG Scale (Right) |
| Q442ObsDR | - |  |  | SI | Forearm Pronator Strength, KTMG Scale (Right) DR |
| Q443 | - |  |  | SI | Forearm Supinator Strength, MRC Scale (Right) |
| Q443ObsDR | - |  |  | SI | Forearm Supinator Strength, MRC Scale (Right) DR |
| Q444 | - |  |  | SI | Forearm Supinator Strength, KTMG Scale (Right) |
| Q444ObsDR | - |  |  | SI | Forearm Supinator Strength, KTMG Scale (Right) DR |
| Q445 | - |  |  | SI | Wrist Palmar Flexor Strength, MRC Scale (Right) |
| Q445ObsDR | - |  |  | SI | Wrist Palmar Flexor Strength, MRC Scale (Right) DR |
| Q446 | - |  |  | SI | Wrist Palmar Flexor Strength, KTMG Scale (Right) |
| Q446ObsDR | - |  |  | SI | Wrist Palmar Flexor Strength, KTMG Scale (Right) D... |
| Q447 | - |  |  | SI | Wrist Dorsiflexor Strength, MRC Scale (Right) |
| Q447ObsDR | - |  |  | SI | Wrist Dorsiflexor Strength, MRC Scale (Right) DR |
| Q448 | - |  |  | SI | Wrist Dorsiflexor Strength, KTMG Scale (Right) |
| Q448ObsDR | - |  |  | SI | Wrist Dorsiflexor Strength, KTMG Scale (Right) DR |
| Q449 | - |  |  | SI | Wrist Ulnar Flexor Strength, MRC Scale (Right) |
| Q449ObsDR | - |  |  | SI | Wrist Ulnar Flexor Strength, MRC Scale (Right) DR |
| Q45 | - |  |  | SI | Plantar flexors |
| Q450 | - |  |  | SI | Wrist Ulnar Flexor Strength, KTMG Scale (Right) |
| Q450ObsDR | - |  |  | SI | Wrist Ulnar Flexor Strength, KTMG Scale (Right) DR |
| Q451 | - |  |  | SI | Wrist Radial Flexor Strength, MRC Scale (Right) |
| Q451ObsDR | - |  |  | SI | Wrist Radial Flexor Strength, MRC Scale (Right) DR |
| Q452 | - |  |  | SI | Wrist Radial Flexor Strength, KTMG Scale (Right) |
| Q452ObsDR | - |  |  | SI | Wrist Radial Flexor Strength, KTMG Scale (Right) D... |
| Q453 | - |  |  | SI | Finger Flexor Strength, MRC Scale (Right) |
| Q453ObsDR | - |  |  | SI | Finger Flexor Strength, MRC Scale (Right) DR |
| Q454 | - |  |  | SI | Finger Flexor Strength, KTMG Scale (Right) |
| Q454ObsDR | - |  |  | SI | Finger Flexor Strength, KTMG Scale (Right) DR |
| Q455 | - |  |  | SI | Finger Extensor Strength, MRC Scale (Right) |
| Q455ObsDR | - |  |  | SI | Finger Extensor Strength, MRC Scale (Right) DR |
| Q456 | - |  |  | SI | Finger Extensor Strength, KTMG Scale (Right) |
| Q456ObsDR | - |  |  | SI | Finger Extensor Strength, KTMG Scale (Right) DR |
| Q457 | - |  |  | SI | Finger Proximal Interphalangeal Flexor Strength, M... |
| Q457ObsDR | - |  |  | SI | Finger Proximal Interphalangeal Flexor Strength, M... |
| Q458 | - |  |  | SI | Finger Proximal Interphalangeal Flexor Strength, K... |
| Q458ObsDR | - |  |  | SI | Finger Proximal Interphalangeal Flexor Strength, K... |
| Q459 | - |  |  | SI | Finger Proximal Interphalangeal Extensor Strength,... |
| Q459ObsDR | - |  |  | SI | Finger Proximal Interphalangeal Extensor Strength,... |
| Q46 | - |  |  | SI | Dorsiflexors |
| Q460 | - |  |  | SI | Finger Proximal Interphalangeal Extensor Strength,... |
| Q460ObsDR | - |  |  | SI | Finger Proximal Interphalangeal Extensor Strength,... |
| Q461 | - |  |  | SI | Fingers Distal Interphalangeal Flexor Strength, MR... |
| Q461ObsDR | - |  |  | SI | Fingers Distal Interphalangeal Flexor Strength, MR... |
| Q462 | - |  |  | SI | Finger Distal Interphalangeal Flexor Strength, KTM... |
| Q462ObsDR | - |  |  | SI | Finger Distal Interphalangeal Flexor Strength, KTM... |
| Q463 | - |  |  | SI | Finger Abductor Strength, MRC Scale (Right) |
| Q463ObsDR | - |  |  | SI | Finger Abductor Strength, MRC Scale (Right) DR |
| Q464 | - |  |  | SI | Finger Abductor Strength, KTMG Scale (Right) |
| Q464ObsDR | - |  |  | SI | Finger Abductor Strength, KTMG Scale (Right) DR |
| Q465 | - |  |  | SI | Fingers Adductor Strength, MRC Scale (Right) |
| Q465ObsDR | - |  |  | SI | Fingers Adductor Strength, MRC Scale (Right) DR |
| Q466 | - |  |  | SI | Finger Adductor Strength, KTMG Scale (Right) |
| Q466ObsDR | - |  |  | SI | Finger Adductor Strength, KTMG Scale (Right) DR |
| Q467 | - |  |  | SI | Thumb Flexor Strength, MRC Scale (Right) |
| Q467ObsDR | - |  |  | SI | Thumb Flexor Strength, MRC Scale (Right) DR |
| Q468 | - |  |  | SI | Thumb Flexor Strength, KTMG Scale (Right) |
| Q468ObsDR | - |  |  | SI | Thumb Flexor Strength, KTMG Scale (Right) DR |
| Q469 | - |  |  | SI | Thumb Extensor Strength, MRC Scale (Right) |
| Q469ObsDR | - |  |  | SI | Thumb Extensor Strength, MRC Scale (Right) DR |
| Q47 | - |  |  | SI | Ulnar Flexors |
| Q470 | - |  |  | SI | Thumb Extensor Strength, KTMG Scale (Right) |
| Q470ObsDR | - |  |  | SI | Thumb Extensor Strength, KTMG Scale (Right) DR |
| Q471 | - |  |  | SI | Thumb Interphalangeal Flexor Strength, MRC Scale (... |
| Q471ObsDR | - |  |  | SI | Thumb Interphalangeal Flexor Strength, MRC Scale (... |
| Q472 | - |  |  | SI | Thumb Interphalangeal Flexor Strength, KTMG Scale ... |
| Q472ObsDR | - |  |  | SI | Thumb Interphalangeal Flexor Strength, KTMG Scale ... |
| Q473 | - |  |  | SI | Thumb Interphalangeal Extensor Strength, MRC Scale... |
| Q473ObsDR | - |  |  | SI | Thumb Interphalangeal Extensor Strength, MRC Scale... |
| Q474 | - |  |  | SI | Thumb Interphalangeal Extensor Strength, KTMG Scal... |
| Q474ObsDR | - |  |  | SI | Thumb Interphalangeal Extensor Strength, KTMG Scal... |
| Q475 | - |  |  | SI | Thumb Abductor Strength, MRC Scale (Right) |
| Q475ObsDR | - |  |  | SI | Thumb Abductor Strength, MRC Scale (Right) DR |
| Q476 | - |  |  | SI | Thumb Abductor Strength, KTMG Scale (Right) |
| Q476ObsDR | - |  |  | SI | Thumb Abductor Strength, KTMG Scale (Right) DR |
| Q477 | - |  |  | SI | Thumb Adductor Strength, MRC Scale (Right) |
| Q477ObsDR | - |  |  | SI | Thumb Adductor Strength, MRC Scale (Right) DR |
| Q478 | - |  |  | SI | Thumb Adductor Strength, KTMG Scale (Right) |
| Q478ObsDR | - |  |  | SI | Thumb Adductor Strength, KTMG Scale (Right) DR |
| Q479 | - |  |  | SI | Thumb Opposer Strength, MRC Scale (Right) |
| Q479ObsDR | - |  |  | SI | Thumb Opposer Strength, MRC Scale (Right) DR |
| Q48 | - |  |  | SI | Radial Flexors |
| Q480 | - |  |  | SI | Thumb Opposer Strength, KTMG Scale (Right) |
| Q480ObsDR | - |  |  | SI | Thumb Opposer Strength, KTMG Scale (Right) DR |
| Q481 | - |  |  | SI | Finger Proximal Interphalangeal Flexor Spasticity,... |
| Q481ObsDR | - |  |  | SI | Finger Proximal Interphalangeal Flexor Spasticity,... |
| Q482 | - |  |  | SI | Wrist Radial Flexor Muscle Tone, MAS (Left) |
| Q482ObsDR | - |  |  | SI | Wrist Radial Flexor Muscle Tone, MAS (Left) DR |
| Q483 | - |  |  | SI | Boyd & Graham's Modified Tardieu Scale (MTS) quant... |
| Q484 | - |  |  | SI | Grading is always performed at the same time of da... |
| Q485 | - |  |  | SI | The MTS is administered by applying passive stretc... |
| Q486 | - |  |  | SI | • The first stretch is ‘as slow as possible’ (refe... |
| Q487 | - |  |  | SI | • The second stretch is either at the ‘speed of th... |
| Q488 | - |  |  | SI | and is used to determine both the angle of muscle ... |
| Q489 | - |  |  | SI | The angle at which the muscle reaction occurs is t... |
| Q49 | - |  |  | SI | Fingers |
| Q490 | - |  |  | SI | where 0 indicates ‘no resistance through the cours... |
| Q491 | - |  |  | SI | V (Velocity to stretch) |
| Q492 | - |  |  | SI | V1 - As slow as possible |
| Q493 | - |  |  | SI | V2 - Speed of the limb segment falling |
| Q494 | - |  |  | SI | V3 - As fast as possible (>natural drop) |
| Q495 | - |  |  | SI | R1 (Angle of catch seen at velocity V2 or V3) |
| Q496 | - |  |  | SI | R2 (Full range of motion achieved when muscle is a... |
| Q497 | - |  |  | SI | R2-R1 (Indicates the level of dynamic contracture ... |
| Q498 | - |  |  | SI | By moving the limb at different velocities, the re... |
| Q499 | - |  |  | SI | A large difference between R1 & R2 values in the o... |
| Q50 | - |  |  | SI | Metacarpophalangeal Flexors |
| Q500 | - |  |  | SI | A small difference in the R1 & R2 measurement in t... |
| Q501 | - |  |  | SI | Scale reference: |
| Q502 | - |  |  | SI | Boyd R, Graham K. Objective measurement of clinica... |
| Q503 | - |  |  | SI | The Modified Ashworth scale (MAS) measures resista... |
| Q504 | - |  |  | SI | • Place the patient in a supine position. |
| Q505 | - |  |  | SI | • If testing a muscle that primarily flexes a join... |
| Q506 | - |  |  | SI | • If testing a muscle that primarily extends a joi... |
| Q507 | - |  |  | SI | • Score based on the classification |
| Q508 | - |  |  | SI | Scale Reference: |
| Q509 | - |  |  | SI | Bohannon RW, Smith MB. Interrater Reliability of a... |
| Q51 | - |  |  | SI | Metacarpophalangeal Extensors |
| Q510 | - |  |  | SI | MMT is a standard set of assessments used to measu... |
| Q511 | - |  |  | SI | There are two common grading systems used to evalu... |
| Q512 | - |  |  | SI | • Medical Research Centre (MRC) Muscle Strength Sc... |
| Q513 | - |  |  | SI | • Key to Muscle Grading (KTMG) |
| Q514 | - |  |  | SI | The scale in this tool combines the two scales so ... |
| Q515 | - |  |  | SI | • Make sure to communicate with the patient all th... |
| Q516 | - |  |  | SI | • Work with the non-dominant (or non-injured) side... |
| Q517 | - |  |  | SI | • Remind your patient to breathe naturally during ... |
| Q518 | - |  |  | SI | • Make sure the patient is dressed in loose clothi... |
| Q519 | - |  |  | SI | • Place the patient in an adequately supported pos... |
| Q52 | - |  |  | SI | Proximal Interphalangeal Extensors |
| Q520 | - |  |  | SI | • Always test first in an anti-gravity position. I... |
| Q521 | - |  |  | SI | • Resistance needs to be applied directly opposite... |
| Q522 | - |  |  | SI | • Plan out the test first, testing all the muscles... |
| Q523 | - |  |  | SI | • Always provide adequate stabilisation to unrelat... |
| Q524 | - |  |  | SI | stabilisation of the shoulder will prevent extra m... |
| Q525 | - |  |  | SI | • Always test both sides in order to compare stren... |
| Q526 | - |  |  | SI | • Avoid doing jerking movements when applying resi... |
| Q527 | - |  |  | SI | • Discontinue testing if patient complains of pain... |
| Q528 | - |  |  | SI | Medical Research Council (MRC) Scale for Muscle St... |
| Q529 | - |  |  | SI | Description |
| Q53 | - |  |  | SI | Distal Interphalangeal Flexors |
| Q530 | - |  |  | SI | 5 |
| Q531 | - |  |  | SI | Normal power |
| Q532 | - |  |  | SI | 4 |
| Q533 | - |  |  | SI | Active movement against gravity and resistance |
| Q534 | - |  |  | SI | 3 |
| Q535 | - |  |  | SI | Active movement against gravity |
| Q536 | - |  |  | SI | 2 |
| Q537 | - |  |  | SI | Active movement, with gravity eliminated |
| Q538 | - |  |  | SI | 1 |
| Q539 | - |  |  | SI | Flicker or trace of contraction |
| Q54 | - |  |  | SI | Distal Interphalangeal Extensors |
| Q540 | - |  |  | SI | 0 |
| Q541 | - |  |  | SI | No contraction |
| Q542 | - |  |  | SI | Scale reference - Medical Research Centre (MRC) Mu... |
| Q543 | - |  |  | SI | Medical Research Council. Aids to the Investigatio... |
| Q544 | - |  |  | SI | Key to Muscle Grading (KTMG) |
| Q545 | - |  |  | SI | Explanation / Description |
| Q546 | - |  |  | SI | 0: Zero |
| Q547 | - |  |  | SI | No contraction felt or seen in the muscle |
| Q548 | - |  |  | SI | 1: Trace (T) |
| Q549 | - |  |  | SI | Tendon becomes prominent or feeble contraction fel... |
| Q55 | - |  |  | SI | Abductors |
| Q550 | - |  |  | SI | 2+: Poor + (P+) |
| Q551 | - |  |  | SI | Moves through partial ROM against gravity (support... |
| Q552 | - |  |  | SI | 2+: Poor + (P+) |
| Q553 | - |  |  | SI | Holds against slight pressure in test position (su... |
| Q554 | - |  |  | SI | 2-: Poor - (P-) |
| Q555 | - |  |  | SI | Moves through partial ROM (supported in horizontal... |
| Q556 | - |  |  | SI | 2: Poor (P) |
| Q557 | - |  |  | SI | Movement through complete ROM for the muscle being... |
| Q558 | - |  |  | SI | 3+: Fair + (F+) |
| Q559 | - |  |  | SI | Holds test position in anti-gravity position again... |
| Q56 | - |  |  | SI | Adductors |
| Q560 | - |  |  | SI | 3-: Fair - (F-) |
| Q561 | - |  |  | SI | Gradual release from test position occurs in anti-... |
| Q562 | - |  |  | SI | 3: Fair (F) |
| Q563 | - |  |  | SI | Holds test position in anti-gravity position (no a... |
| Q564 | - |  |  | SI | 4+: Good + (G+) |
| Q565 | - |  |  | SI | Holds test position in anti-gravity position again... |
| Q566 | - |  |  | SI | 4-: Good - (G-) |
| Q567 | - |  |  | SI | Holds test position in anti-gravity position again... |
| Q568 | - |  |  | SI | 4: Good (G) |
| Q569 | - |  |  | SI | Holds test position in anti-gravity position again... |
| Q57 | - |  |  | SI | Thumb |
| Q570 | - |  |  | SI | 5: Normal (N) |
| Q571 | - |  |  | SI | Holds test position in anti-gravity position again... |
| Q572 | - |  |  | SI | Scale reference - Key to Muscle Grading |
| Q573 | - |  |  | SI | Kendall, F. P., McCreary, E. K., Provance, P. G., ... |
| Q574 | - |  |  | SI | Thumb Abductor Spasticity, MTS (Left) |
| Q574ObsDR | - |  |  | SI | Thumb Abductor Spasticity, MTS (Left) DR |
| Q575 | - |  |  | SI | Thumb Adductor Spasticity, MTS (Left) |
| Q575ObsDR | - |  |  | SI | Thumb Adductor Spasticity, MTS (Left) DR |
| Q576 | - |  |  | SI | finger abductors, MTS (Left) |
| Q576ObsDR | - |  |  | SI | finger abductors, MTS (Left) DR |
| Q577 | - |  |  | SI | Finger Adductor Muscle Tone, MTS (Left) |
| Q577ObsDR | - |  |  | SI | Finger Adductor Muscle Tone, MTS (Left) DR |
| Q578 | - |  |  | SI | Forearm Pronator Strength, MRC Scale (Left) |
| Q578ObsDR | - |  |  | SI | Forearm Pronator Strength, MRC Scale (Left) DR |
| Q579 | - |  |  | SI | R1 shoulder internal rotation (right) |
| Q58 | - |  |  | SI | Metacarpophalangeal Flexors |
| Q580 | - |  |  | SI | R2 shoulder internal rotation (right) |
| Q581 | - |  |  | SI | R2-R1 shoulder internal rotation (right) |
| Q582 | - |  |  | SI | Proximal Interphalangeal Flexors |
| Q583 | - |  |  | SI | Opposers |
| Q584 | - |  |  | SI | Forearm Supinator Muscle Tone, MAS (Right) |
| Q584ObsDR | - |  |  | SI | Forearm Supinator Muscle Tone, MAS (Right) DR |
| Q585 | - |  |  | SI | Finger Proximal Interphalangeal Flexor Muscle Tone... |
| Q585ObsDR | - |  |  | SI | Finger Proximal Interphalangeal Flexor Muscle Tone... |
| Q586 | - |  |  | SI | Finger Distal Interphalangeal Extensor Muscle Tone... |
| Q586ObsDR | - |  |  | SI | Finger Distal Interphalangeal Extensor Muscle Tone... |
| Q587 | - |  |  | SI | Finger Distal Interphalangeal Extensor Strength, M... |
| Q587ObsDR | - |  |  | SI | Finger Distal Interphalangeal Extensor Strength, M... |
| Q588 | - |  |  | SI | Shoulder Internal Rotator  Muscle Tone, MAS (Right... |
| Q588ObsDR | - |  |  | SI | Shoulder Internal Rotator  Muscle Tone, MAS (Right... |
| Q589 | - |  |  | SI | Finger Distal Interphalangeal Extensor Strength, K... |
| Q589ObsDR | - |  |  | SI | Finger Distal Interphalangeal Extensor Strength, K... |
| Q59 | - |  |  | SI | Metacarpophalangeal Extensors |
| Q590 | - |  |  | SI | Joint / Muscle group |
| Q591 | - |  |  | SI | Muscle |
| Q592 | - |  |  | SI | Please refer to the full view of the Spasticity an... |
| Q60 | - |  |  | SI | Proximal Interphalangeal Flexors |
| Q61 | - |  |  | SI | Proximal Interphalangeal Extensors |
| Q62 | - |  |  | SI | Abductors |
| Q63 | - |  |  | SI | Abductors |
| Q64 | - |  |  | SI | Comments |
| Q65 | - |  |  | SI | R1 shoulder flexors (left) |
| Q66 | - |  |  | SI | R1 shoulder extensors (left) |
| Q67 | - |  |  | SI | R1 shoulder retractors (left) |
| Q68 | - |  |  | SI | R1 shoulder protractors (left) |
| Q69 | - |  |  | SI | R1 shoulder abductors (left) |
| Q70 | - |  |  | SI | R1 shoulder adductors (left) |
| Q71 | - |  |  | SI | R1 shoulder internal rotation (left) |
| Q72 | - |  |  | SI | R1 shoulder external rotation (left) |
| Q73 | - |  |  | SI | R1 elbow flexors (left) |
| Q74 | - |  |  | SI | R1 elbow extensors (left) |
| Q75 | - |  |  | SI | R1 forearm pronators (left) |
| Q76 | - |  |  | SI | R1 forearm supinators (left) |
| Q77 | - |  |  | SI | R1 wrist palmar flexors (left) |
| Q78 | - |  |  | SI | R1 wrist dorsiflexors (left) |
| Q79 | - |  |  | SI | R1 ulnar flexors (left) |
| Q80 | - |  |  | SI | R1 radial flexors (left) |
| Q81 | - |  |  | SI | R1 finger metacarpophalangeal flexors (left) |
| Q82 | - |  |  | SI | R1 finger metacarpophalangeal extensors (left) |
| Q83 | - |  |  | SI | R1 finger proximal  interphalangeal flexors (left) |
| Q84 | - |  |  | SI | R1 finger proximal interphalangeal extensors (left... |
| Q85 | - |  |  | SI | R1 finger distal interphalangeal flexors (left) |
| Q86 | - |  |  | SI | R1 finger distal interphalangeal extensors (left) |
| Q87 | - |  |  | SI | R1 finger distal interphalangeal extensors (left) |
| Q88 | - |  |  | SI | R1 finger abductors (left) |
| Q89 | - |  |  | SI | R1 finger adductors (left) |
| Q90 | - |  |  | SI | R1 finger metacarpophalangeal flexors (left) |
| Q91 | - |  |  | SI | R1 thumb metacarpophalangeal extensors (left) |
| Q92 | - |  |  | SI | R1 thumb proximal  interphalangeal flexors (left) |
| Q93 | - |  |  | SI | R1 thumb proximal interphalangeal extensors (left) |
| Q94 | - |  |  | SI | R1 thumb abductors (left) |
| Q95 | - |  |  | SI | R1 thumb adductors (left) |
| Q96 | - |  |  | SI | R1 thumb opposers (left) |
| Q97 | - |  |  | SI | R2 shoulder flexors (left) |
| Q98 | - |  |  | SI | R2 shoulder extensors (left) |
| Q99 | - |  |  | SI | R2 shoulder retractors (left) |
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