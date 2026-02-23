# SQLUser.CT_LocStorageBinStockItem

**Schema:** SQLUser
**Columnas:** 354
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de Ubicaciones**. Servicios, salas, unidades del hospital. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ITM_ParRef | varchar | PK |  | NO | CT_LocStorageBin Parent Reference |
| ITM_Childsub | double |  |  | NO | ITM_Childsub |
| ITM_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| ITM_CreatedDate | date |  |  | SI | Created Date |
| ITM_CreatedTime | time |  |  | SI | Created Time |
| ITM_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ITM_DateFrom | date |  |  | SI | Date From |
| ITM_DateTo | date |  |  | SI | Date To |
| ITM_RowId | varchar |  |  | NO | - |
| ITM_StockItem_DR | bigint |  | FK | SI | Des Ref INCItm |
| ITM_UpdatedDate | date |  |  | SI | Updated Date |
| ITM_UpdatedTime | time |  |  | SI | Updated Time |
| ITM_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Focus of assessment |
| Q04 | - |  |  | SI | Patient oriented to |
| Q05 | - |  |  | SI | Is patient co-operative? |
| Q06 | - |  |  | SI | Cooperative comments |
| Q07 | - |  |  | SI | Cognitive function impression |
| Q08 | - |  |  | SI | If concerns regarding cognitive function, consider... |
| Q09 | - |  |  | SI | Comprehension |
| Q10 | - |  |  | SI | Comprehension of information |
| Q100 | - |  |  | SI | Voice volume comment |
| Q101 | - |  |  | SI | Loudness (phonation) softest |
| Q101ObsDR | - |  |  | SI | Loudness (phonation) softest  DR |
| Q102 | - |  |  | SI | dB |
| Q103 | - |  |  | SI | Loudness (phonation) loudest |
| Q103ObsDR | - |  |  | SI | Loudness (phonation) loudest DR |
| Q104 | - |  |  | SI | dB |
| Q105 | - |  |  | SI | Loudness (phonation) overall pattern |
| Q106 | - |  |  | SI | Loudness (count) softest |
| Q106ObsDR | - |  |  | SI | Loudness (count) softest DR |
| Q107 | - |  |  | SI | dB |
| Q108 | - |  |  | SI | Loudness (count) loudest |
| Q108ObsDR | - |  |  | SI | Loudness (count) loudest DR |
| Q109 | - |  |  | SI | dB |
| Q11 | - |  |  | SI | Able to follow commands |
| Q110 | - |  |  | SI | Loudness (count) overall pattern |
| Q111 | - |  |  | SI | Voice pitch |
| Q112 | - |  |  | SI | Sing a scale (6+ notes), /a:/, count 1 - 5 |
| Q113 | - |  |  | SI | Voice pitch comment |
| Q114 | - |  |  | SI | Voice quality |
| Q115 | - |  |  | SI | Voice quality comment |
| Q116 | - |  |  | SI | Glottal competence |
| Q116ObsDR | - |  |  | SI | Glottal competence DR |
| Q117 | - |  |  | SI | Say 'uh huh |
| Q118 | - |  |  | SI | Glottal compentence comment |
| Q119 | - |  |  | SI | Voluntary cough |
| Q12 | - |  |  | SI | Able to follow commands comment |
| Q120 | - |  |  | SI | Voluntary cough comment |
| Q121 | - |  |  | SI | Resonance - vowel level (INCORRECT CONFIG) |
| Q121ObsDR | - |  |  | SI | Resonance - vowel level (INCORRECT CONFIG) DR |
| Q121a | - |  |  | SI | Resonance - vowel level |
| Q121aObsDR | - |  |  | SI | Resonance - vowel level DR |
| Q122 | - |  |  | SI | Vowel sound /i:/ x 3 |
| Q123 | - |  |  | SI | Resonance vowel comment |
| Q124 | - |  |  | SI | Resonance - phrase level (non-nasals) (INCORRECT C... |
| Q124ObsDR | - |  |  | SI | Resonance - phrase level (non-nasals) (INCORRECT C... |
| Q124a | - |  |  | SI | Resonance - phrase level (non-nasals) |
| Q124aObsDR | - |  |  | SI | Resonance - phrase level (non-nasals) DR |
| Q125 | - |  |  | SI | Say 'He has a tubby cat' or 'Bobby the baby boy |
| Q126 | - |  |  | SI | Resonance phrase non-nasal comment |
| Q127 | - |  |  | SI | Resonance - phrase level (nasals) (INCORRECT CONFI... |
| Q127ObsDR | - |  |  | SI | Resonance - phrase level (nasals) (INCORRECT CONFI... |
| Q127a | - |  |  | SI | Resonance - phrase level (nasals) |
| Q127aObsDR | - |  |  | SI | Resonance - phrase level (nasals) DR |
| Q128 | - |  |  | SI | Say 'The swing is neat and clean' or 'Mop the mudd... |
| Q129 | - |  |  | SI | Resonance phrase nasal comment |
| Q13 | - |  |  | SI | Expression |
| Q130 | - |  |  | SI | Voice impression |
| Q131 | - |  |  | SI | Aerodynamics / Laryngeal Function |
| Q132 | - |  |  | SI | General phonation |
| Q132ObsDR | - |  |  | SI | General phonation DR |
| Q133 | - |  |  | SI | General phonation comment |
| Q134 | - |  |  | SI | Maximum Phonation Time (MPT): Production of vowel ... |
| Q135 | - |  |  | SI | Maximum Phonation Time - Trials |
| Q136 | - |  |  | SI | Phonation time - Trial 1 |
| Q136ObsDR | - |  |  | SI | Phonation time - Trial 1  DR |
| Q137 | - |  |  | SI | seconds |
| Q138 | - |  |  | SI | Phonation time - Trial 2 |
| Q138ObsDR | - |  |  | SI | Phonation time - Trial 2 DR |
| Q139 | - |  |  | SI | seconds |
| Q14 | - |  |  | SI | Conversation |
| Q140 | - |  |  | SI | Phonation time - Trial 3 |
| Q140ObsDR | - |  |  | SI | Phonation time - Trial 3  DR |
| Q141 | - |  |  | SI | seconds |
| Q142 | - |  |  | SI | Maximum Phonation Time (MPT) |
| Q142ObsDR | - |  |  | SI | Maximum Phonation Time (MPT)  DR |
| Q143 | - |  |  | SI | seconds |
| Q144 | - |  |  | SI | Maximum Phonation Time (MPT)comment |
| Q145 | - |  |  | SI | S/Z Ratio: Production of s / z sounds for as long ... |
| Q146 | - |  |  | SI | S/Z Ratio (s) - Trials |
| Q147 | - |  |  | SI | S/Z Ratio (s) - Trial 1 |
| Q147ObsDR | - |  |  | SI | S/Z Ratio (s) - Trial 1 DR |
| Q148 | - |  |  | SI | seconds |
| Q149 | - |  |  | SI | S/Z Ratio (s) - Trial 2 |
| Q149ObsDR | - |  |  | SI | S/Z Ratio (s) - Trial 2 DR |
| Q15 | - |  |  | SI | Conversation comments |
| Q150 | - |  |  | SI | seconds |
| Q151 | - |  |  | SI | S/Z Ratio (s) - Trial 3 |
| Q151ObsDR | - |  |  | SI | S/Z Ratio (s) - Trial 3 DR |
| Q152 | - |  |  | SI | seconds |
| Q153 | - |  |  | SI | S/Z Ratio (z) - Trials |
| Q154 | - |  |  | SI | S/Z Ratio (z) - Trial 1 |
| Q154ObsDR | - |  |  | SI | S/Z Ratio (z) - Trial 1 DR |
| Q155 | - |  |  | SI | seconds |
| Q156 | - |  |  | SI | S/Z Ratio (z) - Trial 2 |
| Q156ObsDR | - |  |  | SI | S/Z Ratio (z) - Trial 2 DR |
| Q157 | - |  |  | SI | seconds |
| Q158 | - |  |  | SI | S/Z Ratio (z) - Trial 3 |
| Q158ObsDR | - |  |  | SI | S/Z Ratio (z) - Trial 3 DR |
| Q159 | - |  |  | SI | seconds |
| Q16 | - |  |  | SI | Able to express needs / wants |
| Q160 | - |  |  | SI | S/Z Ratio |
| Q160ObsDR | - |  |  | SI | S/Z Ratio DR |
| Q161 | - |  |  | SI | S/Z Ratio comment |
| Q162 | - |  |  | SI | Aerodynamics / Laryngeal function impression |
| Q163 | - |  |  | SI | Alternating Motion Rates (AMR) |
| Q164 | - |  |  | SI | AMR (P) |
| Q164ObsDR | - |  |  | SI | AMR (P) DR |
| Q165 | - |  |  | SI | AMR (T) |
| Q165ObsDR | - |  |  | SI | AMR (T) DR |
| Q166 | - |  |  | SI | AMR (K) |
| Q166ObsDR | - |  |  | SI | AMR (K) DR |
| Q167 | - |  |  | SI | per second |
| Q168 | - |  |  | SI | per second |
| Q169 | - |  |  | SI | per second |
| Q17 | - |  |  | SI | Express needs comments |
| Q170 | - |  |  | SI | AMR (P,T,K) |
| Q170ObsDR | - |  |  | SI | AMR (P,T,K) DR |
| Q171 | - |  |  | SI | per second |
| Q172 | - |  |  | SI | Repetition |
| Q173 | - |  |  | SI | Repetition of monosyllables |
| Q173ObsDR | - |  |  | SI | Repetition of monosyllables DR |
| Q174 | - |  |  | SI | Repetition of monosyllables comment |
| Q175 | - |  |  | SI | Repetition of phrases |
| Q175ObsDR | - |  |  | SI | Repetition of phrases DR |
| Q176 | - |  |  | SI | Repetition of phrases comment |
| Q177 | - |  |  | SI | Speech Intelligibility |
| Q178 | - |  |  | SI | Phoneme |
| Q178ObsDR | - |  |  | SI | Phoneme  DR |
| Q179 | - |  |  | SI | Phoneme comment |
| Q18 | - |  |  | SI | Sentence comprehension |
| Q180 | - |  |  | SI | Sentence |
| Q180ObsDR | - |  |  | SI | Sentence  DR |
| Q181 | - |  |  | SI | Sentence comment |
| Q182 | - |  |  | SI | Passage reading |
| Q182ObsDR | - |  |  | SI | Passage reading DR |
| Q183 | - |  |  | SI | Grandfather passage |
| Q184 | - |  |  | SI | Passage reading comment |
| Q185 | - |  |  | SI | Conversational speech |
| Q185ObsDR | - |  |  | SI | Conversational speech DR |
| Q186 | - |  |  | SI | Conversational speech comment |
| Q187 | - |  |  | SI | Prosody (INCORRECT CONFIG) |
| Q187ObsDR | - |  |  | SI | Prosody (INCORRECT CONFIG) DR |
| Q187a | - |  |  | SI | Prosody |
| Q187aObsDR | - |  |  | SI | Prosody DR |
| Q188 | - |  |  | SI | Prosody comment |
| Q189 | - |  |  | SI | Articulation & intelligibility impression |
| Q19 | - |  |  | SI | Sentence comprehension comment |
| Q190 | - |  |  | SI | Tongue general appearance |
| Q190ObsDR | - |  |  | SI | Tongue general appearance DR |
| Q191 | - |  |  | SI | Tongue general appearance comment |
| Q192 | - |  |  | SI | Tongue movement at rest |
| Q192ObsDR | - |  |  | SI | Tongue movement at rest  DR |
| Q193 | - |  |  | SI | Fasciculation, resting tremor |
| Q194 | - |  |  | SI | At rest (fasciculation, resting tremor) comment |
| Q195 | - |  |  | SI | Tongue involuntary movement |
| Q195ObsDR | - |  |  | SI | Tongue involuntary movement DR |
| Q196 | - |  |  | SI | Tongue involuntary movement comment |
| Q197 | - |  |  | SI | For the following tests consider strength, rate, r... |
| Q198 | - |  |  | SI | Tongue protrusion |
| Q198ObsDR | - |  |  | SI | Tongue protrusion DR |
| Q199 | - |  |  | SI | Protrusion comment |
| Q20 | - |  |  | SI | Cognitive communication |
| Q200 | - |  |  | SI | Tongue movement -  side to side |
| Q200ObsDR | - |  |  | SI | Tongue movement -  side to side DR |
| Q201 | - |  |  | SI | Side to side movement comment |
| Q202 | - |  |  | SI | Tongue retraction |
| Q202ObsDR | - |  |  | SI | Tongue retraction DR |
| Q203 | - |  |  | SI | Retraction comment |
| Q204 | - |  |  | SI | Tongue movement - lips and teeth |
| Q204ObsDR | - |  |  | SI | Tongue movement - lips and teeth  DR |
| Q205 | - |  |  | SI | Lick lips, move tongue around all upper and lower ... |
| Q206 | - |  |  | SI | Tongue movement - lips and teeth comment |
| Q207 | - |  |  | SI | Tongue impression |
| Q208 | - |  |  | SI | Respiration - reading |
| Q208ObsDR | - |  |  | SI | Respiration - reading DR |
| Q209 | - |  |  | SI | Respiration - reading comment |
| Q21 | - |  |  | SI | Cognitive communication comment |
| Q210 | - |  |  | SI | Respiratory sufficiency / coordination - speech |
| Q210ObsDR | - |  |  | SI | Respiratory sufficiency / coordination - speech DR |
| Q211 | - |  |  | SI | Respiratory sufficiency and coordination - speech ... |
| Q212 | - |  |  | SI | Respiratory sufficiency / coordination - swallow |
| Q212ObsDR | - |  |  | SI | Respiratory sufficiency / coordination - swallow D... |
| Q213 | - |  |  | SI | Respiratory sufficiency and coordination  - swallo... |
| Q214 | - |  |  | SI | Respiration impression |
| Q215 | - |  |  | SI | Any impairment noted? |
| Q216 | - |  |  | SI | Vision comment |
| Q217 | - |  |  | SI | Any impairment noted? |
| Q218 | - |  |  | SI | Hearing comment |
| Q219 | - |  |  | SI | Decay |
| Q22 | - |  |  | SI | Comprehension and expression impression |
| Q220 | - |  |  | SI | Decay comment |
| Q221 | - |  |  | SI | Missing tooth / teeth |
| Q222 | - |  |  | SI | Missing tooth / teeth comment |
| Q223 | - |  |  | SI | Dentures |
| Q224 | - |  |  | SI | Dentures comment |
| Q225 | - |  |  | SI | Evidence of thrush |
| Q226 | - |  |  | SI | Evidence of thrush comment |
| Q227 | - |  |  | SI | Dentition / Oral comments |
| Q228 | - |  |  | SI | Yes/No response |
| Q23 | - |  |  | SI | Oral Motor and Sensory Examination (Including Bulb... |
| Q24 | - |  |  | SI | Jaw symmetry at rest (INCORRECT CONFIG) |
| Q24ObsDR | - |  |  | SI | Jaw symmetry at rest (INCORRECT CONFIG) DR |
| Q24a | - |  |  | SI | Jaw symmetry at rest |
| Q24aObsDR | - |  |  | SI | Jaw symmetry at rest DR |
| Q25 | - |  |  | SI | Jaw symmetry comment |
| Q26 | - |  |  | SI | Jaw movement on open / close |
| Q26ObsDR | - |  |  | SI | Jaw movement on open / close DR |
| Q27 | - |  |  | SI | Jaw movement on open / close comment |
| Q28 | - |  |  | SI | Resist against open movement |
| Q28ObsDR | - |  |  | SI | Resist against open movement DR |
| Q29 | - |  |  | SI | Resist against open movement comment |
| Q30 | - |  |  | SI | Resist against close  movement |
| Q30ObsDR | - |  |  | SI | Resist against close  movement DR |
| Q31 | - |  |  | SI | Resist against close  movement comment |
| Q32 | - |  |  | SI | Lateral jaw movement |
| Q32ObsDR | - |  |  | SI | Lateral jaw movement DR |
| Q33 | - |  |  | SI | Lateral jaw movement comment |
| Q34 | - |  |  | SI | Mandibular impression |
| Q35 | - |  |  | SI | Face and Lips (Including Cranial Nerve V & VII: Tr... |
| Q36 | - |  |  | SI | Facial Musculature (CN VII) |
| Q37 | - |  |  | SI | Facial symmetry at rest |
| Q37ObsDR | - |  |  | SI | Facial symmetry at rest DR |
| Q38 | - |  |  | SI | Facial symmetry at rest comment |
| Q39 | - |  |  | SI | Facial expression- forehead |
| Q39ObsDR | - |  |  | SI | Facial expression- forehead DR |
| Q40 | - |  |  | SI | Raise eyebrows / lookup |
| Q41 | - |  |  | SI | Facial expression- forehead comment |
| Q42 | - |  |  | SI | Facial expression - eyes |
| Q42ObsDR | - |  |  | SI | Facial expression - eyes DR |
| Q43 | - |  |  | SI | Close eyes tightly |
| Q44 | - |  |  | SI | Facial expression - eyes comment |
| Q45 | - |  |  | SI | Facial Sensation (CN V) |
| Q46 | - |  |  | SI | Facial sensation |
| Q46ObsDR | - |  |  | SI | Facial sensation DR |
| Q47 | - |  |  | SI | Cotton swab on all three branches |
| Q48 | - |  |  | SI | Facial sensation comment |
| Q49 | - |  |  | SI | Lips (CN VII) |
| Q50 | - |  |  | SI | Lip symmetry |
| Q50ObsDR | - |  |  | SI | Lip symmetry DR |
| Q51 | - |  |  | SI | Lip symmetry comment |
| Q52 | - |  |  | SI | Lip range of movement-retraction / lateralization |
| Q52ObsDR | - |  |  | SI | Lip range of movement-retraction / lateralization ... |
| Q53 | - |  |  | SI | Exaggerated smile |
| Q54 | - |  |  | SI | Lip range of movement-retraction / lateralization ... |
| Q55 | - |  |  | SI | Lip range of movement - protrusion |
| Q55ObsDR | - |  |  | SI | Lip range of movement - protrusion  DR |
| Q56 | - |  |  | SI | Pucker lips |
| Q57 | - |  |  | SI | Lip range of movement - protrusion comment |
| Q58 | - |  |  | SI | Lip rate of movement |
| Q58ObsDR | - |  |  | SI | Lip rate of movement DR |
| Q59 | - |  |  | SI | Say ''oo-ee'' for 10 repetitions |
| Q60 | - |  |  | SI | Lip rate of movement comment |
| Q61 | - |  |  | SI | Lip seal |
| Q61ObsDR | - |  |  | SI | Lip seal DR |
| Q62 | - |  |  | SI | Blow air into cheeks hold (15 secs) |
| Q63 | - |  |  | SI | Lip seal comment |
| Q64 | - |  |  | SI | Face / Lip impression |
| Q65 | - |  |  | SI | Anterior 2/3 tongue (CN VII) |
| Q66 | - |  |  | SI | Sensory taste  (Anterior 2/3 tongue) |
| Q66ObsDR | - |  |  | SI | Sensory taste  (Anterior 2/3 tongue)  DR |
| Q67 | - |  |  | SI | Sensory taste  (2/3 tongue)  comment |
| Q68 | - |  |  | SI | Posterior 1/3 tongue (CN IX) |
| Q69 | - |  |  | SI | Sensory taste  (posterior 1/3 Tongue) |
| Q69ObsDR | - |  |  | SI | Sensory taste  (posterior 1/3 Tongue) DR |
| Q70 | - |  |  | SI | Sensory taste  (1/3 tongue) comment |
| Q71 | - |  |  | SI | Cough strength |
| Q72 | - |  |  | SI | Cough observations |
| Q73 | - |  |  | SI | Cough observations comment |
| Q74 | - |  |  | SI | Palate (CN X) |
| Q75 | - |  |  | SI | Gag reflex |
| Q75ObsDR | - |  |  | SI | Gag reflex DR |
| Q76 | - |  |  | SI | Gag reflex comment |
| Q77 | - |  |  | SI | Palate appearance at rest |
| Q77ObsDR | - |  |  | SI | Palate appearance at rest DR |
| Q78 | - |  |  | SI | Palate appearance at rest comment |
| Q79 | - |  |  | SI | Palatal movement |
| Q79ObsDR | - |  |  | SI | Palatal movement DR |
| Q80 | - |  |  | SI | Palatal movement comment |
| Q81 | - |  |  | SI | Palatal elevation |
| Q81ObsDR | - |  |  | SI | Palatal elevation DR |
| Q82 | - |  |  | SI | Say 'ah, ah, ah |
| Q83 | - |  |  | SI | Palatal elevation comment |
| Q84 | - |  |  | SI | Uvula deviation |
| Q84ObsDR | - |  |  | SI | Uvula deviation DR |
| Q85 | - |  |  | SI | Uvula deviation comment |
| Q86 | - |  |  | SI | Palato-pharyngeal impression |
| Q87 | - |  |  | SI | Speech problems associated with swallowing |
| Q88 | - |  |  | SI | Speech problems associated with swallowing comment |
| Q89 | - |  |  | SI | Voice Volume, Pitch & Quality |
| Q90 | - |  |  | SI | Was audio recorded? |
| Q91 | - |  |  | SI | Was consent obtained? |
| Q92 | - |  |  | SI | Passage reading |
| Q93 | - |  |  | SI | Consider pitch, loudness, quality |
| Q94 | - |  |  | SI | Patient's perception of voice (during reading) |
| Q95 | - |  |  | SI | Patient's perception of voice (during reading) com... |
| Q96 | - |  |  | SI | Patient's perception of impairment (during reading... |
| Q97 | - |  |  | SI | Patient's perception of impairment (during reading... |
| Q98 | - |  |  | SI | Voice volume |
| Q98ObsDR | - |  |  | SI | Voice volume DR |
| Q99 | - |  |  | SI | Count to 5 increasing in volume on each number fro... |
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