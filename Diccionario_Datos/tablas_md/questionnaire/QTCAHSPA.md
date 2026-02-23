# questionnaire.QTCAHSPA

> Assessment for Speech Pathology

**Schema:** questionnaire
**Columnas:** 342
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Assessment for Speech Pathology

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | Focus of assessment  |
| Q04 | varchar |  |  | SI | Patient oriented to |
| Q05 | varchar |  |  | SI | Is patient co-operative? |
| Q06 | varchar |  |  | SI | Cooperative comments |
| Q07 | varchar |  |  | SI | Cognitive function impression |
| Q08 | varchar |  |  | SI | If concerns regarding cognitive function, consider... |
| Q09 | varchar |  |  | SI | Comprehension |
| Q10 | varchar |  |  | SI | Comprehension of information  |
| Q100 | varchar |  |  | SI | Voice volume comment |
| Q101 | varchar |  |  | SI | Loudness (phonation) softest  |
| Q101ObsDR | varchar |  | FK | SI | Loudness (phonation) softest  DR |
| Q102 | varchar |  |  | SI | dB |
| Q103 | varchar |  |  | SI | Loudness (phonation) loudest |
| Q103ObsDR | varchar |  | FK | SI | Loudness (phonation) loudest DR |
| Q104 | varchar |  |  | SI | dB |
| Q105 | varchar |  |  | SI | Loudness (phonation) overall pattern |
| Q106 | varchar |  |  | SI | Loudness (count) softest |
| Q106ObsDR | varchar |  | FK | SI | Loudness (count) softest DR |
| Q107 | varchar |  |  | SI | dB |
| Q108 | varchar |  |  | SI | Loudness (count) loudest |
| Q108ObsDR | varchar |  | FK | SI | Loudness (count) loudest DR |
| Q109 | varchar |  |  | SI | dB |
| Q11 | varchar |  |  | SI | Able to follow commands |
| Q110 | varchar |  |  | SI | Loudness (count) overall pattern |
| Q111 | varchar |  |  | SI | Voice pitch |
| Q112 | varchar |  |  | SI | Sing a scale (6+ notes), /a:/, count 1 - 5 |
| Q113 | varchar |  |  | SI | Voice pitch comment |
| Q114 | varchar |  |  | SI | Voice quality |
| Q115 | varchar |  |  | SI | Voice quality comment |
| Q116 | varchar |  |  | SI | Glottal competence |
| Q116ObsDR | varchar |  | FK | SI | Glottal competence DR |
| Q117 | varchar |  |  | SI | Say 'uh huh' |
| Q118 | varchar |  |  | SI | Glottal compentence comment |
| Q119 | varchar |  |  | SI | Voluntary cough |
| Q12 | varchar |  |  | SI | Able to follow commands comment |
| Q120 | varchar |  |  | SI | Voluntary cough comment |
| Q121 | varchar |  |  | SI | Resonance - vowel level (INCORRECT CONFIG) |
| Q121ObsDR | varchar |  | FK | SI | Resonance - vowel level (INCORRECT CONFIG) DR |
| Q121a | varchar |  |  | SI | Resonance - vowel level |
| Q121aObsDR | varchar |  | FK | SI | Resonance - vowel level DR |
| Q122 | varchar |  |  | SI | Vowel sound /i:/ x 3 |
| Q123 | varchar |  |  | SI | Resonance vowel comment |
| Q124 | varchar |  |  | SI | Resonance - phrase level (non-nasals) (INCORRECT C... |
| Q124ObsDR | varchar |  | FK | SI | Resonance - phrase level (non-nasals) (INCORRECT C... |
| Q124a | varchar |  |  | SI | Resonance - phrase level (non-nasals) |
| Q124aObsDR | varchar |  | FK | SI | Resonance - phrase level (non-nasals) DR |
| Q125 | varchar |  |  | SI | Say 'He has a tubby cat' or 'Bobby the baby boy' |
| Q126 | varchar |  |  | SI | Resonance phrase non-nasal comment |
| Q127 | varchar |  |  | SI | Resonance - phrase level (nasals) (INCORRECT CONFI... |
| Q127ObsDR | varchar |  | FK | SI | Resonance - phrase level (nasals) (INCORRECT CONFI... |
| Q127a | varchar |  |  | SI | Resonance - phrase level (nasals) |
| Q127aObsDR | varchar |  | FK | SI | Resonance - phrase level (nasals) DR |
| Q128 | varchar |  |  | SI | Say 'The swing is neat and clean' or 'Mop the mudd... |
| Q129 | varchar |  |  | SI | Resonance phrase nasal comment |
| Q13 | varchar |  |  | SI | Expression |
| Q130 | varchar |  |  | SI | Voice impression |
| Q131 | varchar |  |  | SI | Aerodynamics / Laryngeal Function |
| Q132 | varchar |  |  | SI | General phonation |
| Q132ObsDR | varchar |  | FK | SI | General phonation DR |
| Q133 | varchar |  |  | SI | General phonation comment  |
| Q134 | varchar |  |  | SI | Maximum Phonation Time (MPT): Production of vowel ... |
| Q135 | varchar |  |  | SI | Maximum Phonation Time - Trials |
| Q136 | varchar |  |  | SI | Phonation time - Trial 1  |
| Q136ObsDR | varchar |  | FK | SI | Phonation time - Trial 1  DR |
| Q137 | varchar |  |  | SI | seconds |
| Q138 | varchar |  |  | SI | Phonation time - Trial 2 |
| Q138ObsDR | varchar |  | FK | SI | Phonation time - Trial 2 DR |
| Q139 | varchar |  |  | SI | seconds |
| Q14 | varchar |  |  | SI | Conversation |
| Q140 | varchar |  |  | SI | Phonation time - Trial 3  |
| Q140ObsDR | varchar |  | FK | SI | Phonation time - Trial 3  DR |
| Q141 | varchar |  |  | SI | seconds |
| Q142 | varchar |  |  | SI | Maximum Phonation Time (MPT)  |
| Q142ObsDR | varchar |  | FK | SI | Maximum Phonation Time (MPT)  DR |
| Q143 | varchar |  |  | SI | seconds |
| Q144 | varchar |  |  | SI | Maximum Phonation Time (MPT)comment |
| Q145 | varchar |  |  | SI | S/Z Ratio: Production of s / z sounds for as long ... |
| Q146 | varchar |  |  | SI | S/Z Ratio (s) - Trials |
| Q147 | varchar |  |  | SI | S/Z Ratio (s) - Trial 1 |
| Q147ObsDR | varchar |  | FK | SI | S/Z Ratio (s) - Trial 1 DR |
| Q148 | varchar |  |  | SI | seconds |
| Q149 | varchar |  |  | SI | S/Z Ratio (s) - Trial 2 |
| Q149ObsDR | varchar |  | FK | SI | S/Z Ratio (s) - Trial 2 DR |
| Q15 | varchar |  |  | SI | Conversation comments |
| Q150 | varchar |  |  | SI | seconds |
| Q151 | varchar |  |  | SI | S/Z Ratio (s) - Trial 3 |
| Q151ObsDR | varchar |  | FK | SI | S/Z Ratio (s) - Trial 3 DR |
| Q152 | varchar |  |  | SI | seconds |
| Q153 | varchar |  |  | SI | S/Z Ratio (z) - Trials |
| Q154 | varchar |  |  | SI | S/Z Ratio (z) - Trial 1 |
| Q154ObsDR | varchar |  | FK | SI | S/Z Ratio (z) - Trial 1 DR |
| Q155 | varchar |  |  | SI | seconds |
| Q156 | varchar |  |  | SI | S/Z Ratio (z) - Trial 2 |
| Q156ObsDR | varchar |  | FK | SI | S/Z Ratio (z) - Trial 2 DR |
| Q157 | varchar |  |  | SI | seconds |
| Q158 | varchar |  |  | SI | S/Z Ratio (z) - Trial 3 |
| Q158ObsDR | varchar |  | FK | SI | S/Z Ratio (z) - Trial 3 DR |
| Q159 | varchar |  |  | SI | seconds |
| Q16 | varchar |  |  | SI | Able to express needs / wants |
| Q160 | varchar |  |  | SI | S/Z Ratio |
| Q160ObsDR | varchar |  | FK | SI | S/Z Ratio DR |
| Q161 | varchar |  |  | SI | S/Z Ratio comment  |
| Q162 | varchar |  |  | SI | Aerodynamics / Laryngeal function impression |
| Q163 | varchar |  |  | SI | Alternating Motion Rates (AMR) |
| Q164 | varchar |  |  | SI | AMR (P) |
| Q164ObsDR | varchar |  | FK | SI | AMR (P) DR |
| Q165 | varchar |  |  | SI | AMR (T) |
| Q165ObsDR | varchar |  | FK | SI | AMR (T) DR |
| Q166 | varchar |  |  | SI | AMR (K) |
| Q166ObsDR | varchar |  | FK | SI | AMR (K) DR |
| Q167 | varchar |  |  | SI | per second |
| Q168 | varchar |  |  | SI | per second |
| Q169 | varchar |  |  | SI | per second |
| Q17 | varchar |  |  | SI | Express needs comments |
| Q170 | varchar |  |  | SI | AMR (P,T,K) |
| Q170ObsDR | varchar |  | FK | SI | AMR (P,T,K) DR |
| Q171 | varchar |  |  | SI | per second |
| Q172 | varchar |  |  | SI | Repetition |
| Q173 | varchar |  |  | SI | Repetition of monosyllables |
| Q173ObsDR | varchar |  | FK | SI | Repetition of monosyllables DR |
| Q174 | varchar |  |  | SI | Repetition of monosyllables comment |
| Q175 | varchar |  |  | SI | Repetition of phrases |
| Q175ObsDR | varchar |  | FK | SI | Repetition of phrases DR |
| Q176 | varchar |  |  | SI | Repetition of phrases comment |
| Q177 | varchar |  |  | SI | Speech Intelligibility |
| Q178 | varchar |  |  | SI | Phoneme  |
| Q178ObsDR | varchar |  | FK | SI | Phoneme  DR |
| Q179 | varchar |  |  | SI | Phoneme comment |
| Q18 | varchar |  |  | SI | Sentence comprehension |
| Q180 | varchar |  |  | SI | Sentence  |
| Q180ObsDR | varchar |  | FK | SI | Sentence  DR |
| Q181 | varchar |  |  | SI | Sentence comment |
| Q182 | varchar |  |  | SI | Passage reading |
| Q182ObsDR | varchar |  | FK | SI | Passage reading DR |
| Q183 | varchar |  |  | SI | Grandfather passage |
| Q184 | varchar |  |  | SI | Passage reading comment |
| Q185 | varchar |  |  | SI | Conversational speech |
| Q185ObsDR | varchar |  | FK | SI | Conversational speech DR |
| Q186 | varchar |  |  | SI | Conversational speech comment |
| Q187 | varchar |  |  | SI | Prosody (INCORRECT CONFIG) |
| Q187ObsDR | varchar |  | FK | SI | Prosody (INCORRECT CONFIG) DR |
| Q187a | varchar |  |  | SI | Prosody |
| Q187aObsDR | varchar |  | FK | SI | Prosody DR |
| Q188 | varchar |  |  | SI | Prosody comment |
| Q189 | varchar |  |  | SI | Articulation & intelligibility impression |
| Q19 | varchar |  |  | SI | Sentence comprehension comment |
| Q190 | varchar |  |  | SI | Tongue general appearance |
| Q190ObsDR | varchar |  | FK | SI | Tongue general appearance DR |
| Q191 | varchar |  |  | SI | Tongue general appearance comment |
| Q192 | varchar |  |  | SI | Tongue movement at rest  |
| Q192ObsDR | varchar |  | FK | SI | Tongue movement at rest  DR |
| Q193 | varchar |  |  | SI | Fasciculation, resting tremor |
| Q194 | varchar |  |  | SI | At rest (fasciculation, resting tremor) comment |
| Q195 | varchar |  |  | SI | Tongue involuntary movement |
| Q195ObsDR | varchar |  | FK | SI | Tongue involuntary movement DR |
| Q196 | varchar |  |  | SI | Tongue involuntary movement comment |
| Q197 | varchar |  |  | SI | For the following tests consider strength, rate, r... |
| Q198 | varchar |  |  | SI | Tongue protrusion |
| Q198ObsDR | varchar |  | FK | SI | Tongue protrusion DR |
| Q199 | varchar |  |  | SI | Protrusion comment |
| Q20 | varchar |  |  | SI | Cognitive communication |
| Q200 | varchar |  |  | SI | Tongue movement -  side to side |
| Q200ObsDR | varchar |  | FK | SI | Tongue movement -  side to side DR |
| Q201 | varchar |  |  | SI | Side to side movement comment  |
| Q202 | varchar |  |  | SI | Tongue retraction |
| Q202ObsDR | varchar |  | FK | SI | Tongue retraction DR |
| Q203 | varchar |  |  | SI | Retraction comment |
| Q204 | varchar |  |  | SI | Tongue movement - lips and teeth  |
| Q204ObsDR | varchar |  | FK | SI | Tongue movement - lips and teeth  DR |
| Q205 | varchar |  |  | SI | Lick lips, move tongue around all upper and lower ... |
| Q206 | varchar |  |  | SI | Tongue movement - lips and teeth comment |
| Q207 | varchar |  |  | SI | Tongue impression |
| Q208 | varchar |  |  | SI | Respiration - reading |
| Q208ObsDR | varchar |  | FK | SI | Respiration - reading DR |
| Q209 | varchar |  |  | SI | Respiration - reading comment |
| Q21 | varchar |  |  | SI | Cognitive communication comment  |
| Q210 | varchar |  |  | SI | Respiratory sufficiency / coordination - speech |
| Q210ObsDR | varchar |  | FK | SI | Respiratory sufficiency / coordination - speech DR |
| Q211 | varchar |  |  | SI | Respiratory sufficiency and coordination - speech ... |
| Q212 | varchar |  |  | SI | Respiratory sufficiency / coordination - swallow |
| Q212ObsDR | varchar |  | FK | SI | Respiratory sufficiency / coordination - swallow D... |
| Q213 | varchar |  |  | SI | Respiratory sufficiency and coordination  - swallo... |
| Q214 | varchar |  |  | SI | Respiration impression |
| Q215 | varchar |  |  | SI | Any impairment noted? |
| Q216 | varchar |  |  | SI | Vision comment |
| Q217 | varchar |  |  | SI | Any impairment noted? |
| Q218 | varchar |  |  | SI | Hearing comment |
| Q219 | varchar |  |  | SI | Decay |
| Q22 | varchar |  |  | SI | Comprehension and expression impression |
| Q220 | varchar |  |  | SI | Decay comment |
| Q221 | varchar |  |  | SI | Missing tooth / teeth |
| Q222 | varchar |  |  | SI | Missing tooth / teeth comment |
| Q223 | varchar |  |  | SI | Dentures |
| Q224 | varchar |  |  | SI | Dentures comment |
| Q225 | varchar |  |  | SI | Evidence of thrush |
| Q226 | varchar |  |  | SI | Evidence of thrush comment |
| Q227 | varchar |  |  | SI | Dentition / Oral comments |
| Q228 | varchar |  |  | SI | Yes/No response |
| Q23 | varchar |  |  | SI | Oral Motor and Sensory Examination (Including Bulb... |
| Q24 | varchar |  |  | SI | Jaw symmetry at rest (INCORRECT CONFIG) |
| Q24ObsDR | varchar |  | FK | SI | Jaw symmetry at rest (INCORRECT CONFIG) DR |
| Q24a | varchar |  |  | SI | Jaw symmetry at rest |
| Q24aObsDR | varchar |  | FK | SI | Jaw symmetry at rest DR |
| Q25 | varchar |  |  | SI | Jaw symmetry comment |
| Q26 | varchar |  |  | SI | Jaw movement on open / close |
| Q26ObsDR | varchar |  | FK | SI | Jaw movement on open / close DR |
| Q27 | varchar |  |  | SI | Jaw movement on open / close comment  |
| Q28 | varchar |  |  | SI | Resist against open movement |
| Q28ObsDR | varchar |  | FK | SI | Resist against open movement DR |
| Q29 | varchar |  |  | SI | Resist against open movement comment |
| Q30 | varchar |  |  | SI | Resist against close  movement |
| Q30ObsDR | varchar |  | FK | SI | Resist against close  movement DR |
| Q31 | varchar |  |  | SI | Resist against close  movement comment |
| Q32 | varchar |  |  | SI | Lateral jaw movement |
| Q32ObsDR | varchar |  | FK | SI | Lateral jaw movement DR |
| Q33 | varchar |  |  | SI | Lateral jaw movement comment |
| Q34 | varchar |  |  | SI | Mandibular impression |
| Q35 | varchar |  |  | SI | Face and Lips (Including Cranial Nerve V & VII: Tr... |
| Q36 | varchar |  |  | SI | Facial Musculature (CN VII) |
| Q37 | varchar |  |  | SI | Facial symmetry at rest |
| Q37ObsDR | varchar |  | FK | SI | Facial symmetry at rest DR |
| Q38 | varchar |  |  | SI | Facial symmetry at rest comment |
| Q39 | varchar |  |  | SI | Facial expression- forehead |
| Q39ObsDR | varchar |  | FK | SI | Facial expression- forehead DR |
| Q40 | varchar |  |  | SI | Raise eyebrows / lookup |
| Q41 | varchar |  |  | SI | Facial expression- forehead comment |
| Q42 | varchar |  |  | SI | Facial expression - eyes |
| Q42ObsDR | varchar |  | FK | SI | Facial expression - eyes DR |
| Q43 | varchar |  |  | SI | Close eyes tightly |
| Q44 | varchar |  |  | SI | Facial expression - eyes comment |
| Q45 | varchar |  |  | SI | Facial Sensation (CN V) |
| Q46 | varchar |  |  | SI | Facial sensation |
| Q46ObsDR | varchar |  | FK | SI | Facial sensation DR |
| Q47 | varchar |  |  | SI | Cotton swab on all three branches |
| Q48 | varchar |  |  | SI | Facial sensation comment |
| Q49 | varchar |  |  | SI | Lips (CN VII) |
| Q50 | varchar |  |  | SI | Lip symmetry |
| Q50ObsDR | varchar |  | FK | SI | Lip symmetry DR |
| Q51 | varchar |  |  | SI | Lip symmetry comment |
| Q52 | varchar |  |  | SI | Lip range of movement-retraction / lateralization  |
| Q52ObsDR | varchar |  | FK | SI | Lip range of movement-retraction / lateralization ... |
| Q53 | varchar |  |  | SI | Exaggerated smile |
| Q54 | varchar |  |  | SI | Lip range of movement-retraction / lateralization ... |
| Q55 | varchar |  |  | SI | Lip range of movement - protrusion  |
| Q55ObsDR | varchar |  | FK | SI | Lip range of movement - protrusion  DR |
| Q56 | varchar |  |  | SI | Pucker lips |
| Q57 | varchar |  |  | SI | Lip range of movement - protrusion comment  |
| Q58 | varchar |  |  | SI | Lip rate of movement |
| Q58ObsDR | varchar |  | FK | SI | Lip rate of movement DR |
| Q59 | varchar |  |  | SI | Say ''oo-ee'' for 10 repetitions |
| Q60 | varchar |  |  | SI | Lip rate of movement comment |
| Q61 | varchar |  |  | SI | Lip seal |
| Q61ObsDR | varchar |  | FK | SI | Lip seal DR |
| Q62 | varchar |  |  | SI | Blow air into cheeks hold (15 secs) |
| Q63 | varchar |  |  | SI | Lip seal comment |
| Q64 | varchar |  |  | SI | Face / Lip impression |
| Q65 | varchar |  |  | SI | Anterior 2/3 tongue (CN VII) |
| Q66 | varchar |  |  | SI | Sensory taste  (Anterior 2/3 tongue)  |
| Q66ObsDR | varchar |  | FK | SI | Sensory taste  (Anterior 2/3 tongue)  DR |
| Q67 | varchar |  |  | SI | Sensory taste  (2/3 tongue)  comment |
| Q68 | varchar |  |  | SI | Posterior 1/3 tongue (CN IX) |
| Q69 | varchar |  |  | SI | Sensory taste  (posterior 1/3 Tongue) |
| Q69ObsDR | varchar |  | FK | SI | Sensory taste  (posterior 1/3 Tongue) DR |
| Q70 | varchar |  |  | SI | Sensory taste  (1/3 tongue) comment |
| Q71 | varchar |  |  | SI | Cough strength |
| Q72 | varchar |  |  | SI | Cough observations  |
| Q73 | varchar |  |  | SI | Cough observations comment  |
| Q74 | varchar |  |  | SI | Palate (CN X) |
| Q75 | varchar |  |  | SI | Gag reflex |
| Q75ObsDR | varchar |  | FK | SI | Gag reflex DR |
| Q76 | varchar |  |  | SI | Gag reflex comment |
| Q77 | varchar |  |  | SI | Palate appearance at rest |
| Q77ObsDR | varchar |  | FK | SI | Palate appearance at rest DR |
| Q78 | varchar |  |  | SI | Palate appearance at rest comment |
| Q79 | varchar |  |  | SI | Palatal movement |
| Q79ObsDR | varchar |  | FK | SI | Palatal movement DR |
| Q80 | varchar |  |  | SI | Palatal movement comment |
| Q81 | varchar |  |  | SI | Palatal elevation |
| Q81ObsDR | varchar |  | FK | SI | Palatal elevation DR |
| Q82 | varchar |  |  | SI | Say 'ah, ah, ah' |
| Q83 | varchar |  |  | SI | Palatal elevation comment |
| Q84 | varchar |  |  | SI | Uvula deviation |
| Q84ObsDR | varchar |  | FK | SI | Uvula deviation DR |
| Q85 | varchar |  |  | SI | Uvula deviation comment |
| Q86 | varchar |  |  | SI | Palato-pharyngeal impression |
| Q87 | varchar |  |  | SI | Speech problems associated with swallowing |
| Q88 | varchar |  |  | SI | Speech problems associated with swallowing comment |
| Q89 | varchar |  |  | SI | Voice Volume, Pitch & Quality |
| Q90 | varchar |  |  | SI | Was audio recorded? |
| Q91 | varchar |  |  | SI | Was consent obtained? |
| Q92 | varchar |  |  | SI | Passage reading  |
| Q93 | varchar |  |  | SI | Consider pitch, loudness, quality |
| Q94 | varchar |  |  | SI | Patient's perception of voice (during reading) |
| Q95 | varchar |  |  | SI | Patient's perception of voice (during reading) com... |
| Q96 | varchar |  |  | SI | Patient's perception of impairment (during reading... |
| Q97 | varchar |  |  | SI | Patient's perception of impairment (during reading... |
| Q98 | varchar |  |  | SI | Voice volume |
| Q98ObsDR | varchar |  | FK | SI | Voice volume DR |
| Q99 | varchar |  |  | SI | Count to 5 increasing in volume on each number fro... |
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