# questionnaire.QGXXXNEUEXA

> Neurological Examination

**Schema:** questionnaire
**Columnas:** 395
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Neurological Examination

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Speech  |
| Q01A | varchar |  |  | SI | Dysphonia |
| Q01AN | varchar |  |  | SI | Note |
| Q01AObsDR | varchar |  | FK | SI | Dysphonia DR |
| Q01B | varchar |  |  | SI | Dysarthria |
| Q01BN | varchar |  |  | SI | Note |
| Q01BObsDR | varchar |  | FK | SI | Dysarthria DR |
| Q01C | varchar |  |  | SI | Aphasia |
| Q01CN | varchar |  |  | SI | Note |
| Q01CObsDR | varchar |  | FK | SI | Aphasia DR |
| Q01D | varchar |  |  | SI | Other speech abnormalities |
| Q01DN | varchar |  |  | SI | Note |
| Q01DObsDR | varchar |  | FK | SI | Other speech abnormalities DR |
| Q02 | varchar |  |  | SI | Gait |
| Q02A | varchar |  |  | SI | Ataxic |
| Q02AN | varchar |  |  | SI | Note |
| Q02AObsDR | varchar |  | FK | SI | Ataxic DR |
| Q02B | varchar |  |  | SI | Shuffling |
| Q02BN | varchar |  |  | SI | Note |
| Q02BObsDR | varchar |  | FK | SI | Shuffling DR |
| Q02C | varchar |  |  | SI | Spastic |
| Q02CN | varchar |  |  | SI | Note |
| Q02CObsDR | varchar |  | FK | SI | Spastic DR |
| Q02D | varchar |  |  | SI | Other gait abnormalities |
| Q02DN | varchar |  |  | SI | Note |
| Q02DObsDR | varchar |  | FK | SI | Other gait abnormalities DR |
| Q03 | varchar |  |  | SI | Memory |
| Q03A | varchar |  |  | SI | Impaired short term |
| Q03AN | varchar |  |  | SI | Note |
| Q03AObsDR | varchar |  | FK | SI | Impaired short term DR |
| Q03B | varchar |  |  | SI | Impaired long term |
| Q03BN | varchar |  |  | SI | Note |
| Q03BObsDR | varchar |  | FK | SI | Impaired long term DR |
| Q04 | varchar |  |  | SI | Orientation |
| Q04A | varchar |  |  | SI | Disoriented as to time |
| Q04AN | varchar |  |  | SI | Note |
| Q04AObsDR | varchar |  | FK | SI | Disoriented as to time DR |
| Q04B | varchar |  |  | SI | Disoriented as to place |
| Q04BN | varchar |  |  | SI | Note |
| Q04BObsDR | varchar |  | FK | SI | Disoriented as to place DR |
| Q04C | varchar |  |  | SI | Disoriented as to person |
| Q04CN | varchar |  |  | SI | Note |
| Q04CObsDR | varchar |  | FK | SI | Disoriented as to person DR |
| Q05 | varchar |  |  | SI | Cognitive function |
| Q05A | varchar |  |  | SI | Impaired serial 7 calculations |
| Q05AN | varchar |  |  | SI | Note |
| Q05AObsDR | varchar |  | FK | SI | Impaired serial 7 calculations DR |
| Q05B | varchar |  |  | SI | Impaired abstraction ability |
| Q05BN | varchar |  |  | SI | Note |
| Q05BObsDR | varchar |  | FK | SI | Impaired abstraction ability DR |
| Q05C | varchar |  |  | SI | Impaired judgment |
| Q05CN | varchar |  |  | SI | Note |
| Q05CObsDR | varchar |  | FK | SI | Impaired judgment DR |
| Q05D | varchar |  |  | SI | Poor general fund of information |
| Q05DN | varchar |  |  | SI | Note |
| Q05DObsDR | varchar |  | FK | SI | Poor general fund of information DR |
| Q06 | varchar |  |  | SI | Psychological disturbances |
| Q06A | varchar |  |  | SI | Delusions |
| Q06AN | varchar |  |  | SI | Note |
| Q06AObsDR | varchar |  | FK | SI | Delusions DR |
| Q06B | varchar |  |  | SI | Hallucinations |
| Q06BN | varchar |  |  | SI | Note |
| Q06BObsDR | varchar |  | FK | SI | Hallucinations DR |
| Q06C | varchar |  |  | SI | Illusions |
| Q06CN | varchar |  |  | SI | Note |
| Q06CObsDR | varchar |  | FK | SI | Illusions DR |
| Q06D | varchar |  |  | SI | Other psychological disturbances |
| Q06DN | varchar |  |  | SI | Note |
| Q06DObsDR | varchar |  | FK | SI | Other psychological disturbances DR |
| Q07 | varchar |  |  | SI | Cranial nerves |
| Q07A | varchar |  |  | SI | Visual acuity |
| Q07AN | varchar |  |  | SI | Note |
| Q07AObsDR | varchar |  | FK | SI | Visual acuity DR |
| Q07B | varchar |  |  | SI | Visual field deficit |
| Q07BN | varchar |  |  | SI | Note |
| Q07BObsDR | varchar |  | FK | SI | Visual field deficit DR |
| Q07C | varchar |  |  | SI | Extraocular muscle movement |
| Q07CN | varchar |  |  | SI | Note |
| Q07CObsDR | varchar |  | FK | SI | Extraocular muscle movement DR |
| Q07CRAN | varchar |  |  | SI | Cranial Nerves |
| Q07D | varchar |  |  | SI | Fundoscopy |
| Q07DN | varchar |  |  | SI | Note |
| Q07DObsDR | varchar |  | FK | SI | Fundoscopy DR |
| Q07E | varchar |  |  | SI | Facial sensation |
| Q07EN | varchar |  |  | SI | Note |
| Q07EObsDR | varchar |  | FK | SI | Facial sensation DR |
| Q07F | varchar |  |  | SI | Facial expression muscles |
| Q07FN | varchar |  |  | SI | Note |
| Q07FObsDR | varchar |  | FK | SI | Facial expression muscles DR |
| Q07G | varchar |  |  | SI | Hearing |
| Q07GN | varchar |  |  | SI | Note |
| Q07GObsDR | varchar |  | FK | SI | Hearing DR |
| Q07H | varchar |  |  | SI | Balance |
| Q07HN | varchar |  |  | SI | Note |
| Q07HObsDR | varchar |  | FK | SI | Balance DR |
| Q07I | varchar |  |  | SI | Gag reflex |
| Q07IN | varchar |  |  | SI | Note |
| Q07IObsDR | varchar |  | FK | SI | Gag reflex DR |
| Q07J | varchar |  |  | SI | Uvula deviation |
| Q07JN | varchar |  |  | SI | Note |
| Q07JObsDR | varchar |  | FK | SI | Uvula deviation DR |
| Q07K | varchar |  |  | SI | Voice quality |
| Q07KN | varchar |  |  | SI | Note |
| Q07KObsDR | varchar |  | FK | SI | Voice quality DR |
| Q07L | varchar |  |  | SI | Trapezius strength |
| Q07LN | varchar |  |  | SI | Note |
| Q07LObsDR | varchar |  | FK | SI | Trapezius strength DR |
| Q08 | varchar |  |  | SI | Peripheral sensory system |
| Q08A | varchar |  |  | SI | Decreased sense of light touch |
| Q08AN | varchar |  |  | SI | Note |
| Q08AObsDR | varchar |  | FK | SI | Decreased sense of light touch DR |
| Q08B | varchar |  |  | SI | Decreased sense of pain |
| Q08BN | varchar |  |  | SI | Note |
| Q08BObsDR | varchar |  | FK | SI | Decreased sense of pain DR |
| Q08C | varchar |  |  | SI | Decreased sense of heat |
| Q08CN | varchar |  |  | SI | Note |
| Q08CObsDR | varchar |  | FK | SI | Decreased sense of heat DR |
| Q08D | varchar |  |  | SI | Decreased sense of cold |
| Q08DN | varchar |  |  | SI | Note |
| Q08DObsDR | varchar |  | FK | SI | Decreased sense of cold DR |
| Q08E | varchar |  |  | SI | Decreased sense of vibration |
| Q08EN | varchar |  |  | SI | Note |
| Q08EObsDR | varchar |  | FK | SI | Decreased sense of vibration DR |
| Q08F | varchar |  |  | SI | Rhomberg's test |
| Q08FN | varchar |  |  | SI | Note |
| Q08FObsDR | varchar |  | FK | SI | Rhomberg's test DR |
| Q09 | varchar |  |  | SI | Central nervous system |
| Q09A | varchar |  |  | SI | Abnormal joint position sense |
| Q09AN | varchar |  |  | SI | Note |
| Q09AObsDR | varchar |  | FK | SI | Abnormal joint position sense DR |
| Q09B | varchar |  |  | SI | Impaired stereognosis |
| Q09BN | varchar |  |  | SI | Note |
| Q09BObsDR | varchar |  | FK | SI | Impaired stereognosis DR |
| Q09C | varchar |  |  | SI | Impaired graphesthesia |
| Q09CN | varchar |  |  | SI | Note |
| Q09CObsDR | varchar |  | FK | SI | Impaired graphesthesia DR |
| Q09D | varchar |  |  | SI | Abnormal tactile localisation |
| Q09DN | varchar |  |  | SI | Note |
| Q09DObsDR | varchar |  | FK | SI | Abnormal tactile localisation DR |
| Q10 | varchar |  |  | SI | Muscle appearance |
| Q10A | varchar |  |  | SI | Muscle atrophy |
| Q10AN | varchar |  |  | SI | Note |
| Q10AObsDR | varchar |  | FK | SI | Muscle atrophy DR |
| Q10B | varchar |  |  | SI | Muscle hypertrophy with weakness |
| Q10BN | varchar |  |  | SI | Note |
| Q10BObsDR | varchar |  | FK | SI | Muscle hypertrophy with weakness DR |
| Q10C | varchar |  |  | SI | Resting tremor |
| Q10CN | varchar |  |  | SI | Note |
| Q10CObsDR | varchar |  | FK | SI | Resting tremor DR |
| Q10D | varchar |  |  | SI | Choreoathetoid movements |
| Q10DN | varchar |  |  | SI | Note |
| Q10DObsDR | varchar |  | FK | SI | Choreoathetoid movements DR |
| Q11 | varchar |  |  | SI | Muscle tone |
| Q11A | varchar |  |  | SI | Decreased muscle tone |
| Q11AN | varchar |  |  | SI | Note |
| Q11AObsDR | varchar |  | FK | SI | Decreased muscle tone DR |
| Q11B | varchar |  |  | SI | General spasticity |
| Q11BN | varchar |  |  | SI | Note |
| Q11BObsDR | varchar |  | FK | SI | General spasticity DR |
| Q11C | varchar |  |  | SI | Cogwheel (stepwise) rigidity |
| Q11CN | varchar |  |  | SI | Note |
| Q11CObsDR | varchar |  | FK | SI | Cogwheel (stepwise) rigidity DR |
| Q11D | varchar |  |  | SI | Lead-pipe (uniform) rigidity |
| Q11DN | varchar |  |  | SI | Note |
| Q11DObsDR | varchar |  | FK | SI | Lead-pipe (uniform) rigidity DR |
| Q12 | varchar |  |  | SI | Muscle strength |
| Q12A | varchar |  |  | SI | Strength grade |
| Q12AN | varchar |  |  | SI | Note |
| Q12AObsDR | varchar |  | FK | SI | Strength grade DR |
| Q13 | varchar |  |  | SI | Involuntary movements |
| Q13A | varchar |  |  | SI | Fibrillations |
| Q13AN | varchar |  |  | SI | Note |
| Q13AObsDR | varchar |  | FK | SI | Fibrillations DR |
| Q13B | varchar |  |  | SI | Fasciculations |
| Q13BN | varchar |  |  | SI | Note |
| Q13BObsDR | varchar |  | FK | SI | Fasciculations DR |
| Q13C | varchar |  |  | SI | Tics |
| Q13CN | varchar |  |  | SI | Note |
| Q13CObsDR | varchar |  | FK | SI | Tics DR |
| Q13D | varchar |  |  | SI | Myoclonus |
| Q13DN | varchar |  |  | SI | Note |
| Q13DObsDR | varchar |  | FK | SI | Myoclonus DR |
| Q13E | varchar |  |  | SI | Dystonia |
| Q13EN | varchar |  |  | SI | Note |
| Q13EObsDR | varchar |  | FK | SI | Dystonia DR |
| Q13F | varchar |  |  | SI | Chorea |
| Q13FN | varchar |  |  | SI | Note |
| Q13FObsDR | varchar |  | FK | SI | Chorea DR |
| Q14 | varchar |  |  | SI | Reflexes |
| Q149 | varchar |  |  | SI | I. Olfactory |
| Q14A | varchar |  |  | SI | Abnormal abdominal reflex |
| Q14AN | varchar |  |  | SI | Note |
| Q14AObsDR | varchar |  | FK | SI | Abnormal abdominal reflex DR |
| Q14B | varchar |  |  | SI | Abnormal plantar reflex |
| Q14BN | varchar |  |  | SI | Note |
| Q14BObsDR | varchar |  | FK | SI | Abnormal plantar reflex DR |
| Q14C | varchar |  |  | SI | Abnormal deep tendon reflex |
| Q14CN | varchar |  |  | SI | Note |
| Q14CObsDR | varchar |  | FK | SI | Abnormal deep tendon reflex DR |
| Q14D | varchar |  |  | SI | Abnormal facial reflex |
| Q14DN | varchar |  |  | SI | Note |
| Q14DObsDR | varchar |  | FK | SI | Abnormal facial reflex DR |
| Q15 | varchar |  |  | SI | Cerebellar findings |
| Q150 | varchar |  |  | SI | II. Optic |
| Q151 | varchar |  |  | SI | III. Oculomotor |
| Q152 | varchar |  |  | SI | IV. Trochlear |
| Q153 | varchar |  |  | SI | V. Trigeminal |
| Q154 | varchar |  |  | SI | VI. Abducens |
| Q155 | varchar |  |  | SI | VII. Facial |
| Q155AA | varchar |  |  | SI | Motor |
| Q155AB | varchar |  |  | SI | Sensory-taste (2/3 tongue) |
| Q156 | varchar |  |  | SI | VIII. Vestibulocochlear |
| Q157 | varchar |  |  | SI | X. Vagus |
| Q157AA | varchar |  |  | SI | Gag reflex |
| Q157AB | varchar |  |  | SI | Phonation |
| Q157AC | varchar |  |  | SI | Sensory-taste (1/3 tongue) |
| Q158 | varchar |  |  | SI | XI. Spinal |
| Q159 | varchar |  |  | SI | XII. Hypoglossal |
| Q15A | varchar |  |  | SI | Intention tremor |
| Q15AN | varchar |  |  | SI | Note |
| Q15AObsDR | varchar |  | FK | SI | Intention tremor DR |
| Q15B | varchar |  |  | SI | Incoordination |
| Q15BN | varchar |  |  | SI | Note |
| Q15BObsDR | varchar |  | FK | SI | Incoordination DR |
| Q15C | varchar |  |  | SI | Dysmetria |
| Q15CN | varchar |  |  | SI | Note |
| Q15CObsDR | varchar |  | FK | SI | Dysmetria DR |
| Q15D | varchar |  |  | SI | Dysrhythmia |
| Q15DN | varchar |  |  | SI | Note |
| Q15DObsDR | varchar |  | FK | SI | Dysrhythmia DR |
| Q15E | varchar |  |  | SI | Dysdiadochokinesis |
| Q15EN | varchar |  |  | SI | Note |
| Q15EObsDR | varchar |  | FK | SI | Dysdiadochokinesis DR |
| Q16 | bigint |  |  | SI | Additional notes |
| Q163 | varchar |  |  | SI | Ptosis |
| Q163ObsDR | varchar |  | FK | SI | Ptosis DR |
| Q164 | varchar |  |  | SI | Upward movement |
| Q164ObsDR | varchar |  | FK | SI | Upward movement DR |
| Q165 | varchar |  |  | SI | Downward movement |
| Q165ObsDR | varchar |  | FK | SI | Downward movement DR |
| Q166 | varchar |  |  | SI | Inward movement |
| Q166ObsDR | varchar |  | FK | SI | Inward movement DR |
| Q167 | varchar |  |  | SI | Vertical diplopia |
| Q167ObsDR | varchar |  | FK | SI | Vertical diplopia DR |
| Q168 | varchar |  |  | SI | Hypertropia |
| Q168ObsDR | varchar |  | FK | SI | Hypertropia DR |
| Q169 | varchar |  |  | SI | Facial sensitivity |
| Q169ObsDR | varchar |  | FK | SI | Facial sensitivity DR |
| Q16TxtOnly | bigint |  |  | SI | Additional notes Plain Text Only |
| Q170 | varchar |  |  | SI | Corneal reflex |
| Q170ObsDR | varchar |  | FK | SI | Corneal reflex DR |
| Q171 | varchar |  |  | SI | Motor-clench jaw |
| Q171ObsDR | varchar |  | FK | SI | Motor-clench jaw DR |
| Q172 | varchar |  |  | SI | Inward deviation of eye |
| Q172ObsDR | varchar |  | FK | SI | Inward deviation of eye DR |
| Q173 | varchar |  |  | SI | Inability to abduct eye |
| Q173ObsDR | varchar |  | FK | SI | Inability to abduct eye DR |
| Q174 | varchar |  |  | SI | Elevate eyebrows |
| Q174ObsDR | varchar |  | FK | SI | Elevate eyebrows DR |
| Q175 | varchar |  |  | SI | Close eyes tightly |
| Q175ObsDR | varchar |  | FK | SI | Close eyes tightly DR |
| Q176 | varchar |  |  | SI | Show teeth |
| Q176ObsDR | varchar |  | FK | SI | Show teeth DR |
| Q177 | varchar |  |  | SI | Blow out cheeks |
| Q177ObsDR | varchar |  | FK | SI | Blow out cheeks DR |
| Q178 | varchar |  |  | SI | Sensory IX |
| Q178ObsDR | varchar |  | FK | SI | Sensory IX DR |
| Q179 | varchar |  |  | SI | Motor X |
| Q179ObsDR | varchar |  | FK | SI | Motor X DR |
| Q180 | varchar |  |  | SI | Palate |
| Q180ObsDR | varchar |  | FK | SI | Palate DR |
| Q181 | varchar |  |  | SI | Swallowing |
| Q181ObsDR | varchar |  | FK | SI | Swallowing DR |
| Q182 | varchar |  |  | SI | Elevate shoulder |
| Q182ObsDR | varchar |  | FK | SI | Elevate shoulder DR |
| Q183 | varchar |  |  | SI | Tongue movement |
| Q183ObsDR | varchar |  | FK | SI | Tongue movement DR |
| Q184 | varchar |  |  | SI | Tongue tone |
| Q184ObsDR | varchar |  | FK | SI | Tongue tone DR |
| Q185 | varchar |  |  | SI | Tongue strength |
| Q185ObsDR | varchar |  | FK | SI | Tongue strength DR |
| Q189N | varchar |  |  | SI | Note |
| Q190N | varchar |  |  | SI | Note |
| Q191N | varchar |  |  | SI | Note |
| Q192N | varchar |  |  | SI | Note |
| Q193N | varchar |  |  | SI | Note |
| Q194N | varchar |  |  | SI | Note |
| Q195N | varchar |  |  | SI | Note |
| Q196N | varchar |  |  | SI | Note |
| Q197N | varchar |  |  | SI | Note |
| Q198N | varchar |  |  | SI | Note |
| Q199N | varchar |  |  | SI | Note |
| Q200N | varchar |  |  | SI | Note |
| Q201N | varchar |  |  | SI | Note |
| Q202N | varchar |  |  | SI | Note |
| Q203N | varchar |  |  | SI | Note |
| Q204N | varchar |  |  | SI | Note |
| Q205N | varchar |  |  | SI | Note |
| Q206N | varchar |  |  | SI | Note |
| Q207N | varchar |  |  | SI | Note |
| Q208N | varchar |  |  | SI | Note |
| Q209N | varchar |  |  | SI | Note |
| Q210N | varchar |  |  | SI | Note |
| Q211N | varchar |  |  | SI | Note |
| Q212N | varchar |  |  | SI | Note |
| Q213N | varchar |  |  | SI | Note |
| Q214N | varchar |  |  | SI | Note |
| Q215N | varchar |  |  | SI | Note |
| Q216N | varchar |  |  | SI | Note |
| Q217N | varchar |  |  | SI | Note |
| Q218 | varchar |  |  | SI | Muscle power |
| Q219 | varchar |  |  | SI | Right upper limb |
| Q219ObsDR | varchar |  | FK | SI | Right upper limb DR |
| Q220 | varchar |  |  | SI | Right lower limb |
| Q220ObsDR | varchar |  | FK | SI | Right lower limb DR |
| Q221 | varchar |  |  | SI | Left upper limb |
| Q221ObsDR | varchar |  | FK | SI | Left upper limb DR |
| Q222 | varchar |  |  | SI | Left lower limb |
| Q222ObsDR | varchar |  | FK | SI | Left lower limb DR |
| Q223N | varchar |  |  | SI | Note |
| Q224N | varchar |  |  | SI | Note |
| Q227 | varchar |  |  | SI | Right upper limb |
| Q227A | varchar |  |  | SI | Biceps |
| Q227B | varchar |  |  | SI | Triceps |
| Q227C | varchar |  |  | SI | Pronator |
| Q228 | varchar |  |  | SI | Right lower limb |
| Q228A | varchar |  |  | SI | Patella |
| Q228B | varchar |  |  | SI | Ankle |
| Q229 | varchar |  |  | SI | Left upper limb |
| Q229A | varchar |  |  | SI | Biceps |
| Q229B | varchar |  |  | SI | Triceps |
| Q229C | varchar |  |  | SI | Pronator |
| Q230 | varchar |  |  | SI | Left lower limb |
| Q230A | varchar |  |  | SI | Patella |
| Q230B | varchar |  |  | SI | Ankle |
| Q231 | varchar |  |  | SI | Pupils |
| Q231A | varchar |  |  | SI | Pupil size (R) |
| Q231AN | varchar |  |  | SI | Note |
| Q231AObsDR | varchar |  | FK | SI | Pupil size (R) DR |
| Q231B | varchar |  |  | SI | Pupil reaction (R) |
| Q231BN | varchar |  |  | SI | Note |
| Q231BObsDR | varchar |  | FK | SI | Pupil reaction (R) DR |
| Q231C | varchar |  |  | SI | Pupil size (L) |
| Q231CN | varchar |  |  | SI | Note |
| Q231CObsDR | varchar |  | FK | SI | Pupil size (L) DR |
| Q231D | varchar |  |  | SI | Pupil reaction (L) |
| Q231DN | varchar |  |  | SI | Note |
| Q231DObsDR | varchar |  | FK | SI | Pupil reaction (L) DR |
| Q250 | date |  |  | SI | Date |
| Q251 | time |  |  | SI | Time |
| Q252 | varchar |  |  | SI | IX. Glossopharyngeal |
| Q253 | varchar |  |  | SI | Note |
| Q254 | varchar |  |  | SI | Uvular movement |
| Q255 | varchar |  |  | SI | Note |
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