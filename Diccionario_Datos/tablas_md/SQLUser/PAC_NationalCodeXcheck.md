# SQLUser.PAC_NationalCodeXcheck

**Schema:** SQLUser
**Columnas:** 392
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| XCHECK_RowId | bigint | PK |  | NO | - |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Type of test |
| Q04 | - |  |  | SI | Side of body affected |
| Q05 | - |  |  | SI | Body Region - Left / Right |
| Q06 | - |  |  | SI | Light Touch |
| Q07 | - |  |  | SI | Temperature |
| Q08 | - |  |  | SI | Pinprick |
| Q09 | - |  |  | SI | Pressure |
| Q10 | - |  |  | SI | Tactile Localisation |
| Q100 | - |  |  | SI | Knee - pinprick - left |
| Q101 | - |  |  | SI | Knee - pinprick - right |
| Q102 | - |  |  | SI | Ankle - pinprick - left |
| Q103 | - |  |  | SI | Ankle - pinprick - right |
| Q104 | - |  |  | SI | Foot - pinprick - left |
| Q105 | - |  |  | SI | Foot - pinprick - right |
| Q106 | - |  |  | SI | Face - pressure - left |
| Q107 | - |  |  | SI | Face - pressure - right |
| Q108 | - |  |  | SI | Trunk - pressure - left |
| Q109 | - |  |  | SI | Trunk - pressure - right |
| Q11 | - |  |  | SI | Only complete if Pressure = 2: 2: Normal, otherwis... |
| Q110 | - |  |  | SI | Shoulder - pressure - left |
| Q111 | - |  |  | SI | Shoulder - pressure - right |
| Q112 | - |  |  | SI | Elbow - pressure - left |
| Q113 | - |  |  | SI | Elbow - pressure - right |
| Q114 | - |  |  | SI | Wrist - pressure - left |
| Q115 | - |  |  | SI | Wrist - pressure - right |
| Q116 | - |  |  | SI | Hand - pressure - left |
| Q117 | - |  |  | SI | Hand - pressure - right |
| Q118 | - |  |  | SI | Knee - pressure - left |
| Q119 | - |  |  | SI | Knee - pressure - right |
| Q12 | - |  |  | SI | Body Region |
| Q120 | - |  |  | SI | Ankle - pressure - left |
| Q121 | - |  |  | SI | Ankle - pressure - right |
| Q122 | - |  |  | SI | Foot - pressure - left |
| Q123 | - |  |  | SI | Foot - pressure - right |
| Q124 | - |  |  | SI | Face - tactile localisation - left |
| Q125 | - |  |  | SI | Face - tactile localisation - right |
| Q126 | - |  |  | SI | Trunk - tactile localisation - left |
| Q127 | - |  |  | SI | Trunk - tactile localisation - right |
| Q128 | - |  |  | SI | Shoulder - tactile localisation - left |
| Q129 | - |  |  | SI | Shoulder - tactile localisation - right |
| Q13 | - |  |  | SI | Bilateral Simultaneous Touch |
| Q130 | - |  |  | SI | Elbow - tactile localisation - left |
| Q131 | - |  |  | SI | Elbow - tactile localisation - right |
| Q132 | - |  |  | SI | Wrist - tactile localisation - left |
| Q133 | - |  |  | SI | Wrist - tactile localisation - right |
| Q134 | - |  |  | SI | Hand - tactile localisation - left |
| Q135 | - |  |  | SI | Hand - tactile localisation - right |
| Q136 | - |  |  | SI | Knee - tactile localisation - left |
| Q137 | - |  |  | SI | Knee - tactile localisation - right |
| Q138 | - |  |  | SI | Ankle - tactile localisation - left |
| Q139 | - |  |  | SI | Ankle - tactile localisation - right |
| Q14 | - |  |  | SI | Only complete if Pressure = 2: 2: Normal, otherwis... |
| Q140 | - |  |  | SI | Foot - tactile localisation - left |
| Q141 | - |  |  | SI | Foot - tactile localisation - right |
| Q142 | - |  |  | SI | Face - bilateral simultaneous touch |
| Q143 | - |  |  | SI | Trunk - bilateral simultaneous touch |
| Q144 | - |  |  | SI | Shoulder - bilateral simultaneous touch |
| Q145 | - |  |  | SI | Elbow - bilateral simultaneous touch |
| Q146 | - |  |  | SI | Wrist - bilateral simultaneous touch |
| Q147 | - |  |  | SI | Hand - bilateral simultaneous touch |
| Q148 | - |  |  | SI | Knee - bilateral simultaneous touch |
| Q149 | - |  |  | SI | Ankle - bilateral simultaneous touch |
| Q15 | - |  |  | SI | Proprioception |
| Q150 | - |  |  | SI | Foot - bilateral simultaneous touch |
| Q151 | - |  |  | SI | Shoulder - proprioception |
| Q152 | - |  |  | SI | Elbow - proprioception |
| Q153 | - |  |  | SI | Wrist - proprioception |
| Q154 | - |  |  | SI | Hand - proprioception |
| Q155 | - |  |  | SI | Hip proprioception |
| Q156 | - |  |  | SI | Knee - proprioception |
| Q157 | - |  |  | SI | Ankle - proprioception |
| Q158 | - |  |  | SI | Stereognosis |
| Q159 | - |  |  | SI | 10 cent coin |
| Q16 | - |  |  | SI | Face |
| Q160 | - |  |  | SI | 5 cent coin |
| Q161 | - |  |  | SI | 50 cent coin |
| Q162 | - |  |  | SI | Biro |
| Q163 | - |  |  | SI | Pencil |
| Q164 | - |  |  | SI | Comb |
| Q165 | - |  |  | SI | Scissors |
| Q166 | - |  |  | SI | Sponge |
| Q167 | - |  |  | SI | Flannel |
| Q168 | - |  |  | SI | Cup |
| Q169 | - |  |  | SI | Glass |
| Q17 | - |  |  | SI | Face |
| Q170 | - |  |  | SI | General |
| Q171 | - |  |  | SI | • The patient should be assessed in sitting and in... |
| Q172 | - |  |  | SI | distractions. Each test is described and demonstra... |
| Q173 | - |  |  | SI | • The body area to be tested is as marked on the b... |
| Q174 | - |  |  | SI | movement, whenever he or she feels the test sensat... |
| Q175 | - |  |  | SI | • Each part of the body is assessed three times fo... |
| Q176 | - |  |  | SI | • Presence of a reflex does not count as awareness... |
| Q177 | - |  |  | SI | Tactile Sensation |
| Q178 | - |  |  | SI | Equipment required: |
| Q179 | - |  |  | SI | Blindfold, cotton wool ball, neurotip, two test tu... |
| Q18 | - |  |  | SI | Trunk |
| Q180 | - |  |  | SI | Scoring criteria |
| Q181 | - |  |  | SI | 0 Absent: |
| Q182 | - |  |  | SI | Fails to identify the test sensation on three occa... |
| Q183 | - |  |  | SI | 1 Impaired: |
| Q184 | - |  |  | SI | Identifies the test sensation, but not on all thre... |
| Q185 | - |  |  | SI | 2 Normal: |
| Q186 | - |  |  | SI | Correctly identifies the test sensation on all thr... |
| Q187 | - |  |  | SI | 9 Unable to test |
| Q188 | - |  |  | SI | • Light Touch: |
| Q189 | - |  |  | SI | Touch, not brush, the skin lightly with a cotton w... |
| Q19 | - |  |  | SI | Trunk |
| Q190 | - |  |  | SI | • Pressure: |
| Q191 | - |  |  | SI | Press the skin just enough to deform the skin cont... |
| Q192 | - |  |  | SI | • Pinprick: |
| Q193 | - |  |  | SI | Prick the skin with a neurotip, maintaining even p... |
| Q194 | - |  |  | SI | • Temperature: |
| Q195 | - |  |  | SI | Touch the skin with the side of one of two test tu... |
| Q196 | - |  |  | SI | • Tactile localisation: |
| Q197 | - |  |  | SI | Only test those areas on which the patient has sco... |
| Q198 | - |  |  | SI | and ask the patient to point to the exact spot tha... |
| Q199 | - |  |  | SI | • Bilateral simultaneous touch: |
| Q20 | - |  |  | SI | Shoulder |
| Q200 | - |  |  | SI | Touch corresponding sites on one or both sides of ... |
| Q201 | - |  |  | SI | on pressure section. Record all others as 9. |
| Q202 | - |  |  | SI | Kinaesthetic Sensations / Proprioception |
| Q203 | - |  |  | SI | Equipment required: |
| Q204 | - |  |  | SI | Blindfold. |
| Q205 | - |  |  | SI | • All three aspects of movement are tested: apprec... |
| Q206 | - |  |  | SI | The limb on the affected side of the body is suppo... |
| Q207 | - |  |  | SI | The patient is asked to mirror the change of movem... |
| Q208 | - |  |  | SI | • The upper limb is tested in sitting, and the low... |
| Q209 | - |  |  | SI | Scoring Guide |
| Q21 | - |  |  | SI | Shoulder |
| Q210 | - |  |  | SI | 0 Absent: |
| Q211 | - |  |  | SI | No appreciation of movement taking place. |
| Q212 | - |  |  | SI | 1 Appreciation of movement taking place: |
| Q213 | - |  |  | SI | Patient indicates on each movement that a movement... |
| Q214 | - |  |  | SI | 2 Direction of movement sense: |
| Q215 | - |  |  | SI | Patient is able to appreciate and mirror the direc... |
| Q216 | - |  |  | SI | 3 Joint position sense: |
| Q217 | - |  |  | SI | Accurately mirrors the test movement to within 10°... |
| Q218 | - |  |  | SI | 9 Unable to test |
| Q219 | - |  |  | SI | Stereognosis |
| Q22 | - |  |  | SI | Elbow |
| Q220 | - |  |  | SI | Equipment required: |
| Q221 | - |  |  | SI | Blindfold, 2p coin, 10p coin, 50p coin, biro (scor... |
| Q222 | - |  |  | SI | • The object is placed in the patient's hand for a... |
| Q223 | - |  |  | SI | The object may be moved around the affected hand b... |
| Q224 | - |  |  | SI | Scoring for each object |
| Q225 | - |  |  | SI | 2 Normal: |
| Q226 | - |  |  | SI | Item is correctly named or matched. |
| Q227 | - |  |  | SI | 1 Impaired: |
| Q228 | - |  |  | SI | Some features of object identified or attempts at ... |
| Q229 | - |  |  | SI | 0 Absent: |
| Q23 | - |  |  | SI | Elbow |
| Q230 | - |  |  | SI | Unable to identify the object in any manner. |
| Q231 | - |  |  | SI | 9 Unable to test |
| Q232 | - |  |  | SI | Trunk - Left |
| Q233 | - |  |  | SI | Trunk - Right |
| Q234 | - |  |  | SI | Trunk - pinprick - left |
| Q235 | - |  |  | SI | Face - light touch - left |
| Q236 | - |  |  | SI | Face - light touch - right |
| Q237 | - |  |  | SI | Trunk - light touch - left |
| Q238 | - |  |  | SI | Trunk - light touch - right |
| Q239 | - |  |  | SI | Shoulder - light touch - left |
| Q24 | - |  |  | SI | Wrist |
| Q240 | - |  |  | SI | Shoulder - light touch - right |
| Q241 | - |  |  | SI | Elbow - light touch - left |
| Q242 | - |  |  | SI | Elbow - light touch - right |
| Q243 | - |  |  | SI | Wrist - light touch - left |
| Q244 | - |  |  | SI | Wrist - light touch - right |
| Q245 | - |  |  | SI | Hand - light touch - left |
| Q246 | - |  |  | SI | Hand - light touch - right |
| Q247 | - |  |  | SI | Knee - light touch - left |
| Q248 | - |  |  | SI | Knee - light touch - right |
| Q249 | - |  |  | SI | Ankle - light touch - left |
| Q25 | - |  |  | SI | Wrist |
| Q250 | - |  |  | SI | Ankle - light touch - right |
| Q251 | - |  |  | SI | Foot - light touch - left |
| Q252 | - |  |  | SI | Foot - light touch - right |
| Q253 | - |  |  | SI | Face - temperature - left |
| Q254 | - |  |  | SI | Face - temperature - right |
| Q255 | - |  |  | SI | Trunk - temperature - left |
| Q256 | - |  |  | SI | Trunk - temperature - right |
| Q257 | - |  |  | SI | Shoulder - temperature - left |
| Q258 | - |  |  | SI | Shoulder - temperature - right |
| Q259 | - |  |  | SI | Elbow - temperature - left |
| Q26 | - |  |  | SI | Hand |
| Q260 | - |  |  | SI | Elbow - temperature - right |
| Q261 | - |  |  | SI | Wrist - temperature - left |
| Q262 | - |  |  | SI | Wrist - temperature - right |
| Q263 | - |  |  | SI | Hand - temperature - left |
| Q264 | - |  |  | SI | Hand - temperature - right |
| Q265 | - |  |  | SI | Knee - temperature - left |
| Q266 | - |  |  | SI | Knee - temperature -  right |
| Q267 | - |  |  | SI | Ankle - temperature - left |
| Q268 | - |  |  | SI | Ankle - temperature - right |
| Q269 | - |  |  | SI | Foot - temperature - left |
| Q27 | - |  |  | SI | Hand |
| Q270 | - |  |  | SI | Foot - temperature - right |
| Q271 | - |  |  | SI | Face - pinprick - left |
| Q272 | - |  |  | SI | Face - pinprick - right |
| Q273 | - |  |  | SI | Trunk - pinprick - left |
| Q274 | - |  |  | SI | Trunk - pinprick - right |
| Q275 | - |  |  | SI | Shoulder - pinprick - left |
| Q276 | - |  |  | SI | Shoulder - pinprick - right |
| Q277 | - |  |  | SI | Elbow - pinprick - left |
| Q278 | - |  |  | SI | Elbow - pinprick - right |
| Q279 | - |  |  | SI | Wrist - pinprick - left |
| Q28 | - |  |  | SI | Hip |
| Q280 | - |  |  | SI | Wrist - pinprick - right |
| Q281 | - |  |  | SI | Hand - pinprick - left |
| Q282 | - |  |  | SI | Hand - pinprick - right |
| Q283 | - |  |  | SI | Knee - pinprick - left |
| Q284 | - |  |  | SI | Knee - pinprick - right |
| Q285 | - |  |  | SI | Ankle - pinprick - left |
| Q286 | - |  |  | SI | Ankle - pinprick - right |
| Q287 | - |  |  | SI | Foot - pinprick - left |
| Q288 | - |  |  | SI | Foot - pinprick - right |
| Q289 | - |  |  | SI | Face - pressure - left |
| Q29 | - |  |  | SI | Knee |
| Q290 | - |  |  | SI | Face - pressure - right |
| Q291 | - |  |  | SI | Body Chart |
| Q292 | - |  |  | SI | Trunk - pressure - left |
| Q293 | - |  |  | SI | Trunk - pressure - right |
| Q294 | - |  |  | SI | Shoulder - pressure - left |
| Q295 | - |  |  | SI | Shoulder - pressure - right |
| Q296 | - |  |  | SI | Elbow - pressure - left |
| Q297 | - |  |  | SI | Elbow - pressure - right |
| Q298 | - |  |  | SI | Wrist - pressure - left |
| Q299 | - |  |  | SI | Wrist - pressure - right |
| Q30 | - |  |  | SI | Knee |
| Q300 | - |  |  | SI | Hand - pressure - left |
| Q301 | - |  |  | SI | Hand - pressure - right |
| Q302 | - |  |  | SI | Knee - pressure - left |
| Q303 | - |  |  | SI | Knee - pressure - right |
| Q304 | - |  |  | SI | Ankle - pressure - left |
| Q305 | - |  |  | SI | Ankle - pressure - right |
| Q306 | - |  |  | SI | Foot - pressure - left |
| Q307 | - |  |  | SI | Foot - pressure - right |
| Q308 | - |  |  | SI | Face - tactile localisation - left |
| Q309 | - |  |  | SI | Face - tactile localisation - right |
| Q31 | - |  |  | SI | Ankle |
| Q310 | - |  |  | SI | Trunk - tactile localisation - left |
| Q311 | - |  |  | SI | Trunk - tactile localisation - right |
| Q312 | - |  |  | SI | Shoulder - tactile localisation - left |
| Q313 | - |  |  | SI | Shoulder - tactile localisation - right |
| Q314 | - |  |  | SI | Elbow - tactile localisation - left |
| Q315 | - |  |  | SI | Elbow - tactile localisation - right |
| Q316 | - |  |  | SI | Wrist - tactile localisation - left |
| Q317 | - |  |  | SI | Wrist - tactile localisation - right |
| Q318 | - |  |  | SI | Hand - tactile localisation - left |
| Q319 | - |  |  | SI | Hand - tactile localisation - right |
| Q32 | - |  |  | SI | Ankle |
| Q320 | - |  |  | SI | Knee - tactile localisation - left |
| Q321 | - |  |  | SI | Knee - tactile localisation - right |
| Q322 | - |  |  | SI | Ankle - tactile localisation - left |
| Q323 | - |  |  | SI | Ankle - tactile localisation - right |
| Q324 | - |  |  | SI | Foot - tactile localisation - left |
| Q325 | - |  |  | SI | Foot - tactile localisation - right |
| Q326 | - |  |  | SI | Face - bilateral simultaneous touch |
| Q327 | - |  |  | SI | Trunk - bilateral simultaneous touch |
| Q328 | - |  |  | SI | Shoulder - bilateral simultaneous touch |
| Q329 | - |  |  | SI | Elbow - bilateral simultaneous touch |
| Q33 | - |  |  | SI | Foot |
| Q330 | - |  |  | SI | Wrist - bilateral simultaneous touch |
| Q331 | - |  |  | SI | Hand - bilateral simultaneous touch |
| Q332 | - |  |  | SI | Knee - bilateral simultaneous touch |
| Q333 | - |  |  | SI | Ankle - bilateral simultaneous touch |
| Q334 | - |  |  | SI | Foot - bilateral simultaneous touch |
| Q335 | - |  |  | SI | Shoulder - proprioception |
| Q336 | - |  |  | SI | Elbow - proprioception |
| Q337 | - |  |  | SI | Wrist - proprioception |
| Q338 | - |  |  | SI | Hand - proprioception |
| Q339 | - |  |  | SI | Hip proprioception |
| Q34 | - |  |  | SI | Foot |
| Q340 | - |  |  | SI | Knee - proprioception |
| Q341 | - |  |  | SI | Ankle - proprioception |
| Q342 | - |  |  | SI | Hip |
| Q35 | - |  |  | SI | Face - Left |
| Q36 | - |  |  | SI | Face - Right |
| Q37 | - |  |  | SI | Shoulder - Left |
| Q38 | - |  |  | SI | Shoulder - Right |
| Q39 | - |  |  | SI | Elbow - Left |
| Q40 | - |  |  | SI | Elbow - Right |
| Q41 | - |  |  | SI | Wrist - Left |
| Q42 | - |  |  | SI | Wrist - Right |
| Q43 | - |  |  | SI | Hand - Left |
| Q44 | - |  |  | SI | Hand - Right |
| Q45 | - |  |  | SI | Hip |
| Q46 | - |  |  | SI | Knee - Left |
| Q47 | - |  |  | SI | Knee - Right |
| Q48 | - |  |  | SI | Ankle - Left |
| Q49 | - |  |  | SI | Ankle - Right |
| Q50 | - |  |  | SI | Foot - Left |
| Q51 | - |  |  | SI | Foot - Right |
| Q52 | - |  |  | SI | Face - light touch - left |
| Q53 | - |  |  | SI | Face - light touch - right |
| Q54 | - |  |  | SI | Trunk - light touch - left |
| Q55 | - |  |  | SI | Trunk - light touch - right |
| Q56 | - |  |  | SI | Shoulder - light touch - left |
| Q57 | - |  |  | SI | Shoulder - light touch - right |
| Q58 | - |  |  | SI | Elbow - light touch - left |
| Q59 | - |  |  | SI | Elbow - light touch - right |
| Q60 | - |  |  | SI | Wrist - light touch - left |
| Q61 | - |  |  | SI | Wrist - light touch - right |
| Q62 | - |  |  | SI | Hand - light touch - left |
| Q63 | - |  |  | SI | Hand - light touch - right |
| Q64 | - |  |  | SI | Knee - light touch - left |
| Q65 | - |  |  | SI | Knee - light touch - right |
| Q66 | - |  |  | SI | Ankle - light touch - left |
| Q67 | - |  |  | SI | Ankle - light touch - right |
| Q68 | - |  |  | SI | Foot - light touch - left |
| Q69 | - |  |  | SI | Foot - light touch - right |
| Q70 | - |  |  | SI | Face - temperature - left |
| Q71 | - |  |  | SI | Face - temperature - right |
| Q72 | - |  |  | SI | Trunk - temperature - left |
| Q73 | - |  |  | SI | Trunk - temperature - right |
| Q74 | - |  |  | SI | Shoulder - temperature - left |
| Q75 | - |  |  | SI | Shoulder - temperature - right |
| Q76 | - |  |  | SI | Elbow - temperature - left |
| Q77 | - |  |  | SI | Elbow - temperature - right |
| Q78 | - |  |  | SI | Wrist - temperature - left |
| Q79 | - |  |  | SI | Wrist - temperature - right |
| Q80 | - |  |  | SI | Hand - temperature - left |
| Q81 | - |  |  | SI | Hand - temperature - right |
| Q82 | - |  |  | SI | Knee - temperature - left |
| Q83 | - |  |  | SI | Knee - temperature - right |
| Q84 | - |  |  | SI | Ankle - temperature - left |
| Q85 | - |  |  | SI | Ankle - temperature - right |
| Q86 | - |  |  | SI | Foot - temperature - left |
| Q87 | - |  |  | SI | Foot - temperature - right |
| Q88 | - |  |  | SI | Face - pinprick - left |
| Q89 | - |  |  | SI | Face - pinprick - right |
| Q90 | - |  |  | SI | Trunk- light touch - left |
| Q91 | - |  |  | SI | Trunk - pinprick - right |
| Q92 | - |  |  | SI | Shoulder - pinprick - left |
| Q93 | - |  |  | SI | Shoulder - pinprick - right |
| Q94 | - |  |  | SI | Elbow - pinprick - left |
| Q95 | - |  |  | SI | Elbow - pinprick - right |
| Q96 | - |  |  | SI | Wrist - pinprick - left |
| Q97 | - |  |  | SI | Wrist - pinprick - right |
| Q98 | - |  |  | SI | Hand - pinprick - left |
| Q99 | - |  |  | SI | Hand - pinprick - right |
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
| XCHECK_AddVal | varchar |  |  | SI | Additional ValidationXCHECK_A |
| XCHECK_CodeType | varchar |  |  | SI | Code Type |
| XCHECK_CreatedDate | date |  |  | SI | Created Date |
| XCHECK_CreatedTime | time |  |  | SI | Created Time |
| XCHECK_CreatedUser_DR | bigint |  | FK | SI | Created User |
| XCHECK_UpdatedDate | date |  |  | SI | Updated Date |
| XCHECK_UpdatedTime | time |  |  | SI | Updated Time |
| XCHECK_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| XCHECK_Value | varchar |  |  | SI | Value |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*